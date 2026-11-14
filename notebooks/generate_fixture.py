"""Generate explicitly invented SNMP storage values; no device is queried."""

import hashlib
import json
from pathlib import Path


def main():
    """Write numerically sorted snmprec records and their provenance."""
    folder = Path(__file__).resolve().parent / "fixtures"
    folder.mkdir(exist_ok=True)
    rows = [
        (1, "Memory", 8192, 2097152, 1572864, 2),
        (7, "Root volume", 4096, 33554432, 29360128, 4),
        (31, "Data volume", 65536, 33554432, 16777216, 4),
        (42, "Backup volume", 4096, 134217728, 125829120, 4),
        (99, "Unavailable size", 4096, 0, 0, 4),
    ]
    records = [
        "1.3.6.1.2.1.1.1.0|4|Synthetic storage notebook agent",
        "1.3.6.1.2.1.1.5.0|4|invented-storage-host",
        "1.3.6.1.2.1.1.3.0|67|8640000",
    ]
    for index, label, allocation, size, used, kind in rows:
        fields = [
            (1, 2, index),
            (2, 6, f"1.3.6.1.2.1.25.2.1.{kind}"),
            (3, 4, label),
            (4, 2, allocation),
            (5, 2, size),
            (6, 2, used),
        ]
        for column, tag, value in fields:
            records.append(f"1.3.6.1.2.1.25.2.3.1.{column}.{index}|{tag}|{value}")
    records.sort(key=lambda line: tuple(map(int, line.split("|", 1)[0].split("."))))
    target = folder / "public.snmprec"
    target.write_text("\n".join(records) + "\n")
    manifest = {
        "provenance": "All labels, counts and uptime invented for this notebook; no device capture.",
        "format": "snmpsim snmprec numeric OID | ASN.1 tag | value",
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "rows": len(rows),
        "allocation_unit": "bytes per allocation unit",
        "size_and_used_units": "allocation units",
        "uptime_unit": "hundredths of a second",
        "time": "Static synthetic fixture; no observation timestamp or rate inference.",
    }
    (folder / "provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
