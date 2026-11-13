# SNMP MIB module (IANA-RTPROTO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IANA-RTPROTO-MIB
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
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaRtProtoMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 84)
)
if mibBuilder.loadTexts:
    ianaRtProtoMIB.setRevisions(
        ("2016-04-25 00:00",
         "2016-04-06 00:00",
         "2012-08-30 00:00",
         "2011-07-22 00:00",
         "2000-09-26 00:00")
    )
if mibBuilder.loadTexts:
    ianaRtProtoMIB.setLastUpdated("201604250000Z")
if mibBuilder.loadTexts:
    ianaRtProtoMIB.setOrganization("IANA")
if mibBuilder.loadTexts:
    ianaRtProtoMIB.setContactInfo(" Internet Assigned Numbers Authority Internet Corporation for Assigned Names and Numbers 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Phone: +1 310 301 5800 EMail: iana&iana.org")
if mibBuilder.loadTexts:
    ianaRtProtoMIB.setDescription("This MIB module defines the IANAipRouteProtocol and IANAipMRouteProtocol textual conventions for use in MIBs which need to identify unicast or multicast routing mechanisms. Any additions or changes to the contents of this MIB module require either publication of an RFC, or Designated Expert Review as defined in RFC 2434, Guidelines for Writing an IANA Considerations Section in RFCs. The Designated Expert will be selected by the IESG Area Director(s) of the Routing Area.")


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAipRouteProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("dvmrp", 17),
          ("rpl", 18),
          ("dhcp", 19),
          ("ttdp", 20))
    )

    if mibBuilder.loadTexts:
        description = "A mechanism for learning routes. Inclusion of values for routing protocols is not intended to imply that those protocols need be supported."


class IANAipMRouteProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("dvmrp", 4),
          ("mospf", 5),
          ("pimSparseDense", 6),
          ("cbt", 7),
          ("pimSparseMode", 8),
          ("pimDenseMode", 9),
          ("igmpOnly", 10),
          ("bgmp", 11),
          ("msdp", 12))
    )

    if mibBuilder.loadTexts:
        description = "The multicast routing protocol. Inclusion of values for multicast routing protocols is not intended to imply that those protocols need be supported."


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "IANA-RTPROTO-MIB",
    **{"IANAipRouteProtocol": IANAipRouteProtocol,
       "IANAipMRouteProtocol": IANAipMRouteProtocol,
       "ianaRtProtoMIB": ianaRtProtoMIB}
)
