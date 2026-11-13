"""Shared fixtures: a worker client and the local SNMP agent (snmpsim)."""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest
from vgi.client import Client

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def client() -> Iterator[Client]:
    """A client that launches the worker as a subprocess, the way DuckDB does."""
    with Client([sys.executable, "-m", "snmp_worker.worker"]) as c:
        yield c


@pytest.fixture(scope="session")
def agent() -> Iterator[str]:
    """Start test/snmp_agent/serve.py and return its ``127.0.0.1:<port>`` address."""
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "test" / "snmp_agent" / "serve.py")],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert proc.stdout is not None
    line = proc.stdout.readline().strip()
    assert line.startswith("PORT:"), line
    yield f"127.0.0.1:{line.removeprefix('PORT:')}"
    proc.terminate()
    proc.wait(timeout=10)
