# SNMP MIB module (HCNUM-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/HCNUM-TC
# Produced by pysmi-2.0.0 (pysmi mibdump --generate-mib-texts)

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.import_symbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.import_symbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.import_symbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter64,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.import_symbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter64",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hcnumTC = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 78)
)
if mibBuilder.loadTexts:
    hcnumTC.setRevisions(
        ("2000-06-08 00:00",)
    )
if mibBuilder.loadTexts:
    hcnumTC.setLastUpdated("200006080000Z")
if mibBuilder.loadTexts:
    hcnumTC.setOrganization("IETF OPS Area")
if mibBuilder.loadTexts:
    hcnumTC.setContactInfo(" E-mail: mibs@ops.ietf.org Subscribe: majordomo@psg.com with msg body: subscribe mibs Andy Bierman Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 USA +1 408-527-3711 abierman@cisco.com Keith McCloghrie Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 USA +1 408-526-5260 kzm@cisco.com Randy Presuhn BMC Software, Inc. Office 1-3141 2141 North First Street San Jose, California 95131 USA +1 408 546-1006 rpresuhn@bmc.com")
if mibBuilder.loadTexts:
    hcnumTC.setDescription("A MIB module containing textual conventions for high capacity data types. This module addresses an immediate need for data types not directly supported in the SMIv2. This short-term solution is meant to be deprecated as a long-term solution is deployed.")


# Types definitions


# TEXTUAL-CONVENTIONS



class CounterBasedGauge64(TextualConvention, Counter64):
    status = "current"
    if mibBuilder.loadTexts:
        description = "The CounterBasedGauge64 type represents a non-negative integer, which may increase or decrease, but shall never exceed a maximum value, nor fall below a minimum value. The maximum value can not be greater than 2^64-1 (18446744073709551615 decimal), and the minimum value can not be smaller than 0. The value of a CounterBasedGauge64 has its maximum value whenever the information being modeled is greater than or equal to its maximum value, and has its minimum value whenever the information being modeled is smaller than or equal to its minimum value. If the information being modeled subsequently decreases below (increases above) the maximum (minimum) value, the CounterBasedGauge64 also decreases (increases). Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short-term solution, and may be deprecated as a long term solution is defined and deployed to replace it."


class ZeroBasedCounter64(TextualConvention, Counter64):
    status = "current"
    if mibBuilder.loadTexts:
        description = "This TC describes an object which counts events with the following semantics: objects of this type will be set to zero(0) on creation and will thereafter count appropriate events, wrapping back to zero(0) when the value 2^64 is reached. Provided that an application discovers the new object within the minimum time to wrap it can use the initial value as a delta since it last polled the table of which this object is part. It is important for a management station to be aware of this minimum time and the actual time between polls, and to discard data if the actual time is too long or there is no defined minimum time. Typically this TC is used in tables where the INDEX space is constantly changing and/or the TimeFilter mechanism is in use. Note that this textual convention does not retain all the semantics of the Counter64 base type. Specifically, a Counter64 has an arbitrary initial value, but objects defined with this TC are required to start at the value zero. This behavior is not likely to have any adverse effects on management applications which are expecting Counter64 semantics. This textual convention represents a limited and short-term solution, and may be deprecated as a long term solution is defined and deployed to replace it."


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "HCNUM-TC",
    **{"CounterBasedGauge64": CounterBasedGauge64,
       "ZeroBasedCounter64": ZeroBasedCounter64,
       "hcnumTC": hcnumTC}
)
