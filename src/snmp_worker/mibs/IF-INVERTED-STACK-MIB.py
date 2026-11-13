# SNMP MIB module (IF-INVERTED-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IF-INVERTED-STACK-MIB
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

(ifStackGroup2,
 ifStackHigherLayer,
 ifStackLowerLayer) = mibBuilder.import_symbols(
    "IF-MIB",
    "ifStackGroup2",
    "ifStackHigherLayer",
    "ifStackLowerLayer")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.import_symbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ifInvertedStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 77)
)
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setRevisions(
        ("2000-06-14 00:00",)
    )
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setLastUpdated("200006140000Z")
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setOrganization("IETF Interfaces MIB Working Group")
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setContactInfo(" Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US 408-526-5260 kzm@cisco.com")
if mibBuilder.loadTexts:
    ifInvertedStackMIB.setDescription("The MIB module which provides the Inverted Stack Table for interface sub-layers.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfInvMIBObjects_ObjectIdentity = ObjectIdentity
ifInvMIBObjects = _IfInvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1)
)
_IfInvStackTable_Object = MibTable
ifInvStackTable = _IfInvStackTable_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1)
)
if mibBuilder.loadTexts:
    ifInvStackTable.setStatus("current")
if mibBuilder.loadTexts:
    ifInvStackTable.setReference("ifStackTable of RFC 2863")
if mibBuilder.loadTexts:
    ifInvStackTable.setDescription("A table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'underneath' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs underneath the sub-layer with ifIndex value y, then this table contains: ifInvStackStatus.x.y=active For each ifIndex value, z, which identifies an active interface, there are always at least two instantiated rows in this table associated with z. For one of these rows, z is the value of ifStackHigherLayer; for the other, z is the value of ifStackLowerLayer. (If z is not involved in multiplexing, then these are the only two rows associated with z.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifInvStackStatus.z.0=active ifInvStackStatus.0.z=active This table contains exactly the same number of rows as the ifStackTable, but the rows appear in a different order.")
_IfInvStackEntry_Object = MibTableRow
ifInvStackEntry = _IfInvStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1, 1)
)
ifInvStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    ifInvStackEntry.setStatus("current")
if mibBuilder.loadTexts:
    ifInvStackEntry.setDescription("Information on a particular relationship between two sub- layers, specifying that one sub-layer runs underneath the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.")
_IfInvStackStatus_Type = RowStatus
_IfInvStackStatus_Object = MibTableColumn
ifInvStackStatus = _IfInvStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1),
    _IfInvStackStatus_Type()
)
ifInvStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInvStackStatus.setStatus("current")
if mibBuilder.loadTexts:
    ifInvStackStatus.setDescription("The status of the relationship between two sub-layers. An instance of this object exists for each instance of the ifStackStatus object, and vice versa. For example, if the variable ifStackStatus.H.L exists, then the variable ifInvStackStatus.L.H must also exist, and vice versa. In addition, the two variables always have the same value. However, unlike ifStackStatus, the ifInvStackStatus object is NOT write-able. A network management application wishing to change a relationship between sub-layers H and L cannot do so by modifying the value of ifInvStackStatus.L.H, but must instead modify the value of ifStackStatus.H.L. After the ifStackTable is modified, the change will be reflected in this table.")
_IfInvConformance_ObjectIdentity = ObjectIdentity
ifInvConformance = _IfInvConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2)
)
_IfInvGroups_ObjectIdentity = ObjectIdentity
ifInvGroups = _IfInvGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 1)
)
_IfInvCompliances_ObjectIdentity = ObjectIdentity
ifInvCompliances = _IfInvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 2)
)

# Managed Objects groups

ifInvStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)
)
ifInvStackGroup.setObjects(
    ("IF-INVERTED-STACK-MIB", "ifInvStackStatus")
)
if mibBuilder.loadTexts:
    ifInvStackGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifInvStackGroup.setDescription("A collection of objects providing inverted information on the layering of MIB-II interfaces.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifInvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)
)
ifInvCompliance.setObjects(
      *(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"),
        ("IF-MIB", "ifStackGroup2"))
)
if mibBuilder.loadTexts:
    ifInvCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ifInvCompliance.setDescription("The compliance statement for SNMP entities which provide inverted information on the layering of network interfaces.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "IF-INVERTED-STACK-MIB",
    **{"ifInvertedStackMIB": ifInvertedStackMIB,
       "ifInvMIBObjects": ifInvMIBObjects,
       "ifInvStackTable": ifInvStackTable,
       "ifInvStackEntry": ifInvStackEntry,
       "ifInvStackStatus": ifInvStackStatus,
       "ifInvConformance": ifInvConformance,
       "ifInvGroups": ifInvGroups,
       "ifInvStackGroup": ifInvStackGroup,
       "ifInvCompliances": ifInvCompliances,
       "ifInvCompliance": ifInvCompliance}
)
