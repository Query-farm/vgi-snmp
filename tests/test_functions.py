"""Unit tests. The SQL-level tests live in test/sql and run through DuckDB."""

from __future__ import annotations

import socket
from decimal import Decimal
from typing import Any

import pyarrow as pa
import pytest
from pysnmp.proto import rfc1902
from vgi.arguments import Arguments
from vgi.client import Client

from snmp_worker.client import Credentials, Session, SnmpError, parse_target, resolve_credentials
from snmp_worker.common import varbind_rows
from snmp_worker.mib import column_kind, column_value, mibs, render_value
from snmp_worker.oid_functions import to_name, to_oid
from snmp_worker.snmp_table import readable_columns, table_schema

SCHEMA = ["main"]


def _table(client: Client, name: str, *positional: Any, **named: Any) -> pa.Table:
    arguments = Arguments(
        positional=tuple(pa.scalar(v) for v in positional),
        named={k: pa.scalar(v) for k, v in named.items()},
    )
    batches = list(client.table_function(function_name=name, schema_path=SCHEMA, arguments=arguments))
    return pa.Table.from_batches(batches)


def _session(agent: str, **overrides: Any) -> Session:
    credentials = overrides.pop("credentials", Credentials(version="2c", community="public"))
    settings = {"timeout": 1.0, "retries": 0, **overrides}
    return Session(target=parse_target(agent, None), credentials=credentials, **settings)


# ---------------------------------------------------------------- targets and credentials


@pytest.mark.parametrize(
    ("text", "port", "expected"),
    [
        ("router1", None, ("router1", 161, False)),
        ("10.0.0.1:1161", None, ("10.0.0.1", 1161, False)),
        ("10.0.0.1", 1162, ("10.0.0.1", 1162, False)),
        ("::1", None, ("::1", 161, True)),
        ("[2001:db8::1]:10161", None, ("2001:db8::1", 10161, True)),
    ],
)
def test_parse_target(text: str, port: int | None, expected: tuple[str, int, bool]) -> None:
    target = parse_target(text, port)
    assert (target.host, target.port, target.ipv6) == expected


def test_parse_target_scope_and_errors() -> None:
    assert parse_target("10.0.0.1", None).scope == "snmp://10.0.0.1:161"
    assert parse_target("[::1]:162", None).scope == "snmp://[::1]:162"
    for bad in ["", "h:0", "h:x", "[::1", "[::1]x"]:
        with pytest.raises(SnmpError):
            parse_target(bad, None)
    with pytest.raises(SnmpError, match="also given"):
        parse_target("h:1161", 161)


def test_credentials_precedence(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in [
        "SNMP_COMMUNITY",
        "SNMP_USER",
        "SNMP_AUTH_KEY",
        "SNMP_PRIV_KEY",
        "SNMP_AUTH_PROTOCOL",
        "SNMP_PRIV_PROTOCOL",
    ]:
        monkeypatch.delenv(var, raising=False)
    assert resolve_credentials(version=None, community=None, secret=None) == Credentials(
        version="2c", community="public"
    )
    monkeypatch.setenv("SNMP_COMMUNITY", "from-env")
    assert resolve_credentials(version=None, community=None, secret=None).community == "from-env"
    secret = {"community": pa.scalar("from-secret")}
    assert resolve_credentials(version=None, community=None, secret=secret).community == "from-secret"
    assert resolve_credentials(version="1", community="from-arg", secret=secret).community == "from-arg"

    v3 = resolve_credentials(
        version=None,
        community=None,
        secret={"user": pa.scalar("u"), "auth_key": pa.scalar("a" * 8), "priv_key": pa.scalar("p" * 8)},
    )
    assert (v3.version, v3.auth_protocol, v3.priv_protocol) == ("3", "sha", "aes")
    no_auth = resolve_credentials(version="3", community=None, secret={"user": pa.scalar("u")})
    assert (no_auth.auth_protocol, no_auth.priv_protocol) == ("none", "none")
    with pytest.raises(SnmpError, match="unknown SNMPv3 auth protocol"):
        resolve_credentials(
            version="3", community=None, secret={"user": pa.scalar("u"), "auth_protocol": pa.scalar("rot13")}
        )
    with pytest.raises(SnmpError, match="also needs authentication"):
        resolve_credentials(
            version="3", community=None, secret={"user": pa.scalar("u"), "priv_key": pa.scalar("p" * 8)}
        )


# ---------------------------------------------------------------- MIB resolution


def test_resolve_names() -> None:
    assert to_oid(
        ["IF-MIB::ifInOctets.3", "sysDescr.0", ".1.3.6.1", "ifHCInOctets", "nope", None, "IF-MIB::sysDescr"]
    ) == [
        "1.3.6.1.2.1.2.2.1.10.3",
        "1.3.6.1.2.1.1.1.0",
        "1.3.6.1",
        "1.3.6.1.2.1.31.1.1.1.6",
        None,
        None,
        None,
    ]
    assert to_name(["1.3.6.1.2.1.1.3.0", "1.3.6.1.4.1.9.1.1", "1.3.6.1.2.1.25.2.3.1.6.1", "x", "9.9", None]) == [
        "SNMPv2-MIB::sysUpTime.0",
        "SNMPv2-SMI::enterprises.9.1.1",
        "HOST-RESOURCES-MIB::hrStorageUsed.1",
        None,
        None,
        None,
    ]


def test_table_schemas() -> None:
    iftable = mibs().table("ifTable")
    assert len(iftable.columns) == 22
    schema = table_schema(iftable)
    assert schema.names[:3] == ["_index", "ifIndex", "ifDescr"]
    assert schema.field("ifOperStatus").type == pa.string()
    assert schema.field("ifInOctets").type == pa.int64()
    assert table_schema(mibs().table("IF-MIB::ifXEntry")).field("ifHCInOctets").type == pa.uint64()
    assert table_schema(mibs().table("ifName")).names[:3] == ["_index", "ifIndex", "ifName"]
    arp = mibs().table("ipNetToPhysicalTable")
    assert [o.name for o in arp.index] == [
        "ipNetToPhysicalIfIndex",
        "ipNetToPhysicalNetAddressType",
        "ipNetToPhysicalNetAddress",
    ]
    assert "ipNetToPhysicalIfIndex" not in [c.name for c in readable_columns(arp)]
    for bad in ["sysDescr", "system", "nope"]:
        with pytest.raises(ValueError):
            mibs().table(bad)


def test_render_values() -> None:
    oper = mibs().lookup("ifOperStatus")
    phys = mibs().lookup("ifPhysAddress")
    hc = mibs().lookup("ifHCInOctets")
    assert oper is not None and phys is not None and hc is not None
    assert render_value(rfc1902.Integer32(2), oper.syntax).text == "down"
    assert render_value(rfc1902.Integer32(99), oper.syntax).text == "99"  # out-of-range enum falls back
    assert render_value(rfc1902.OctetString(b"\x00\x11\x22\x33\x44\x55"), phys.syntax).text == "00:11:22:33:44:55"
    big = render_value(rfc1902.Counter64(2**64 - 1), hc.syntax)
    assert (big.type, big.number) == ("Counter64", Decimal(2**64 - 1))
    ip = render_value(rfc1902.IpAddress("192.0.2.1"), None)
    assert (ip.type, ip.text, ip.raw) == ("IpAddress", "192.0.2.1", b"\xc0\x00\x02\x01")
    assert render_value(rfc1902.ObjectIdentifier("1.3.6.1"), None).text == "1.3.6.1"
    assert column_kind(hc.syntax).sql_type == "UBIGINT"
    assert column_value(oper.syntax, rfc1902.Integer32(1)) == "up"
    assert column_value(hc.syntax, rfc1902.Counter64(5)) == 5


# ---------------------------------------------------------------- against the local agent


def test_get_v2c(agent: str) -> None:
    binds = _session(agent).get(
        [mibs().resolve("sysName.0"), mibs().resolve("sysORTable.0"), mibs().resolve("ifSpeed.10")]
    )
    cols = varbind_rows(mibs(), agent, binds)
    assert cols["value"] == ["edge-router-1", None, "4294967295"]
    assert cols["type"] == ["OCTET STRING", "noSuchInstance", "Gauge32"]
    assert cols["name"] == ["SNMPv2-MIB::sysName.0", "SNMPv2-MIB::sysORTable.0", "IF-MIB::ifSpeed.10"]


def test_get_v1_splits_on_no_such_name(agent: str) -> None:
    session = _session(agent, credentials=Credentials(version="1", community="public"))
    binds = session.get([mibs().resolve("sysName.0"), mibs().resolve("sysORTable.0"), mibs().resolve("sysLocation.0")])
    cols = varbind_rows(mibs(), agent, binds)
    assert cols["type"] == ["OCTET STRING", "noSuchObject", "OCTET STRING"]
    assert cols["value"][2] == "Rack 4, Example DC"


def test_bulk_and_next_agree(agent: str) -> None:
    root = mibs().resolve("ifDescr")
    (bulk,) = _session(agent).next_rows([root], 10)
    (nxt,) = _session(agent, credentials=Credentials(version="1", community="public")).next_rows([root], 10)
    assert [str(v) for _, v in bulk[:3]] == ["lo", "eth0", "eth1"]
    assert nxt[0][0] == bulk[0][0]


def test_v3_auth_priv(agent: str) -> None:
    credentials = resolve_credentials(
        version="3",
        community=None,
        secret={"user": pa.scalar("simulator"), "auth_key": pa.scalar("auctoritas"), "priv_key": pa.scalar("privatus")},
    )
    (bind,) = _session(agent, credentials=credentials, context="public").get([mibs().resolve("sysName.0")])
    assert str(bind[1]) == "edge-router-1"


def test_wrong_community_times_out(agent: str) -> None:
    with pytest.raises(SnmpError, match="No SNMP response"):
        _session(agent, credentials=Credentials(version="2c", community="wrong"), timeout=0.2).get(
            [(1, 3, 6, 1, 2, 1, 1, 1, 0)]
        )


def test_unreachable_port_times_out() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
        with pytest.raises(SnmpError, match=r"127\.0\.0\.1"):
            _session(f"127.0.0.1:{port}", timeout=0.2).get([(1, 3, 6, 1, 2, 1, 1, 1, 0)])


def test_context_needs_v3(agent: str) -> None:
    with pytest.raises(SnmpError, match="SNMPv3 only"):
        _session(agent, context="public").get([(1, 3, 6, 1, 2, 1, 1, 1, 0)])


# ---------------------------------------------------------------- through the worker (offline functions)


def test_mib_objects_through_worker(client: Client) -> None:
    table = _table(client, "snmp_mib_objects", module="IF-MIB", kind="table")
    assert set(table.column("name").to_pylist()) >= {"ifTable", "ifXTable", "ifStackTable"}
    everything = _table(client, "snmp_mib_objects")
    assert everything.num_rows > 1000
    modules = set(everything.column("module").to_pylist())
    assert {"IF-MIB", "HOST-RESOURCES-MIB", "UCD-SNMP-MIB"} <= modules
    assert not any(str(m).startswith(("__", "PYSNMP-")) for m in modules)
