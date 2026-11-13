"""A local SNMP agent for the tests: snmpsim serving test/snmp_agent/data.

Prints ``PORT:<n>`` on stdout once the agent answers, then runs until killed, the
same contract the integration harness uses for its other helper servers.

Communities (= data files): ``public`` and ``private`` from data/, plus ``big``, a
generated device with 2,500 interfaces, so walks and tables span several batches.
SNMPv3: user ``simulator``, SHA auth key ``auctoritas``, AES priv key ``privatus``;
snmpsim selects the data file by v3 context name, so pass ``context := 'public'``.
"""

from __future__ import annotations

import os
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BIG_INTERFACES = 2_500

V3_USER = "simulator"
V3_AUTH_KEY = "auctoritas"
V3_PRIV_KEY = "privatus"


def _sorted_records(lines: list[str]) -> list[str]:
    """snmpsim needs records in OID order."""
    records = [line for line in lines if line.strip()]
    return sorted(records, key=lambda line: tuple(int(x) for x in line.split("|", 1)[0].split(".")))


def _big_device() -> list[str]:
    lines = [
        "1.3.6.1.2.1.1.1.0|4|VGI big test agent",
        "1.3.6.1.2.1.1.5.0|4|big-switch",
        f"1.3.6.1.2.1.2.1.0|2|{BIG_INTERFACES}",
    ]
    for i in range(1, BIG_INTERFACES + 1):
        lines.append(f"1.3.6.1.2.1.2.2.1.1.{i}|2|{i}")
        lines.append(f"1.3.6.1.2.1.2.2.1.2.{i}|4|port{i}")
        lines.append(f"1.3.6.1.2.1.2.2.1.8.{i}|2|{1 if i % 2 else 2}")
        lines.append(f"1.3.6.1.2.1.2.2.1.10.{i}|65|{i * 1000}")
    return lines


READY_TIMEOUT = 180.0

# SNMPv2c GET sysDescr.0, community "public", request-id 1 (hand-encoded BER).
_PROBE = bytes.fromhex("302902010104067075626c6963a01c020400000001020100020100300e300c06082b060102010101000500")


def _answers(port: int) -> bool:
    """Send one GET and report whether the agent replied within a second."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(1.0)
        try:
            sock.sendto(_PROBE, ("127.0.0.1", port))
            sock.recvfrom(4096)
        except OSError:
            return False
        return True


def _free_udp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def main() -> None:
    """Prepare the data directory, start snmpsim and announce its port."""
    work = Path(tempfile.mkdtemp(prefix="vgi-snmp-agent-"))
    data = work / "data"
    data.mkdir()
    for source in sorted((HERE / "data").glob("*.snmprec")):
        records = _sorted_records(source.read_text().splitlines())
        (data / source.name).write_text("\n".join(records) + "\n")
    (data / "big.snmprec").write_text("\n".join(_sorted_records(_big_device())) + "\n")

    port = _free_udp_port()
    # Run the responder module with this interpreter: no console-script path to find (Windows).
    command = [
        sys.executable,
        "-m",
        "snmpsim.commands.responder",
        f"--data-dir={data}",
        f"--cache-dir={work / 'cache'}",
        f"--agent-udpv4-endpoint=127.0.0.1:{port}",
        f"--v3-user={V3_USER}",
        f"--v3-auth-key={V3_AUTH_KEY}",
        "--v3-auth-proto=SHA",
        f"--v3-priv-key={V3_PRIV_KEY}",
        "--v3-priv-proto=AES",
        "--logging-method=stderr",
        "--log-level=error",
    ]
    env = {**os.environ, "PYTHONUNBUFFERED": "1"}
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)

    def stop(*_: object) -> None:
        child.terminate()
        shutil.rmtree(work, ignore_errors=True)
        os._exit(0)

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)

    def drain() -> None:
        assert child.stdout is not None
        for line in child.stdout:
            sys.stderr.write(line)

    threading.Thread(target=drain, daemon=True).start()

    # Ready means answering SNMP, not having logged a line (pipes are buffered on Windows).
    deadline = time.monotonic() + READY_TIMEOUT
    while not _answers(port):
        if child.poll() is not None:
            sys.stderr.write("snmpsim exited before answering\n")
            sys.exit(1)
        if time.monotonic() > deadline:
            sys.stderr.write(f"snmpsim did not answer within {READY_TIMEOUT:g}s\n")
            child.terminate()
            sys.exit(1)
    print(f"PORT:{port}", flush=True)
    child.wait()
    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
