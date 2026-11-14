"""Run a disposable loopback SNMP agent; domain calculations remain in SQL."""

import atexit
import os
import socket
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory

_PROBE = bytes.fromhex("302902010104067075626c6963a01c020400000001020100020100300e300c06082b060102010101000500")
_ENV_KEYS = (
    "SNMP_COMMUNITY",
    "SNMP_USER",
    "SNMP_AUTH_PROTOCOL",
    "SNMP_AUTH_KEY",
    "SNMP_PRIV_PROTOCOL",
    "SNMP_PRIV_KEY",
    "SNMP_MIB_DIRS",
)


class LocalAgent:
    """Serve only the bundled synthetic fixture on 127.0.0.1."""

    def __init__(self):
        """Start snmpsim and wait for a real SNMP response before returning."""
        self.previous = {key: os.environ.pop(key, None) for key in _ENV_KEYS}
        self.work = TemporaryDirectory(prefix="vgi-snmp-notebook-")
        self.process = None
        self.closed = False
        self.log = (Path(self.work.name) / "agent.log").open("w+")
        atexit.register(self.close)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(("127.0.0.1", 0))
            self.port = sock.getsockname()[1]
        self.host = f"127.0.0.1:{self.port}"
        command = [
            sys.executable,
            "-m",
            "snmpsim.commands.responder",
            f"--data-dir={Path(__file__).resolve().parent / 'fixtures'}",
            f"--cache-dir={self.work.name}/cache",
            f"--agent-udpv4-endpoint={self.host}",
            "--logging-method=stderr",
            "--log-level=error",
        ]
        try:
            self.process = subprocess.Popen(command, stdout=self.log, stderr=subprocess.STDOUT)
            deadline = time.monotonic() + 60
            while time.monotonic() < deadline:
                if self.process.poll() is not None:
                    self.log.seek(0)
                    raise RuntimeError("Local SNMP agent failed: " + self.log.read())
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    sock.settimeout(0.5)
                    sock.sendto(_PROBE, ("127.0.0.1", self.port))
                    try:
                        sock.recvfrom(4096)
                        return
                    except TimeoutError:
                        pass
            raise TimeoutError("Local synthetic SNMP agent did not answer within 60 seconds")
        except BaseException:
            self.close()
            raise

    def close(self):
        """Stop the child, remove its cache, and restore inherited settings."""
        if self.closed:
            return
        self.closed = True
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)
        self.log.close()
        self.work.cleanup()
        for key, value in self.previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
