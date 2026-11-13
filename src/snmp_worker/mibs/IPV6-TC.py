# SNMP MIB module (IPV6-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IPV6-TC
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6Address(TextualConvention, OctetString):
    status = "obsolete"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16

    if mibBuilder.loadTexts:
        description = "This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order. This object is obsoleted by INET-ADDRESS-MIB::InetAddress."


class Ipv6AddressPrefix(TextualConvention, OctetString):
    status = "obsolete"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )

    if mibBuilder.loadTexts:
        description = "This data type is used to model IPv6 address prefixes. This is a binary string of up to 16 octets in network byte-order. This object is obsoleted by INET-ADDRESS-MIB::InetAddress."


class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    status = "obsolete"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )

    if mibBuilder.loadTexts:
        description = "This data type is used to model IPv6 address interface identifiers. This is a binary string of up to 8 octets in network byte-order. This object is obsoleted by IP-MIB::Ipv6AddressIfIdentifierTC."


class Ipv6IfIndex(TextualConvention, Integer32):
    status = "obsolete"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = "A unique value, greater than zero for each internetwork-layer interface in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each internetwork-layer interface must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization. This object is obsoleted by IF-MIB::InterfaceIndex."


class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    status = "obsolete"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = "This textual convention is an extension of the Ipv6IfIndex convention. The latter defines a greater than zero value used to identify an IPv6 interface in the managed system. This extension permits the additional value of zero. The value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where interface was unknown, or when none or all interfaces need to be referenced. This object is obsoleted by IF-MIB::InterfaceIndexOrZero."


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "IPV6-TC",
    **{"Ipv6Address": Ipv6Address,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "Ipv6AddressIfIdentifier": Ipv6AddressIfIdentifier,
       "Ipv6IfIndex": Ipv6IfIndex,
       "Ipv6IfIndexOrZero": Ipv6IfIndexOrZero}
)
