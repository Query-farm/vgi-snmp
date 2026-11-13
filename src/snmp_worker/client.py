"""SNMP transport: targets, credentials and the GET / GETNEXT / GETBULK primitives.

pysnmp is asyncio-based; table functions are synchronous. Every request runs on one
private event loop in a daemon thread, so a single ``SnmpEngine`` (with its USM
engine-ID discovery cache) is shared by every query in the process.

Credentials resolve per target, in this order: the function's ``community`` argument,
then a DuckDB secret of type ``snmp`` whose ``SCOPE`` is a prefix of
``snmp://<host>:<port>``, then the ``SNMP_*`` environment variables, then the
community ``public``. Credentials are never written to table-function state.
"""

from __future__ import annotations

import asyncio
import ipaddress
import os
import threading
from collections.abc import Coroutine
from dataclasses import dataclass
from typing import Any

import pyarrow as pa
from pysnmp.hlapi.v3arch import asyncio as hlapi
from pysnmp.proto import rfc1905
from vgi.catalog import SecretTypeSpec

SECRET_TYPE = "snmp"
DEFAULT_PORT = 161
DEFAULT_COMMUNITY = "public"

ENV_COMMUNITY = "SNMP_COMMUNITY"
ENV_USER = "SNMP_USER"
ENV_AUTH_PROTOCOL = "SNMP_AUTH_PROTOCOL"
ENV_AUTH_KEY = "SNMP_AUTH_KEY"
ENV_PRIV_PROTOCOL = "SNMP_PRIV_PROTOCOL"
ENV_PRIV_KEY = "SNMP_PRIV_KEY"

VERSIONS = ["1", "2c", "3"]

AUTH_PROTOCOLS: dict[str, Any] = {
    "none": hlapi.usmNoAuthProtocol,
    "md5": hlapi.usmHMACMD5AuthProtocol,
    "sha": hlapi.usmHMACSHAAuthProtocol,
    "sha224": hlapi.usmHMAC128SHA224AuthProtocol,
    "sha256": hlapi.usmHMAC192SHA256AuthProtocol,
    "sha384": hlapi.usmHMAC256SHA384AuthProtocol,
    "sha512": hlapi.usmHMAC384SHA512AuthProtocol,
}
PRIV_PROTOCOLS: dict[str, Any] = {
    "none": hlapi.usmNoPrivProtocol,
    "des": hlapi.usmDESPrivProtocol,
    "3des": hlapi.usm3DESEDEPrivProtocol,
    "aes": hlapi.usmAesCfb128Protocol,
    "aes128": hlapi.usmAesCfb128Protocol,
    "aes192": hlapi.usmAesCfb192Protocol,
    "aes256": hlapi.usmAesCfb256Protocol,
    "aes192blmt": hlapi.usmAesBlumenthalCfb192Protocol,
    "aes256blmt": hlapi.usmAesBlumenthalCfb256Protocol,
}

_REDACT = {"redact": "true"}

# Registered with DuckDB: CREATE SECRET (TYPE snmp, SCOPE 'snmp://10.0.0.', COMMUNITY '...').
SNMP_SECRET_TYPE = SecretTypeSpec(
    name=SECRET_TYPE,
    description=(
        "SNMP credentials: a v1/v2c community or SNMPv3 USM user. SCOPE is matched as a "
        "prefix of 'snmp://<host>:<port>', so one secret can cover a host, a subnet or all agents."
    ),
    schema=pa.schema(
        [
            pa.field("community", pa.string(), metadata={**_REDACT, "vgi_doc": "SNMPv1/v2c community string."}),
            pa.field("user", pa.string(), metadata={"vgi_doc": "SNMPv3 USM user (security name)."}),
            pa.field(
                "auth_protocol",
                pa.string(),
                metadata={"vgi_doc": "SNMPv3 auth protocol: none, md5, sha, sha224, sha256, sha384 or sha512."},
            ),
            pa.field("auth_key", pa.string(), metadata={**_REDACT, "vgi_doc": "SNMPv3 authentication passphrase."}),
            pa.field(
                "priv_protocol",
                pa.string(),
                metadata={"vgi_doc": "SNMPv3 privacy protocol: none, des, 3des, aes (aes128), aes192 or aes256."},
            ),
            pa.field(
                "priv_key", pa.string(), metadata={**_REDACT, "vgi_doc": "SNMPv3 privacy (encryption) passphrase."}
            ),
        ],
        metadata={"vgi_doc_url": "https://github.com/Query-farm/vgi-snmp#credentials"},
    ),
)


class SnmpError(RuntimeError):
    """An SNMP request failed (timeout, authentication, agent error)."""


# ---------------------------------------------------------------- targets


@dataclass(frozen=True, slots=True)
class Target:
    """Where to send requests: host, UDP port and address family."""

    host: str
    port: int
    ipv6: bool

    @property
    def scope(self) -> str:
        """The path DuckDB secret scopes are matched against."""
        host = f"[{self.host}]" if self.ipv6 else self.host
        return f"snmp://{host}:{self.port}"

    def __str__(self) -> str:
        """``host:port`` for messages."""
        return self.scope.removeprefix("snmp://")


def parse_target(text: str, port: int | None) -> Target:
    """Parse ``host``, ``host:port``, ``[v6addr]:port`` or a bare IPv6 address.

    Args:
        text: The host argument.
        port: The ``port`` named argument, if given.

    Returns:
        The target, with the default port 161 when none was given.

    Raises:
        SnmpError: Empty host, bad port, or a port that conflicts with ``port``.

    """
    text = text.strip()
    if not text:
        raise SnmpError("host must not be empty")
    host, embedded = text, None
    if text.startswith("["):
        end = text.find("]")
        if end < 0:
            raise SnmpError(f"unterminated IPv6 literal in host {text!r}")
        host, rest = text[1:end], text[end + 1 :]
        if rest:
            if not rest.startswith(":"):
                raise SnmpError(f"unexpected text after IPv6 literal in host {text!r}")
            embedded = rest[1:]
    elif text.count(":") == 1:
        host, embedded = text.split(":")
    ipv6 = ":" in host
    if ipv6:
        try:
            ipaddress.IPv6Address(host)
        except ValueError as err:
            raise SnmpError(f"invalid IPv6 address {host!r}") from err
    effective = port
    if embedded is not None:
        if not embedded.isdigit() or not 0 < int(embedded) < 65536:
            raise SnmpError(f"invalid port in host {text!r}")
        if port is not None and port != int(embedded):
            raise SnmpError(f"host {text!r} names port {embedded} but port := {port} was also given")
        effective = int(embedded)
    return Target(host=host, port=effective or DEFAULT_PORT, ipv6=ipv6)


# ---------------------------------------------------------------- credentials


@dataclass(frozen=True, slots=True)
class Credentials:
    """Resolved security parameters for one target. Never serialized."""

    version: str
    community: str
    user: str | None = None
    auth_protocol: str = "none"
    auth_key: str | None = None
    priv_protocol: str = "none"
    priv_key: str | None = None

    def auth_data(self) -> Any:
        """Build the pysnmp authentication object."""
        if self.version in ("1", "2c"):
            return hlapi.CommunityData(self.community, mpModel=0 if self.version == "1" else 1)
        if not self.user:
            raise SnmpError(
                "SNMPv3 needs a user: CREATE SECRET (TYPE snmp, USER '...', AUTH_KEY '...', PRIV_KEY '...') "
                f"or set {ENV_USER}"
            )
        return hlapi.UsmUserData(
            self.user,
            authKey=self.auth_key,
            privKey=self.priv_key,
            authProtocol=AUTH_PROTOCOLS[self.auth_protocol],
            privProtocol=PRIV_PROTOCOLS[self.priv_protocol],
        )


def _secret_str(secret: dict[str, Any] | None, key: str) -> str | None:
    if not secret:
        return None
    value = secret.get(key)
    if value is None:
        return None
    py = value.as_py() if hasattr(value, "as_py") else value
    return str(py) if py not in (None, "") else None


def _protocol(name: str | None, key: str | None, table: dict[str, Any], default: str, what: str) -> str:
    if name is None:
        return default if key else "none"
    normalized = name.strip().lower().replace("-", "").replace("_", "")
    if normalized not in table:
        raise SnmpError(f"unknown SNMPv3 {what} protocol {name!r}; expected one of {', '.join(table)}")
    if normalized != "none" and not key:
        raise SnmpError(f"SNMPv3 {what} protocol {name!r} needs a {what}_key")
    return normalized


def resolve_credentials(
    *,
    version: str | None,
    community: str | None,
    secret: dict[str, Any] | None,
) -> Credentials:
    """Combine arguments, the scoped secret and the environment into `Credentials`.

    ``version`` defaults to ``3`` when a v3 user is configured, else ``2c``.
    """
    user = _secret_str(secret, "user") or os.environ.get(ENV_USER) or None
    if version is None:
        version = "3" if user and community is None else "2c"
    if version not in VERSIONS:
        raise SnmpError(f"unknown SNMP version {version!r}; expected one of {', '.join(VERSIONS)}")
    resolved_community = (
        community or _secret_str(secret, "community") or os.environ.get(ENV_COMMUNITY) or DEFAULT_COMMUNITY
    )
    if version != "3":
        return Credentials(version=version, community=resolved_community)
    auth_key = _secret_str(secret, "auth_key") or os.environ.get(ENV_AUTH_KEY) or None
    priv_key = _secret_str(secret, "priv_key") or os.environ.get(ENV_PRIV_KEY) or None
    auth_name = _secret_str(secret, "auth_protocol") or os.environ.get(ENV_AUTH_PROTOCOL) or None
    priv_name = _secret_str(secret, "priv_protocol") or os.environ.get(ENV_PRIV_PROTOCOL) or None
    auth = _protocol(auth_name, auth_key, AUTH_PROTOCOLS, "sha", "auth")
    priv = _protocol(priv_name, priv_key, PRIV_PROTOCOLS, "aes", "priv")
    if priv != "none" and auth == "none":
        raise SnmpError("SNMPv3 privacy (priv_key) also needs authentication (auth_key)")
    return Credentials(
        version="3",
        community=resolved_community,
        user=user,
        auth_protocol=auth,
        auth_key=auth_key,
        priv_protocol=priv,
        priv_key=priv_key,
    )


# ---------------------------------------------------------------- the event loop


class _Loop:
    """A private asyncio loop in a daemon thread, plus the shared SnmpEngine."""

    def __init__(self) -> None:
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.loop.run_forever, name="snmp-loop", daemon=True)
        self.thread.start()
        self.engine: Any = None

    def run[T](self, coro: Coroutine[Any, Any, T]) -> T:
        return asyncio.run_coroutine_threadsafe(coro, self.loop).result()


_LOOP: _Loop | None = None
_LOOP_LOCK = threading.Lock()


def _loop() -> _Loop:
    global _LOOP
    if _LOOP is None:
        with _LOOP_LOCK:
            if _LOOP is None:
                _LOOP = _Loop()
    return _LOOP


# ---------------------------------------------------------------- sessions

VarBind = tuple[tuple[int, ...], Any]


@dataclass(frozen=True, slots=True)
class Session:
    """One target with its credentials and request settings."""

    target: Target
    credentials: Credentials
    timeout: float
    retries: int
    context: str = ""

    def _where(self) -> str:
        return f"SNMPv{self.credentials.version} {self.target}"

    async def _transport(self) -> Any:
        cls = hlapi.Udp6TransportTarget if self.target.ipv6 else hlapi.UdpTransportTarget
        try:
            return await cls.create((self.target.host, self.target.port), timeout=self.timeout, retries=self.retries)
        except Exception as err:
            raise SnmpError(f"{self._where()}: cannot resolve host: {err}") from err

    async def _request(
        self, kind: str, varbinds: list[tuple[int, ...]], max_repetitions: int
    ) -> tuple[Any, Any, int, list[VarBind]]:
        state = _loop()
        if state.engine is None:
            state.engine = hlapi.SnmpEngine()
        objects = [hlapi.ObjectType(hlapi.ObjectIdentity(oid)) for oid in varbinds]
        context = hlapi.ContextData(contextName=self.context)
        auth = self.credentials.auth_data()
        transport = await self._transport()
        if kind == "get":
            result = await hlapi.get_cmd(state.engine, auth, transport, context, *objects, lookupMib=False)
        elif kind == "next":
            result = await hlapi.next_cmd(state.engine, auth, transport, context, *objects, lookupMib=False)
        else:
            result = await hlapi.bulk_cmd(
                state.engine, auth, transport, context, 0, max_repetitions, *objects, lookupMib=False
            )
        indication, status, index, binds = result
        return indication, status, int(index or 0), [(tuple(o), v) for o, v in binds]

    def _call(self, kind: str, oids: list[tuple[int, ...]], max_repetitions: int = 0) -> tuple[str, int, list[VarBind]]:
        """Run one request; returns (error-status name, error index, varbinds)."""
        if self.context and self.credentials.version != "3":
            raise SnmpError(f"{self._where()}: context := {self.context!r} applies to SNMPv3 only")
        try:
            indication, status, index, binds = _loop().run(self._request(kind, oids, max_repetitions))
        except SnmpError:
            raise
        except Exception as err:
            raise SnmpError(f"{self._where()}: {type(err).__name__}: {err}") from err
        if indication:
            hint = ""
            if "timeout" in str(indication).lower():
                hint = (
                    f" (after {self.retries + 1} attempt(s) of {self.timeout:g}s; check the host, port, "
                    "community or v3 credentials, and that the agent allows this manager)"
                )
            raise SnmpError(f"{self._where()}: {indication}{hint}")
        name = status.prettyPrint() if hasattr(status, "prettyPrint") else str(status)
        return ("noError" if not int(status) else name), index, binds

    def get(self, oids: list[tuple[int, ...]]) -> list[VarBind]:
        """GET each OID; missing objects come back as noSuchObject/noSuchInstance values.

        Requests are split so that ``tooBig`` responses and SNMPv1's whole-PDU
        ``noSuchName`` errors still yield one result per OID.
        """
        results: dict[int, VarBind] = {}
        pending = list(range(len(oids)))
        chunk = 32
        while pending:
            batch = pending[:chunk]
            status, index, binds = self._call("get", [oids[i] for i in batch])
            if status == "noError":
                for i, bind in zip(batch, binds, strict=True):
                    results[i] = bind
                pending = pending[len(batch) :]
            elif status == "tooBig" and chunk > 1:
                chunk = max(1, chunk // 2)
            elif status == "noSuchName" and 1 <= index <= len(batch):
                missing = batch[index - 1]
                results[missing] = (oids[missing], rfc1905.noSuchObject)
                pending.remove(missing)
            else:
                raise SnmpError(f"{self._where()}: agent returned {status} for GET")
        return [results[i] for i in range(len(oids))]

    def next_rows(self, oids: list[tuple[int, ...]], max_repetitions: int) -> list[list[VarBind]]:
        """Advance each cursor: up to ``max_repetitions`` successors per OID.

        Returns one list per input OID. GETBULK is used for v2c/v3 and GETNEXT for v1;
        an empty list means that cursor has reached the end of the MIB view.
        """
        if self.credentials.version == "1":
            out: list[list[VarBind]] = []
            for oid in oids:
                status, _index, binds = self._call("next", [oid])
                if status == "noSuchName":
                    out.append([])
                elif status != "noError":
                    raise SnmpError(f"{self._where()}: agent returned {status} for GETNEXT")
                else:
                    out.append(list(binds))
            return out
        reps = max_repetitions
        while True:
            status, _index, binds = self._call("bulk", oids, reps)
            if status == "tooBig" and reps > 1:
                reps = max(1, reps // 2)
                continue
            if status != "noError":
                raise SnmpError(f"{self._where()}: agent returned {status} for GETBULK")
            break
        width = len(oids)
        columns: list[list[VarBind]] = [[] for _ in oids]
        for position, bind in enumerate(binds):
            columns[position % width].append(bind)
        return columns


def is_end(value: Any) -> bool:
    """Tell whether a value is endOfMibView."""
    return bool(value.tagSet == rfc1905.EndOfMibView.tagSet)


def is_exception(value: Any) -> bool:
    """Tell whether a value is noSuchObject, noSuchInstance or endOfMibView."""
    return bool(
        value.tagSet in (rfc1905.NoSuchObject.tagSet, rfc1905.NoSuchInstance.tagSet, rfc1905.EndOfMibView.tagSet)
    )
