# SNMP MIB module (IP-FORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IP-FORWARD-MIB
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

(IANAipRouteProtocol,) = mibBuilder.import_symbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndexOrZero,) = mibBuilder.import_symbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.import_symbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(ip,) = mibBuilder.import_symbols(
    "IP-MIB",
    "ip")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Gauge32,
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
    "Counter32",
    "Gauge32",
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
 RowStatus,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipForward = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24)
)
if mibBuilder.loadTexts:
    ipForward.setRevisions(
        ("2006-02-01 00:00",
         "1996-09-19 00:00",
         "1992-07-02 21:56")
    )
if mibBuilder.loadTexts:
    ipForward.setLastUpdated("200602010000Z")
if mibBuilder.loadTexts:
    ipForward.setOrganization("IETF IPv6 Working Group http://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts:
    ipForward.setContactInfo("Editor: Brian Haberman Johns Hopkins University - Applied Physics Laboratory Mailstop 17-S442 11100 Johns Hopkins Road Laurel MD, 20723-6099 USA Phone: +1-443-778-1319 Email: brian@innovationslab.net Send comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts:
    ipForward.setDescription("The MIB module for the management of CIDR multipath IP Routes. Copyright (C) The Internet Society (2006). This version of this MIB module is a part of RFC 4292; see the RFC itself for full legal notices.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpForwardNumber_Type = Gauge32
_IpForwardNumber_Object = MibScalar
ipForwardNumber = _IpForwardNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 1),
    _IpForwardNumber_Type()
)
ipForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNumber.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardNumber.setDescription("The number of current ipForwardTable entries that are not invalid.")
_IpForwardTable_Object = MibTable
ipForwardTable = _IpForwardTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2)
)
if mibBuilder.loadTexts:
    ipForwardTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardTable.setReference("RFC 1213 Section 6.6, The IP Group")
if mibBuilder.loadTexts:
    ipForwardTable.setDescription("This entity's IP Routing table.")
_IpForwardEntry_Object = MibTableRow
ipForwardEntry = _IpForwardEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1)
)
ipForwardEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "ipForwardDest"),
    (0, "IP-FORWARD-MIB", "ipForwardProto"),
    (0, "IP-FORWARD-MIB", "ipForwardPolicy"),
    (0, "IP-FORWARD-MIB", "ipForwardNextHop"),
)
if mibBuilder.loadTexts:
    ipForwardEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardEntry.setDescription("A particular route to a particular destination, under a particular policy.")
_IpForwardDest_Type = IpAddress
_IpForwardDest_Object = MibTableColumn
ipForwardDest = _IpForwardDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 1),
    _IpForwardDest_Type()
)
ipForwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardDest.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardDest.setDescription("The destination IP address of this route. An entry with a value of 0.0.0.0 is considered a default route. This object may not take a Multicast (Class D) address value. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the ipForwardMask object is not equal to x.")


class _IpForwardMask_Type(IpAddress):
    """Custom type ipForwardMask based on IpAddress"""
    defaultHexValue = "00000000"


_IpForwardMask_Type.__name__ = "IpAddress"
_IpForwardMask_Object = MibTableColumn
ipForwardMask = _IpForwardMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 2),
    _IpForwardMask_Type()
)
ipForwardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMask.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMask.setDescription("Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the ipForwardDest field. For those systems that do not support arbitrary subnet masks, an agent constructs the value of the ipForwardMask by reference to the IP Address Class. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the ipForwardDest object is not equal to ipForwardDest.")


class _IpForwardPolicy_Type(Integer32):
    """Custom type ipForwardPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpForwardPolicy_Type.__name__ = "Integer32"
_IpForwardPolicy_Object = MibTableColumn
ipForwardPolicy = _IpForwardPolicy_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 3),
    _IpForwardPolicy_Type()
)
ipForwardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardPolicy.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardPolicy.setDescription("The general set of conditions that would cause the selection of one multipath route (set of next hops for a given destination) is referred to as 'policy'. Unless the mechanism indicated by ipForwardProto specifies otherwise, the policy specifier is the IP TOS Field. The encoding of IP TOS is as specified by the following convention. Zero indicates the default path if no more specific policy applies. +-----+-----+-----+-----+-----+-----+-----+-----+ | | | | | PRECEDENCE | TYPE OF SERVICE | 0 | | | | | +-----+-----+-----+-----+-----+-----+-----+-----+ IP TOS IP TOS Field Policy Field Policy Contents Code Contents Code 0 0 0 0 ==> 0 0 0 0 1 ==> 2 0 0 1 0 ==> 4 0 0 1 1 ==> 6 0 1 0 0 ==> 8 0 1 0 1 ==> 10 0 1 1 0 ==> 12 0 1 1 1 ==> 14 1 0 0 0 ==> 16 1 0 0 1 ==> 18 1 0 1 0 ==> 20 1 0 1 1 ==> 22 1 1 0 0 ==> 24 1 1 0 1 ==> 26 1 1 1 0 ==> 28 1 1 1 1 ==> 30 Protocols defining 'policy' otherwise must either define a set of values that are valid for this object or must implement an integer-instanced policy table for which this object's value acts as an index.")
_IpForwardNextHop_Type = IpAddress
_IpForwardNextHop_Object = MibTableColumn
ipForwardNextHop = _IpForwardNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 4),
    _IpForwardNextHop_Type()
)
ipForwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNextHop.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardNextHop.setDescription("On remote routes, the address of the next system en route; otherwise, 0.0.0.0.")


class _IpForwardIfIndex_Type(Integer32):
    """Custom type ipForwardIfIndex based on Integer32"""
    defaultValue = 0


_IpForwardIfIndex_Type.__name__ = "Integer32"
_IpForwardIfIndex_Object = MibTableColumn
ipForwardIfIndex = _IpForwardIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 5),
    _IpForwardIfIndex_Type()
)
ipForwardIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardIfIndex.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardIfIndex.setDescription("The ifIndex value that identifies the local interface through which the next hop of this route should be reached.")


class _IpForwardType_Type(Integer32):
    """Custom type ipForwardType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_IpForwardType_Type.__name__ = "Integer32"
_IpForwardType_Object = MibTableColumn
ipForwardType = _IpForwardType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 6),
    _IpForwardType_Type()
)
ipForwardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardType.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardType.setDescription("The type of route. Note that local(3) refers to a route for which the next hop is the final destination; remote(4) refers to a route for which the next hop is not the final destination. Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipForwardTable object. That is, it effectively disassociates the destination identified with said entry from the route identified with said entry. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipForwardType object.")


class _IpForwardProto_Type(Integer32):
    """Custom type ipForwardProto based on Integer32"""
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
              15)
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
          ("is-is", 9),
          ("es-is", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15))
    )


_IpForwardProto_Type.__name__ = "Integer32"
_IpForwardProto_Object = MibTableColumn
ipForwardProto = _IpForwardProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 7),
    _IpForwardProto_Type()
)
ipForwardProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardProto.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardProto.setDescription("The routing mechanism via which this route was learned. Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols.")


class _IpForwardAge_Type(Integer32):
    """Custom type ipForwardAge based on Integer32"""
    defaultValue = 0


_IpForwardAge_Type.__name__ = "Integer32"
_IpForwardAge_Object = MibTableColumn
ipForwardAge = _IpForwardAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 8),
    _IpForwardAge_Type()
)
ipForwardAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardAge.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardAge.setDescription("The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned.")
_IpForwardInfo_Type = ObjectIdentifier
_IpForwardInfo_Object = MibTableColumn
ipForwardInfo = _IpForwardInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 9),
    _IpForwardInfo_Type()
)
ipForwardInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardInfo.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardInfo.setDescription("A reference to MIB definitions specific to the particular routing protocol that is responsible for this route, as determined by the value specified in the route's ipForwardProto value. If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value.")


class _IpForwardNextHopAS_Type(Integer32):
    """Custom type ipForwardNextHopAS based on Integer32"""
    defaultValue = 0


_IpForwardNextHopAS_Type.__name__ = "Integer32"
_IpForwardNextHopAS_Object = MibTableColumn
ipForwardNextHopAS = _IpForwardNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 10),
    _IpForwardNextHopAS_Type()
)
ipForwardNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardNextHopAS.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardNextHopAS.setDescription("The Autonomous System Number of the Next Hop. When this is unknown or not relevant to the protocol indicated by ipForwardProto, zero.")


class _IpForwardMetric1_Type(Integer32):
    """Custom type ipForwardMetric1 based on Integer32"""
    defaultValue = -1


_IpForwardMetric1_Type.__name__ = "Integer32"
_IpForwardMetric1_Object = MibTableColumn
ipForwardMetric1 = _IpForwardMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 11),
    _IpForwardMetric1_Type()
)
ipForwardMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric1.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMetric1.setDescription("The primary routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipForwardProto value. If this metric is not used, its value should be set to -1.")


class _IpForwardMetric2_Type(Integer32):
    """Custom type ipForwardMetric2 based on Integer32"""
    defaultValue = -1


_IpForwardMetric2_Type.__name__ = "Integer32"
_IpForwardMetric2_Object = MibTableColumn
ipForwardMetric2 = _IpForwardMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 12),
    _IpForwardMetric2_Type()
)
ipForwardMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric2.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMetric2.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipForwardProto value. If this metric is not used, its value should be set to -1.")


class _IpForwardMetric3_Type(Integer32):
    """Custom type ipForwardMetric3 based on Integer32"""
    defaultValue = -1


_IpForwardMetric3_Type.__name__ = "Integer32"
_IpForwardMetric3_Object = MibTableColumn
ipForwardMetric3 = _IpForwardMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 13),
    _IpForwardMetric3_Type()
)
ipForwardMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric3.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMetric3.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipForwardProto value. If this metric is not used, its value should be set to -1.")


class _IpForwardMetric4_Type(Integer32):
    """Custom type ipForwardMetric4 based on Integer32"""
    defaultValue = -1


_IpForwardMetric4_Type.__name__ = "Integer32"
_IpForwardMetric4_Object = MibTableColumn
ipForwardMetric4 = _IpForwardMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 14),
    _IpForwardMetric4_Type()
)
ipForwardMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric4.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMetric4.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipForwardProto value. If this metric is not used, its value should be set to -1.")


class _IpForwardMetric5_Type(Integer32):
    """Custom type ipForwardMetric5 based on Integer32"""
    defaultValue = -1


_IpForwardMetric5_Type.__name__ = "Integer32"
_IpForwardMetric5_Object = MibTableColumn
ipForwardMetric5 = _IpForwardMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 15),
    _IpForwardMetric5_Type()
)
ipForwardMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric5.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMetric5.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipForwardProto value. If this metric is not used, its value should be set to -1.")
_IpCidrRouteNumber_Type = Gauge32
_IpCidrRouteNumber_Object = MibScalar
ipCidrRouteNumber = _IpCidrRouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 3),
    _IpCidrRouteNumber_Type()
)
ipCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteNumber.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteNumber.setDescription("The number of current ipCidrRouteTable entries that are not invalid. This object is deprecated in favor of inetCidrRouteNumber and the inetCidrRouteTable.")
_IpCidrRouteTable_Object = MibTable
ipCidrRouteTable = _IpCidrRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4)
)
if mibBuilder.loadTexts:
    ipCidrRouteTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteTable.setReference("RFC 1213 Section 6.6, The IP Group")
if mibBuilder.loadTexts:
    ipCidrRouteTable.setDescription("This entity's IP Routing table. This table has been deprecated in favor of the IP version neutral inetCidrRouteTable.")
_IpCidrRouteEntry_Object = MibTableRow
ipCidrRouteEntry = _IpCidrRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1)
)
ipCidrRouteEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "ipCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteMask"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteTos"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipCidrRouteEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteEntry.setDescription("A particular route to a particular destination, under a particular policy.")
_IpCidrRouteDest_Type = IpAddress
_IpCidrRouteDest_Object = MibTableColumn
ipCidrRouteDest = _IpCidrRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 1),
    _IpCidrRouteDest_Type()
)
ipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteDest.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteDest.setDescription("The destination IP address of this route. This object may not take a Multicast (Class D) address value. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the ipCidrRouteMask object is not equal to x.")
_IpCidrRouteMask_Type = IpAddress
_IpCidrRouteMask_Object = MibTableColumn
ipCidrRouteMask = _IpCidrRouteMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 2),
    _IpCidrRouteMask_Type()
)
ipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteMask.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMask.setDescription("Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the ipCidrRouteDest field. For those systems that do not support arbitrary subnet masks, an agent constructs the value of the ipCidrRouteMask by reference to the IP Address Class. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the ipCidrRouteDest object is not equal to ipCidrRouteDest.")


class _IpCidrRouteTos_Type(Integer32):
    """Custom type ipCidrRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpCidrRouteTos_Type.__name__ = "Integer32"
_IpCidrRouteTos_Object = MibTableColumn
ipCidrRouteTos = _IpCidrRouteTos_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 3),
    _IpCidrRouteTos_Type()
)
ipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteTos.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteTos.setDescription("The policy specifier is the IP TOS Field. The encoding of IP TOS is as specified by the following convention. Zero indicates the default path if no more specific policy applies. +-----+-----+-----+-----+-----+-----+-----+-----+ | | | | | PRECEDENCE | TYPE OF SERVICE | 0 | | | | | +-----+-----+-----+-----+-----+-----+-----+-----+ IP TOS IP TOS Field Policy Field Policy Contents Code Contents Code 0 0 0 0 ==> 0 0 0 0 1 ==> 2 0 0 1 0 ==> 4 0 0 1 1 ==> 6 0 1 0 0 ==> 8 0 1 0 1 ==> 10 0 1 1 0 ==> 12 0 1 1 1 ==> 14 1 0 0 0 ==> 16 1 0 0 1 ==> 18 1 0 1 0 ==> 20 1 0 1 1 ==> 22 1 1 0 0 ==> 24 1 1 0 1 ==> 26 1 1 1 0 ==> 28 1 1 1 1 ==> 30")
_IpCidrRouteNextHop_Type = IpAddress
_IpCidrRouteNextHop_Object = MibTableColumn
ipCidrRouteNextHop = _IpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 4),
    _IpCidrRouteNextHop_Type()
)
ipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteNextHop.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteNextHop.setDescription("On remote routes, the address of the next system en route; Otherwise, 0.0.0.0.")


class _IpCidrRouteIfIndex_Type(Integer32):
    """Custom type ipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_IpCidrRouteIfIndex_Type.__name__ = "Integer32"
_IpCidrRouteIfIndex_Object = MibTableColumn
ipCidrRouteIfIndex = _IpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 5),
    _IpCidrRouteIfIndex_Type()
)
ipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteIfIndex.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteIfIndex.setDescription("The ifIndex value that identifies the local interface through which the next hop of this route should be reached.")


class _IpCidrRouteType_Type(Integer32):
    """Custom type ipCidrRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_IpCidrRouteType_Type.__name__ = "Integer32"
_IpCidrRouteType_Object = MibTableColumn
ipCidrRouteType = _IpCidrRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 6),
    _IpCidrRouteType_Type()
)
ipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteType.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteType.setDescription("The type of route. Note that local(3) refers to a route for which the next hop is the final destination; remote(4) refers to a route for which the next hop is not the final destination. Routes that do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally. reject (2) refers to a route that, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes.")


class _IpCidrRouteProto_Type(Integer32):
    """Custom type ipCidrRouteProto based on Integer32"""
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
              16)
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
          ("ciscoEigrp", 16))
    )


_IpCidrRouteProto_Type.__name__ = "Integer32"
_IpCidrRouteProto_Object = MibTableColumn
ipCidrRouteProto = _IpCidrRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 7),
    _IpCidrRouteProto_Type()
)
ipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteProto.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteProto.setDescription("The routing mechanism via which this route was learned. Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols.")


class _IpCidrRouteAge_Type(Integer32):
    """Custom type ipCidrRouteAge based on Integer32"""
    defaultValue = 0


_IpCidrRouteAge_Type.__name__ = "Integer32"
_IpCidrRouteAge_Object = MibTableColumn
ipCidrRouteAge = _IpCidrRouteAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 8),
    _IpCidrRouteAge_Type()
)
ipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteAge.setDescription("The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned.")
_IpCidrRouteInfo_Type = ObjectIdentifier
_IpCidrRouteInfo_Object = MibTableColumn
ipCidrRouteInfo = _IpCidrRouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 9),
    _IpCidrRouteInfo_Type()
)
ipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteInfo.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteInfo.setDescription("A reference to MIB definitions specific to the particular routing protocol that is responsible for this route, as determined by the value specified in the route's ipCidrRouteProto value. If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value.")


class _IpCidrRouteNextHopAS_Type(Integer32):
    """Custom type ipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_IpCidrRouteNextHopAS_Type.__name__ = "Integer32"
_IpCidrRouteNextHopAS_Object = MibTableColumn
ipCidrRouteNextHopAS = _IpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 10),
    _IpCidrRouteNextHopAS_Type()
)
ipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteNextHopAS.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteNextHopAS.setDescription("The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing- protocol specified in the route's ipCidrRouteProto value. When this object is unknown or not relevant its value should be set to zero.")


class _IpCidrRouteMetric1_Type(Integer32):
    """Custom type ipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric1_Type.__name__ = "Integer32"
_IpCidrRouteMetric1_Object = MibTableColumn
ipCidrRouteMetric1 = _IpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 11),
    _IpCidrRouteMetric1_Type()
)
ipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric1.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMetric1.setDescription("The primary routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _IpCidrRouteMetric2_Type(Integer32):
    """Custom type ipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric2_Type.__name__ = "Integer32"
_IpCidrRouteMetric2_Object = MibTableColumn
ipCidrRouteMetric2 = _IpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 12),
    _IpCidrRouteMetric2_Type()
)
ipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric2.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMetric2.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _IpCidrRouteMetric3_Type(Integer32):
    """Custom type ipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric3_Type.__name__ = "Integer32"
_IpCidrRouteMetric3_Object = MibTableColumn
ipCidrRouteMetric3 = _IpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 13),
    _IpCidrRouteMetric3_Type()
)
ipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric3.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMetric3.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _IpCidrRouteMetric4_Type(Integer32):
    """Custom type ipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric4_Type.__name__ = "Integer32"
_IpCidrRouteMetric4_Object = MibTableColumn
ipCidrRouteMetric4 = _IpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 14),
    _IpCidrRouteMetric4_Type()
)
ipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric4.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMetric4.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _IpCidrRouteMetric5_Type(Integer32):
    """Custom type ipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric5_Type.__name__ = "Integer32"
_IpCidrRouteMetric5_Object = MibTableColumn
ipCidrRouteMetric5 = _IpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 15),
    _IpCidrRouteMetric5_Type()
)
ipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric5.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteMetric5.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's ipCidrRouteProto value. If this metric is not used, its value should be set to -1.")
_IpCidrRouteStatus_Type = RowStatus
_IpCidrRouteStatus_Object = MibTableColumn
ipCidrRouteStatus = _IpCidrRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 16),
    _IpCidrRouteStatus_Type()
)
ipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteStatus.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipCidrRouteStatus.setDescription("The row status variable, used according to row installation and removal conventions.")
_IpForwardConformance_ObjectIdentity = ObjectIdentity
ipForwardConformance = _IpForwardConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5)
)
_IpForwardGroups_ObjectIdentity = ObjectIdentity
ipForwardGroups = _IpForwardGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1)
)
_IpForwardCompliances_ObjectIdentity = ObjectIdentity
ipForwardCompliances = _IpForwardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2)
)
_InetCidrRouteNumber_Type = Gauge32
_InetCidrRouteNumber_Object = MibScalar
inetCidrRouteNumber = _InetCidrRouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 6),
    _InetCidrRouteNumber_Type()
)
inetCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteNumber.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteNumber.setDescription("The number of current inetCidrRouteTable entries that are not invalid.")
_InetCidrRouteTable_Object = MibTable
inetCidrRouteTable = _InetCidrRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7)
)
if mibBuilder.loadTexts:
    inetCidrRouteTable.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteTable.setReference("RFC 1213 Section 6.6, The IP Group")
if mibBuilder.loadTexts:
    inetCidrRouteTable.setDescription("This entity's IP Routing table.")
_InetCidrRouteEntry_Object = MibTableRow
inetCidrRouteEntry = _InetCidrRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1)
)
inetCidrRouteEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "inetCidrRouteDestType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    inetCidrRouteEntry.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteEntry.setDescription("A particular route to a particular destination, under a particular policy (as reflected in the inetCidrRoutePolicy object). Dynamically created rows will survive an agent reboot. Implementers need to be aware that if the total number of elements (octets or sub-identifiers) in inetCidrRouteDest, inetCidrRoutePolicy, and inetCidrRouteNextHop exceeds 111 then OIDs of column instances in this table will have more than 128 sub- identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_InetCidrRouteDestType_Type = InetAddressType
_InetCidrRouteDestType_Object = MibTableColumn
inetCidrRouteDestType = _InetCidrRouteDestType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 1),
    _InetCidrRouteDestType_Type()
)
inetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteDestType.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteDestType.setReference("RFC 4001")
if mibBuilder.loadTexts:
    inetCidrRouteDestType.setDescription("The type of the inetCidrRouteDest address, as defined in the InetAddress MIB. Only those address types that may appear in an actual routing table are allowed as values of this object.")
_InetCidrRouteDest_Type = InetAddress
_InetCidrRouteDest_Object = MibTableColumn
inetCidrRouteDest = _InetCidrRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 2),
    _InetCidrRouteDest_Type()
)
inetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteDest.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteDest.setDescription("The destination IP address of this route. The type of this address is determined by the value of the inetCidrRouteDestType object. The values for the index objects inetCidrRouteDest and inetCidrRoutePfxLen must be consistent. When the value of inetCidrRouteDest (excluding the zone index, if one is present) is x, then the bitwise logical-AND of x with the value of the mask formed from the corresponding index object inetCidrRoutePfxLen MUST be equal to x. If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests.")
_InetCidrRoutePfxLen_Type = InetAddressPrefixLength
_InetCidrRoutePfxLen_Object = MibTableColumn
inetCidrRoutePfxLen = _InetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 3),
    _InetCidrRoutePfxLen_Type()
)
inetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRoutePfxLen.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRoutePfxLen.setDescription("Indicates the number of leading one bits which form the mask to be logical-ANDed with the destination address before being compared to the value in the inetCidrRouteDest field. The values for the index objects inetCidrRouteDest and inetCidrRoutePfxLen must be consistent. When the value of inetCidrRouteDest (excluding the zone index, if one is present) is x, then the bitwise logical-AND of x with the value of the mask formed from the corresponding index object inetCidrRoutePfxLen MUST be equal to x. If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests.")
_InetCidrRoutePolicy_Type = ObjectIdentifier
_InetCidrRoutePolicy_Object = MibTableColumn
inetCidrRoutePolicy = _InetCidrRoutePolicy_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 4),
    _InetCidrRoutePolicy_Type()
)
inetCidrRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRoutePolicy.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRoutePolicy.setDescription("This object is an opaque object without any defined semantics. Its purpose is to serve as an additional index that may delineate between multiple entries to the same destination. The value { 0 0 } shall be used as the default value for this object.")
_InetCidrRouteNextHopType_Type = InetAddressType
_InetCidrRouteNextHopType_Object = MibTableColumn
inetCidrRouteNextHopType = _InetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 5),
    _InetCidrRouteNextHopType_Type()
)
inetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopType.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopType.setReference("RFC 4001")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopType.setDescription("The type of the inetCidrRouteNextHop address, as defined in the InetAddress MIB. Value should be set to unknown(0) for non-remote routes. Only those address types that may appear in an actual routing table are allowed as values of this object.")
_InetCidrRouteNextHop_Type = InetAddress
_InetCidrRouteNextHop_Object = MibTableColumn
inetCidrRouteNextHop = _InetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 6),
    _InetCidrRouteNextHop_Type()
)
inetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteNextHop.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteNextHop.setDescription("On remote routes, the address of the next system en route. For non-remote routes, a zero length string. The type of this address is determined by the value of the inetCidrRouteNextHopType object.")
_InetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_InetCidrRouteIfIndex_Object = MibTableColumn
inetCidrRouteIfIndex = _InetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 7),
    _InetCidrRouteIfIndex_Type()
)
inetCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteIfIndex.setDescription("The ifIndex value that identifies the local interface through which the next hop of this route should be reached. A value of 0 is valid and represents the scenario where no interface is specified.")


class _InetCidrRouteType_Type(Integer32):
    """Custom type inetCidrRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4),
          ("blackhole", 5))
    )


_InetCidrRouteType_Type.__name__ = "Integer32"
_InetCidrRouteType_Object = MibTableColumn
inetCidrRouteType = _InetCidrRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 8),
    _InetCidrRouteType_Type()
)
inetCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteType.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteType.setDescription("The type of route. Note that local(3) refers to a route for which the next hop is the final destination; remote(4)refers to a route for which the next hop is not the final destination. Routes that do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally. reject(2) refers to a route that, if matched, discards the message as unreachable and returns a notification (e.g. ICMP error) to the message sender. This is used in some protocols as a means of correctly aggregating routes. blackhole(5) refers to a route which, if matched, discards the message silently.")
_InetCidrRouteProto_Type = IANAipRouteProtocol
_InetCidrRouteProto_Object = MibTableColumn
inetCidrRouteProto = _InetCidrRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 9),
    _InetCidrRouteProto_Type()
)
inetCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteProto.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteProto.setDescription("The routing mechanism via which this route was learned. Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols.")
_InetCidrRouteAge_Type = Gauge32
_InetCidrRouteAge_Object = MibTableColumn
inetCidrRouteAge = _InetCidrRouteAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 10),
    _InetCidrRouteAge_Type()
)
inetCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteAge.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteAge.setDescription("The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of 'too old' can be implied except through knowledge of the routing protocol by which the route was learned.")


class _InetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type inetCidrRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_InetCidrRouteNextHopAS_Type.__name__ = "InetAutonomousSystemNumber"
_InetCidrRouteNextHopAS_Object = MibTableColumn
inetCidrRouteNextHopAS = _InetCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 11),
    _InetCidrRouteNextHopAS_Type()
)
inetCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopAS.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopAS.setDescription("The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing- protocol specified in the route's inetCidrRouteProto value. When this object is unknown or not relevant its value should be set to zero.")


class _InetCidrRouteMetric1_Type(Integer32):
    """Custom type inetCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric1_Type.__name__ = "Integer32"
_InetCidrRouteMetric1_Object = MibTableColumn
inetCidrRouteMetric1 = _InetCidrRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 12),
    _InetCidrRouteMetric1_Type()
)
inetCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric1.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteMetric1.setDescription("The primary routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's inetCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _InetCidrRouteMetric2_Type(Integer32):
    """Custom type inetCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric2_Type.__name__ = "Integer32"
_InetCidrRouteMetric2_Object = MibTableColumn
inetCidrRouteMetric2 = _InetCidrRouteMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 13),
    _InetCidrRouteMetric2_Type()
)
inetCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric2.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteMetric2.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's inetCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _InetCidrRouteMetric3_Type(Integer32):
    """Custom type inetCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric3_Type.__name__ = "Integer32"
_InetCidrRouteMetric3_Object = MibTableColumn
inetCidrRouteMetric3 = _InetCidrRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 14),
    _InetCidrRouteMetric3_Type()
)
inetCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric3.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteMetric3.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's inetCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _InetCidrRouteMetric4_Type(Integer32):
    """Custom type inetCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric4_Type.__name__ = "Integer32"
_InetCidrRouteMetric4_Object = MibTableColumn
inetCidrRouteMetric4 = _InetCidrRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 15),
    _InetCidrRouteMetric4_Type()
)
inetCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric4.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteMetric4.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's inetCidrRouteProto value. If this metric is not used, its value should be set to -1.")


class _InetCidrRouteMetric5_Type(Integer32):
    """Custom type inetCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric5_Type.__name__ = "Integer32"
_InetCidrRouteMetric5_Object = MibTableColumn
inetCidrRouteMetric5 = _InetCidrRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 16),
    _InetCidrRouteMetric5_Type()
)
inetCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric5.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteMetric5.setDescription("An alternate routing metric for this route. The semantics of this metric are determined by the routing- protocol specified in the route's inetCidrRouteProto value. If this metric is not used, its value should be set to -1.")
_InetCidrRouteStatus_Type = RowStatus
_InetCidrRouteStatus_Object = MibTableColumn
inetCidrRouteStatus = _InetCidrRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 17),
    _InetCidrRouteStatus_Type()
)
inetCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteStatus.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteStatus.setDescription("The row status variable, used according to row installation and removal conventions. A row entry cannot be modified when the status is marked as active(1).")
_InetCidrRouteDiscards_Type = Counter32
_InetCidrRouteDiscards_Object = MibScalar
inetCidrRouteDiscards = _InetCidrRouteDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 8),
    _InetCidrRouteDiscards_Type()
)
inetCidrRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteDiscards.setStatus("current")
if mibBuilder.loadTexts:
    inetCidrRouteDiscards.setDescription("The number of valid route entries discarded from the inetCidrRouteTable. Discarded route entries do not appear in the inetCidrRouteTable. One possible reason for discarding an entry would be to free-up buffer space for other route table entries.")

# Managed Objects groups

ipForwardMultiPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 2)
)
ipForwardMultiPathGroup.setObjects(
      *(("IP-FORWARD-MIB", "ipForwardNumber"),
        ("IP-FORWARD-MIB", "ipForwardDest"),
        ("IP-FORWARD-MIB", "ipForwardMask"),
        ("IP-FORWARD-MIB", "ipForwardPolicy"),
        ("IP-FORWARD-MIB", "ipForwardNextHop"),
        ("IP-FORWARD-MIB", "ipForwardIfIndex"),
        ("IP-FORWARD-MIB", "ipForwardType"),
        ("IP-FORWARD-MIB", "ipForwardProto"),
        ("IP-FORWARD-MIB", "ipForwardAge"),
        ("IP-FORWARD-MIB", "ipForwardInfo"),
        ("IP-FORWARD-MIB", "ipForwardNextHopAS"),
        ("IP-FORWARD-MIB", "ipForwardMetric1"),
        ("IP-FORWARD-MIB", "ipForwardMetric2"),
        ("IP-FORWARD-MIB", "ipForwardMetric3"),
        ("IP-FORWARD-MIB", "ipForwardMetric4"),
        ("IP-FORWARD-MIB", "ipForwardMetric5"))
)
if mibBuilder.loadTexts:
    ipForwardMultiPathGroup.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipForwardMultiPathGroup.setDescription("IP Multipath Route Table.")

ipForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 3)
)
ipForwardCidrRouteGroup.setObjects(
      *(("IP-FORWARD-MIB", "ipCidrRouteNumber"),
        ("IP-FORWARD-MIB", "ipCidrRouteDest"),
        ("IP-FORWARD-MIB", "ipCidrRouteMask"),
        ("IP-FORWARD-MIB", "ipCidrRouteTos"),
        ("IP-FORWARD-MIB", "ipCidrRouteNextHop"),
        ("IP-FORWARD-MIB", "ipCidrRouteIfIndex"),
        ("IP-FORWARD-MIB", "ipCidrRouteType"),
        ("IP-FORWARD-MIB", "ipCidrRouteProto"),
        ("IP-FORWARD-MIB", "ipCidrRouteAge"),
        ("IP-FORWARD-MIB", "ipCidrRouteInfo"),
        ("IP-FORWARD-MIB", "ipCidrRouteNextHopAS"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric1"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric2"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric3"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric4"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric5"),
        ("IP-FORWARD-MIB", "ipCidrRouteStatus"))
)
if mibBuilder.loadTexts:
    ipForwardCidrRouteGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipForwardCidrRouteGroup.setDescription("The CIDR Route Table. This group has been deprecated and replaced with inetForwardCidrRouteGroup.")

inetForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 4)
)
inetForwardCidrRouteGroup.setObjects(
      *(("IP-FORWARD-MIB", "inetCidrRouteDiscards"),
        ("IP-FORWARD-MIB", "inetCidrRouteIfIndex"),
        ("IP-FORWARD-MIB", "inetCidrRouteType"),
        ("IP-FORWARD-MIB", "inetCidrRouteProto"),
        ("IP-FORWARD-MIB", "inetCidrRouteAge"),
        ("IP-FORWARD-MIB", "inetCidrRouteNextHopAS"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric1"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric2"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric3"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric4"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric5"),
        ("IP-FORWARD-MIB", "inetCidrRouteStatus"),
        ("IP-FORWARD-MIB", "inetCidrRouteNumber"))
)
if mibBuilder.loadTexts:
    inetForwardCidrRouteGroup.setStatus("current")
if mibBuilder.loadTexts:
    inetForwardCidrRouteGroup.setDescription("The IP version-independent CIDR Route Table.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipForwardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 1)
)
ipForwardCompliance.setObjects(
    ("IP-FORWARD-MIB", "ipForwardCidrRouteGroup")
)
if mibBuilder.loadTexts:
    ipForwardCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    ipForwardCompliance.setDescription("The compliance statement for SNMPv2 entities that implement the ipForward MIB. This compliance statement has been deprecated and replaced with ipForwardFullCompliance and ipForwardReadOnlyCompliance.")

ipForwardOldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 2)
)
ipForwardOldCompliance.setObjects(
    ("IP-FORWARD-MIB", "ipForwardMultiPathGroup")
)
if mibBuilder.loadTexts:
    ipForwardOldCompliance.setStatus(
        "obsolete"
    )
if mibBuilder.loadTexts:
    ipForwardOldCompliance.setDescription("The compliance statement for SNMP entities which implement the ipForward MIB.")

ipForwardFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 3)
)
ipForwardFullCompliance.setObjects(
    ("IP-FORWARD-MIB", "inetForwardCidrRouteGroup")
)
if mibBuilder.loadTexts:
    ipForwardFullCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ipForwardFullCompliance.setDescription("When this MIB is implemented for read-create, the implementation can claim full compliance. There are a number of INDEX objects that cannot be represented in the form of OBJECT clauses in SMIv2, but for which there are compliance requirements, expressed in OBJECT clause form in this description: -- OBJECT inetCidrRouteDestType -- SYNTAX InetAddressType (ipv4(1), ipv6(2), -- ipv4z(3), ipv6z(4)) -- DESCRIPTION -- This MIB requires support for global and -- non-global ipv4 and ipv6 addresses. -- -- OBJECT inetCidrRouteDest -- SYNTAX InetAddress (SIZE (4 | 8 | 16 | 20)) -- DESCRIPTION -- This MIB requires support for global and -- non-global IPv4 and IPv6 addresses. -- -- OBJECT inetCidrRouteNextHopType -- SYNTAX InetAddressType (unknown(0), ipv4(1), -- ipv6(2), ipv4z(3) -- ipv6z(4)) -- DESCRIPTION -- This MIB requires support for global and -- non-global ipv4 and ipv6 addresses. -- -- OBJECT inetCidrRouteNextHop -- SYNTAX InetAddress (SIZE (0 | 4 | 8 | 16 | 20)) -- DESCRIPTION -- This MIB requires support for global and -- non-global IPv4 and IPv6 addresses. ")

ipForwardReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 4)
)
ipForwardReadOnlyCompliance.setObjects(
    ("IP-FORWARD-MIB", "inetForwardCidrRouteGroup")
)
if mibBuilder.loadTexts:
    ipForwardReadOnlyCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ipForwardReadOnlyCompliance.setDescription("When this MIB is implemented without support for read- create (i.e., in read-only mode), the implementation can claim read-only compliance.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "IP-FORWARD-MIB",
    **{"ipForward": ipForward,
       "ipForwardNumber": ipForwardNumber,
       "ipForwardTable": ipForwardTable,
       "ipForwardEntry": ipForwardEntry,
       "ipForwardDest": ipForwardDest,
       "ipForwardMask": ipForwardMask,
       "ipForwardPolicy": ipForwardPolicy,
       "ipForwardNextHop": ipForwardNextHop,
       "ipForwardIfIndex": ipForwardIfIndex,
       "ipForwardType": ipForwardType,
       "ipForwardProto": ipForwardProto,
       "ipForwardAge": ipForwardAge,
       "ipForwardInfo": ipForwardInfo,
       "ipForwardNextHopAS": ipForwardNextHopAS,
       "ipForwardMetric1": ipForwardMetric1,
       "ipForwardMetric2": ipForwardMetric2,
       "ipForwardMetric3": ipForwardMetric3,
       "ipForwardMetric4": ipForwardMetric4,
       "ipForwardMetric5": ipForwardMetric5,
       "ipCidrRouteNumber": ipCidrRouteNumber,
       "ipCidrRouteTable": ipCidrRouteTable,
       "ipCidrRouteEntry": ipCidrRouteEntry,
       "ipCidrRouteDest": ipCidrRouteDest,
       "ipCidrRouteMask": ipCidrRouteMask,
       "ipCidrRouteTos": ipCidrRouteTos,
       "ipCidrRouteNextHop": ipCidrRouteNextHop,
       "ipCidrRouteIfIndex": ipCidrRouteIfIndex,
       "ipCidrRouteType": ipCidrRouteType,
       "ipCidrRouteProto": ipCidrRouteProto,
       "ipCidrRouteAge": ipCidrRouteAge,
       "ipCidrRouteInfo": ipCidrRouteInfo,
       "ipCidrRouteNextHopAS": ipCidrRouteNextHopAS,
       "ipCidrRouteMetric1": ipCidrRouteMetric1,
       "ipCidrRouteMetric2": ipCidrRouteMetric2,
       "ipCidrRouteMetric3": ipCidrRouteMetric3,
       "ipCidrRouteMetric4": ipCidrRouteMetric4,
       "ipCidrRouteMetric5": ipCidrRouteMetric5,
       "ipCidrRouteStatus": ipCidrRouteStatus,
       "ipForwardConformance": ipForwardConformance,
       "ipForwardGroups": ipForwardGroups,
       "ipForwardMultiPathGroup": ipForwardMultiPathGroup,
       "ipForwardCidrRouteGroup": ipForwardCidrRouteGroup,
       "inetForwardCidrRouteGroup": inetForwardCidrRouteGroup,
       "ipForwardCompliances": ipForwardCompliances,
       "ipForwardCompliance": ipForwardCompliance,
       "ipForwardOldCompliance": ipForwardOldCompliance,
       "ipForwardFullCompliance": ipForwardFullCompliance,
       "ipForwardReadOnlyCompliance": ipForwardReadOnlyCompliance,
       "inetCidrRouteNumber": inetCidrRouteNumber,
       "inetCidrRouteTable": inetCidrRouteTable,
       "inetCidrRouteEntry": inetCidrRouteEntry,
       "inetCidrRouteDestType": inetCidrRouteDestType,
       "inetCidrRouteDest": inetCidrRouteDest,
       "inetCidrRoutePfxLen": inetCidrRoutePfxLen,
       "inetCidrRoutePolicy": inetCidrRoutePolicy,
       "inetCidrRouteNextHopType": inetCidrRouteNextHopType,
       "inetCidrRouteNextHop": inetCidrRouteNextHop,
       "inetCidrRouteIfIndex": inetCidrRouteIfIndex,
       "inetCidrRouteType": inetCidrRouteType,
       "inetCidrRouteProto": inetCidrRouteProto,
       "inetCidrRouteAge": inetCidrRouteAge,
       "inetCidrRouteNextHopAS": inetCidrRouteNextHopAS,
       "inetCidrRouteMetric1": inetCidrRouteMetric1,
       "inetCidrRouteMetric2": inetCidrRouteMetric2,
       "inetCidrRouteMetric3": inetCidrRouteMetric3,
       "inetCidrRouteMetric4": inetCidrRouteMetric4,
       "inetCidrRouteMetric5": inetCidrRouteMetric5,
       "inetCidrRouteStatus": inetCidrRouteStatus,
       "inetCidrRouteDiscards": inetCidrRouteDiscards}
)
