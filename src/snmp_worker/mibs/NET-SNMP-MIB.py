# SNMP MIB module (NET-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/NET-SNMP-MIB
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
 enterprises,
 iso) = mibBuilder.import_symbols(
    "SNMPv2-SMI",
    "Bits",
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072)
)
if mibBuilder.loadTexts:
    netSnmp.setRevisions(
        ("2002-01-30 00:00",)
    )
if mibBuilder.loadTexts:
    netSnmp.setLastUpdated("200201300000Z")
if mibBuilder.loadTexts:
    netSnmp.setOrganization("www.net-snmp.org")
if mibBuilder.loadTexts:
    netSnmp.setContactInfo("postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts:
    netSnmp.setDescription("Top-level infrastructure of the Net-SNMP project enterprise MIB tree")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetSnmpObjects_ObjectIdentity = ObjectIdentity
netSnmpObjects = _NetSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1)
)
_NetSnmpEnumerations_ObjectIdentity = ObjectIdentity
netSnmpEnumerations = _NetSnmpEnumerations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3)
)
_NetSnmpModuleIDs_ObjectIdentity = ObjectIdentity
netSnmpModuleIDs = _NetSnmpModuleIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1)
)
_NetSnmpAgentOIDs_ObjectIdentity = ObjectIdentity
netSnmpAgentOIDs = _NetSnmpAgentOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2)
)
_NetSnmpDomains_ObjectIdentity = ObjectIdentity
netSnmpDomains = _NetSnmpDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3)
)
_NetSnmpNotificationPrefix_ObjectIdentity = ObjectIdentity
netSnmpNotificationPrefix = _NetSnmpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 4)
)
_NetSnmpNotifications_ObjectIdentity = ObjectIdentity
netSnmpNotifications = _NetSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0)
)
_NetSnmpNotificationObjects_ObjectIdentity = ObjectIdentity
netSnmpNotificationObjects = _NetSnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 4, 1)
)
_NetSnmpConformance_ObjectIdentity = ObjectIdentity
netSnmpConformance = _NetSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 5)
)
_NetSnmpCompliances_ObjectIdentity = ObjectIdentity
netSnmpCompliances = _NetSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 5, 1)
)
_NetSnmpGroups_ObjectIdentity = ObjectIdentity
netSnmpGroups = _NetSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2)
)
_NetSnmpExperimental_ObjectIdentity = ObjectIdentity
netSnmpExperimental = _NetSnmpExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 9999)
)
_NetSnmpPlaypen_ObjectIdentity = ObjectIdentity
netSnmpPlaypen = _NetSnmpPlaypen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 9999, 9999)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "NET-SNMP-MIB",
    **{"netSnmp": netSnmp,
       "netSnmpObjects": netSnmpObjects,
       "netSnmpEnumerations": netSnmpEnumerations,
       "netSnmpModuleIDs": netSnmpModuleIDs,
       "netSnmpAgentOIDs": netSnmpAgentOIDs,
       "netSnmpDomains": netSnmpDomains,
       "netSnmpNotificationPrefix": netSnmpNotificationPrefix,
       "netSnmpNotifications": netSnmpNotifications,
       "netSnmpNotificationObjects": netSnmpNotificationObjects,
       "netSnmpConformance": netSnmpConformance,
       "netSnmpCompliances": netSnmpCompliances,
       "netSnmpGroups": netSnmpGroups,
       "netSnmpExperimental": netSnmpExperimental,
       "netSnmpPlaypen": netSnmpPlaypen}
)
