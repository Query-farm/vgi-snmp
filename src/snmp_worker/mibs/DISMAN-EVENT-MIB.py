# SNMP MIB module (DISMAN-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/DISMAN-EVENT-MIB
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

(SnmpAdminString,) = mibBuilder.import_symbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,) = mibBuilder.import_symbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.import_symbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 mib_2,
 zeroDotZero) = mibBuilder.import_symbols(
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
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dismanEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 88)
)
if mibBuilder.loadTexts:
    dismanEventMIB.setRevisions(
        ("2001-11-14 00:00",
         "2000-10-16 00:00")
    )
if mibBuilder.loadTexts:
    dismanEventMIB.setLastUpdated("200111140000Z")
if mibBuilder.loadTexts:
    dismanEventMIB.setOrganization("IETF Distributed Management Working Group")
if mibBuilder.loadTexts:
    dismanEventMIB.setContactInfo("Ramanathan Kavasseri Cisco Systems, Inc. 170 West Tasman Drive, San Jose CA 95134-1706. Phone: +1 408 526 4527 Email: ramk@cisco.com")
if mibBuilder.loadTexts:
    dismanEventMIB.setDescription("The MIB module for defining event triggers and actions for network management purposes.")


# Types definitions


# TEXTUAL-CONVENTIONS



class FailureReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("sampleOverrun", -6),
          ("badType", -5),
          ("noResponse", -4),
          ("destinationUnreachable", -3),
          ("badDestination", -2),
          ("localResourceLack", -1),
          ("noError", 0),
          ("tooBig", 1),
          ("noSuchName", 2),
          ("badValue", 3),
          ("readOnly", 4),
          ("genErr", 5),
          ("noAccess", 6),
          ("wrongType", 7),
          ("wrongLength", 8),
          ("wrongEncoding", 9),
          ("wrongValue", 10),
          ("noCreation", 11),
          ("inconsistentValue", 12),
          ("resourceUnavailable", 13),
          ("commitFailed", 14),
          ("undoFailed", 15),
          ("authorizationError", 16),
          ("notWritable", 17),
          ("inconsistentName", 18))
    )

    if mibBuilder.loadTexts:
        description = "Reasons for failures in an attempt to perform a management request. The first group of errors, numbered less than 0, are related to problems in sending the request. The existence of a particular error code here does not imply that all implementations are capable of sensing that error and returning that code. The second group, numbered greater than 0, are copied directly from SNMP protocol operations and are intended to carry exactly the meanings defined for the protocol as returned in an SNMP response. localResourceLack some local resource such as memory lacking or mteResourceSampleInstanceMaximum exceeded badDestination unrecognized domain name or otherwise invalid destination address destinationUnreachable can't get to destination address noResponse no response to SNMP request badType the data syntax of a retrieved object as not as expected sampleOverrun another sample attempt occurred before the previous one completed"


# MIB Managed Objects in the order of their OIDs

_SysUpTimeInstance_ObjectIdentity = ObjectIdentity
sysUpTimeInstance = _SysUpTimeInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 3, 0)
)
_DismanEventMIBObjects_ObjectIdentity = ObjectIdentity
dismanEventMIBObjects = _DismanEventMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1)
)
_MteResource_ObjectIdentity = ObjectIdentity
mteResource = _MteResource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 1)
)


class _MteResourceSampleMinimum_Type(Integer32):
    """Custom type mteResourceSampleMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MteResourceSampleMinimum_Type.__name__ = "Integer32"
_MteResourceSampleMinimum_Object = MibScalar
mteResourceSampleMinimum = _MteResourceSampleMinimum_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 1),
    _MteResourceSampleMinimum_Type()
)
mteResourceSampleMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteResourceSampleMinimum.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleMinimum.setUnits("seconds")
if mibBuilder.loadTexts:
    mteResourceSampleMinimum.setDescription("The minimum mteTriggerFrequency this system will accept. A system may use the larger values of this minimum to lessen the impact of constant sampling. For larger sampling intervals the system samples less often and suffers less overhead. This object provides a way to enforce such lower overhead for all triggers created after it is set. Unless explicitly resource limited, a system's value for this object SHOULD be 1, allowing as small as a 1 second interval for ongoing trigger sampling. Changing this value will not invalidate an existing setting of mteTriggerFrequency.")
_MteResourceSampleInstanceMaximum_Type = Unsigned32
_MteResourceSampleInstanceMaximum_Object = MibScalar
mteResourceSampleInstanceMaximum = _MteResourceSampleInstanceMaximum_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 2),
    _MteResourceSampleInstanceMaximum_Type()
)
mteResourceSampleInstanceMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceMaximum.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceMaximum.setUnits("instances")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceMaximum.setDescription("The maximum number of instance entries this system will support for sampling. These are the entries that maintain state, one for each instance of each sampled object as selected by mteTriggerValueID. Note that wildcarded objects result in multiple instances of this state. A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources. Unless explicitly resource limited, a system's value for this object SHOULD be 0. Changing this value will not eliminate or inhibit existing sample state but could prevent allocation of additional state information.")
_MteResourceSampleInstances_Type = Gauge32
_MteResourceSampleInstances_Object = MibScalar
mteResourceSampleInstances = _MteResourceSampleInstances_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 3),
    _MteResourceSampleInstances_Type()
)
mteResourceSampleInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstances.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstances.setUnits("instances")
if mibBuilder.loadTexts:
    mteResourceSampleInstances.setDescription("The number of currently active instance entries as defined for mteResourceSampleInstanceMaximum.")
_MteResourceSampleInstancesHigh_Type = Gauge32
_MteResourceSampleInstancesHigh_Object = MibScalar
mteResourceSampleInstancesHigh = _MteResourceSampleInstancesHigh_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 4),
    _MteResourceSampleInstancesHigh_Type()
)
mteResourceSampleInstancesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstancesHigh.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstancesHigh.setUnits("instances")
if mibBuilder.loadTexts:
    mteResourceSampleInstancesHigh.setDescription("The highest value of mteResourceSampleInstances that has occurred since initialization of the management system.")
_MteResourceSampleInstanceLacks_Type = Counter32
_MteResourceSampleInstanceLacks_Object = MibScalar
mteResourceSampleInstanceLacks = _MteResourceSampleInstanceLacks_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 5),
    _MteResourceSampleInstanceLacks_Type()
)
mteResourceSampleInstanceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceLacks.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceLacks.setUnits("instances")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceLacks.setDescription("The number of times this system could not take a new sample because that allocation would have exceeded the limit set by mteResourceSampleInstanceMaximum.")
_MteTrigger_ObjectIdentity = ObjectIdentity
mteTrigger = _MteTrigger_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 2)
)
_MteTriggerFailures_Type = Counter32
_MteTriggerFailures_Object = MibScalar
mteTriggerFailures = _MteTriggerFailures_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 1),
    _MteTriggerFailures_Type()
)
mteTriggerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteTriggerFailures.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerFailures.setUnits("failures")
if mibBuilder.loadTexts:
    mteTriggerFailures.setDescription("The number of times an attempt to check for a trigger condition has failed. This counts individually for each attempt in a group of targets or each attempt for a wildcarded object.")
_MteTriggerTable_Object = MibTable
mteTriggerTable = _MteTriggerTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mteTriggerTable.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerTable.setDescription("A table of management event trigger information.")
_MteTriggerEntry_Object = MibTableRow
mteTriggerEntry = _MteTriggerEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1)
)
mteTriggerEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerEntry.setDescription("Information about a single trigger. Applications create and delete entries using mteTriggerEntryStatus.")


class _MteOwner_Type(SnmpAdminString):
    """Custom type mteOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteOwner_Type.__name__ = "SnmpAdminString"
_MteOwner_Object = MibTableColumn
mteOwner = _MteOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 1),
    _MteOwner_Type()
)
mteOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteOwner.setDescription("The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator.")


class _MteTriggerName_Type(SnmpAdminString):
    """Custom type mteTriggerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteTriggerName_Type.__name__ = "SnmpAdminString"
_MteTriggerName_Object = MibTableColumn
mteTriggerName = _MteTriggerName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 2),
    _MteTriggerName_Type()
)
mteTriggerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteTriggerName.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerName.setDescription("A locally-unique, administratively assigned name for the trigger within the scope of mteOwner.")


class _MteTriggerComment_Type(SnmpAdminString):
    """Custom type mteTriggerComment based on SnmpAdminString"""
    defaultHexValue = ""


_MteTriggerComment_Type.__name__ = "SnmpAdminString"
_MteTriggerComment_Object = MibTableColumn
mteTriggerComment = _MteTriggerComment_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 3),
    _MteTriggerComment_Type()
)
mteTriggerComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerComment.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerComment.setDescription("A description of the trigger's function and use.")


class _MteTriggerTest_Type(Bits):
    """Custom type mteTriggerTest based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("existence", 0),
          ("boolean", 1),
          ("threshold", 2))
    )

_MteTriggerTest_Type.__name__ = "Bits"
_MteTriggerTest_Object = MibTableColumn
mteTriggerTest = _MteTriggerTest_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 4),
    _MteTriggerTest_Type()
)
mteTriggerTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerTest.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerTest.setDescription("The type of trigger test to perform. For 'boolean' and 'threshold' tests, the object at mteTriggerValueID MUST evaluate to an integer, that is, anything that ends up encoded for transmission (that is, in BER, not ASN.1) as an integer. For 'existence', the specific test is as selected by mteTriggerExistenceTest. When an object appears, vanishes or changes value, the trigger fires. If the object's appearance caused the trigger firing, the object MUST vanish before the trigger can be fired again for it, and vice versa. If the trigger fired due to a change in the object's value, it will be fired again on every successive value change for that object. For 'boolean', the specific test is as selected by mteTriggerBooleanTest. If the test result is true the trigger fires. The trigger will not fire again until the value has become false and come back to true. For 'threshold' the test works as described below for mteTriggerThresholdStartup, mteTriggerThresholdRising, and mteTriggerThresholdFalling. Note that combining 'boolean' and 'threshold' tests on the same object may be somewhat redundant.")


class _MteTriggerSampleType_Type(Integer32):
    """Custom type mteTriggerSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_MteTriggerSampleType_Type.__name__ = "Integer32"
_MteTriggerSampleType_Object = MibTableColumn
mteTriggerSampleType = _MteTriggerSampleType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 5),
    _MteTriggerSampleType_Type()
)
mteTriggerSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerSampleType.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerSampleType.setDescription("The type of sampling to perform. An 'absoluteValue' sample requires only a single sample to be meaningful, and is exactly the value of the object at mteTriggerValueID at the sample time. A 'deltaValue' requires two samples to be meaningful and is thus not available for testing until the second and subsequent samples after the object at mteTriggerValueID is first found to exist. It is the difference between the two samples. For unsigned values it is always positive, based on unsigned arithmetic. For signed values it can be positive or negative. For SNMP counters to be meaningful they should be sampled as a 'deltaValue'. For 'deltaValue' mteTriggerDeltaTable contains further parameters. If only 'existence' is set in mteTriggerTest this object has no meaning.")


class _MteTriggerValueID_Type(ObjectIdentifier):
    """Custom type mteTriggerValueID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteTriggerValueID_Type.__name__ = "ObjectIdentifier"
_MteTriggerValueID_Object = MibTableColumn
mteTriggerValueID = _MteTriggerValueID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 6),
    _MteTriggerValueID_Type()
)
mteTriggerValueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerValueID.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerValueID.setDescription("The object identifier of the MIB object to sample to see if the trigger should fire. This may be wildcarded by truncating all or part of the instance portion, in which case the value is obtained as if with a GetNext function, checking multiple values if they exist. If such wildcarding is applied, mteTriggerValueIDWildcard must be 'true' and if not it must be 'false'. Bad object identifiers or a mismatch between truncating the identifier and the value of mteTriggerValueIDWildcard result in operation as one would expect when providing the wrong identifier to a Get or GetNext operation. The Get will fail or get the wrong object. The GetNext will indeed get whatever is next, proceeding until it runs past the initial part of the identifier and perhaps many unintended objects for confusing results. If the value syntax of those objects is not usable, that results in a 'badType' error that terminates the scan. Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.")


class _MteTriggerValueIDWildcard_Type(TruthValue):
    """Custom type mteTriggerValueIDWildcard based on TruthValue"""
    defaultValue = 2


_MteTriggerValueIDWildcard_Type.__name__ = "TruthValue"
_MteTriggerValueIDWildcard_Object = MibTableColumn
mteTriggerValueIDWildcard = _MteTriggerValueIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 7),
    _MteTriggerValueIDWildcard_Type()
)
mteTriggerValueIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerValueIDWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerValueIDWildcard.setDescription("Control for whether mteTriggerValueID is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard.")


class _MteTriggerTargetTag_Type(SnmpTagValue):
    """Custom type mteTriggerTargetTag based on SnmpTagValue"""
    defaultHexValue = ""


_MteTriggerTargetTag_Type.__name__ = "SnmpTagValue"
_MteTriggerTargetTag_Object = MibTableColumn
mteTriggerTargetTag = _MteTriggerTargetTag_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 8),
    _MteTriggerTargetTag_Type()
)
mteTriggerTargetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerTargetTag.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerTargetTag.setDescription("The tag for the target(s) from which to obtain the condition for a trigger check. A length of 0 indicates the local system. In this case, access to the objects indicated by mteTriggerValueID is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'. Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks. Otherwise access rights are checked according to the security parameters resulting from the tag.")


class _MteTriggerContextName_Type(SnmpAdminString):
    """Custom type mteTriggerContextName based on SnmpAdminString"""
    defaultHexValue = ""


_MteTriggerContextName_Type.__name__ = "SnmpAdminString"
_MteTriggerContextName_Object = MibTableColumn
mteTriggerContextName = _MteTriggerContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 9),
    _MteTriggerContextName_Type()
)
mteTriggerContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerContextName.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerContextName.setDescription("The management context from which to obtain mteTriggerValueID. This may be wildcarded by leaving characters off the end. For example use 'Repeater' to wildcard to 'Repeater1', 'Repeater2', 'Repeater-999.87b', and so on. To indicate such wildcarding is intended, mteTriggerContextNameWildcard must be 'true'. Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time. Operation of this feature assumes that the local system has a list of available contexts against which to apply the wildcard. If the objects are being read from the local system, this is clearly the system's own list of contexts. For a remote system a local version of such a list is not defined by any current standard and may not be available, so this function MAY not be supported.")


class _MteTriggerContextNameWildcard_Type(TruthValue):
    """Custom type mteTriggerContextNameWildcard based on TruthValue"""
    defaultValue = 2


_MteTriggerContextNameWildcard_Type.__name__ = "TruthValue"
_MteTriggerContextNameWildcard_Object = MibTableColumn
mteTriggerContextNameWildcard = _MteTriggerContextNameWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 10),
    _MteTriggerContextNameWildcard_Type()
)
mteTriggerContextNameWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerContextNameWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerContextNameWildcard.setDescription("Control for whether mteTriggerContextName is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard.")


class _MteTriggerFrequency_Type(Unsigned32):
    """Custom type mteTriggerFrequency based on Unsigned32"""
    defaultValue = 600


_MteTriggerFrequency_Type.__name__ = "Unsigned32"
_MteTriggerFrequency_Object = MibTableColumn
mteTriggerFrequency = _MteTriggerFrequency_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 11),
    _MteTriggerFrequency_Type()
)
mteTriggerFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerFrequency.setUnits("seconds")
if mibBuilder.loadTexts:
    mteTriggerFrequency.setDescription("The number of seconds to wait between trigger samples. To encourage consistency in sampling, the interval is measured from the beginning of one check to the beginning of the next and the timer is restarted immediately when it expires, not when the check completes. If the next sample begins before the previous one completed the system may either attempt to make the check or treat this as an error condition with the error 'sampleOverrun'. A frequency of 0 indicates instantaneous recognition of the condition. This is not possible in many cases, but may be supported in cases where it makes sense and the system is able to do so. This feature allows the MIB to be used in implementations where such interrupt-driven behavior is possible and is not likely to be supported for all MIB objects even then since such sampling generally has to be tightly integrated into low-level code. Systems that can support this SHOULD document those cases where it can be used. In cases where it can not, setting this object to 0 should be disallowed.")


class _MteTriggerObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerObjectsOwner_Object = MibTableColumn
mteTriggerObjectsOwner = _MteTriggerObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 12),
    _MteTriggerObjectsOwner_Type()
)
mteTriggerObjectsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerObjectsOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerObjectsOwner.setDescription("To go with mteTriggerObjects, the mteOwner of a group of objects from mteObjectsTable.")


class _MteTriggerObjects_Type(SnmpAdminString):
    """Custom type mteTriggerObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerObjects_Object = MibTableColumn
mteTriggerObjects = _MteTriggerObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 13),
    _MteTriggerObjects_Type()
)
mteTriggerObjects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerObjects.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerObjects.setDescription("The mteObjectsName of a group of objects from mteObjectsTable. These objects are to be added to any Notification resulting from the firing of this trigger. A list of objects may also be added based on the event or on the value of mteTriggerTest. A length of 0 indicates no additional objects.")


class _MteTriggerEnabled_Type(TruthValue):
    """Custom type mteTriggerEnabled based on TruthValue"""
    defaultValue = 2


_MteTriggerEnabled_Type.__name__ = "TruthValue"
_MteTriggerEnabled_Object = MibTableColumn
mteTriggerEnabled = _MteTriggerEnabled_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 14),
    _MteTriggerEnabled_Type()
)
mteTriggerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEnabled.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerEnabled.setDescription("A control to allow a trigger to be configured but not used. When the value is 'false' the trigger is not sampled. Whenever the value goes from 'false' to 'true', the trigger is treated as being initialized. That is, no history is kept of any trigger sample values from previous times when this control may have been enabled. If this object is set to 'true' when its value is already 'true', the operation has no effect; that is, the trigger is not re-initialized, and there is no error.")
_MteTriggerEntryStatus_Type = RowStatus
_MteTriggerEntryStatus_Object = MibTableColumn
mteTriggerEntryStatus = _MteTriggerEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 15),
    _MteTriggerEntryStatus_Type()
)
mteTriggerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEntryStatus.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerEntryStatus.setDescription("The control that allows creation and deletion of entries. Once made active an entry may not be modified except to modify the value of mteTriggerEnabled or to delete the entry.")


class _MteTriggerEntryStorageType_Type(StorageType):
    """Custom type mteTriggerEntryStorageType based on StorageType"""
    defaultValue = 3


_MteTriggerEntryStorageType_Type.__name__ = "StorageType"
_MteTriggerEntryStorageType_Object = MibTableColumn
mteTriggerEntryStorageType = _MteTriggerEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 16),
    _MteTriggerEntryStorageType_Type()
)
mteTriggerEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEntryStorageType.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerEntryStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row, except for mteTriggerEnabled. ")
_MteTriggerDeltaTable_Object = MibTable
mteTriggerDeltaTable = _MteTriggerDeltaTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mteTriggerDeltaTable.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerDeltaTable.setDescription("A table of management event trigger information for delta sampling.")
_MteTriggerDeltaEntry_Object = MibTableRow
mteTriggerDeltaEntry = _MteTriggerDeltaEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1)
)
mteTriggerDeltaEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerDeltaEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerDeltaEntry.setDescription("Information about a single trigger's delta sampling. Entries automatically exist in this this table for each mteTriggerEntry that has mteTriggerSampleType set to 'deltaValue'.")


class _MteTriggerDeltaDiscontinuityID_Type(ObjectIdentifier):
    """Custom type mteTriggerDeltaDiscontinuityID based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 1, 3, 0)


_MteTriggerDeltaDiscontinuityID_Type.__name__ = "ObjectIdentifier"
_MteTriggerDeltaDiscontinuityID_Object = MibTableColumn
mteTriggerDeltaDiscontinuityID = _MteTriggerDeltaDiscontinuityID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 1),
    _MteTriggerDeltaDiscontinuityID_Type()
)
mteTriggerDeltaDiscontinuityID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityID.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityID.setDescription("The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at mteTriggerValueID. The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match mteTriggerValueID. This object supports normal checking for a discontinuity in a counter. Note that if this object does not point to sysUpTime discontinuity checking MUST still check sysUpTime for an overall discontinuity. If the object identified is not accessible the sample attempt is in error, with the error code as from an SNMP request. Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation. The Get will fail or get the wrong object. If the value syntax of those objects is not usable, that results in an error that terminates the sample with a 'badType' error code.")


class _MteTriggerDeltaDiscontinuityIDWildcard_Type(TruthValue):
    """Custom type mteTriggerDeltaDiscontinuityIDWildcard based on TruthValue"""
    defaultValue = 2


_MteTriggerDeltaDiscontinuityIDWildcard_Type.__name__ = "TruthValue"
_MteTriggerDeltaDiscontinuityIDWildcard_Object = MibTableColumn
mteTriggerDeltaDiscontinuityIDWildcard = _MteTriggerDeltaDiscontinuityIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 2),
    _MteTriggerDeltaDiscontinuityIDWildcard_Type()
)
mteTriggerDeltaDiscontinuityIDWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDWildcard.setDescription("Control for whether mteTriggerDeltaDiscontinuityID is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard. Note that the value of this object will be the same as that of the corresponding instance of mteTriggerValueIDWildcard when the corresponding mteTriggerSampleType is 'deltaValue'.")


class _MteTriggerDeltaDiscontinuityIDType_Type(Integer32):
    """Custom type mteTriggerDeltaDiscontinuityIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timeTicks", 1),
          ("timeStamp", 2),
          ("dateAndTime", 3))
    )


_MteTriggerDeltaDiscontinuityIDType_Type.__name__ = "Integer32"
_MteTriggerDeltaDiscontinuityIDType_Object = MibTableColumn
mteTriggerDeltaDiscontinuityIDType = _MteTriggerDeltaDiscontinuityIDType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 3),
    _MteTriggerDeltaDiscontinuityIDType_Type()
)
mteTriggerDeltaDiscontinuityIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDType.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDType.setDescription("The value 'timeTicks' indicates the mteTriggerDeltaDiscontinuityID of this row is of syntax TimeTicks. The value 'timeStamp' indicates syntax TimeStamp. The value 'dateAndTime' indicates syntax DateAndTime.")
_MteTriggerExistenceTable_Object = MibTable
mteTriggerExistenceTable = _MteTriggerExistenceTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mteTriggerExistenceTable.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceTable.setDescription("A table of management event trigger information for existence triggers.")
_MteTriggerExistenceEntry_Object = MibTableRow
mteTriggerExistenceEntry = _MteTriggerExistenceEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1)
)
mteTriggerExistenceEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerExistenceEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceEntry.setDescription("Information about a single existence trigger. Entries automatically exist in this this table for each mteTriggerEntry that has 'existence' set in mteTriggerTest.")


class _MteTriggerExistenceTest_Type(Bits):
    """Custom type mteTriggerExistenceTest based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("present", 0),
          ("absent", 1),
          ("changed", 2))
    )

_MteTriggerExistenceTest_Type.__name__ = "Bits"
_MteTriggerExistenceTest_Object = MibTableColumn
mteTriggerExistenceTest = _MteTriggerExistenceTest_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 1),
    _MteTriggerExistenceTest_Type()
)
mteTriggerExistenceTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceTest.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceTest.setDescription("The type of existence test to perform. The trigger fires when the object at mteTriggerValueID is seen to go from present to absent, from absent to present, or to have it's value changed, depending on which tests are selected: present(0) - when this test is selected, the trigger fires when the mteTriggerValueID object goes from absent to present. absent(1) - when this test is selected, the trigger fires when the mteTriggerValueID object goes from present to absent. changed(2) - when this test is selected, the trigger fires the mteTriggerValueID object value changes. Once the trigger has fired for either presence or absence it will not fire again for that state until the object has been to the other state. ")


class _MteTriggerExistenceStartup_Type(Bits):
    """Custom type mteTriggerExistenceStartup based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("present", 0),
          ("absent", 1))
    )

_MteTriggerExistenceStartup_Type.__name__ = "Bits"
_MteTriggerExistenceStartup_Object = MibTableColumn
mteTriggerExistenceStartup = _MteTriggerExistenceStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 2),
    _MteTriggerExistenceStartup_Type()
)
mteTriggerExistenceStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceStartup.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceStartup.setDescription("Control for whether an event may be triggered when this entry is first set to 'active' and the test specified by mteTriggerExistenceTest is true. Setting an option causes that trigger to fire when its test is true.")


class _MteTriggerExistenceObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceObjectsOwner_Object = MibTableColumn
mteTriggerExistenceObjectsOwner = _MteTriggerExistenceObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 3),
    _MteTriggerExistenceObjectsOwner_Type()
)
mteTriggerExistenceObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjectsOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjectsOwner.setDescription("To go with mteTriggerExistenceObjects, the mteOwner of a group of objects from mteObjectsTable.")


class _MteTriggerExistenceObjects_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceObjects_Object = MibTableColumn
mteTriggerExistenceObjects = _MteTriggerExistenceObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 4),
    _MteTriggerExistenceObjects_Type()
)
mteTriggerExistenceObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjects.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjects.setDescription("The mteObjectsName of a group of objects from mteObjectsTable. These objects are to be added to any Notification resulting from the firing of this trigger for this test. A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest. A length of 0 indicates no additional objects.")


class _MteTriggerExistenceEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceEventOwner_Object = MibTableColumn
mteTriggerExistenceEventOwner = _MteTriggerExistenceEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 5),
    _MteTriggerExistenceEventOwner_Type()
)
mteTriggerExistenceEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceEventOwner.setDescription("To go with mteTriggerExistenceEvent, the mteOwner of an event entry from the mteEventTable.")


class _MteTriggerExistenceEvent_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceEvent_Object = MibTableColumn
mteTriggerExistenceEvent = _MteTriggerExistenceEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 6),
    _MteTriggerExistenceEvent_Type()
)
mteTriggerExistenceEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerExistenceEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'existence' and this trigger fires. A length of 0 indicates no event.")
_MteTriggerBooleanTable_Object = MibTable
mteTriggerBooleanTable = _MteTriggerBooleanTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mteTriggerBooleanTable.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanTable.setDescription("A table of management event trigger information for boolean triggers.")
_MteTriggerBooleanEntry_Object = MibTableRow
mteTriggerBooleanEntry = _MteTriggerBooleanEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1)
)
mteTriggerBooleanEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerBooleanEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanEntry.setDescription("Information about a single boolean trigger. Entries automatically exist in this this table for each mteTriggerEntry that has 'boolean' set in mteTriggerTest.")


class _MteTriggerBooleanComparison_Type(Integer32):
    """Custom type mteTriggerBooleanComparison based on Integer32"""
    defaultValue = 1

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
        *(("unequal", 1),
          ("equal", 2),
          ("less", 3),
          ("lessOrEqual", 4),
          ("greater", 5),
          ("greaterOrEqual", 6))
    )


_MteTriggerBooleanComparison_Type.__name__ = "Integer32"
_MteTriggerBooleanComparison_Object = MibTableColumn
mteTriggerBooleanComparison = _MteTriggerBooleanComparison_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 1),
    _MteTriggerBooleanComparison_Type()
)
mteTriggerBooleanComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanComparison.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanComparison.setDescription("The type of boolean comparison to perform. The value at mteTriggerValueID is compared to mteTriggerBooleanValue, so for example if mteTriggerBooleanComparison is 'less' the result would be true if the value at mteTriggerValueID is less than the value of mteTriggerBooleanValue.")


class _MteTriggerBooleanValue_Type(Integer32):
    """Custom type mteTriggerBooleanValue based on Integer32"""
    defaultValue = 0


_MteTriggerBooleanValue_Type.__name__ = "Integer32"
_MteTriggerBooleanValue_Object = MibTableColumn
mteTriggerBooleanValue = _MteTriggerBooleanValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 2),
    _MteTriggerBooleanValue_Type()
)
mteTriggerBooleanValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanValue.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanValue.setDescription("The value to use for the test specified by mteTriggerBooleanTest.")


class _MteTriggerBooleanStartup_Type(TruthValue):
    """Custom type mteTriggerBooleanStartup based on TruthValue"""
    defaultValue = 1


_MteTriggerBooleanStartup_Type.__name__ = "TruthValue"
_MteTriggerBooleanStartup_Object = MibTableColumn
mteTriggerBooleanStartup = _MteTriggerBooleanStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 3),
    _MteTriggerBooleanStartup_Type()
)
mteTriggerBooleanStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanStartup.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanStartup.setDescription("Control for whether an event may be triggered when this entry is first set to 'active' or a new instance of the object at mteTriggerValueID is found and the test specified by mteTriggerBooleanComparison is true. In that case an event is triggered if mteTriggerBooleanStartup is 'true'.")


class _MteTriggerBooleanObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanObjectsOwner_Object = MibTableColumn
mteTriggerBooleanObjectsOwner = _MteTriggerBooleanObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 4),
    _MteTriggerBooleanObjectsOwner_Type()
)
mteTriggerBooleanObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjectsOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjectsOwner.setDescription("To go with mteTriggerBooleanObjects, the mteOwner of a group of objects from mteObjectsTable.")


class _MteTriggerBooleanObjects_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanObjects_Object = MibTableColumn
mteTriggerBooleanObjects = _MteTriggerBooleanObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 5),
    _MteTriggerBooleanObjects_Type()
)
mteTriggerBooleanObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjects.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjects.setDescription("The mteObjectsName of a group of objects from mteObjectsTable. These objects are to be added to any Notification resulting from the firing of this trigger for this test. A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest. A length of 0 indicates no additional objects.")


class _MteTriggerBooleanEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanEventOwner_Object = MibTableColumn
mteTriggerBooleanEventOwner = _MteTriggerBooleanEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 6),
    _MteTriggerBooleanEventOwner_Type()
)
mteTriggerBooleanEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanEventOwner.setDescription("To go with mteTriggerBooleanEvent, the mteOwner of an event entry from mteEventTable.")


class _MteTriggerBooleanEvent_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanEvent_Object = MibTableColumn
mteTriggerBooleanEvent = _MteTriggerBooleanEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 7),
    _MteTriggerBooleanEvent_Type()
)
mteTriggerBooleanEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerBooleanEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'boolean' and this trigger fires. A length of 0 indicates no event.")
_MteTriggerThresholdTable_Object = MibTable
mteTriggerThresholdTable = _MteTriggerThresholdTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mteTriggerThresholdTable.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdTable.setDescription("A table of management event trigger information for threshold triggers.")
_MteTriggerThresholdEntry_Object = MibTableRow
mteTriggerThresholdEntry = _MteTriggerThresholdEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1)
)
mteTriggerThresholdEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerThresholdEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdEntry.setDescription("Information about a single threshold trigger. Entries automatically exist in this table for each mteTriggerEntry that has 'threshold' set in mteTriggerTest.")


class _MteTriggerThresholdStartup_Type(Integer32):
    """Custom type mteTriggerThresholdStartup based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rising", 1),
          ("falling", 2),
          ("risingOrFalling", 3))
    )


_MteTriggerThresholdStartup_Type.__name__ = "Integer32"
_MteTriggerThresholdStartup_Object = MibTableColumn
mteTriggerThresholdStartup = _MteTriggerThresholdStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 1),
    _MteTriggerThresholdStartup_Type()
)
mteTriggerThresholdStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdStartup.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdStartup.setDescription("The event that may be triggered when this entry is first set to 'active' and a new instance of the object at mteTriggerValueID is found. If the first sample after this instance becomes active is greater than or equal to mteTriggerThresholdRising and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance. If the first sample after this entry becomes active is less than or equal to mteTriggerThresholdFalling and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling', then one mteTriggerThresholdRisingEvent is triggered for that instance.")


class _MteTriggerThresholdRising_Type(Integer32):
    """Custom type mteTriggerThresholdRising based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdRising_Type.__name__ = "Integer32"
_MteTriggerThresholdRising_Object = MibTableColumn
mteTriggerThresholdRising = _MteTriggerThresholdRising_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 2),
    _MteTriggerThresholdRising_Type()
)
mteTriggerThresholdRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRising.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdRising.setDescription("A threshold value to check against if mteTriggerType is 'threshold'. When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, one mteTriggerThresholdRisingEvent is triggered. That event is also triggered if the first sample after this entry becomes active is greater than or equal to this threshold and mteTriggerThresholdStartup is equal to 'rising' or 'risingOrFalling'. After a rising event is generated, another such event is not triggered until the sampled value falls below this threshold and reaches mteTriggerThresholdFalling.")


class _MteTriggerThresholdFalling_Type(Integer32):
    """Custom type mteTriggerThresholdFalling based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdFalling_Type.__name__ = "Integer32"
_MteTriggerThresholdFalling_Object = MibTableColumn
mteTriggerThresholdFalling = _MteTriggerThresholdFalling_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 3),
    _MteTriggerThresholdFalling_Type()
)
mteTriggerThresholdFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFalling.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdFalling.setDescription("A threshold value to check against if mteTriggerType is 'threshold'. When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, one mteTriggerThresholdFallingEvent is triggered. That event is also triggered if the first sample after this entry becomes active is less than or equal to this threshold and mteTriggerThresholdStartup is equal to 'falling' or 'risingOrFalling'. After a falling event is generated, another such event is not triggered until the sampled value rises above this threshold and reaches mteTriggerThresholdRising.")


class _MteTriggerThresholdDeltaRising_Type(Integer32):
    """Custom type mteTriggerThresholdDeltaRising based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdDeltaRising_Type.__name__ = "Integer32"
_MteTriggerThresholdDeltaRising_Object = MibTableColumn
mteTriggerThresholdDeltaRising = _MteTriggerThresholdDeltaRising_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 4),
    _MteTriggerThresholdDeltaRising_Type()
)
mteTriggerThresholdDeltaRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRising.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRising.setDescription("A threshold value to check against if mteTriggerType is 'threshold'. When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n-1)) is greater than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n-1) - value(n-2)) was less than this threshold, one mteTriggerThresholdDeltaRisingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) - value(1), where value(1) is the first sample taken of that instance, is greater than or equal to this threshold. After a rising event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaFalling.")


class _MteTriggerThresholdDeltaFalling_Type(Integer32):
    """Custom type mteTriggerThresholdDeltaFalling based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdDeltaFalling_Type.__name__ = "Integer32"
_MteTriggerThresholdDeltaFalling_Object = MibTableColumn
mteTriggerThresholdDeltaFalling = _MteTriggerThresholdDeltaFalling_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 5),
    _MteTriggerThresholdDeltaFalling_Type()
)
mteTriggerThresholdDeltaFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFalling.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFalling.setDescription("A threshold value to check against if mteTriggerType is 'threshold'. When the delta value (difference) between the current sampled value (value(n)) and the previous sampled value (value(n-1)) is less than or equal to this threshold, and the delta value calculated at the last sampling interval (i.e. value(n-1) - value(n-2)) was greater than this threshold, one mteTriggerThresholdDeltaFallingEvent is triggered. That event is also triggered if the first delta value calculated after this entry becomes active, i.e. value(2) - value(1), where value(1) is the first sample taken of that instance, is less than or equal to this threshold. After a falling event is generated, another such event is not triggered until the delta value falls below this threshold and reaches mteTriggerThresholdDeltaRising.")


class _MteTriggerThresholdObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdObjectsOwner_Object = MibTableColumn
mteTriggerThresholdObjectsOwner = _MteTriggerThresholdObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 6),
    _MteTriggerThresholdObjectsOwner_Type()
)
mteTriggerThresholdObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjectsOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjectsOwner.setDescription("To go with mteTriggerThresholdObjects, the mteOwner of a group of objects from mteObjectsTable.")


class _MteTriggerThresholdObjects_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdObjects_Object = MibTableColumn
mteTriggerThresholdObjects = _MteTriggerThresholdObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 7),
    _MteTriggerThresholdObjects_Type()
)
mteTriggerThresholdObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjects.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjects.setDescription("The mteObjectsName of a group of objects from mteObjectsTable. These objects are to be added to any Notification resulting from the firing of this trigger for this test. A list of objects may also be added based on the overall trigger, the event or other settings in mteTriggerTest. A length of 0 indicates no additional objects.")


class _MteTriggerThresholdRisingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdRisingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdRisingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdRisingEventOwner_Object = MibTableColumn
mteTriggerThresholdRisingEventOwner = _MteTriggerThresholdRisingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 8),
    _MteTriggerThresholdRisingEventOwner_Type()
)
mteTriggerThresholdRisingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEventOwner.setDescription("To go with mteTriggerThresholdRisingEvent, the mteOwner of an event entry from mteEventTable.")


class _MteTriggerThresholdRisingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdRisingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdRisingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdRisingEvent_Object = MibTableColumn
mteTriggerThresholdRisingEvent = _MteTriggerThresholdRisingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 9),
    _MteTriggerThresholdRisingEvent_Type()
)
mteTriggerThresholdRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdRising. A length of 0 indicates no event.")


class _MteTriggerThresholdFallingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdFallingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdFallingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdFallingEventOwner_Object = MibTableColumn
mteTriggerThresholdFallingEventOwner = _MteTriggerThresholdFallingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 10),
    _MteTriggerThresholdFallingEventOwner_Type()
)
mteTriggerThresholdFallingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEventOwner.setDescription("To go with mteTriggerThresholdFallingEvent, the mteOwner of an event entry from mteEventTable.")


class _MteTriggerThresholdFallingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdFallingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdFallingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdFallingEvent_Object = MibTableColumn
mteTriggerThresholdFallingEvent = _MteTriggerThresholdFallingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 11),
    _MteTriggerThresholdFallingEvent_Type()
)
mteTriggerThresholdFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdFalling. A length of 0 indicates no event.")


class _MteTriggerThresholdDeltaRisingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaRisingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaRisingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaRisingEventOwner_Object = MibTableColumn
mteTriggerThresholdDeltaRisingEventOwner = _MteTriggerThresholdDeltaRisingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 12),
    _MteTriggerThresholdDeltaRisingEventOwner_Type()
)
mteTriggerThresholdDeltaRisingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEventOwner.setDescription("To go with mteTriggerThresholdDeltaRisingEvent, the mteOwner of an event entry from mteEventTable.")


class _MteTriggerThresholdDeltaRisingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaRisingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaRisingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaRisingEvent_Object = MibTableColumn
mteTriggerThresholdDeltaRisingEvent = _MteTriggerThresholdDeltaRisingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 13),
    _MteTriggerThresholdDeltaRisingEvent_Type()
)
mteTriggerThresholdDeltaRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaRising. A length of 0 indicates no event.")


class _MteTriggerThresholdDeltaFallingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaFallingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaFallingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaFallingEventOwner_Object = MibTableColumn
mteTriggerThresholdDeltaFallingEventOwner = _MteTriggerThresholdDeltaFallingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 14),
    _MteTriggerThresholdDeltaFallingEventOwner_Type()
)
mteTriggerThresholdDeltaFallingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEventOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEventOwner.setDescription("To go with mteTriggerThresholdDeltaFallingEvent, the mteOwner of an event entry from mteEventTable.")


class _MteTriggerThresholdDeltaFallingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaFallingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaFallingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaFallingEvent_Object = MibTableColumn
mteTriggerThresholdDeltaFallingEvent = _MteTriggerThresholdDeltaFallingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 15),
    _MteTriggerThresholdDeltaFallingEvent_Type()
)
mteTriggerThresholdDeltaFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEvent.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEvent.setDescription("The mteEventName of the event to invoke when mteTriggerType is 'threshold' and this trigger fires based on mteTriggerThresholdDeltaFalling. A length of 0 indicates no event.")
_MteObjects_ObjectIdentity = ObjectIdentity
mteObjects = _MteObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 3)
)
_MteObjectsTable_Object = MibTable
mteObjectsTable = _MteObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mteObjectsTable.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsTable.setDescription("A table of objects that can be added to notifications based on the trigger, trigger test, or event, as pointed to by entries in those tables.")
_MteObjectsEntry_Object = MibTableRow
mteObjectsEntry = _MteObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1)
)
mteObjectsEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (0, "DISMAN-EVENT-MIB", "mteObjectsName"),
    (0, "DISMAN-EVENT-MIB", "mteObjectsIndex"),
)
if mibBuilder.loadTexts:
    mteObjectsEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsEntry.setDescription("A group of objects. Applications create and delete entries using mteObjectsEntryStatus. When adding objects to a notification they are added in the lexical order of their index in this table. Those associated with a trigger come first, then trigger test, then event.")


class _MteObjectsName_Type(SnmpAdminString):
    """Custom type mteObjectsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteObjectsName_Type.__name__ = "SnmpAdminString"
_MteObjectsName_Object = MibTableColumn
mteObjectsName = _MteObjectsName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 1),
    _MteObjectsName_Type()
)
mteObjectsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteObjectsName.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsName.setDescription("A locally-unique, administratively assigned name for a group of objects.")


class _MteObjectsIndex_Type(Unsigned32):
    """Custom type mteObjectsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MteObjectsIndex_Type.__name__ = "Unsigned32"
_MteObjectsIndex_Object = MibTableColumn
mteObjectsIndex = _MteObjectsIndex_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 2),
    _MteObjectsIndex_Type()
)
mteObjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteObjectsIndex.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsIndex.setDescription("An arbitrary integer for the purpose of identifying individual objects within a mteObjectsName group. Objects within a group are placed in the notification in the numerical order of this index. Groups are placed in the notification in the order of the selections for overall trigger, trigger test, and event. Within trigger test they are in the same order as the numerical values of the bits defined for mteTriggerTest. Bad object identifiers or a mismatch between truncating the identifier and the value of mteDeltaDiscontinuityIDWildcard result in operation as one would expect when providing the wrong identifier to a Get operation. The Get will fail or get the wrong object. If the object is not available it is omitted from the notification.")


class _MteObjectsID_Type(ObjectIdentifier):
    """Custom type mteObjectsID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteObjectsID_Type.__name__ = "ObjectIdentifier"
_MteObjectsID_Object = MibTableColumn
mteObjectsID = _MteObjectsID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 3),
    _MteObjectsID_Type()
)
mteObjectsID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsID.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsID.setDescription("The object identifier of a MIB object to add to a Notification that results from the firing of a trigger. This may be wildcarded by truncating all or part of the instance portion, in which case the instance portion of the OID for obtaining this object will be the same as that used in obtaining the mteTriggerValueID that fired. If such wildcarding is applied, mteObjectsIDWildcard must be 'true' and if not it must be 'false'. Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time.")


class _MteObjectsIDWildcard_Type(TruthValue):
    """Custom type mteObjectsIDWildcard based on TruthValue"""
    defaultValue = 2


_MteObjectsIDWildcard_Type.__name__ = "TruthValue"
_MteObjectsIDWildcard_Object = MibTableColumn
mteObjectsIDWildcard = _MteObjectsIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 4),
    _MteObjectsIDWildcard_Type()
)
mteObjectsIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsIDWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsIDWildcard.setDescription("Control for whether mteObjectsID is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard.")
_MteObjectsEntryStatus_Type = RowStatus
_MteObjectsEntryStatus_Object = MibTableColumn
mteObjectsEntryStatus = _MteObjectsEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 5),
    _MteObjectsEntryStatus_Type()
)
mteObjectsEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsEntryStatus.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsEntryStatus.setDescription("The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to delete it.")


class _MteObjectsEntryStorageType_Type(StorageType):
    """Custom type mteObjectsEntryStorageType based on StorageType"""
    defaultValue = 3


_MteObjectsEntryStorageType_Type.__name__ = "StorageType"
_MteObjectsEntryStorageType_Object = MibTableColumn
mteObjectsEntryStorageType = _MteObjectsEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 6),
    _MteObjectsEntryStorageType_Type()
)
mteObjectsEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsEntryStorageType.setStatus("current")
if mibBuilder.loadTexts:
    mteObjectsEntryStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
_MteEvent_ObjectIdentity = ObjectIdentity
mteEvent = _MteEvent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 4)
)
_MteEventFailures_Type = Counter32
_MteEventFailures_Object = MibScalar
mteEventFailures = _MteEventFailures_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 1),
    _MteEventFailures_Type()
)
mteEventFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteEventFailures.setStatus("current")
if mibBuilder.loadTexts:
    mteEventFailures.setDescription("The number of times an attempt to invoke an event has failed. This counts individually for each attempt in a group of targets or each attempt for a wildcarded trigger object.")
_MteEventTable_Object = MibTable
mteEventTable = _MteEventTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mteEventTable.setStatus("current")
if mibBuilder.loadTexts:
    mteEventTable.setDescription("A table of management event action information.")
_MteEventEntry_Object = MibTableRow
mteEventEntry = _MteEventEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1)
)
mteEventEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteEventEntry.setDescription("Information about a single event. Applications create and delete entries using mteEventEntryStatus.")


class _MteEventName_Type(SnmpAdminString):
    """Custom type mteEventName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteEventName_Type.__name__ = "SnmpAdminString"
_MteEventName_Object = MibTableColumn
mteEventName = _MteEventName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 1),
    _MteEventName_Type()
)
mteEventName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteEventName.setStatus("current")
if mibBuilder.loadTexts:
    mteEventName.setDescription("A locally-unique, administratively assigned name for the event.")


class _MteEventComment_Type(SnmpAdminString):
    """Custom type mteEventComment based on SnmpAdminString"""
    defaultHexValue = ""


_MteEventComment_Type.__name__ = "SnmpAdminString"
_MteEventComment_Object = MibTableColumn
mteEventComment = _MteEventComment_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 2),
    _MteEventComment_Type()
)
mteEventComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventComment.setStatus("current")
if mibBuilder.loadTexts:
    mteEventComment.setDescription("A description of the event's function and use.")


class _MteEventActions_Type(Bits):
    """Custom type mteEventActions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("notification", 0),
          ("set", 1))
    )

_MteEventActions_Type.__name__ = "Bits"
_MteEventActions_Object = MibTableColumn
mteEventActions = _MteEventActions_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 3),
    _MteEventActions_Type()
)
mteEventActions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventActions.setStatus("current")
if mibBuilder.loadTexts:
    mteEventActions.setDescription("The actions to perform when this event occurs. For 'notification', Traps and/or Informs are sent according to the configuration in the SNMP Notification MIB. For 'set', an SNMP Set operation is performed according to control values in this entry.")


class _MteEventEnabled_Type(TruthValue):
    """Custom type mteEventEnabled based on TruthValue"""
    defaultValue = 2


_MteEventEnabled_Type.__name__ = "TruthValue"
_MteEventEnabled_Object = MibTableColumn
mteEventEnabled = _MteEventEnabled_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 4),
    _MteEventEnabled_Type()
)
mteEventEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEnabled.setStatus("current")
if mibBuilder.loadTexts:
    mteEventEnabled.setDescription("A control to allow an event to be configured but not used. When the value is 'false' the event does not execute even if triggered.")
_MteEventEntryStatus_Type = RowStatus
_MteEventEntryStatus_Object = MibTableColumn
mteEventEntryStatus = _MteEventEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 5),
    _MteEventEntryStatus_Type()
)
mteEventEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEntryStatus.setStatus("current")
if mibBuilder.loadTexts:
    mteEventEntryStatus.setDescription("The control that allows creation and deletion of entries. Once made active an entry MAY not be modified except to modify the value of mteEventEnabled or to delete the entry.")


class _MteEventEntryStorageType_Type(StorageType):
    """Custom type mteEventEntryStorageType based on StorageType"""
    defaultValue = 3


_MteEventEntryStorageType_Type.__name__ = "StorageType"
_MteEventEntryStorageType_Object = MibTableColumn
mteEventEntryStorageType = _MteEventEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 6),
    _MteEventEntryStorageType_Type()
)
mteEventEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEntryStorageType.setStatus("current")
if mibBuilder.loadTexts:
    mteEventEntryStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
_MteEventNotificationTable_Object = MibTable
mteEventNotificationTable = _MteEventNotificationTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mteEventNotificationTable.setStatus("current")
if mibBuilder.loadTexts:
    mteEventNotificationTable.setDescription("A table of information about notifications to be sent as a consequence of management events.")
_MteEventNotificationEntry_Object = MibTableRow
mteEventNotificationEntry = _MteEventNotificationEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1)
)
mteEventNotificationEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventNotificationEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteEventNotificationEntry.setDescription("Information about a single event's notification. Entries automatically exist in this this table for each mteEventEntry that has 'notification' set in mteEventActions.")


class _MteEventNotification_Type(ObjectIdentifier):
    """Custom type mteEventNotification based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteEventNotification_Type.__name__ = "ObjectIdentifier"
_MteEventNotification_Object = MibTableColumn
mteEventNotification = _MteEventNotification_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 1),
    _MteEventNotification_Type()
)
mteEventNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotification.setStatus("current")
if mibBuilder.loadTexts:
    mteEventNotification.setDescription("The object identifier from the NOTIFICATION-TYPE for the notification to use if mteEventActions has 'notification' set.")


class _MteEventNotificationObjectsOwner_Type(SnmpAdminString):
    """Custom type mteEventNotificationObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteEventNotificationObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteEventNotificationObjectsOwner_Object = MibTableColumn
mteEventNotificationObjectsOwner = _MteEventNotificationObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 2),
    _MteEventNotificationObjectsOwner_Type()
)
mteEventNotificationObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotificationObjectsOwner.setStatus("current")
if mibBuilder.loadTexts:
    mteEventNotificationObjectsOwner.setDescription("To go with mteEventNotificationObjects, the mteOwner of a group of objects from mteObjectsTable.")


class _MteEventNotificationObjects_Type(SnmpAdminString):
    """Custom type mteEventNotificationObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteEventNotificationObjects_Type.__name__ = "SnmpAdminString"
_MteEventNotificationObjects_Object = MibTableColumn
mteEventNotificationObjects = _MteEventNotificationObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 3),
    _MteEventNotificationObjects_Type()
)
mteEventNotificationObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotificationObjects.setStatus("current")
if mibBuilder.loadTexts:
    mteEventNotificationObjects.setDescription("The mteObjectsName of a group of objects from mteObjectsTable if mteEventActions has 'notification' set. These objects are to be added to any Notification generated by this event. Objects may also be added based on the trigger that stimulated the event. A length of 0 indicates no additional objects.")
_MteEventSetTable_Object = MibTable
mteEventSetTable = _MteEventSetTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4)
)
if mibBuilder.loadTexts:
    mteEventSetTable.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetTable.setDescription("A table of management event action information.")
_MteEventSetEntry_Object = MibTableRow
mteEventSetEntry = _MteEventSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1)
)
mteEventSetEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventSetEntry.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetEntry.setDescription("Information about a single event's set option. Entries automatically exist in this this table for each mteEventEntry that has 'set' set in mteEventActions.")


class _MteEventSetObject_Type(ObjectIdentifier):
    """Custom type mteEventSetObject based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteEventSetObject_Type.__name__ = "ObjectIdentifier"
_MteEventSetObject_Object = MibTableColumn
mteEventSetObject = _MteEventSetObject_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 1),
    _MteEventSetObject_Type()
)
mteEventSetObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetObject.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetObject.setDescription("The object identifier from the MIB object to set if mteEventActions has 'set' set. This object identifier may be wildcarded by leaving sub-identifiers off the end, in which case nteEventSetObjectWildCard must be 'true'. If mteEventSetObject is wildcarded the instance used to set the object to which it points is the same as the instance from the value of mteTriggerValueID that triggered the event. Each instance that fills the wildcard is independent of any additional instances, that is, wildcarded objects operate as if there were a separate table entry for each instance that fills the wildcard without having to actually predict all possible instances ahead of time. Bad object identifiers or a mismatch between truncating the identifier and the value of mteSetObjectWildcard result in operation as one would expect when providing the wrong identifier to a Set operation. The Set will fail or set the wrong object. If the value syntax of the destination object is not correct, the Set fails with the normal SNMP error code.")


class _MteEventSetObjectWildcard_Type(TruthValue):
    """Custom type mteEventSetObjectWildcard based on TruthValue"""
    defaultValue = 2


_MteEventSetObjectWildcard_Type.__name__ = "TruthValue"
_MteEventSetObjectWildcard_Object = MibTableColumn
mteEventSetObjectWildcard = _MteEventSetObjectWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 2),
    _MteEventSetObjectWildcard_Type()
)
mteEventSetObjectWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetObjectWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetObjectWildcard.setDescription("Control over whether mteEventSetObject is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set.")


class _MteEventSetValue_Type(Integer32):
    """Custom type mteEventSetValue based on Integer32"""
    defaultValue = 0


_MteEventSetValue_Type.__name__ = "Integer32"
_MteEventSetValue_Object = MibTableColumn
mteEventSetValue = _MteEventSetValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 3),
    _MteEventSetValue_Type()
)
mteEventSetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetValue.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetValue.setDescription("The value to which to set the object at mteEventSetObject if mteEventActions has 'set' set.")


class _MteEventSetTargetTag_Type(SnmpTagValue):
    """Custom type mteEventSetTargetTag based on SnmpTagValue"""
    defaultHexValue = ""


_MteEventSetTargetTag_Type.__name__ = "SnmpTagValue"
_MteEventSetTargetTag_Object = MibTableColumn
mteEventSetTargetTag = _MteEventSetTargetTag_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 4),
    _MteEventSetTargetTag_Type()
)
mteEventSetTargetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetTargetTag.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetTargetTag.setDescription("The tag for the target(s) at which to set the object at mteEventSetObject to mteEventSetValue if mteEventActions has 'set' set. Systems limited to self management MAY reject a non-zero length for the value of this object. A length of 0 indicates the local system. In this case, access to the objects indicated by mteEventSetObject is under the security credentials of the requester that set mteTriggerEntryStatus to 'active'. Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks. Otherwise access rights are checked according to the security parameters resulting from the tag.")


class _MteEventSetContextName_Type(SnmpAdminString):
    """Custom type mteEventSetContextName based on SnmpAdminString"""
    defaultHexValue = ""


_MteEventSetContextName_Type.__name__ = "SnmpAdminString"
_MteEventSetContextName_Object = MibTableColumn
mteEventSetContextName = _MteEventSetContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 5),
    _MteEventSetContextName_Type()
)
mteEventSetContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetContextName.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetContextName.setDescription("The management context in which to set mteEventObjectID. if mteEventActions has 'set' set. This may be wildcarded by leaving characters off the end. To indicate such wildcarding mteEventSetContextNameWildcard must be 'true'. If this context name is wildcarded the value used to complete the wildcarding of mteTriggerContextName will be appended.")


class _MteEventSetContextNameWildcard_Type(TruthValue):
    """Custom type mteEventSetContextNameWildcard based on TruthValue"""
    defaultValue = 2


_MteEventSetContextNameWildcard_Type.__name__ = "TruthValue"
_MteEventSetContextNameWildcard_Object = MibTableColumn
mteEventSetContextNameWildcard = _MteEventSetContextNameWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 6),
    _MteEventSetContextNameWildcard_Type()
)
mteEventSetContextNameWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetContextNameWildcard.setStatus("current")
if mibBuilder.loadTexts:
    mteEventSetContextNameWildcard.setDescription("Control for whether mteEventSetContextName is to be treated as fully-specified or wildcarded, with 'true' indicating wildcard if mteEventActions has 'set' set.")
_DismanEventMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
dismanEventMIBNotificationPrefix = _DismanEventMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2)
)
_DismanEventMIBNotifications_ObjectIdentity = ObjectIdentity
dismanEventMIBNotifications = _DismanEventMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2, 0)
)
_DismanEventMIBNotificationObjects_ObjectIdentity = ObjectIdentity
dismanEventMIBNotificationObjects = _DismanEventMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2, 1)
)
_MteHotTrigger_Type = SnmpAdminString
_MteHotTrigger_Object = MibScalar
mteHotTrigger = _MteHotTrigger_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 1),
    _MteHotTrigger_Type()
)
mteHotTrigger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotTrigger.setStatus("current")
if mibBuilder.loadTexts:
    mteHotTrigger.setDescription("The name of the trigger causing the notification.")
_MteHotTargetName_Type = SnmpAdminString
_MteHotTargetName_Object = MibScalar
mteHotTargetName = _MteHotTargetName_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 2),
    _MteHotTargetName_Type()
)
mteHotTargetName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotTargetName.setStatus("current")
if mibBuilder.loadTexts:
    mteHotTargetName.setDescription("The SNMP Target MIB's snmpTargetAddrName related to the notification.")
_MteHotContextName_Type = SnmpAdminString
_MteHotContextName_Object = MibScalar
mteHotContextName = _MteHotContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 3),
    _MteHotContextName_Type()
)
mteHotContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotContextName.setStatus("current")
if mibBuilder.loadTexts:
    mteHotContextName.setDescription("The context name related to the notification. This MUST be as fully-qualified as possible, including filling in wildcard information determined in processing.")
_MteHotOID_Type = ObjectIdentifier
_MteHotOID_Object = MibScalar
mteHotOID = _MteHotOID_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 4),
    _MteHotOID_Type()
)
mteHotOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotOID.setStatus("current")
if mibBuilder.loadTexts:
    mteHotOID.setDescription("The object identifier of the destination object related to the notification. This MUST be as fully-qualified as possible, including filling in wildcard information determined in processing. For a trigger-related notification this is from mteTriggerValueID. For a set failure this is from mteEventSetObject.")
_MteHotValue_Type = Integer32
_MteHotValue_Object = MibScalar
mteHotValue = _MteHotValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 5),
    _MteHotValue_Type()
)
mteHotValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotValue.setStatus("current")
if mibBuilder.loadTexts:
    mteHotValue.setDescription("The value of the object at mteTriggerValueID when a trigger fired.")
_MteFailedReason_Type = FailureReason
_MteFailedReason_Object = MibScalar
mteFailedReason = _MteFailedReason_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 6),
    _MteFailedReason_Type()
)
mteFailedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteFailedReason.setStatus("current")
if mibBuilder.loadTexts:
    mteFailedReason.setDescription("The reason for the failure of an attempt to check for a trigger condition or set an object in response to an event.")
_DismanEventMIBConformance_ObjectIdentity = ObjectIdentity
dismanEventMIBConformance = _DismanEventMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3)
)
_DismanEventMIBCompliances_ObjectIdentity = ObjectIdentity
dismanEventMIBCompliances = _DismanEventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3, 1)
)
_DismanEventMIBGroups_ObjectIdentity = ObjectIdentity
dismanEventMIBGroups = _DismanEventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3, 2)
)

# Managed Objects groups

dismanEventResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 1)
)
dismanEventResourceGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteResourceSampleMinimum"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceMaximum"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstances"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstancesHigh"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceLacks"))
)
if mibBuilder.loadTexts:
    dismanEventResourceGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanEventResourceGroup.setDescription("Event resource status and control objects.")

dismanEventTriggerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 2)
)
dismanEventTriggerGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteTriggerFailures"),
        ("DISMAN-EVENT-MIB", "mteTriggerComment"),
        ("DISMAN-EVENT-MIB", "mteTriggerTest"),
        ("DISMAN-EVENT-MIB", "mteTriggerSampleType"),
        ("DISMAN-EVENT-MIB", "mteTriggerValueID"),
        ("DISMAN-EVENT-MIB", "mteTriggerValueIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerTargetTag"),
        ("DISMAN-EVENT-MIB", "mteTriggerContextName"),
        ("DISMAN-EVENT-MIB", "mteTriggerContextNameWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerFrequency"),
        ("DISMAN-EVENT-MIB", "mteTriggerObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerEnabled"),
        ("DISMAN-EVENT-MIB", "mteTriggerEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteTriggerEntryStorageType"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityID"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDType"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceTest"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanComparison"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanValue"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEvent"))
)
if mibBuilder.loadTexts:
    dismanEventTriggerGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanEventTriggerGroup.setDescription("Event triggers.")

dismanEventObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 3)
)
dismanEventObjectsGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteObjectsID"),
        ("DISMAN-EVENT-MIB", "mteObjectsIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteObjectsEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteObjectsEntryStorageType"))
)
if mibBuilder.loadTexts:
    dismanEventObjectsGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanEventObjectsGroup.setDescription("Supplemental objects.")

dismanEventEventGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 4)
)
dismanEventEventGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteEventFailures"),
        ("DISMAN-EVENT-MIB", "mteEventComment"),
        ("DISMAN-EVENT-MIB", "mteEventActions"),
        ("DISMAN-EVENT-MIB", "mteEventEnabled"),
        ("DISMAN-EVENT-MIB", "mteEventEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteEventEntryStorageType"),
        ("DISMAN-EVENT-MIB", "mteEventNotification"),
        ("DISMAN-EVENT-MIB", "mteEventNotificationObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteEventNotificationObjects"),
        ("DISMAN-EVENT-MIB", "mteEventSetObject"),
        ("DISMAN-EVENT-MIB", "mteEventSetObjectWildcard"),
        ("DISMAN-EVENT-MIB", "mteEventSetValue"),
        ("DISMAN-EVENT-MIB", "mteEventSetTargetTag"),
        ("DISMAN-EVENT-MIB", "mteEventSetContextName"),
        ("DISMAN-EVENT-MIB", "mteEventSetContextNameWildcard"))
)
if mibBuilder.loadTexts:
    dismanEventEventGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanEventEventGroup.setDescription("Events.")

dismanEventNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 5)
)
dismanEventNotificationObjectGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    dismanEventNotificationObjectGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanEventNotificationObjectGroup.setDescription("Notification objects.")


# Notification objects

mteTriggerFired = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 1)
)
mteTriggerFired.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerFired.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    mteTriggerFired.setDescription("Notification that the trigger indicated by the object instances has fired, for triggers with mteTriggerType 'boolean' or 'existence'.")

mteTriggerRising = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 2)
)
mteTriggerRising.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerRising.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    mteTriggerRising.setDescription("Notification that the rising threshold was met for triggers with mteTriggerType 'threshold'.")

mteTriggerFalling = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 3)
)
mteTriggerFalling.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerFalling.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    mteTriggerFalling.setDescription("Notification that the falling threshold was met for triggers with mteTriggerType 'threshold'.")

mteTriggerFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 4)
)
mteTriggerFailure.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    mteTriggerFailure.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    mteTriggerFailure.setDescription("Notification that an attempt to check a trigger has failed. The network manager must enable this notification only with a certain fear and trembling, as it can easily crowd out more important information. It should be used only to help diagnose a problem that has appeared in the error counters and can not be found otherwise.")

mteEventSetFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 5)
)
mteEventSetFailure.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    mteEventSetFailure.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    mteEventSetFailure.setDescription("Notification that an attempt to do a set in response to an event has failed. The network manager must enable this notification only with a certain fear and trembling, as it can easily crowd out more important information. It should be used only to help diagnose a problem that has appeared in the error counters and can not be found otherwise.")


# Notifications groups

dismanEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 6)
)
dismanEventNotificationGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteTriggerFired"),
        ("DISMAN-EVENT-MIB", "mteTriggerRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerFailure"),
        ("DISMAN-EVENT-MIB", "mteEventSetFailure"))
)
if mibBuilder.loadTexts:
    dismanEventNotificationGroup.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    dismanEventNotificationGroup.setDescription("Notifications.")


# Agent capabilities


# Module compliance

dismanEventMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 88, 3, 1, 1)
)
dismanEventMIBCompliance.setObjects(
      *(("DISMAN-EVENT-MIB", "dismanEventResourceGroup"),
        ("DISMAN-EVENT-MIB", "dismanEventTriggerGroup"),
        ("DISMAN-EVENT-MIB", "dismanEventObjectsGroup"),
        ("DISMAN-EVENT-MIB", "dismanEventEventGroup"),
        ("DISMAN-EVENT-MIB", "dismanEventNotificationObjectGroup"),
        ("DISMAN-EVENT-MIB", "dismanEventNotificationGroup"))
)
if mibBuilder.loadTexts:
    dismanEventMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    dismanEventMIBCompliance.setDescription("The compliance statement for entities which implement the Event MIB.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "DISMAN-EVENT-MIB",
    **{"FailureReason": FailureReason,
       "sysUpTimeInstance": sysUpTimeInstance,
       "dismanEventMIB": dismanEventMIB,
       "dismanEventMIBObjects": dismanEventMIBObjects,
       "mteResource": mteResource,
       "mteResourceSampleMinimum": mteResourceSampleMinimum,
       "mteResourceSampleInstanceMaximum": mteResourceSampleInstanceMaximum,
       "mteResourceSampleInstances": mteResourceSampleInstances,
       "mteResourceSampleInstancesHigh": mteResourceSampleInstancesHigh,
       "mteResourceSampleInstanceLacks": mteResourceSampleInstanceLacks,
       "mteTrigger": mteTrigger,
       "mteTriggerFailures": mteTriggerFailures,
       "mteTriggerTable": mteTriggerTable,
       "mteTriggerEntry": mteTriggerEntry,
       "mteOwner": mteOwner,
       "mteTriggerName": mteTriggerName,
       "mteTriggerComment": mteTriggerComment,
       "mteTriggerTest": mteTriggerTest,
       "mteTriggerSampleType": mteTriggerSampleType,
       "mteTriggerValueID": mteTriggerValueID,
       "mteTriggerValueIDWildcard": mteTriggerValueIDWildcard,
       "mteTriggerTargetTag": mteTriggerTargetTag,
       "mteTriggerContextName": mteTriggerContextName,
       "mteTriggerContextNameWildcard": mteTriggerContextNameWildcard,
       "mteTriggerFrequency": mteTriggerFrequency,
       "mteTriggerObjectsOwner": mteTriggerObjectsOwner,
       "mteTriggerObjects": mteTriggerObjects,
       "mteTriggerEnabled": mteTriggerEnabled,
       "mteTriggerEntryStatus": mteTriggerEntryStatus,
       "mteTriggerEntryStorageType": mteTriggerEntryStorageType,
       "mteTriggerDeltaTable": mteTriggerDeltaTable,
       "mteTriggerDeltaEntry": mteTriggerDeltaEntry,
       "mteTriggerDeltaDiscontinuityID": mteTriggerDeltaDiscontinuityID,
       "mteTriggerDeltaDiscontinuityIDWildcard": mteTriggerDeltaDiscontinuityIDWildcard,
       "mteTriggerDeltaDiscontinuityIDType": mteTriggerDeltaDiscontinuityIDType,
       "mteTriggerExistenceTable": mteTriggerExistenceTable,
       "mteTriggerExistenceEntry": mteTriggerExistenceEntry,
       "mteTriggerExistenceTest": mteTriggerExistenceTest,
       "mteTriggerExistenceStartup": mteTriggerExistenceStartup,
       "mteTriggerExistenceObjectsOwner": mteTriggerExistenceObjectsOwner,
       "mteTriggerExistenceObjects": mteTriggerExistenceObjects,
       "mteTriggerExistenceEventOwner": mteTriggerExistenceEventOwner,
       "mteTriggerExistenceEvent": mteTriggerExistenceEvent,
       "mteTriggerBooleanTable": mteTriggerBooleanTable,
       "mteTriggerBooleanEntry": mteTriggerBooleanEntry,
       "mteTriggerBooleanComparison": mteTriggerBooleanComparison,
       "mteTriggerBooleanValue": mteTriggerBooleanValue,
       "mteTriggerBooleanStartup": mteTriggerBooleanStartup,
       "mteTriggerBooleanObjectsOwner": mteTriggerBooleanObjectsOwner,
       "mteTriggerBooleanObjects": mteTriggerBooleanObjects,
       "mteTriggerBooleanEventOwner": mteTriggerBooleanEventOwner,
       "mteTriggerBooleanEvent": mteTriggerBooleanEvent,
       "mteTriggerThresholdTable": mteTriggerThresholdTable,
       "mteTriggerThresholdEntry": mteTriggerThresholdEntry,
       "mteTriggerThresholdStartup": mteTriggerThresholdStartup,
       "mteTriggerThresholdRising": mteTriggerThresholdRising,
       "mteTriggerThresholdFalling": mteTriggerThresholdFalling,
       "mteTriggerThresholdDeltaRising": mteTriggerThresholdDeltaRising,
       "mteTriggerThresholdDeltaFalling": mteTriggerThresholdDeltaFalling,
       "mteTriggerThresholdObjectsOwner": mteTriggerThresholdObjectsOwner,
       "mteTriggerThresholdObjects": mteTriggerThresholdObjects,
       "mteTriggerThresholdRisingEventOwner": mteTriggerThresholdRisingEventOwner,
       "mteTriggerThresholdRisingEvent": mteTriggerThresholdRisingEvent,
       "mteTriggerThresholdFallingEventOwner": mteTriggerThresholdFallingEventOwner,
       "mteTriggerThresholdFallingEvent": mteTriggerThresholdFallingEvent,
       "mteTriggerThresholdDeltaRisingEventOwner": mteTriggerThresholdDeltaRisingEventOwner,
       "mteTriggerThresholdDeltaRisingEvent": mteTriggerThresholdDeltaRisingEvent,
       "mteTriggerThresholdDeltaFallingEventOwner": mteTriggerThresholdDeltaFallingEventOwner,
       "mteTriggerThresholdDeltaFallingEvent": mteTriggerThresholdDeltaFallingEvent,
       "mteObjects": mteObjects,
       "mteObjectsTable": mteObjectsTable,
       "mteObjectsEntry": mteObjectsEntry,
       "mteObjectsName": mteObjectsName,
       "mteObjectsIndex": mteObjectsIndex,
       "mteObjectsID": mteObjectsID,
       "mteObjectsIDWildcard": mteObjectsIDWildcard,
       "mteObjectsEntryStatus": mteObjectsEntryStatus,
       "mteObjectsEntryStorageType": mteObjectsEntryStorageType,
       "mteEvent": mteEvent,
       "mteEventFailures": mteEventFailures,
       "mteEventTable": mteEventTable,
       "mteEventEntry": mteEventEntry,
       "mteEventName": mteEventName,
       "mteEventComment": mteEventComment,
       "mteEventActions": mteEventActions,
       "mteEventEnabled": mteEventEnabled,
       "mteEventEntryStatus": mteEventEntryStatus,
       "mteEventEntryStorageType": mteEventEntryStorageType,
       "mteEventNotificationTable": mteEventNotificationTable,
       "mteEventNotificationEntry": mteEventNotificationEntry,
       "mteEventNotification": mteEventNotification,
       "mteEventNotificationObjectsOwner": mteEventNotificationObjectsOwner,
       "mteEventNotificationObjects": mteEventNotificationObjects,
       "mteEventSetTable": mteEventSetTable,
       "mteEventSetEntry": mteEventSetEntry,
       "mteEventSetObject": mteEventSetObject,
       "mteEventSetObjectWildcard": mteEventSetObjectWildcard,
       "mteEventSetValue": mteEventSetValue,
       "mteEventSetTargetTag": mteEventSetTargetTag,
       "mteEventSetContextName": mteEventSetContextName,
       "mteEventSetContextNameWildcard": mteEventSetContextNameWildcard,
       "dismanEventMIBNotificationPrefix": dismanEventMIBNotificationPrefix,
       "dismanEventMIBNotifications": dismanEventMIBNotifications,
       "mteTriggerFired": mteTriggerFired,
       "mteTriggerRising": mteTriggerRising,
       "mteTriggerFalling": mteTriggerFalling,
       "mteTriggerFailure": mteTriggerFailure,
       "mteEventSetFailure": mteEventSetFailure,
       "dismanEventMIBNotificationObjects": dismanEventMIBNotificationObjects,
       "mteHotTrigger": mteHotTrigger,
       "mteHotTargetName": mteHotTargetName,
       "mteHotContextName": mteHotContextName,
       "mteHotOID": mteHotOID,
       "mteHotValue": mteHotValue,
       "mteFailedReason": mteFailedReason,
       "dismanEventMIBConformance": dismanEventMIBConformance,
       "dismanEventMIBCompliances": dismanEventMIBCompliances,
       "dismanEventMIBCompliance": dismanEventMIBCompliance,
       "dismanEventMIBGroups": dismanEventMIBGroups,
       "dismanEventResourceGroup": dismanEventResourceGroup,
       "dismanEventTriggerGroup": dismanEventTriggerGroup,
       "dismanEventObjectsGroup": dismanEventObjectsGroup,
       "dismanEventEventGroup": dismanEventEventGroup,
       "dismanEventNotificationObjectGroup": dismanEventNotificationObjectGroup,
       "dismanEventNotificationGroup": dismanEventNotificationGroup}
)
