# SNMP MIB module (IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IPV6-MIB
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

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix,
 Ipv6IfIndex,
 Ipv6IfIndexOrZero) = mibBuilder.import_symbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix",
    "Ipv6IfIndex",
    "Ipv6IfIndexOrZero")

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
 NotificationType,
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
    "Counter32",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
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
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ipv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 55)
)
if mibBuilder.loadTexts:
    ipv6MIB.setRevisions(
        ("2017-02-22 00:00",
         "1998-02-05 21:55")
    )
if mibBuilder.loadTexts:
    ipv6MIB.setLastUpdated("201702220000Z")
if mibBuilder.loadTexts:
    ipv6MIB.setOrganization("IETF IPv6 Working Group")
if mibBuilder.loadTexts:
    ipv6MIB.setContactInfo(" Dimitry Haskin Postal: Bay Networks, Inc. 660 Technology Park Drive. Billerica, MA 01821 US Tel: +1-978-916-8124 E-mail: dhaskin@baynetworks.com Steve Onishi Postal: Bay Networks, Inc. 3 Federal Street Billerica, MA 01821 US Tel: +1-978-916-3816 E-mail: sonishi@baynetworks.com")
if mibBuilder.loadTexts:
    ipv6MIB.setDescription("The obsolete MIB module for entities implementing the IPv6 protocol. Use the IP-MIB or IP-FORWARD-MIB instead. Copyright (c) 2017 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipv6MIBObjects_ObjectIdentity = ObjectIdentity
ipv6MIBObjects = _Ipv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 1)
)


class _Ipv6Forwarding_Type(Integer32):
    """Custom type ipv6Forwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_Ipv6Forwarding_Type.__name__ = "Integer32"
_Ipv6Forwarding_Object = MibScalar
ipv6Forwarding = _Ipv6Forwarding_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 1),
    _Ipv6Forwarding_Type()
)
ipv6Forwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Forwarding.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6Forwarding.setDescription("The indication of whether this entity is acting as an IPv6 router in respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams. IPv6 hosts do not (except those source-routed via the host). Note that for some managed nodes, this object may take on only a subset of the values possible. Accordingly, it is appropriate for an agent to return a `wrongValue' response if a management station attempts to change this object to an inappropriate value. This object is obsoleted by IP-MIB::ipv6IpForwarding.")


class _Ipv6DefaultHopLimit_Type(Integer32):
    """Custom type ipv6DefaultHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ipv6DefaultHopLimit_Type.__name__ = "Integer32"
_Ipv6DefaultHopLimit_Object = MibScalar
ipv6DefaultHopLimit = _Ipv6DefaultHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 2),
    _Ipv6DefaultHopLimit_Type()
)
ipv6DefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultHopLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6DefaultHopLimit.setDescription("The default value inserted into the Hop Limit field of the IPv6 header of datagrams originated at this entity, whenever a Hop Limit value is not supplied by the transport layer protocol. This object is obsoleted by IP-MIB::ipv6IpDefaultHopLimit.")
_Ipv6Interfaces_Type = Unsigned32
_Ipv6Interfaces_Object = MibScalar
ipv6Interfaces = _Ipv6Interfaces_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 3),
    _Ipv6Interfaces_Type()
)
ipv6Interfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6Interfaces.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6Interfaces.setDescription("The number of IPv6 interfaces (regardless of their current state) present on this system. This object is obsolete; there is no direct replacement, but its value can be derived from the number of rows in the IP-MIB::ipv6InterfaceTable.")
_Ipv6IfTableLastChange_Type = TimeStamp
_Ipv6IfTableLastChange_Object = MibScalar
ipv6IfTableLastChange = _Ipv6IfTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 4),
    _Ipv6IfTableLastChange_Type()
)
ipv6IfTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfTableLastChange.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfTableLastChange.setDescription("The value of sysUpTime at the time of the last insertion or removal of an entry in the ipv6IfTable. If the number of entries has been unchanged since the last re-initialization of the local network management subsystem, then this object contains a zero value. This object is obsoleted by IP-MIB::ipv6InterfaceTableLastChange.")
_Ipv6IfTable_Object = MibTable
ipv6IfTable = _Ipv6IfTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5)
)
if mibBuilder.loadTexts:
    ipv6IfTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfTable.setDescription("The IPv6 Interfaces table contains information on the entity's internetwork-layer interfaces. An IPv6 interface constitutes a logical network layer attachment to the layer immediately below IPv6 including internet layer 'tunnels', such as tunnels over IPv4 or IPv6 itself. This table is obsoleted by IP-MIB::ipv6InterfaceTable.")
_Ipv6IfEntry_Object = MibTableRow
ipv6IfEntry = _Ipv6IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1)
)
ipv6IfEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    ipv6IfEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfEntry.setDescription("An interface entry containing objects about a particular IPv6 interface. This object is obsoleted by IP-MIB::ipv6InterfaceEntry.")
_Ipv6IfIndex_Type = Ipv6IfIndex
_Ipv6IfIndex_Object = MibTableColumn
ipv6IfIndex = _Ipv6IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 1),
    _Ipv6IfIndex_Type()
)
ipv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6IfIndex.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfIndex.setDescription("A unique non-zero value identifying the particular IPv6 interface. This object is obsoleted. In the IP-MIB, interfaces are simply identified by IfIndex.")
_Ipv6IfDescr_Type = DisplayString
_Ipv6IfDescr_Object = MibTableColumn
ipv6IfDescr = _Ipv6IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 2),
    _Ipv6IfDescr_Type()
)
ipv6IfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfDescr.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfDescr.setDescription("A textual string containing information about the interface. This string may be set by the network management system. This object is obsoleted by IF-MIB::ifDescr.")
_Ipv6IfLowerLayer_Type = VariablePointer
_Ipv6IfLowerLayer_Object = MibTableColumn
ipv6IfLowerLayer = _Ipv6IfLowerLayer_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 3),
    _Ipv6IfLowerLayer_Type()
)
ipv6IfLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfLowerLayer.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfLowerLayer.setDescription("This object identifies the protocol layer over which this network interface operates. If this network interface operates over the data-link layer, then the value of this object refers to an instance of ifIndex [RFC1573]. If this network interface operates over an IPv4 interface, the value of this object refers to an instance of ipAdEntAddr [RFC1213]. If this network interface operates over another IPv6 interface, the value of this object refers to an instance of ipv6IfIndex. If this network interface is not currently operating over an active protocol layer, then the value of this object should be set to the OBJECT ID { 0 0 }. This object is obsolete. The IF-STACK-TABLE may be used to express relationships between interfaces.")
_Ipv6IfEffectiveMtu_Type = Unsigned32
_Ipv6IfEffectiveMtu_Object = MibTableColumn
ipv6IfEffectiveMtu = _Ipv6IfEffectiveMtu_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 4),
    _Ipv6IfEffectiveMtu_Type()
)
ipv6IfEffectiveMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfEffectiveMtu.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfEffectiveMtu.setUnits("octets")
if mibBuilder.loadTexts:
    ipv6IfEffectiveMtu.setDescription("The size of the largest IPv6 packet which can be sent/received on the interface, specified in octets. This object is obsolete. The value of IF-MIB::ifMtu for the corresponding value of ifIndex represents the MTU of the interface.")


class _Ipv6IfReasmMaxSize_Type(Unsigned32):
    """Custom type ipv6IfReasmMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6IfReasmMaxSize_Type.__name__ = "Unsigned32"
_Ipv6IfReasmMaxSize_Object = MibTableColumn
ipv6IfReasmMaxSize = _Ipv6IfReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 5),
    _Ipv6IfReasmMaxSize_Type()
)
ipv6IfReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfReasmMaxSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfReasmMaxSize.setUnits("octets")
if mibBuilder.loadTexts:
    ipv6IfReasmMaxSize.setDescription("The size of the largest IPv6 datagram which this entity can re-assemble from incoming IPv6 fragmented datagrams received on this interface. This object is obsoleted by IP-MIB::ipv6InterfaceReasmMaxSize.")
_Ipv6IfIdentifier_Type = Ipv6AddressIfIdentifier
_Ipv6IfIdentifier_Object = MibTableColumn
ipv6IfIdentifier = _Ipv6IfIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 6),
    _Ipv6IfIdentifier_Type()
)
ipv6IfIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfIdentifier.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfIdentifier.setDescription("The Interface Identifier for this interface that is (at least) unique on the link this interface is attached to. The Interface Identifier is combined with an address prefix to form an interface address. By default, the Interface Identifier is autoconfigured according to the rules of the link type this interface is attached to. This object is obsoleted by IP-MIB::ipv6InterfaceIdentifier.")


class _Ipv6IfIdentifierLength_Type(Integer32):
    """Custom type ipv6IfIdentifierLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Ipv6IfIdentifierLength_Type.__name__ = "Integer32"
_Ipv6IfIdentifierLength_Object = MibTableColumn
ipv6IfIdentifierLength = _Ipv6IfIdentifierLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 7),
    _Ipv6IfIdentifierLength_Type()
)
ipv6IfIdentifierLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfIdentifierLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfIdentifierLength.setUnits("bits")
if mibBuilder.loadTexts:
    ipv6IfIdentifierLength.setDescription("The length of the Interface Identifier in bits. This object is obsolete. It can be derived from the length of IP-MIB::ipv6InterfaceIdentifier; Interface Identifiers that are not an even number of octets are not supported.")
_Ipv6IfPhysicalAddress_Type = PhysAddress
_Ipv6IfPhysicalAddress_Object = MibTableColumn
ipv6IfPhysicalAddress = _Ipv6IfPhysicalAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 8),
    _Ipv6IfPhysicalAddress_Type()
)
ipv6IfPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfPhysicalAddress.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfPhysicalAddress.setDescription("The interface's physical address. For example, for an IPv6 interface attached to an 802.x link, this object normally contains a MAC address. Note that in some cases this address may differ from the address of the interface's protocol sub-layer. The interface's media-specific MIB must define the bit and byte ordering and the format of the value of this object. For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length. This object is obsoleted by IF-MIB::ifPhysAddress.")


class _Ipv6IfAdminStatus_Type(Integer32):
    """Custom type ipv6IfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Ipv6IfAdminStatus_Type.__name__ = "Integer32"
_Ipv6IfAdminStatus_Object = MibTableColumn
ipv6IfAdminStatus = _Ipv6IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 9),
    _Ipv6IfAdminStatus_Type()
)
ipv6IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfAdminStatus.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfAdminStatus.setDescription("The desired state of the interface. When a managed system initializes, all IPv6 interfaces start with ipv6IfAdminStatus in the down(2) state. As a result of either explicit management action or per configuration information retained by the managed system, ipv6IfAdminStatus is then changed to the up(1) state (or remains in the down(2) state). This object is obsolete. IPv6 does not have a separate admin status; the admin status of the interface is represented by IF-MIB::ifAdminStatus.")


class _Ipv6IfOperStatus_Type(Integer32):
    """Custom type ipv6IfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("noIfIdentifier", 3),
          ("unknown", 4),
          ("notPresent", 5))
    )


_Ipv6IfOperStatus_Type.__name__ = "Integer32"
_Ipv6IfOperStatus_Object = MibTableColumn
ipv6IfOperStatus = _Ipv6IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 10),
    _Ipv6IfOperStatus_Type()
)
ipv6IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfOperStatus.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfOperStatus.setDescription("The current operational state of the interface. The noIfIdentifier(3) state indicates that no valid Interface Identifier is assigned to the interface. This state usually indicates that the link-local interface address failed Duplicate Address Detection. If ipv6IfAdminStatus is down(2) then ipv6IfOperStatus should be down(2). If ipv6IfAdminStatus is changed to up(1) then ipv6IfOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should remain in the down(2) or noIfIdentifier(3) state if and only if there is a fault that prevents it from going to the up(1) state; it should remain in the notPresent(5) state if the interface has missing (typically, lower layer) components. This object is obsolete. IPv6 does not have a separate operational status; the operational status of the interface is represented by IF-MIB::ifOperStatus.")
_Ipv6IfLastChange_Type = TimeStamp
_Ipv6IfLastChange_Object = MibTableColumn
ipv6IfLastChange = _Ipv6IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 11),
    _Ipv6IfLastChange_Type()
)
ipv6IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfLastChange.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfLastChange.setDescription("The value of sysUpTime at the time the interface entered its current operational state. If the current state was entered prior to the last re-initialization of the local network management subsystem, then this object contains a zero value. This object is obsolete. The last change of IF-MIB::ifOperStatus is represented by IF-MIB::ifLastChange.")
_Ipv6IfStatsTable_Object = MibTable
ipv6IfStatsTable = _Ipv6IfStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6)
)
if mibBuilder.loadTexts:
    ipv6IfStatsTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsTable.setDescription("IPv6 interface traffic statistics. This table is obsoleted by the IP-MIB::ipIfStatsTable.")
_Ipv6IfStatsEntry_Object = MibTableRow
ipv6IfStatsEntry = _Ipv6IfStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipv6IfStatsEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsEntry.setDescription("An interface statistics entry containing objects at a particular IPv6 interface. This object is obsoleted by the IP-MIB::ipIfStatsEntry.")
_Ipv6IfStatsInReceives_Type = Counter32
_Ipv6IfStatsInReceives_Object = MibTableColumn
ipv6IfStatsInReceives = _Ipv6IfStatsInReceives_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 1),
    _Ipv6IfStatsInReceives_Type()
)
ipv6IfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInReceives.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInReceives.setDescription("The total number of input datagrams received by the interface, including those received in error. This object is obsoleted by IP-MIB::ipIfStatsHCInReceives.")
_Ipv6IfStatsInHdrErrors_Type = Counter32
_Ipv6IfStatsInHdrErrors_Object = MibTableColumn
ipv6IfStatsInHdrErrors = _Ipv6IfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 2),
    _Ipv6IfStatsInHdrErrors_Type()
)
ipv6IfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInHdrErrors.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInHdrErrors.setDescription("The number of input datagrams discarded due to errors in their IPv6 headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IPv6 options, etc. This object is obsoleted by IP-MIB::ipIfStatsInHdrErrors.")
_Ipv6IfStatsInTooBigErrors_Type = Counter32
_Ipv6IfStatsInTooBigErrors_Object = MibTableColumn
ipv6IfStatsInTooBigErrors = _Ipv6IfStatsInTooBigErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 3),
    _Ipv6IfStatsInTooBigErrors_Type()
)
ipv6IfStatsInTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInTooBigErrors.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInTooBigErrors.setDescription("The number of input datagrams that could not be forwarded because their size exceeded the link MTU of outgoing interface. This object is obsoleted. It was not replicated in the IP-MIB due to feedback that systems did not retain the incoming interface of a packet that failed fragmentation.")
_Ipv6IfStatsInNoRoutes_Type = Counter32
_Ipv6IfStatsInNoRoutes_Object = MibTableColumn
ipv6IfStatsInNoRoutes = _Ipv6IfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 4),
    _Ipv6IfStatsInNoRoutes_Type()
)
ipv6IfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInNoRoutes.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInNoRoutes.setDescription("The number of input datagrams discarded because no route could be found to transmit them to their destination. This object is obsoleted by IP-MIB::ipIfStatsInNoRoutes.")
_Ipv6IfStatsInAddrErrors_Type = Counter32
_Ipv6IfStatsInAddrErrors_Object = MibTableColumn
ipv6IfStatsInAddrErrors = _Ipv6IfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 5),
    _Ipv6IfStatsInAddrErrors_Type()
)
ipv6IfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInAddrErrors.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInAddrErrors.setDescription("The number of input datagrams discarded because the IPv6 address in their IPv6 header's destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., ::0) and unsupported addresses (e.g., addresses with unallocated prefixes). For entities which are not IPv6 routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address. This object is obsoleted by IP-MIB::ipIfStatsInAddrErrors.")
_Ipv6IfStatsInUnknownProtos_Type = Counter32
_Ipv6IfStatsInUnknownProtos_Object = MibTableColumn
ipv6IfStatsInUnknownProtos = _Ipv6IfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 6),
    _Ipv6IfStatsInUnknownProtos_Type()
)
ipv6IfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInUnknownProtos.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInUnknownProtos.setDescription("The number of locally-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol. This counter is incremented at the interface to which these datagrams were addressed which might not be necessarily the input interface for some of the datagrams. This object is obsoleted by IP-MIB::ipIfStatsInUnknownProtos.")
_Ipv6IfStatsInTruncatedPkts_Type = Counter32
_Ipv6IfStatsInTruncatedPkts_Object = MibTableColumn
ipv6IfStatsInTruncatedPkts = _Ipv6IfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 7),
    _Ipv6IfStatsInTruncatedPkts_Type()
)
ipv6IfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInTruncatedPkts.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInTruncatedPkts.setDescription("The number of input datagrams discarded because datagram frame didn't carry enough data. This object is obsoleted by IP-MIB::ipIfStatsInTruncatedPkts.")
_Ipv6IfStatsInDiscards_Type = Counter32
_Ipv6IfStatsInDiscards_Object = MibTableColumn
ipv6IfStatsInDiscards = _Ipv6IfStatsInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 8),
    _Ipv6IfStatsInDiscards_Type()
)
ipv6IfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInDiscards.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInDiscards.setDescription("The number of input IPv6 datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space). Note that this counter does not include any datagrams discarded while awaiting re-assembly. This object is obsoleted by IP-MIB::ipIfStatsInDiscards.")
_Ipv6IfStatsInDelivers_Type = Counter32
_Ipv6IfStatsInDelivers_Object = MibTableColumn
ipv6IfStatsInDelivers = _Ipv6IfStatsInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 9),
    _Ipv6IfStatsInDelivers_Type()
)
ipv6IfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInDelivers.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInDelivers.setDescription("The total number of datagrams successfully delivered to IPv6 user-protocols (including ICMP). This counter is incremented at the interface to which these datagrams were addressed which might not be necessarily the input interface for some of the datagrams. This object is obsoleted by IP-MIB::ipIfStatsHCInDelivers.")
_Ipv6IfStatsOutForwDatagrams_Type = Counter32
_Ipv6IfStatsOutForwDatagrams_Object = MibTableColumn
ipv6IfStatsOutForwDatagrams = _Ipv6IfStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 10),
    _Ipv6IfStatsOutForwDatagrams_Type()
)
ipv6IfStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutForwDatagrams.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutForwDatagrams.setDescription("The number of output datagrams which this entity received and forwarded to their final destinations. In entities which do not act as IPv6 routers, this counter will include only those packets which were Source-Routed via this entity, and the Source-Route processing was successful. Note that for a successfully forwarded datagram the counter of the outgoing interface is incremented. This object is obsoleted by IP-MIB::ipIfStatsHCOutForwDatagrams.")
_Ipv6IfStatsOutRequests_Type = Counter32
_Ipv6IfStatsOutRequests_Object = MibTableColumn
ipv6IfStatsOutRequests = _Ipv6IfStatsOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 11),
    _Ipv6IfStatsOutRequests_Type()
)
ipv6IfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutRequests.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutRequests.setDescription("The total number of IPv6 datagrams which local IPv6 user-protocols (including ICMP) supplied to IPv6 in requests for transmission. Note that this counter does not include any datagrams counted in ipv6IfStatsOutForwDatagrams. This object is obsoleted by IP-MIB::ipIfStatsHCOutRequests.")
_Ipv6IfStatsOutDiscards_Type = Counter32
_Ipv6IfStatsOutDiscards_Object = MibTableColumn
ipv6IfStatsOutDiscards = _Ipv6IfStatsOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 12),
    _Ipv6IfStatsOutDiscards_Type()
)
ipv6IfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutDiscards.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutDiscards.setDescription("The number of output IPv6 datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space). Note that this counter would include datagrams counted in ipv6IfStatsOutForwDatagrams if any such packets met this (discretionary) discard criterion. This object is obsoleted by IP-MIB::ipIfStatsOutDiscards.")
_Ipv6IfStatsOutFragOKs_Type = Counter32
_Ipv6IfStatsOutFragOKs_Object = MibTableColumn
ipv6IfStatsOutFragOKs = _Ipv6IfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 13),
    _Ipv6IfStatsOutFragOKs_Type()
)
ipv6IfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragOKs.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragOKs.setDescription("The number of IPv6 datagrams that have been successfully fragmented at this output interface. This object is obsoleted by IP-MIB::ipIfStatsOutFragOKs.")
_Ipv6IfStatsOutFragFails_Type = Counter32
_Ipv6IfStatsOutFragFails_Object = MibTableColumn
ipv6IfStatsOutFragFails = _Ipv6IfStatsOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 14),
    _Ipv6IfStatsOutFragFails_Type()
)
ipv6IfStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragFails.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragFails.setDescription("The number of IPv6 datagrams that have been discarded because they needed to be fragmented at this output interface but could not be. This object is obsoleted by IP-MIB::ipIfStatsOutFragFails.")
_Ipv6IfStatsOutFragCreates_Type = Counter32
_Ipv6IfStatsOutFragCreates_Object = MibTableColumn
ipv6IfStatsOutFragCreates = _Ipv6IfStatsOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 15),
    _Ipv6IfStatsOutFragCreates_Type()
)
ipv6IfStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragCreates.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragCreates.setDescription("The number of output datagram fragments that have been generated as a result of fragmentation at this output interface. This object is obsoleted by IP-MIB::ipIfStatsOutFragCreates.")
_Ipv6IfStatsReasmReqds_Type = Counter32
_Ipv6IfStatsReasmReqds_Object = MibTableColumn
ipv6IfStatsReasmReqds = _Ipv6IfStatsReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 16),
    _Ipv6IfStatsReasmReqds_Type()
)
ipv6IfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmReqds.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmReqds.setDescription("The number of IPv6 fragments received which needed to be reassembled at this interface. Note that this counter is incremented at the interface to which these fragments were addressed which might not be necessarily the input interface for some of the fragments. This object is obsoleted by IP-MIB::ipIfStatsReasmReqds.")
_Ipv6IfStatsReasmOKs_Type = Counter32
_Ipv6IfStatsReasmOKs_Object = MibTableColumn
ipv6IfStatsReasmOKs = _Ipv6IfStatsReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 17),
    _Ipv6IfStatsReasmOKs_Type()
)
ipv6IfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmOKs.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmOKs.setDescription("The number of IPv6 datagrams successfully reassembled. Note that this counter is incremented at the interface to which these datagrams were addressed which might not be necessarily the input interface for some of the fragments. This object is obsoleted by IP-MIB::ipIfStatsReasmOKs.")
_Ipv6IfStatsReasmFails_Type = Counter32
_Ipv6IfStatsReasmFails_Object = MibTableColumn
ipv6IfStatsReasmFails = _Ipv6IfStatsReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 18),
    _Ipv6IfStatsReasmFails_Type()
)
ipv6IfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmFails.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmFails.setDescription("The number of failures detected by the IPv6 re- assembly algorithm (for whatever reason: timed out, errors, etc.). Note that this is not necessarily a count of discarded IPv6 fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received. This counter is incremented at the interface to which these fragments were addressed which might not be necessarily the input interface for some of the fragments. This object is obsoleted by IP-MIB::ipIfStatsReasmFails.")
_Ipv6IfStatsInMcastPkts_Type = Counter32
_Ipv6IfStatsInMcastPkts_Object = MibTableColumn
ipv6IfStatsInMcastPkts = _Ipv6IfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 19),
    _Ipv6IfStatsInMcastPkts_Type()
)
ipv6IfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInMcastPkts.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsInMcastPkts.setDescription("The number of multicast packets received by the interface This object is obsoleted by IP-MIB::ipIfStatsHCInMcastPkts.")
_Ipv6IfStatsOutMcastPkts_Type = Counter32
_Ipv6IfStatsOutMcastPkts_Object = MibTableColumn
ipv6IfStatsOutMcastPkts = _Ipv6IfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 20),
    _Ipv6IfStatsOutMcastPkts_Type()
)
ipv6IfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutMcastPkts.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfStatsOutMcastPkts.setDescription("The number of multicast packets transmitted by the interface This object is obsoleted by IP-MIB::ipIfStatsHCOutMcastPkts.")
_Ipv6AddrPrefixTable_Object = MibTable
ipv6AddrPrefixTable = _Ipv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7)
)
if mibBuilder.loadTexts:
    ipv6AddrPrefixTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixTable.setDescription("The list of IPv6 address prefixes of IPv6 interfaces. This table is obsoleted by IP-MIB::ipAddressPrefixTable.")
_Ipv6AddrPrefixEntry_Object = MibTableRow
ipv6AddrPrefixEntry = _Ipv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1)
)
ipv6AddrPrefixEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6AddrPrefix"),
    (0, "IPV6-MIB", "ipv6AddrPrefixLength"),
)
if mibBuilder.loadTexts:
    ipv6AddrPrefixEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixEntry.setDescription("An interface entry containing objects of a particular IPv6 address prefix. This entry is obsoleted by IP-MIB::ipAddressPrefixEntry.")
_Ipv6AddrPrefix_Type = Ipv6AddressPrefix
_Ipv6AddrPrefix_Object = MibTableColumn
ipv6AddrPrefix = _Ipv6AddrPrefix_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 1),
    _Ipv6AddrPrefix_Type()
)
ipv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrPrefix.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefix.setDescription("The prefix associated with the this interface. This object is obsoleted by IP-MIB::ipAddressPrefixPrefix.")


class _Ipv6AddrPrefixLength_Type(Integer32):
    """Custom type ipv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6AddrPrefixLength_Type.__name__ = "Integer32"
_Ipv6AddrPrefixLength_Object = MibTableColumn
ipv6AddrPrefixLength = _Ipv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 2),
    _Ipv6AddrPrefixLength_Type()
)
ipv6AddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrPrefixLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixLength.setUnits("bits")
if mibBuilder.loadTexts:
    ipv6AddrPrefixLength.setDescription("The length of the prefix (in bits). This object is obsoleted by IP-MIB::ipAddressPrefixLength.")
_Ipv6AddrPrefixOnLinkFlag_Type = TruthValue
_Ipv6AddrPrefixOnLinkFlag_Object = MibTableColumn
ipv6AddrPrefixOnLinkFlag = _Ipv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 3),
    _Ipv6AddrPrefixOnLinkFlag_Type()
)
ipv6AddrPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixOnLinkFlag.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixOnLinkFlag.setDescription("This object has the value 'true(1)', if this prefix can be used for on-link determination and the value 'false(2)' otherwise. This object is obsoleted by IP-MIB::ipAddressPrefixOnLinkFlag.")
_Ipv6AddrPrefixAutonomousFlag_Type = TruthValue
_Ipv6AddrPrefixAutonomousFlag_Object = MibTableColumn
ipv6AddrPrefixAutonomousFlag = _Ipv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 4),
    _Ipv6AddrPrefixAutonomousFlag_Type()
)
ipv6AddrPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAutonomousFlag.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAutonomousFlag.setDescription("Autonomous address configuration flag. When true(1), indicates that this prefix can be used for autonomous address configuration (i.e. can be used to form a local interface address). If false(2), it is not used to autoconfigure a local interface address. This object is obsoleted by IP-MIB::ipAddressPrefixAutonomousFlag.")
_Ipv6AddrPrefixAdvPreferredLifetime_Type = Unsigned32
_Ipv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
ipv6AddrPrefixAdvPreferredLifetime = _Ipv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 5),
    _Ipv6AddrPrefixAdvPreferredLifetime_Type()
)
ipv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvPreferredLifetime.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvPreferredLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvPreferredLifetime.setDescription("It is the length of time in seconds that this prefix will remain preferred, i.e. time until deprecation. A value of 4,294,967,295 represents infinity. The address generated from a deprecated prefix should no longer be used as a source address in new communications, but packets received on such an interface are processed as expected. This object is obsoleted by IP-MIB::ipAddressPrefixAdvPreferredLifetime.")
_Ipv6AddrPrefixAdvValidLifetime_Type = Unsigned32
_Ipv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
ipv6AddrPrefixAdvValidLifetime = _Ipv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 6),
    _Ipv6AddrPrefixAdvValidLifetime_Type()
)
ipv6AddrPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvValidLifetime.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvValidLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvValidLifetime.setDescription("It is the length of time in seconds that this prefix will remain valid, i.e. time until invalidation. A value of 4,294,967,295 represents infinity. The address generated from an invalidated prefix should not appear as the destination or source address of a packet. This object is obsoleted by IP-MIB::ipAddressPrefixAdvValidLifetime.")
_Ipv6AddrTable_Object = MibTable
ipv6AddrTable = _Ipv6AddrTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8)
)
if mibBuilder.loadTexts:
    ipv6AddrTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrTable.setDescription("The table of addressing information relevant to this node's interface addresses. This table is obsoleted by IP-MIB::ipAddressTable.")
_Ipv6AddrEntry_Object = MibTableRow
ipv6AddrEntry = _Ipv6AddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1)
)
ipv6AddrEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6AddrAddress"),
)
if mibBuilder.loadTexts:
    ipv6AddrEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrEntry.setDescription("The addressing information for one of this node's interface addresses. This entry is obsoleted by IP-MIB::ipAddressEntry.")
_Ipv6AddrAddress_Type = Ipv6Address
_Ipv6AddrAddress_Object = MibTableColumn
ipv6AddrAddress = _Ipv6AddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 1),
    _Ipv6AddrAddress_Type()
)
ipv6AddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrAddress.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrAddress.setDescription("The IPv6 address to which this entry's addressing information pertains. This object is obsoleted by IP-MIB::ipAddressAddr.")


class _Ipv6AddrPfxLength_Type(Integer32):
    """Custom type ipv6AddrPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6AddrPfxLength_Type.__name__ = "Integer32"
_Ipv6AddrPfxLength_Object = MibTableColumn
ipv6AddrPfxLength = _Ipv6AddrPfxLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 2),
    _Ipv6AddrPfxLength_Type()
)
ipv6AddrPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPfxLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPfxLength.setUnits("bits")
if mibBuilder.loadTexts:
    ipv6AddrPfxLength.setDescription("The length of the prefix (in bits) associated with the IPv6 address of this entry. This object is obsoleted by the IP-MIB::ipAddressPrefixLength in the row of the IP-MIB::ipAddressPrefixTable to which the IP-MIB::ipAddressPrefix points.")


class _Ipv6AddrType_Type(Integer32):
    """Custom type ipv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("stateful", 2),
          ("unknown", 3))
    )


_Ipv6AddrType_Type.__name__ = "Integer32"
_Ipv6AddrType_Object = MibTableColumn
ipv6AddrType = _Ipv6AddrType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 3),
    _Ipv6AddrType_Type()
)
ipv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrType.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrType.setDescription("The type of address. Note that 'stateless(1)' refers to an address that was statelessly autoconfigured; 'stateful(2)' refers to a address which was acquired by via a stateful protocol (e.g. DHCPv6, manual configuration). This object is obsoleted by IP-MIB::ipAddressOrigin.")
_Ipv6AddrAnycastFlag_Type = TruthValue
_Ipv6AddrAnycastFlag_Object = MibTableColumn
ipv6AddrAnycastFlag = _Ipv6AddrAnycastFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 4),
    _Ipv6AddrAnycastFlag_Type()
)
ipv6AddrAnycastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrAnycastFlag.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrAnycastFlag.setDescription("This object has the value 'true(1)', if this address is an anycast address and the value 'false(2)' otherwise. This object is obsoleted by a value of 'anycast(2)' in IP-MIB::ipAddressType.")


class _Ipv6AddrStatus_Type(Integer32):
    """Custom type ipv6AddrStatus based on Integer32"""
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
        *(("preferred", 1),
          ("deprecated", 2),
          ("invalid", 3),
          ("inaccessible", 4),
          ("unknown", 5))
    )


_Ipv6AddrStatus_Type.__name__ = "Integer32"
_Ipv6AddrStatus_Object = MibTableColumn
ipv6AddrStatus = _Ipv6AddrStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 5),
    _Ipv6AddrStatus_Type()
)
ipv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrStatus.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrStatus.setDescription("Address status. The preferred(1) state indicates that this is a valid address that can appear as the destination or source address of a packet. The deprecated(2) state indicates that this is a valid but deprecated address that should no longer be used as a source address in new communications, but packets addressed to such an address are processed as expected. The invalid(3) state indicates that this is not valid address which should not appear as the destination or source address of a packet. The inaccessible(4) state indicates that the address is not accessible because the interface to which this address is assigned is not operational. This object is obsoleted by IP-MIB::ipAddressStatus.")
_Ipv6RouteNumber_Type = Gauge32
_Ipv6RouteNumber_Object = MibScalar
ipv6RouteNumber = _Ipv6RouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 9),
    _Ipv6RouteNumber_Type()
)
ipv6RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNumber.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteNumber.setDescription("The number of current ipv6RouteTable entries. This is primarily to avoid having to read the table in order to determine this number. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteNumber.")
_Ipv6DiscardedRoutes_Type = Counter32
_Ipv6DiscardedRoutes_Object = MibScalar
ipv6DiscardedRoutes = _Ipv6DiscardedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 10),
    _Ipv6DiscardedRoutes_Type()
)
ipv6DiscardedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DiscardedRoutes.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6DiscardedRoutes.setDescription("The number of routing entries which were chosen to be discarded even though they are valid. One possible reason for discarding such an entry could be to free-up buffer space for other routing entries. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteDiscards.")
_Ipv6RouteTable_Object = MibTable
ipv6RouteTable = _Ipv6RouteTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11)
)
if mibBuilder.loadTexts:
    ipv6RouteTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteTable.setDescription("IPv6 Routing table. This table contains an entry for each valid IPv6 unicast route that can be used for packet forwarding determination. This table is obsoleted by IP-FORWARD-MIB::inetCidrRouteTable.")
_Ipv6RouteEntry_Object = MibTableRow
ipv6RouteEntry = _Ipv6RouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1)
)
ipv6RouteEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6RouteDest"),
    (0, "IPV6-MIB", "ipv6RoutePfxLength"),
    (0, "IPV6-MIB", "ipv6RouteIndex"),
)
if mibBuilder.loadTexts:
    ipv6RouteEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteEntry.setDescription("A routing entry. This entry is obsoleted by IP-FORWARD-MIB::inetCidrRouteEntry.")
_Ipv6RouteDest_Type = Ipv6Address
_Ipv6RouteDest_Object = MibTableColumn
ipv6RouteDest = _Ipv6RouteDest_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 1),
    _Ipv6RouteDest_Type()
)
ipv6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RouteDest.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteDest.setDescription("The destination IPv6 address of this route. This object may not take a Multicast address value. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteDest.")


class _Ipv6RoutePfxLength_Type(Integer32):
    """Custom type ipv6RoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6RoutePfxLength_Type.__name__ = "Integer32"
_Ipv6RoutePfxLength_Object = MibTableColumn
ipv6RoutePfxLength = _Ipv6RoutePfxLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 2),
    _Ipv6RoutePfxLength_Type()
)
ipv6RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RoutePfxLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RoutePfxLength.setUnits("bits")
if mibBuilder.loadTexts:
    ipv6RoutePfxLength.setDescription("Indicates the prefix length of the destination address. This object is obsoleted by IP-FORWARD-MIB::inetCidrRoutePfxLen.")
_Ipv6RouteIndex_Type = Unsigned32
_Ipv6RouteIndex_Object = MibTableColumn
ipv6RouteIndex = _Ipv6RouteIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 3),
    _Ipv6RouteIndex_Type()
)
ipv6RouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RouteIndex.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteIndex.setDescription("The value which uniquely identifies the route among the routes to the same network layer destination. The way this value is chosen is implementation specific but it must be unique for ipv6RouteDest/ipv6RoutePfxLength pair and remain constant for the life of the route. This object is obsoleted by IP-FORWARD-MIB::inetCidrRoutePolicy.")
_Ipv6RouteIfIndex_Type = Ipv6IfIndexOrZero
_Ipv6RouteIfIndex_Object = MibTableColumn
ipv6RouteIfIndex = _Ipv6RouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 4),
    _Ipv6RouteIfIndex_Type()
)
ipv6RouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteIfIndex.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteIfIndex.setDescription("The index value which uniquely identifies the local interface through which the next hop of this route should be reached. The interface identified by a particular value of this index is the same interface as identified by the same value of ipv6IfIndex. For routes of the discard type this value can be zero. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteIfIndex.")
_Ipv6RouteNextHop_Type = Ipv6Address
_Ipv6RouteNextHop_Object = MibTableColumn
ipv6RouteNextHop = _Ipv6RouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 5),
    _Ipv6RouteNextHop_Type()
)
ipv6RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNextHop.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteNextHop.setDescription("On remote routes, the address of the next system en route; otherwise, ::0 ('00000000000000000000000000000000'H in ASN.1 string representation). This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteNextHop.")


class _Ipv6RouteType_Type(Integer32):
    """Custom type ipv6RouteType based on Integer32"""
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
          ("discard", 2),
          ("local", 3),
          ("remote", 4))
    )


_Ipv6RouteType_Type.__name__ = "Integer32"
_Ipv6RouteType_Object = MibTableColumn
ipv6RouteType = _Ipv6RouteType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 6),
    _Ipv6RouteType_Type()
)
ipv6RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteType.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteType.setDescription("The type of route. Note that 'local(3)' refers to a route for which the next hop is the final destination; 'remote(4)' refers to a route for which the next hop is not the final destination; 'discard(2)' refers to a route indicating that packets to destinations matching this route are to be discarded (sometimes called black-hole route). This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteType.")


class _Ipv6RouteProtocol_Type(Integer32):
    """Custom type ipv6RouteProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("ndisc", 4),
          ("rip", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("idrp", 8),
          ("igrp", 9))
    )


_Ipv6RouteProtocol_Type.__name__ = "Integer32"
_Ipv6RouteProtocol_Object = MibTableColumn
ipv6RouteProtocol = _Ipv6RouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 7),
    _Ipv6RouteProtocol_Type()
)
ipv6RouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteProtocol.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteProtocol.setDescription("The routing mechanism via which this route was learned. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteProto.")
_Ipv6RoutePolicy_Type = Integer32
_Ipv6RoutePolicy_Object = MibTableColumn
ipv6RoutePolicy = _Ipv6RoutePolicy_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 8),
    _Ipv6RoutePolicy_Type()
)
ipv6RoutePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RoutePolicy.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RoutePolicy.setDescription("The general set of conditions that would cause the selection of one multipath route (set of next hops for a given destination) is referred to as 'policy'. Unless the mechanism indicated by ipv6RouteProtocol specified otherwise, the policy specifier is the 8-bit Traffic Class field of the IPv6 packet header that is zero extended at the left to a 32-bit value. Protocols defining 'policy' otherwise must either define a set of values which are valid for this object or must implement an integer- instanced policy table for which this object's value acts as an index. This object is obsoleted by IP-FORWARD-MIB::inetCidrRoutePolicy.")
_Ipv6RouteAge_Type = Unsigned32
_Ipv6RouteAge_Object = MibTableColumn
ipv6RouteAge = _Ipv6RouteAge_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 9),
    _Ipv6RouteAge_Type()
)
ipv6RouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteAge.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteAge.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6RouteAge.setDescription("The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteAge.")
_Ipv6RouteNextHopRDI_Type = Unsigned32
_Ipv6RouteNextHopRDI_Object = MibTableColumn
ipv6RouteNextHopRDI = _Ipv6RouteNextHopRDI_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 10),
    _Ipv6RouteNextHopRDI_Type()
)
ipv6RouteNextHopRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNextHopRDI.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteNextHopRDI.setDescription("The Routing Domain ID of the Next Hop. The semantics of this object are determined by the routing-protocol specified in the route's ipv6RouteProtocol value. When this object is unknown or not relevant its value should be set to zero. This object is obsolete, and it has no replacement. The Routing Domain ID concept did not catch on.")
_Ipv6RouteMetric_Type = Unsigned32
_Ipv6RouteMetric_Object = MibTableColumn
ipv6RouteMetric = _Ipv6RouteMetric_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 11),
    _Ipv6RouteMetric_Type()
)
ipv6RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteMetric.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteMetric.setDescription("The routing metric for this route. The semantics of this metric are determined by the routing protocol specified in the route's ipv6RouteProtocol value. When this is unknown or not relevant to the protocol indicated by ipv6RouteProtocol, the object value should be set to its maximum value (4,294,967,295). This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteMetric1.")
_Ipv6RouteWeight_Type = Unsigned32
_Ipv6RouteWeight_Object = MibTableColumn
ipv6RouteWeight = _Ipv6RouteWeight_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 12),
    _Ipv6RouteWeight_Type()
)
ipv6RouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteWeight.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteWeight.setDescription("The system internal weight value for this route. The semantics of this value are determined by the implementation specific rules. Generally, within routes with the same ipv6RoutePolicy value, the lower the weight value the more preferred is the route. This object is obsoleted, and it has not been replaced.")
_Ipv6RouteInfo_Type = RowPointer
_Ipv6RouteInfo_Object = MibTableColumn
ipv6RouteInfo = _Ipv6RouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 13),
    _Ipv6RouteInfo_Type()
)
ipv6RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteInfo.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteInfo.setDescription("A reference to MIB definitions specific to the particular routing protocol which is responsible for this route, as determined by the value specified in the route's ipv6RouteProto value. If this information is not present, its value should be set to the OBJECT ID { 0 0 }, which is a syntactically valid object identifier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value. This object is obsoleted, and it has not been replaced.")


class _Ipv6RouteValid_Type(TruthValue):
    """Custom type ipv6RouteValid based on TruthValue"""
    defaultValue = 1


_Ipv6RouteValid_Type.__name__ = "TruthValue"
_Ipv6RouteValid_Object = MibTableColumn
ipv6RouteValid = _Ipv6RouteValid_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 14),
    _Ipv6RouteValid_Type()
)
ipv6RouteValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6RouteValid.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteValid.setDescription("Setting this object to the value 'false(2)' has the effect of invalidating the corresponding entry in the ipv6RouteTable object. That is, it effectively disassociates the destination identified with said entry from the route identified with said entry. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipv6RouteValid object. This object is obsoleted by IP-FORWARD-MIB::inetCidrRouteStatus.")
_Ipv6NetToMediaTable_Object = MibTable
ipv6NetToMediaTable = _Ipv6NetToMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12)
)
if mibBuilder.loadTexts:
    ipv6NetToMediaTable.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaTable.setDescription("The IPv6 Address Translation table used for mapping from IPv6 addresses to physical addresses. The IPv6 address translation table contain the Ipv6Address to `physical' address equivalencies. Some interfaces do not use translation tables for determining address equivalencies; if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries. This table is obsoleted by IP-MIB::ipNetToPhysicalTable.")
_Ipv6NetToMediaEntry_Object = MibTableRow
ipv6NetToMediaEntry = _Ipv6NetToMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1)
)
ipv6NetToMediaEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipv6NetToMediaEntry.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaEntry.setDescription("Each entry contains one IPv6 address to `physical' address equivalence. This entry is obsoleted by IP-MIB::ipNetToPhysicalEntry.")
_Ipv6NetToMediaNetAddress_Type = Ipv6Address
_Ipv6NetToMediaNetAddress_Object = MibTableColumn
ipv6NetToMediaNetAddress = _Ipv6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 1),
    _Ipv6NetToMediaNetAddress_Type()
)
ipv6NetToMediaNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6NetToMediaNetAddress.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaNetAddress.setDescription("The IPv6 Address corresponding to the media-dependent `physical' address. This object is obsoleted by IP-MIB::ipNetToPhysicalNetAddress.")
_Ipv6NetToMediaPhysAddress_Type = PhysAddress
_Ipv6NetToMediaPhysAddress_Object = MibTableColumn
ipv6NetToMediaPhysAddress = _Ipv6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 2),
    _Ipv6NetToMediaPhysAddress_Type()
)
ipv6NetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NetToMediaPhysAddress.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaPhysAddress.setDescription("The media-dependent `physical' address. This object is obsoleted by IP-MIB::ipNetToPhysicalPhysAddress.")


class _Ipv6NetToMediaType_Type(Integer32):
    """Custom type ipv6NetToMediaType based on Integer32"""
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
          ("dynamic", 2),
          ("static", 3),
          ("local", 4))
    )


_Ipv6NetToMediaType_Type.__name__ = "Integer32"
_Ipv6NetToMediaType_Object = MibTableColumn
ipv6NetToMediaType = _Ipv6NetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 3),
    _Ipv6NetToMediaType_Type()
)
ipv6NetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NetToMediaType.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaType.setDescription("The type of the mapping. The 'dynamic(2)' type indicates that the IPv6 address to physical addresses mapping has been dynamically resolved using the IPv6 Neighbor Discovery protocol. The static(3)' types indicates that the mapping has been statically configured. The local(4) indicates that the mapping is provided for an entity's own interface address. This object is obsoleted by IP-MIB::ipNetToPhysicalType.")


class _Ipv6IfNetToMediaState_Type(Integer32):
    """Custom type ipv6IfNetToMediaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6))
    )


_Ipv6IfNetToMediaState_Type.__name__ = "Integer32"
_Ipv6IfNetToMediaState_Object = MibTableColumn
ipv6IfNetToMediaState = _Ipv6IfNetToMediaState_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 4),
    _Ipv6IfNetToMediaState_Type()
)
ipv6IfNetToMediaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaState.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaState.setDescription("The Neighbor Unreachability Detection [RFC2461] state for the interface when the address mapping in this entry is used. This object is obsoleted by IP-MIB::ipNetToPhysicalState.")
_Ipv6IfNetToMediaLastUpdated_Type = TimeStamp
_Ipv6IfNetToMediaLastUpdated_Object = MibTableColumn
ipv6IfNetToMediaLastUpdated = _Ipv6IfNetToMediaLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 5),
    _Ipv6IfNetToMediaLastUpdated_Type()
)
ipv6IfNetToMediaLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaLastUpdated.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaLastUpdated.setDescription("The value of sysUpTime at the time this entry was last updated. If this entry was updated prior to the last re-initialization of the local network management subsystem, then this object contains a zero value. This object is obsoleted by IP-MIB::ipNetToPhysicalLastUpdated.")


class _Ipv6NetToMediaValid_Type(TruthValue):
    """Custom type ipv6NetToMediaValid based on TruthValue"""
    defaultValue = 1


_Ipv6NetToMediaValid_Type.__name__ = "TruthValue"
_Ipv6NetToMediaValid_Object = MibTableColumn
ipv6NetToMediaValid = _Ipv6NetToMediaValid_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 6),
    _Ipv6NetToMediaValid_Type()
)
ipv6NetToMediaValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6NetToMediaValid.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6NetToMediaValid.setDescription("Setting this object to the value 'false(2)' has the effect of invalidating the corresponding entry in the ipv6NetToMediaTable. That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipv6NetToMediaValid object. This object is obsoleted by IP-MIB::ipNetToPhysicalRowStatus.")
_Ipv6Notifications_ObjectIdentity = ObjectIdentity
ipv6Notifications = _Ipv6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 2)
)
_Ipv6NotificationPrefix_ObjectIdentity = ObjectIdentity
ipv6NotificationPrefix = _Ipv6NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 2, 0)
)
_Ipv6Conformance_ObjectIdentity = ObjectIdentity
ipv6Conformance = _Ipv6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3)
)
_Ipv6Compliances_ObjectIdentity = ObjectIdentity
ipv6Compliances = _Ipv6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3, 1)
)
_Ipv6Groups_ObjectIdentity = ObjectIdentity
ipv6Groups = _Ipv6Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3, 2)
)
ipv6IfEntry.registerAugmentions(
    ("IPV6-MIB",
     "ipv6IfStatsEntry")
)
ipv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())

# Managed Objects groups

ipv6GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 55, 3, 2, 1)
)
ipv6GeneralGroup.setObjects(
      *(("IPV6-MIB", "ipv6Forwarding"),
        ("IPV6-MIB", "ipv6DefaultHopLimit"),
        ("IPV6-MIB", "ipv6Interfaces"),
        ("IPV6-MIB", "ipv6IfTableLastChange"),
        ("IPV6-MIB", "ipv6IfDescr"),
        ("IPV6-MIB", "ipv6IfLowerLayer"),
        ("IPV6-MIB", "ipv6IfEffectiveMtu"),
        ("IPV6-MIB", "ipv6IfReasmMaxSize"),
        ("IPV6-MIB", "ipv6IfIdentifier"),
        ("IPV6-MIB", "ipv6IfIdentifierLength"),
        ("IPV6-MIB", "ipv6IfPhysicalAddress"),
        ("IPV6-MIB", "ipv6IfAdminStatus"),
        ("IPV6-MIB", "ipv6IfOperStatus"),
        ("IPV6-MIB", "ipv6IfLastChange"),
        ("IPV6-MIB", "ipv6IfStatsInReceives"),
        ("IPV6-MIB", "ipv6IfStatsInHdrErrors"),
        ("IPV6-MIB", "ipv6IfStatsInTooBigErrors"),
        ("IPV6-MIB", "ipv6IfStatsInNoRoutes"),
        ("IPV6-MIB", "ipv6IfStatsInAddrErrors"),
        ("IPV6-MIB", "ipv6IfStatsInUnknownProtos"),
        ("IPV6-MIB", "ipv6IfStatsInTruncatedPkts"),
        ("IPV6-MIB", "ipv6IfStatsInDiscards"),
        ("IPV6-MIB", "ipv6IfStatsInDelivers"),
        ("IPV6-MIB", "ipv6IfStatsOutForwDatagrams"),
        ("IPV6-MIB", "ipv6IfStatsOutRequests"),
        ("IPV6-MIB", "ipv6IfStatsOutDiscards"),
        ("IPV6-MIB", "ipv6IfStatsOutFragOKs"),
        ("IPV6-MIB", "ipv6IfStatsOutFragFails"),
        ("IPV6-MIB", "ipv6IfStatsOutFragCreates"),
        ("IPV6-MIB", "ipv6IfStatsReasmReqds"),
        ("IPV6-MIB", "ipv6IfStatsReasmOKs"),
        ("IPV6-MIB", "ipv6IfStatsReasmFails"),
        ("IPV6-MIB", "ipv6IfStatsInMcastPkts"),
        ("IPV6-MIB", "ipv6IfStatsOutMcastPkts"),
        ("IPV6-MIB", "ipv6AddrPrefixOnLinkFlag"),
        ("IPV6-MIB", "ipv6AddrPrefixAutonomousFlag"),
        ("IPV6-MIB", "ipv6AddrPrefixAdvPreferredLifetime"),
        ("IPV6-MIB", "ipv6AddrPrefixAdvValidLifetime"),
        ("IPV6-MIB", "ipv6AddrPfxLength"),
        ("IPV6-MIB", "ipv6AddrType"),
        ("IPV6-MIB", "ipv6AddrAnycastFlag"),
        ("IPV6-MIB", "ipv6AddrStatus"),
        ("IPV6-MIB", "ipv6RouteNumber"),
        ("IPV6-MIB", "ipv6DiscardedRoutes"),
        ("IPV6-MIB", "ipv6RouteIfIndex"),
        ("IPV6-MIB", "ipv6RouteNextHop"),
        ("IPV6-MIB", "ipv6RouteType"),
        ("IPV6-MIB", "ipv6RouteProtocol"),
        ("IPV6-MIB", "ipv6RoutePolicy"),
        ("IPV6-MIB", "ipv6RouteAge"),
        ("IPV6-MIB", "ipv6RouteNextHopRDI"),
        ("IPV6-MIB", "ipv6RouteMetric"),
        ("IPV6-MIB", "ipv6RouteWeight"),
        ("IPV6-MIB", "ipv6RouteInfo"),
        ("IPV6-MIB", "ipv6RouteValid"),
        ("IPV6-MIB", "ipv6NetToMediaPhysAddress"),
        ("IPV6-MIB", "ipv6NetToMediaType"),
        ("IPV6-MIB", "ipv6IfNetToMediaState"),
        ("IPV6-MIB", "ipv6IfNetToMediaLastUpdated"),
        ("IPV6-MIB", "ipv6NetToMediaValid"))
)
if mibBuilder.loadTexts:
    ipv6GeneralGroup.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6GeneralGroup.setDescription("The IPv6 group of objects providing for basic management of IPv6 entities. This group is obsoleted by various groups in IP-MIB.")


# Notification objects

ipv6IfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 55, 2, 0, 1)
)
ipv6IfStateChange.setObjects(
      *(("IPV6-MIB", "ipv6IfDescr"),
        ("IPV6-MIB", "ipv6IfOperStatus"))
)
if mibBuilder.loadTexts:
    ipv6IfStateChange.setStatus(
        "obsolete"
    )
if mibBuilder.loadTexts:
    ipv6IfStateChange.setDescription("An ipv6IfStateChange notification signifies that there has been a change in the state of an ipv6 interface. This notification should be generated when the interface's operational status transitions to or from the up(1) state. This object is obsoleted by IF-MIB::linkUp and IF-MIB::linkDown notifications.")


# Notifications groups

ipv6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 55, 3, 2, 2)
)
ipv6NotificationGroup.setObjects(
    ("IPV6-MIB", "ipv6IfStateChange")
)
if mibBuilder.loadTexts:
    ipv6NotificationGroup.setStatus(
        "obsolete"
    )
if mibBuilder.loadTexts:
    ipv6NotificationGroup.setDescription("The notification that an IPv6 entity is required to implement. This group is obsoleted by IF-MIB::linkUpDownNotificationsGroup.")


# Agent capabilities


# Module compliance

ipv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 55, 3, 1, 1)
)
ipv6Compliance.setObjects(
      *(("IPV6-MIB", "ipv6GeneralGroup"),
        ("IPV6-MIB", "ipv6NotificationGroup"))
)
if mibBuilder.loadTexts:
    ipv6Compliance.setStatus(
        "obsolete"
    )
if mibBuilder.loadTexts:
    ipv6Compliance.setDescription("The compliance statement for SNMPv2 entities which implement ipv6 MIB. This compliance statement is obsoleted by IP-MIB::ipMIBCompliance2.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "IPV6-MIB",
    **{"ipv6MIB": ipv6MIB,
       "ipv6MIBObjects": ipv6MIBObjects,
       "ipv6Forwarding": ipv6Forwarding,
       "ipv6DefaultHopLimit": ipv6DefaultHopLimit,
       "ipv6Interfaces": ipv6Interfaces,
       "ipv6IfTableLastChange": ipv6IfTableLastChange,
       "ipv6IfTable": ipv6IfTable,
       "ipv6IfEntry": ipv6IfEntry,
       "ipv6IfIndex": ipv6IfIndex,
       "ipv6IfDescr": ipv6IfDescr,
       "ipv6IfLowerLayer": ipv6IfLowerLayer,
       "ipv6IfEffectiveMtu": ipv6IfEffectiveMtu,
       "ipv6IfReasmMaxSize": ipv6IfReasmMaxSize,
       "ipv6IfIdentifier": ipv6IfIdentifier,
       "ipv6IfIdentifierLength": ipv6IfIdentifierLength,
       "ipv6IfPhysicalAddress": ipv6IfPhysicalAddress,
       "ipv6IfAdminStatus": ipv6IfAdminStatus,
       "ipv6IfOperStatus": ipv6IfOperStatus,
       "ipv6IfLastChange": ipv6IfLastChange,
       "ipv6IfStatsTable": ipv6IfStatsTable,
       "ipv6IfStatsEntry": ipv6IfStatsEntry,
       "ipv6IfStatsInReceives": ipv6IfStatsInReceives,
       "ipv6IfStatsInHdrErrors": ipv6IfStatsInHdrErrors,
       "ipv6IfStatsInTooBigErrors": ipv6IfStatsInTooBigErrors,
       "ipv6IfStatsInNoRoutes": ipv6IfStatsInNoRoutes,
       "ipv6IfStatsInAddrErrors": ipv6IfStatsInAddrErrors,
       "ipv6IfStatsInUnknownProtos": ipv6IfStatsInUnknownProtos,
       "ipv6IfStatsInTruncatedPkts": ipv6IfStatsInTruncatedPkts,
       "ipv6IfStatsInDiscards": ipv6IfStatsInDiscards,
       "ipv6IfStatsInDelivers": ipv6IfStatsInDelivers,
       "ipv6IfStatsOutForwDatagrams": ipv6IfStatsOutForwDatagrams,
       "ipv6IfStatsOutRequests": ipv6IfStatsOutRequests,
       "ipv6IfStatsOutDiscards": ipv6IfStatsOutDiscards,
       "ipv6IfStatsOutFragOKs": ipv6IfStatsOutFragOKs,
       "ipv6IfStatsOutFragFails": ipv6IfStatsOutFragFails,
       "ipv6IfStatsOutFragCreates": ipv6IfStatsOutFragCreates,
       "ipv6IfStatsReasmReqds": ipv6IfStatsReasmReqds,
       "ipv6IfStatsReasmOKs": ipv6IfStatsReasmOKs,
       "ipv6IfStatsReasmFails": ipv6IfStatsReasmFails,
       "ipv6IfStatsInMcastPkts": ipv6IfStatsInMcastPkts,
       "ipv6IfStatsOutMcastPkts": ipv6IfStatsOutMcastPkts,
       "ipv6AddrPrefixTable": ipv6AddrPrefixTable,
       "ipv6AddrPrefixEntry": ipv6AddrPrefixEntry,
       "ipv6AddrPrefix": ipv6AddrPrefix,
       "ipv6AddrPrefixLength": ipv6AddrPrefixLength,
       "ipv6AddrPrefixOnLinkFlag": ipv6AddrPrefixOnLinkFlag,
       "ipv6AddrPrefixAutonomousFlag": ipv6AddrPrefixAutonomousFlag,
       "ipv6AddrPrefixAdvPreferredLifetime": ipv6AddrPrefixAdvPreferredLifetime,
       "ipv6AddrPrefixAdvValidLifetime": ipv6AddrPrefixAdvValidLifetime,
       "ipv6AddrTable": ipv6AddrTable,
       "ipv6AddrEntry": ipv6AddrEntry,
       "ipv6AddrAddress": ipv6AddrAddress,
       "ipv6AddrPfxLength": ipv6AddrPfxLength,
       "ipv6AddrType": ipv6AddrType,
       "ipv6AddrAnycastFlag": ipv6AddrAnycastFlag,
       "ipv6AddrStatus": ipv6AddrStatus,
       "ipv6RouteNumber": ipv6RouteNumber,
       "ipv6DiscardedRoutes": ipv6DiscardedRoutes,
       "ipv6RouteTable": ipv6RouteTable,
       "ipv6RouteEntry": ipv6RouteEntry,
       "ipv6RouteDest": ipv6RouteDest,
       "ipv6RoutePfxLength": ipv6RoutePfxLength,
       "ipv6RouteIndex": ipv6RouteIndex,
       "ipv6RouteIfIndex": ipv6RouteIfIndex,
       "ipv6RouteNextHop": ipv6RouteNextHop,
       "ipv6RouteType": ipv6RouteType,
       "ipv6RouteProtocol": ipv6RouteProtocol,
       "ipv6RoutePolicy": ipv6RoutePolicy,
       "ipv6RouteAge": ipv6RouteAge,
       "ipv6RouteNextHopRDI": ipv6RouteNextHopRDI,
       "ipv6RouteMetric": ipv6RouteMetric,
       "ipv6RouteWeight": ipv6RouteWeight,
       "ipv6RouteInfo": ipv6RouteInfo,
       "ipv6RouteValid": ipv6RouteValid,
       "ipv6NetToMediaTable": ipv6NetToMediaTable,
       "ipv6NetToMediaEntry": ipv6NetToMediaEntry,
       "ipv6NetToMediaNetAddress": ipv6NetToMediaNetAddress,
       "ipv6NetToMediaPhysAddress": ipv6NetToMediaPhysAddress,
       "ipv6NetToMediaType": ipv6NetToMediaType,
       "ipv6IfNetToMediaState": ipv6IfNetToMediaState,
       "ipv6IfNetToMediaLastUpdated": ipv6IfNetToMediaLastUpdated,
       "ipv6NetToMediaValid": ipv6NetToMediaValid,
       "ipv6Notifications": ipv6Notifications,
       "ipv6NotificationPrefix": ipv6NotificationPrefix,
       "ipv6IfStateChange": ipv6IfStateChange,
       "ipv6Conformance": ipv6Conformance,
       "ipv6Compliances": ipv6Compliances,
       "ipv6Compliance": ipv6Compliance,
       "ipv6Groups": ipv6Groups,
       "ipv6GeneralGroup": ipv6GeneralGroup,
       "ipv6NotificationGroup": ipv6NotificationGroup}
)
