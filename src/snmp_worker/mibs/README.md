# Pre-compiled MIB modules

These files are generated, not hand-written: pysmi translated each MIB's ASN.1 source
into the pysnmp data model, keeping DESCRIPTION/UNITS texts. The worker loads them with
`pysnmp.smi.builder.DirMibSource` on top of the modules that ship with pysnmp.

Regenerate (sources from <https://mibs.pysnmp.com/asn1/>):

```bash
uvx --from pysmi mibdump --mib-source 'https://mibs.pysnmp.com/asn1/@mib@' \
    --mib-searcher "$(python -c 'import pysnmp.smi.mibs, os; print(os.path.dirname(pysnmp.smi.mibs.__file__))')" \
    --destination-directory src/snmp_worker/mibs --no-python-compile --generate-mib-texts \
    IF-MIB IP-MIB TCP-MIB UDP-MIB HOST-RESOURCES-MIB HOST-RESOURCES-TYPES ENTITY-SENSOR-MIB \
    EtherLike-MIB IP-FORWARD-MIB UCD-SNMP-MIB NET-SNMP-MIB NET-SNMP-AGENT-MIB DISMAN-EVENT-MIB \
    IPV6-MIB IF-INVERTED-STACK-MIB
# then: drop the per-host header lines, and rename mibBuilder.importSymbols/exportSymbols
# to import_symbols/export_symbols (pysnmp 7 deprecates the camelCase names).
```

BRIDGE-MIB, Q-BRIDGE-MIB and LLDP-MIB are not included: the sources at mibs.pysnmp.com
import RFC-1212 macros that pysmi fails to parse.

## Provenance and terms

| Modules | Source |
|---|---|
| IF-MIB, IP-MIB, IP-FORWARD-MIB, IPV6-MIB, IPV6-TC, TCP-MIB, UDP-MIB, HOST-RESOURCES-MIB, HOST-RESOURCES-TYPES, ENTITY-MIB, ENTITY-SENSOR-MIB, EtherLike-MIB, DISMAN-EVENT-MIB, IF-INVERTED-STACK-MIB, HCNUM-TC, UUID-TC-MIB, SNMPv2-MIB | IETF RFCs. Code components of IETF documents are licensed under the Simplified BSD License (IETF Trust Legal Provisions, section 4). |
| IANAifType-MIB, IANA-ENTITY-MIB, IANA-RTPROTO-MIB | IANA-maintained registries. |
| UCD-SNMP-MIB, NET-SNMP-MIB, NET-SNMP-AGENT-MIB | The Net-SNMP project, under its BSD-style license. |
