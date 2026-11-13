# SNMP MIB module (ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/ETHERLIKE-MIB
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

(InterfaceIndex,
 ifIndex) = mibBuilder.import_symbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
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
 mib_2,
 transmission) = mibBuilder.import_symbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
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
    "mib-2",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

etherMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 35)
)
if mibBuilder.loadTexts:
    etherMIB.setRevisions(
        ("1999-08-24 04:00",
         "1998-06-03 21:50",
         "1994-02-03 04:00")
    )
if mibBuilder.loadTexts:
    etherMIB.setLastUpdated("9908240400Z")
if mibBuilder.loadTexts:
    etherMIB.setOrganization("IETF Ethernet Interfaces and Hub MIB Working Group")
if mibBuilder.loadTexts:
    etherMIB.setContactInfo("WG E-mail: hubmib@hprnd.rose.hp.com To subscribe: hubmib-request@hprnd.rose.hp.com Chair: Dan Romascanu Postal: Lucent Technologies Atidum Technology Park, Bldg. 3 Tel Aviv 61131 Israel Tel: +972 3 645 8414 E-mail: dromasca@lucent.com Editor: John Flick Postal: Hewlett-Packard Company 8000 Foothills Blvd. M/S 5557 Roseville, CA 95747-5557 USA Tel: +1 916 785 4018 Fax: +1 916 785 1199 E-mail: johnf@rose.hp.com Editor: Jeffrey Johnson Postal: RedBack Networks 2570 North First Street, Suite 410 San Jose, CA, 95131 USA Tel: +1 408 571 2699 Fax: +1 408 571 2698 E-Mail: jeff@redbacknetworks.com")
if mibBuilder.loadTexts:
    etherMIB.setDescription("The MIB module to describe generic objects for Ethernet-like network interfaces. The following reference is used throughout this MIB module: [IEEE 802.3 Std] refers to: IEEE Std 802.3, 1998 Edition: 'Information technology - Telecommunications and information exchange between systems - Local and metropolitan area networks - Specific requirements - Part 3: Carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specifications', September 1998. Of particular interest is Clause 30, '10Mb/s, 100Mb/s and 1000Mb/s Management'.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7)
)
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsTable.setDescription("Statistics for a collection of ethernet-like interfaces attached to a particular system. There will be one row in this table for each ethernet-like interface in the system.")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsEntry.setDescription("Statistics for a particular interface to an ethernet-like medium.")
_Dot3StatsIndex_Type = InterfaceIndex
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsIndex.setReference("RFC 2233, ifIndex")
if mibBuilder.loadTexts:
    dot3StatsIndex.setDescription("An index value that uniquely identifies an interface to an ethernet-like medium. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setReference("[IEEE 802.3 Std.], 30.3.1.1.7, aAlignmentErrors")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setDescription("A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check. The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC. This counter does not increment for 8-bit wide group encoding schemes. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setReference("[IEEE 802.3 Std.], 30.3.1.1.6, aFrameCheckSequenceErrors.")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setDescription("A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check. This count does not include frames received with frame-too-long or frame-too-short error. The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC. Note: Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setReference("[IEEE 802.3 Std.], 30.3.1.1.3, aSingleCollisionFrames.")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setDescription("A count of successfully transmitted frames on a particular interface for which transmission is inhibited by exactly one collision. A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsMultipleCollisionFrames object. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setReference("[IEEE 802.3 Std.], 30.3.1.1.4, aMultipleCollisionFrames.")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setDescription("A count of successfully transmitted frames on a particular interface for which transmission is inhibited by more than one collision. A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsSingleCollisionFrames object. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setReference("[IEEE 802.3 Std.], 7.2.4.6, also 30.3.2.1.4, aSQETestErrors.")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setDescription("A count of times that the SQE TEST ERROR message is generated by the PLS sublayer for a particular interface. The SQE TEST ERROR is set in accordance with the rules for verification of the SQE detection mechanism in the PLS Carrier Sense Function as described in IEEE Std. 802.3, 1998 Edition, section 7.2.4.6. This counter does not increment on interfaces operating at speeds greater than 10 Mb/s, or on interfaces operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setReference("[IEEE 802.3 Std.], 30.3.1.1.9, aFramesWithDeferredXmissions.")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setDescription("A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy. The count represented by an instance of this object does not include frames involved in collisions. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setReference("[IEEE 802.3 Std.], 30.3.1.1.10, aLateCollisions.")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setDescription("The number of times that a collision is detected on a particular interface later than one slotTime into the transmission of a packet. A (late) collision included in a count represented by an instance of this object is also considered as a (generic) collision for purposes of other collision-related statistics. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setReference("[IEEE 802.3 Std.], 30.3.1.1.11, aFramesAbortedDueToXSColls.")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setDescription("A count of frames for which transmission on a particular interface fails due to excessive collisions. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setReference("[IEEE 802.3 Std.], 30.3.1.1.12, aFramesLostDueToIntMACXmitError.")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setDescription("A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object. The precise meaning of the count represented by an instance of this object is implementation- specific. In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setReference("[IEEE 802.3 Std.], 30.3.1.1.13, aCarrierSenseErrors.")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setDescription("The number of times that the carrier sense condition was lost or never asserted when attempting to transmit a frame on a particular interface. The count represented by an instance of this object is incremented at most once per transmission attempt, even if the carrier sense condition fluctuates during a transmission attempt. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setReference("[IEEE 802.3 Std.], 30.3.1.1.25, aFrameTooLongErrors.")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setDescription("A count of frames received on a particular interface that exceed the maximum permitted frame size. The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setReference("[IEEE 802.3 Std.], 30.3.1.1.15, aFramesLostDueToIntMACRcvError.")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setDescription("A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object. The precise meaning of the count represented by an instance of this object is implementation- specific. In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3StatsEtherChipSet_Type = ObjectIdentifier
_Dot3StatsEtherChipSet_Object = MibTableColumn
dot3StatsEtherChipSet = _Dot3StatsEtherChipSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 17),
    _Dot3StatsEtherChipSet_Type()
)
dot3StatsEtherChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsEtherChipSet.setStatus("deprecated")
if mibBuilder.loadTexts:
    dot3StatsEtherChipSet.setDescription("******** THIS OBJECT IS DEPRECATED ******** This object contains an OBJECT IDENTIFIER which identifies the chipset used to realize the interface. Ethernet-like interfaces are typically built out of several different chips. The MIB implementor is presented with a decision of which chip to identify via this object. The implementor should identify the chip which is usually called the Medium Access Control chip. If no such chip is easily identifiable, the implementor should identify the chip which actually gathers the transmit and receive statistics and error indications. This would allow a manager station to correlate the statistics and the chip generating them, giving it the ability to take into account any known anomalies in the chip.")
_Dot3StatsSymbolErrors_Type = Counter32
_Dot3StatsSymbolErrors_Object = MibTableColumn
dot3StatsSymbolErrors = _Dot3StatsSymbolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 18),
    _Dot3StatsSymbolErrors_Type()
)
dot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setReference("[IEEE 802.3 Std.], 30.3.2.1.5, aSymbolErrorDuringCarrier.")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setDescription("For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present. For an interface operating in half-duplex mode at 1000 Mb/s, the number of times the receiving media is non-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII. For an interface operating in full-duplex mode at 1000 Mb/s, the number of times the receiving media is non-idle a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII. The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event. This count does not increment if a collision is present. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")


class _Dot3StatsDuplexStatus_Type(Integer32):
    """Custom type dot3StatsDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_Dot3StatsDuplexStatus_Type.__name__ = "Integer32"
_Dot3StatsDuplexStatus_Object = MibTableColumn
dot3StatsDuplexStatus = _Dot3StatsDuplexStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 19),
    _Dot3StatsDuplexStatus_Type()
)
dot3StatsDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setStatus("current")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setReference("[IEEE 802.3 Std.], 30.3.1.1.32, aDuplexStatus.")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setDescription("The current mode of operation of the MAC entity. 'unknown' indicates that the current duplex mode could not be determined. Management control of the duplex mode is accomplished through the MAU MIB. When an interface does not support autonegotiation, or when autonegotiation is not enabled, the duplex mode is controlled using ifMauDefaultType. When autonegotiation is supported and enabled, duplex mode is controlled using ifMauAutoNegAdvertisedBits. In either case, the currently operating duplex mode is reflected both in this object and in ifMauType. Note that this object provides redundant information with ifMauType. Normally, redundant objects are discouraged. However, in this instance, it allows a management application to determine the duplex status of an interface without having to know every possible value of ifMauType. This was felt to be sufficiently valuable to justify the redundancy.")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("current")
if mibBuilder.loadTexts:
    dot3CollTable.setReference("[IEEE 802.3 Std.], 30.3.1.1.30, aCollisionFrames.")
if mibBuilder.loadTexts:
    dot3CollTable.setDescription("A collection of collision histograms for a particular set of interfaces.")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ETHERLIKE-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("current")
if mibBuilder.loadTexts:
    dot3CollEntry.setDescription("A cell in the histogram of per-frame collisions for a particular interface. An instance of this object represents the frequency of individual MAC frames for which the transmission (successful or otherwise) on a particular interface is accompanied by a particular number of media collisions.")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("current")
if mibBuilder.loadTexts:
    dot3CollCount.setDescription("The number of per-frame media collisions for which a particular collision histogram cell represents the frequency on a particular interface.")
_Dot3CollFrequencies_Type = Counter32
_Dot3CollFrequencies_Object = MibTableColumn
dot3CollFrequencies = _Dot3CollFrequencies_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3),
    _Dot3CollFrequencies_Type()
)
dot3CollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setStatus("current")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setDescription("A count of individual MAC frames for which the transmission (successful or otherwise) on a particular interface occurs after the frame has experienced exactly the number of collisions in the associated dot3CollCount object. For example, a frame which is transmitted on interface 77 after experiencing exactly 4 collisions would be indicated by incrementing only dot3CollFrequencies.77.4. No other instance of dot3CollFrequencies would be incremented in this example. This counter does not increment when the interface is operating in full-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3Tests_ObjectIdentity = ObjectIdentity
dot3Tests = _Dot3Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6)
)
_Dot3TestTdr_ObjectIdentity = ObjectIdentity
dot3TestTdr = _Dot3TestTdr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 1)
)
if mibBuilder.loadTexts:
    dot3TestTdr.setStatus("current")
if mibBuilder.loadTexts:
    dot3TestTdr.setDescription("The Time-Domain Reflectometry (TDR) test is specific to ethernet-like interfaces of type 10Base5 and 10Base2. The TDR value may be useful in determining the approximate distance to a cable fault. It is advisable to repeat this test to check for a consistent resulting TDR value, to verify that there is a fault. A TDR test returns as its result the time interval, measured in 10 MHz ticks or 100 nsec units, between the start of TDR test transmission and the subsequent detection of a collision or deassertion of carrier. On successful completion of a TDR test, the result is stored as the value of an appropriate instance of an appropriate vendor specific MIB object, and the OBJECT IDENTIFIER of that instance is stored in the appropriate instance of the appropriate test result code object (thereby indicating where the result has been stored).")
_Dot3TestLoopBack_ObjectIdentity = ObjectIdentity
dot3TestLoopBack = _Dot3TestLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 2)
)
if mibBuilder.loadTexts:
    dot3TestLoopBack.setStatus("current")
if mibBuilder.loadTexts:
    dot3TestLoopBack.setDescription("This test configures the MAC chip and executes an internal loopback test of memory, data paths, and the MAC chip logic. This loopback test can only be executed if the interface is offline. Once the test has completed, the MAC chip should be reinitialized for network operation, but it should remain offline. If an error occurs during a test, the appropriate test result object will be set to indicate a failure. The two OBJECT IDENTIFIER values dot3ErrorInitError and dot3ErrorLoopbackError may be used to provided more information as values for an appropriate test result code object.")
_Dot3Errors_ObjectIdentity = ObjectIdentity
dot3Errors = _Dot3Errors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7)
)
_Dot3ErrorInitError_ObjectIdentity = ObjectIdentity
dot3ErrorInitError = _Dot3ErrorInitError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot3ErrorInitError.setStatus("current")
if mibBuilder.loadTexts:
    dot3ErrorInitError.setDescription("Couldn't initialize MAC chip for test.")
_Dot3ErrorLoopbackError_ObjectIdentity = ObjectIdentity
dot3ErrorLoopbackError = _Dot3ErrorLoopbackError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    dot3ErrorLoopbackError.setStatus("current")
if mibBuilder.loadTexts:
    dot3ErrorLoopbackError.setDescription("Expected data not received (or not received correctly) in loopback test.")
_Dot3ControlTable_Object = MibTable
dot3ControlTable = _Dot3ControlTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9)
)
if mibBuilder.loadTexts:
    dot3ControlTable.setStatus("current")
if mibBuilder.loadTexts:
    dot3ControlTable.setDescription("A table of descriptive and status information about the MAC Control sublayer on the ethernet-like interfaces attached to a particular system. There will be one row in this table for each ethernet-like interface in the system which implements the MAC Control sublayer. If some, but not all, of the ethernet-like interfaces in the system implement the MAC Control sublayer, there will be fewer rows in this table than in the dot3StatsTable.")
_Dot3ControlEntry_Object = MibTableRow
dot3ControlEntry = _Dot3ControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1)
)
dot3ControlEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3ControlEntry.setStatus("current")
if mibBuilder.loadTexts:
    dot3ControlEntry.setDescription("An entry in the table, containing information about the MAC Control sublayer on a single ethernet-like interface.")


class _Dot3ControlFunctionsSupported_Type(Bits):
    """Custom type dot3ControlFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        ("pause", 0)
    )

_Dot3ControlFunctionsSupported_Type.__name__ = "Bits"
_Dot3ControlFunctionsSupported_Object = MibTableColumn
dot3ControlFunctionsSupported = _Dot3ControlFunctionsSupported_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 1),
    _Dot3ControlFunctionsSupported_Type()
)
dot3ControlFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setStatus("current")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setReference("[IEEE 802.3 Std.], 30.3.3.2, aMACControlFunctionsSupported.")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setDescription("A list of the possible MAC Control functions implemented for this interface.")
_Dot3ControlInUnknownOpcodes_Type = Counter32
_Dot3ControlInUnknownOpcodes_Object = MibTableColumn
dot3ControlInUnknownOpcodes = _Dot3ControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 2),
    _Dot3ControlInUnknownOpcodes_Type()
)
dot3ControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setStatus("current")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setReference("[IEEE 802.3 Std.], 30.3.3.5, aUnsupportedOpcodesReceived")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setDescription("A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3PauseTable_Object = MibTable
dot3PauseTable = _Dot3PauseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10)
)
if mibBuilder.loadTexts:
    dot3PauseTable.setStatus("current")
if mibBuilder.loadTexts:
    dot3PauseTable.setDescription("A table of descriptive and status information about the MAC Control PAUSE function on the ethernet-like interfaces attached to a particular system. There will be one row in this table for each ethernet-like interface in the system which supports the MAC Control PAUSE function (i.e., the 'pause' bit in the corresponding instance of dot3ControlFunctionsSupported is set). If some, but not all, of the ethernet-like interfaces in the system implement the MAC Control PAUSE function (for example, if some interfaces only support half-duplex), there will be fewer rows in this table than in the dot3StatsTable.")
_Dot3PauseEntry_Object = MibTableRow
dot3PauseEntry = _Dot3PauseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1)
)
dot3PauseEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3PauseEntry.setStatus("current")
if mibBuilder.loadTexts:
    dot3PauseEntry.setDescription("An entry in the table, containing information about the MAC Control PAUSE function on a single ethernet-like interface.")


class _Dot3PauseAdminMode_Type(Integer32):
    """Custom type dot3PauseAdminMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseAdminMode_Type.__name__ = "Integer32"
_Dot3PauseAdminMode_Object = MibTableColumn
dot3PauseAdminMode = _Dot3PauseAdminMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 1),
    _Dot3PauseAdminMode_Type()
)
dot3PauseAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3PauseAdminMode.setStatus("current")
if mibBuilder.loadTexts:
    dot3PauseAdminMode.setDescription("This object is used to configure the default administrative PAUSE mode for this interface. This object represents the administratively-configured PAUSE mode for this interface. If auto-negotiation is not enabled or is not implemented for the active MAU attached to this interface, the value of this object determines the operational PAUSE mode of the interface whenever it is operating in full-duplex mode. In this case, a set to this object will force the interface into the specified mode. If auto-negotiation is implemented and enabled for the MAU attached to this interface, the PAUSE mode for this interface is determined by auto-negotiation, and the value of this object denotes the mode to which the interface will automatically revert if/when auto-negotiation is later disabled. Note that when auto-negotiation is running, administrative control of the PAUSE mode may be accomplished using the ifMauAutoNegCapAdvertisedBits object in the MAU-MIB. Note that the value of this object is ignored when the interface is not operating in full-duplex mode. An attempt to set this object to 'enabledXmit(2)' or 'enabledRcv(3)' will fail on interfaces that do not support operation at greater than 100 Mb/s.")


class _Dot3PauseOperMode_Type(Integer32):
    """Custom type dot3PauseOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseOperMode_Type.__name__ = "Integer32"
_Dot3PauseOperMode_Object = MibTableColumn
dot3PauseOperMode = _Dot3PauseOperMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 2),
    _Dot3PauseOperMode_Type()
)
dot3PauseOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3PauseOperMode.setStatus("current")
if mibBuilder.loadTexts:
    dot3PauseOperMode.setDescription("This object reflects the PAUSE mode currently in use on this interface, as determined by either (1) the result of the auto-negotiation function or (2) if auto-negotiation is not enabled or is not implemented for the active MAU attached to this interface, by the value of dot3PauseAdminMode. Interfaces operating at 100 Mb/s or less will never return 'enabledXmit(2)' or 'enabledRcv(3)'. Interfaces operating in half-duplex mode will always return 'disabled(1)'. Interfaces on which auto-negotiation is enabled but not yet completed should return the value 'disabled(1)'.")
_Dot3InPauseFrames_Type = Counter32
_Dot3InPauseFrames_Object = MibTableColumn
dot3InPauseFrames = _Dot3InPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 3),
    _Dot3InPauseFrames_Type()
)
dot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setReference("[IEEE 802.3 Std.], 30.3.4.3, aPAUSEMACCtrlFramesReceived.")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setDescription("A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation. This counter does not increment when the interface is operating in half-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_Dot3OutPauseFrames_Type = Counter32
_Dot3OutPauseFrames_Object = MibTableColumn
dot3OutPauseFrames = _Dot3OutPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 4),
    _Dot3OutPauseFrames_Type()
)
dot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setReference("[IEEE 802.3 Std.], 30.3.4.2, aPAUSEMACCtrlFramesTransmitted.")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setDescription("A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation. This counter does not increment when the interface is operating in half-duplex mode. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_EtherMIBObjects_ObjectIdentity = ObjectIdentity
etherMIBObjects = _EtherMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 1)
)
_EtherConformance_ObjectIdentity = ObjectIdentity
etherConformance = _EtherConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2)
)
_EtherGroups_ObjectIdentity = ObjectIdentity
etherGroups = _EtherGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 1)
)
_EtherCompliances_ObjectIdentity = ObjectIdentity
etherCompliances = _EtherCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 2)
)

# Managed Objects groups

etherStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 1)
)
etherStatsGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsSQETestErrors"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("ETHERLIKE-MIB", "dot3StatsEtherChipSet"))
)
if mibBuilder.loadTexts:
    etherStatsGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    etherStatsGroup.setDescription("********* THIS GROUP IS DEPRECATED ********** A collection of objects providing information applicable to all ethernet-like network interfaces. This object group has been deprecated and replaced by etherStatsBaseGroup and etherStatsLowSpeedGroup.")

etherCollisionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 2)
)
etherCollisionTableGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3CollFrequencies")
)
if mibBuilder.loadTexts:
    etherCollisionTableGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherCollisionTableGroup.setDescription("A collection of objects providing a histogram of packets successfully transmitted after experiencing exactly N collisions.")

etherStats100MbsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 3)
)
etherStats100MbsGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("ETHERLIKE-MIB", "dot3StatsEtherChipSet"),
        ("ETHERLIKE-MIB", "dot3StatsSymbolErrors"))
)
if mibBuilder.loadTexts:
    etherStats100MbsGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    etherStats100MbsGroup.setDescription("********* THIS GROUP IS DEPRECATED ********** A collection of objects providing information applicable to 100 Mb/sec ethernet-like network interfaces. This object group has been deprecated and replaced by etherStatsBaseGroup and etherStatsHighSpeedGroup.")

etherStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 4)
)
etherStatsBaseGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"))
)
if mibBuilder.loadTexts:
    etherStatsBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsBaseGroup.setDescription("A collection of objects providing information applicable to all ethernet-like network interfaces.")

etherStatsLowSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 5)
)
etherStatsLowSpeedGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsSQETestErrors")
)
if mibBuilder.loadTexts:
    etherStatsLowSpeedGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsLowSpeedGroup.setDescription("A collection of objects providing information applicable to ethernet-like network interfaces capable of operating at 10 Mb/s or slower in half-duplex mode.")

etherStatsHighSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 6)
)
etherStatsHighSpeedGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsSymbolErrors")
)
if mibBuilder.loadTexts:
    etherStatsHighSpeedGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighSpeedGroup.setDescription("A collection of objects providing information applicable to ethernet-like network interfaces capable of operating at 100 Mb/s or faster.")

etherDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 7)
)
etherDuplexGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsDuplexStatus")
)
if mibBuilder.loadTexts:
    etherDuplexGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherDuplexGroup.setDescription("A collection of objects providing information about the duplex mode of an ethernet-like network interface.")

etherControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 8)
)
etherControlGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3ControlFunctionsSupported"),
        ("ETHERLIKE-MIB", "dot3ControlInUnknownOpcodes"))
)
if mibBuilder.loadTexts:
    etherControlGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherControlGroup.setDescription("A collection of objects providing information about the MAC Control sublayer on ethernet-like network interfaces.")

etherControlPauseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 9)
)
etherControlPauseGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3PauseAdminMode"),
        ("ETHERLIKE-MIB", "dot3PauseOperMode"),
        ("ETHERLIKE-MIB", "dot3InPauseFrames"),
        ("ETHERLIKE-MIB", "dot3OutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherControlPauseGroup.setStatus("current")
if mibBuilder.loadTexts:
    etherControlPauseGroup.setDescription("A collection of objects providing information about and control of the MAC Control PAUSE function on ethernet-like network interfaces.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etherCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 1)
)
etherCompliance.setObjects(
      *(("ETHERLIKE-MIB", "etherStatsGroup"),
        ("ETHERLIKE-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    etherCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    etherCompliance.setDescription("******** THIS COMPLIANCE IS DEPRECATED ******** The compliance statement for managed network entities which have ethernet-like network interfaces. This compliance is deprecated and replaced by dot3Compliance.")

ether100MbsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 2)
)
ether100MbsCompliance.setObjects(
      *(("ETHERLIKE-MIB", "etherStats100MbsGroup"),
        ("ETHERLIKE-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    ether100MbsCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    ether100MbsCompliance.setDescription("******** THIS COMPLIANCE IS DEPRECATED ******** The compliance statement for managed network entities which have 100 Mb/sec ethernet-like network interfaces. This compliance is deprecated and replaced by dot3Compliance.")

dot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 3)
)
dot3Compliance.setObjects(
      *(("ETHERLIKE-MIB", "etherStatsBaseGroup"),
        ("ETHERLIKE-MIB", "etherDuplexGroup"),
        ("ETHERLIKE-MIB", "etherStatsLowSpeedGroup"),
        ("ETHERLIKE-MIB", "etherStatsHighSpeedGroup"),
        ("ETHERLIKE-MIB", "etherControlGroup"),
        ("ETHERLIKE-MIB", "etherControlPauseGroup"),
        ("ETHERLIKE-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    dot3Compliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    dot3Compliance.setDescription("The compliance statement for managed network entities which have ethernet-like network interfaces.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "ETHERLIKE-MIB",
    **{"dot3": dot3,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3StatsEtherChipSet": dot3StatsEtherChipSet,
       "dot3StatsSymbolErrors": dot3StatsSymbolErrors,
       "dot3StatsDuplexStatus": dot3StatsDuplexStatus,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequencies": dot3CollFrequencies,
       "dot3Tests": dot3Tests,
       "dot3TestTdr": dot3TestTdr,
       "dot3TestLoopBack": dot3TestLoopBack,
       "dot3Errors": dot3Errors,
       "dot3ErrorInitError": dot3ErrorInitError,
       "dot3ErrorLoopbackError": dot3ErrorLoopbackError,
       "dot3ControlTable": dot3ControlTable,
       "dot3ControlEntry": dot3ControlEntry,
       "dot3ControlFunctionsSupported": dot3ControlFunctionsSupported,
       "dot3ControlInUnknownOpcodes": dot3ControlInUnknownOpcodes,
       "dot3PauseTable": dot3PauseTable,
       "dot3PauseEntry": dot3PauseEntry,
       "dot3PauseAdminMode": dot3PauseAdminMode,
       "dot3PauseOperMode": dot3PauseOperMode,
       "dot3InPauseFrames": dot3InPauseFrames,
       "dot3OutPauseFrames": dot3OutPauseFrames,
       "etherMIB": etherMIB,
       "etherMIBObjects": etherMIBObjects,
       "etherConformance": etherConformance,
       "etherGroups": etherGroups,
       "etherStatsGroup": etherStatsGroup,
       "etherCollisionTableGroup": etherCollisionTableGroup,
       "etherStats100MbsGroup": etherStats100MbsGroup,
       "etherStatsBaseGroup": etherStatsBaseGroup,
       "etherStatsLowSpeedGroup": etherStatsLowSpeedGroup,
       "etherStatsHighSpeedGroup": etherStatsHighSpeedGroup,
       "etherDuplexGroup": etherDuplexGroup,
       "etherControlGroup": etherControlGroup,
       "etherControlPauseGroup": etherControlPauseGroup,
       "etherCompliances": etherCompliances,
       "etherCompliance": etherCompliance,
       "ether100MbsCompliance": ether100MbsCompliance,
       "dot3Compliance": dot3Compliance}
)
