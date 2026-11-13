# SNMP MIB module (UCD-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/UCD-SNMP-MIB
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

(CounterBasedGauge64,) = mibBuilder.import_symbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.import_symbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.import_symbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ucdavis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021)
)
if mibBuilder.loadTexts:
    ucdavis.setRevisions(
        ("2016-06-10 00:00",
         "2014-07-31 00:00",
         "2011-05-14 00:00",
         "2009-01-19 00:00",
         "2006-11-22 00:00",
         "2004-04-07 00:00",
         "2002-09-05 00:00",
         "2001-09-20 00:00",
         "2001-01-17 00:00",
         "1999-12-09 00:00")
    )
if mibBuilder.loadTexts:
    ucdavis.setLastUpdated("201606100000Z")
if mibBuilder.loadTexts:
    ucdavis.setOrganization("University of California, Davis")
if mibBuilder.loadTexts:
    ucdavis.setContactInfo("This mib is no longer being maintained by the University of California and is now in life-support-mode and being maintained by the net-snmp project. The best place to write for public questions about the net-snmp-coders mailing list at net-snmp-coders@lists.sourceforge.net. postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net ")
if mibBuilder.loadTexts:
    ucdavis.setDescription("This file defines the private UCD SNMP MIB extensions.")


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(TextualConvention, Opaque):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7

    if mibBuilder.loadTexts:
        description = "A single precision floating-point number. The semantics and encoding are identical for type 'single' defined in IEEE Standard for Binary Floating-Point, ANSI/IEEE Std 754-1985. The value is restricted to the BER serialization of the following ASN.1 type: FLOATTYPE ::= [120] IMPLICIT FloatType (note: the value 120 is the sum of '30'h and '48'h) The BER serialization of the length for values of this type must use the definite length, short encoding form. For example, the BER serialization of value 123 of type FLOATTYPE is '9f780442f60000'h. (The tag is '9f78'h; the length is '04'h; and the value is '42f60000'h.) The BER serialization of value '9f780442f60000'h of data type Opaque is '44079f780442f60000'h. (The tag is '44'h; the length is '07'h; and the value is '9f780442f60000'h."


class UCDErrorFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("error", 1))
    )

    if mibBuilder.loadTexts:
        description = "Represents a possible error condition"


class UCDErrorFix(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("runFix", 1))
    )

    if mibBuilder.loadTexts:
        description = "Represents a 'push-button' object, to invoke a suitable configured action. Will always return 0 when read."


# MIB Managed Objects in the order of their OIDs

_PrTable_Object = MibTable
prTable = _PrTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2)
)
if mibBuilder.loadTexts:
    prTable.setStatus("current")
if mibBuilder.loadTexts:
    prTable.setDescription("A table containing information on running programs/daemons configured for monitoring in the snmpd.conf file of the agent. Processes violating the number of running processes required by the agent's configuration file are flagged with numerical and textual errors.")
_PrEntry_Object = MibTableRow
prEntry = _PrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1)
)
prEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "prIndex"),
)
if mibBuilder.loadTexts:
    prEntry.setStatus("current")
if mibBuilder.loadTexts:
    prEntry.setDescription("An entry containing a process and its statistics.")


class _PrIndex_Type(Integer32):
    """Custom type prIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrIndex_Type.__name__ = "Integer32"
_PrIndex_Object = MibTableColumn
prIndex = _PrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 1),
    _PrIndex_Type()
)
prIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIndex.setStatus("current")
if mibBuilder.loadTexts:
    prIndex.setDescription("Reference Index for each observed process.")
_PrNames_Type = DisplayString
_PrNames_Object = MibTableColumn
prNames = _PrNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 2),
    _PrNames_Type()
)
prNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prNames.setStatus("current")
if mibBuilder.loadTexts:
    prNames.setDescription("The process name we're counting/checking on.")
_PrMin_Type = Integer32
_PrMin_Object = MibTableColumn
prMin = _PrMin_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 3),
    _PrMin_Type()
)
prMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMin.setStatus("current")
if mibBuilder.loadTexts:
    prMin.setDescription("The minimum number of processes that should be running. An error flag is generated if the number of running processes is < the minimum.")
_PrMax_Type = Integer32
_PrMax_Object = MibTableColumn
prMax = _PrMax_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 4),
    _PrMax_Type()
)
prMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMax.setStatus("current")
if mibBuilder.loadTexts:
    prMax.setDescription("The maximum number of processes that should be running. An error flag is generated if the number of running processes is > the maximum.")
_PrCount_Type = Integer32
_PrCount_Object = MibTableColumn
prCount = _PrCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 5),
    _PrCount_Type()
)
prCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prCount.setStatus("current")
if mibBuilder.loadTexts:
    prCount.setDescription("The number of current processes running with the name in question.")
_PrErrorFlag_Type = UCDErrorFlag
_PrErrorFlag_Object = MibTableColumn
prErrorFlag = _PrErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 100),
    _PrErrorFlag_Type()
)
prErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    prErrorFlag.setDescription("A Error flag to indicate trouble with a process. It goes to 1 if there is an error, 0 if no error.")
_PrErrMessage_Type = DisplayString
_PrErrMessage_Object = MibTableColumn
prErrMessage = _PrErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 101),
    _PrErrMessage_Type()
)
prErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrMessage.setStatus("current")
if mibBuilder.loadTexts:
    prErrMessage.setDescription("An error message describing the problem (if one exists).")
_PrErrFix_Type = UCDErrorFix
_PrErrFix_Object = MibTableColumn
prErrFix = _PrErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 102),
    _PrErrFix_Type()
)
prErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prErrFix.setStatus("current")
if mibBuilder.loadTexts:
    prErrFix.setDescription("Setting this to one will try to fix the problem if the agent has been configured with a script to call to attempt to fix problems automatically using remote snmp operations.")
_PrErrFixCmd_Type = DisplayString
_PrErrFixCmd_Object = MibTableColumn
prErrFixCmd = _PrErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 103),
    _PrErrFixCmd_Type()
)
prErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrFixCmd.setStatus("current")
if mibBuilder.loadTexts:
    prErrFixCmd.setDescription("The command that gets run when the prErrFix column is set to 1.")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 4)
)
_MemIndex_Type = Integer32
_MemIndex_Object = MibScalar
memIndex = _MemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 1),
    _MemIndex_Type()
)
memIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIndex.setStatus("current")
if mibBuilder.loadTexts:
    memIndex.setDescription("Bogus Index. This should always return the integer 0.")
_MemErrorName_Type = DisplayString
_MemErrorName_Object = MibScalar
memErrorName = _MemErrorName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 2),
    _MemErrorName_Type()
)
memErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memErrorName.setStatus("current")
if mibBuilder.loadTexts:
    memErrorName.setDescription("Bogus Name. This should always return the string 'swap'.")
_MemTotalSwap_Type = Integer32
_MemTotalSwap_Object = MibScalar
memTotalSwap = _MemTotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 3),
    _MemTotalSwap_Type()
)
memTotalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwap.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwap.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalSwap.setDescription("The total amount of swap space configured for this host.")
_MemAvailSwap_Type = Integer32
_MemAvailSwap_Object = MibScalar
memAvailSwap = _MemAvailSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 4),
    _MemAvailSwap_Type()
)
memAvailSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwap.setStatus("current")
if mibBuilder.loadTexts:
    memAvailSwap.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailSwap.setDescription("The amount of swap space currently unused or available.")
_MemTotalReal_Type = Integer32
_MemTotalReal_Object = MibScalar
memTotalReal = _MemTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 5),
    _MemTotalReal_Type()
)
memTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal.setStatus("current")
if mibBuilder.loadTexts:
    memTotalReal.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalReal.setDescription("The total amount of real/physical memory installed on this host.")
_MemAvailReal_Type = Integer32
_MemAvailReal_Object = MibScalar
memAvailReal = _MemAvailReal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 6),
    _MemAvailReal_Type()
)
memAvailReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailReal.setStatus("current")
if mibBuilder.loadTexts:
    memAvailReal.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailReal.setDescription("The amount of real/physical memory currently unused or available.")
_MemTotalSwapTXT_Type = Integer32
_MemTotalSwapTXT_Object = MibScalar
memTotalSwapTXT = _MemTotalSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 7),
    _MemTotalSwapTXT_Type()
)
memTotalSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setDescription("The total amount of swap space or virtual memory allocated for text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of swap space or virtual memory.")
_MemAvailSwapTXT_Type = Integer32
_MemAvailSwapTXT_Object = MibScalar
memAvailSwapTXT = _MemAvailSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 8),
    _MemAvailSwapTXT_Type()
)
memAvailSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setStatus("deprecated")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setDescription("The amount of swap space or virtual memory currently being used by text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of swap space or virtual memory. Note that (despite the name), this value reports the amount used, rather than the amount free or available for use. For clarity, this object is being deprecated in favour of 'memUsedSwapTXT(16).")
_MemTotalRealTXT_Type = Integer32
_MemTotalRealTXT_Object = MibScalar
memTotalRealTXT = _MemTotalRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 9),
    _MemTotalRealTXT_Type()
)
memTotalRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalRealTXT.setStatus("current")
if mibBuilder.loadTexts:
    memTotalRealTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalRealTXT.setDescription("The total amount of real/physical memory allocated for text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of physical memory.")
_MemAvailRealTXT_Type = Integer32
_MemAvailRealTXT_Object = MibScalar
memAvailRealTXT = _MemAvailRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 10),
    _MemAvailRealTXT_Type()
)
memAvailRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailRealTXT.setStatus("deprecated")
if mibBuilder.loadTexts:
    memAvailRealTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailRealTXT.setDescription("The amount of real/physical memory currently being used by text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of physical memory. Note that (despite the name), this value reports the amount used, rather than the amount free or available for use. For clarity, this object is being deprecated in favour of 'memUsedRealTXT(17).")
_MemTotalFree_Type = Integer32
_MemTotalFree_Object = MibScalar
memTotalFree = _MemTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 11),
    _MemTotalFree_Type()
)
memTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalFree.setStatus("current")
if mibBuilder.loadTexts:
    memTotalFree.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalFree.setDescription("The total amount of memory free or available for use on this host. This value typically covers both real memory and swap space or virtual memory.")
_MemMinimumSwap_Type = Integer32
_MemMinimumSwap_Object = MibScalar
memMinimumSwap = _MemMinimumSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 12),
    _MemMinimumSwap_Type()
)
memMinimumSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMinimumSwap.setStatus("current")
if mibBuilder.loadTexts:
    memMinimumSwap.setUnits("kB")
if mibBuilder.loadTexts:
    memMinimumSwap.setDescription("The minimum amount of swap space expected to be kept free or available during normal operation of this host. If this value (as reported by 'memAvailSwap(4)') falls below the specified level, then 'memSwapError(100)' will be set to 1 and an error message made available via 'memSwapErrorMsg(101)'.")
_MemShared_Type = Integer32
_MemShared_Object = MibScalar
memShared = _MemShared_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 13),
    _MemShared_Type()
)
memShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memShared.setStatus("current")
if mibBuilder.loadTexts:
    memShared.setUnits("kB")
if mibBuilder.loadTexts:
    memShared.setDescription("The total amount of real or virtual memory currently allocated for use as shared memory. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemBuffer_Type = Integer32
_MemBuffer_Object = MibScalar
memBuffer = _MemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 14),
    _MemBuffer_Type()
)
memBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBuffer.setStatus("current")
if mibBuilder.loadTexts:
    memBuffer.setUnits("kB")
if mibBuilder.loadTexts:
    memBuffer.setDescription("The total amount of real or virtual memory currently allocated for use as memory buffers. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemCached_Type = Integer32
_MemCached_Object = MibScalar
memCached = _MemCached_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 15),
    _MemCached_Type()
)
memCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCached.setStatus("current")
if mibBuilder.loadTexts:
    memCached.setUnits("kB")
if mibBuilder.loadTexts:
    memCached.setDescription("The total amount of real or virtual memory currently allocated for use as cached memory. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemUsedSwapTXT_Type = Integer32
_MemUsedSwapTXT_Object = MibScalar
memUsedSwapTXT = _MemUsedSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 16),
    _MemUsedSwapTXT_Type()
)
memUsedSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsedSwapTXT.setStatus("current")
if mibBuilder.loadTexts:
    memUsedSwapTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memUsedSwapTXT.setDescription("The amount of swap space or virtual memory currently being used by text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of swap space or virtual memory.")
_MemUsedRealTXT_Type = Integer32
_MemUsedRealTXT_Object = MibScalar
memUsedRealTXT = _MemUsedRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 17),
    _MemUsedRealTXT_Type()
)
memUsedRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsedRealTXT.setStatus("current")
if mibBuilder.loadTexts:
    memUsedRealTXT.setUnits("kB")
if mibBuilder.loadTexts:
    memUsedRealTXT.setDescription("The amount of real/physical memory currently being used by text pages on this host. This object will not be implemented on hosts where the underlying operating system does not distinguish text pages from other uses of physical memory.")
_MemTotalSwapX_Type = CounterBasedGauge64
_MemTotalSwapX_Object = MibScalar
memTotalSwapX = _MemTotalSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 18),
    _MemTotalSwapX_Type()
)
memTotalSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwapX.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalSwapX.setDescription("The total amount of swap space configured for this host.")
_MemAvailSwapX_Type = CounterBasedGauge64
_MemAvailSwapX_Object = MibScalar
memAvailSwapX = _MemAvailSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 19),
    _MemAvailSwapX_Type()
)
memAvailSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memAvailSwapX.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailSwapX.setDescription("The amount of swap space currently unused or available.")
_MemTotalRealX_Type = CounterBasedGauge64
_MemTotalRealX_Object = MibScalar
memTotalRealX = _MemTotalRealX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 20),
    _MemTotalRealX_Type()
)
memTotalRealX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalRealX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalRealX.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalRealX.setDescription("The total amount of real/physical memory installed on this host.")
_MemAvailRealX_Type = CounterBasedGauge64
_MemAvailRealX_Object = MibScalar
memAvailRealX = _MemAvailRealX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 21),
    _MemAvailRealX_Type()
)
memAvailRealX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailRealX.setStatus("current")
if mibBuilder.loadTexts:
    memAvailRealX.setUnits("kB")
if mibBuilder.loadTexts:
    memAvailRealX.setDescription("The amount of real/physical memory currently unused or available.")
_MemTotalFreeX_Type = CounterBasedGauge64
_MemTotalFreeX_Object = MibScalar
memTotalFreeX = _MemTotalFreeX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 22),
    _MemTotalFreeX_Type()
)
memTotalFreeX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalFreeX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalFreeX.setUnits("kB")
if mibBuilder.loadTexts:
    memTotalFreeX.setDescription("The total amount of memory free or available for use on this host. This value typically covers both real memory and swap space or virtual memory.")
_MemMinimumSwapX_Type = CounterBasedGauge64
_MemMinimumSwapX_Object = MibScalar
memMinimumSwapX = _MemMinimumSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 23),
    _MemMinimumSwapX_Type()
)
memMinimumSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMinimumSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memMinimumSwapX.setUnits("kB")
if mibBuilder.loadTexts:
    memMinimumSwapX.setDescription("The minimum amount of swap space expected to be kept free or available during normal operation of this host. If this value (as reported by 'memAvailSwap(4)') falls below the specified level, then 'memSwapError(100)' will be set to 1 and an error message made available via 'memSwapErrorMsg(101)'.")
_MemSharedX_Type = CounterBasedGauge64
_MemSharedX_Object = MibScalar
memSharedX = _MemSharedX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 24),
    _MemSharedX_Type()
)
memSharedX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSharedX.setStatus("current")
if mibBuilder.loadTexts:
    memSharedX.setUnits("kB")
if mibBuilder.loadTexts:
    memSharedX.setDescription("The total amount of real or virtual memory currently allocated for use as shared memory. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemBufferX_Type = CounterBasedGauge64
_MemBufferX_Object = MibScalar
memBufferX = _MemBufferX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 25),
    _MemBufferX_Type()
)
memBufferX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBufferX.setStatus("current")
if mibBuilder.loadTexts:
    memBufferX.setUnits("kB")
if mibBuilder.loadTexts:
    memBufferX.setDescription("The total amount of real or virtual memory currently allocated for use as memory buffers. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemCachedX_Type = CounterBasedGauge64
_MemCachedX_Object = MibScalar
memCachedX = _MemCachedX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 26),
    _MemCachedX_Type()
)
memCachedX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCachedX.setStatus("current")
if mibBuilder.loadTexts:
    memCachedX.setUnits("kB")
if mibBuilder.loadTexts:
    memCachedX.setDescription("The total amount of real or virtual memory currently allocated for use as cached memory. This object will not be implemented on hosts where the underlying operating system does not explicitly identify memory as specifically reserved for this purpose.")
_MemSwapError_Type = UCDErrorFlag
_MemSwapError_Object = MibScalar
memSwapError = _MemSwapError_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 100),
    _MemSwapError_Type()
)
memSwapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapError.setStatus("current")
if mibBuilder.loadTexts:
    memSwapError.setDescription("Indicates whether the amount of available swap space (as reported by 'memAvailSwap(4)'), is less than the desired minimum (specified by 'memMinimumSwap(12)').")
_MemSwapErrorMsg_Type = DisplayString
_MemSwapErrorMsg_Object = MibScalar
memSwapErrorMsg = _MemSwapErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 101),
    _MemSwapErrorMsg_Type()
)
memSwapErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapErrorMsg.setStatus("current")
if mibBuilder.loadTexts:
    memSwapErrorMsg.setDescription("Describes whether the amount of available swap space (as reported by 'memAvailSwap(4)'), is less than the desired minimum (specified by 'memMinimumSwap(12)').")
_ExtTable_Object = MibTable
extTable = _ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8)
)
if mibBuilder.loadTexts:
    extTable.setStatus("current")
if mibBuilder.loadTexts:
    extTable.setDescription("A table of extensible commands returning output and result codes. These commands are configured via the agent's snmpd.conf file.")
_ExtEntry_Object = MibTableRow
extEntry = _ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1)
)
extEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "extIndex"),
)
if mibBuilder.loadTexts:
    extEntry.setStatus("current")
if mibBuilder.loadTexts:
    extEntry.setDescription("An entry containing an extensible script/program and its output.")


class _ExtIndex_Type(Integer32):
    """Custom type extIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtIndex_Type.__name__ = "Integer32"
_ExtIndex_Object = MibTableColumn
extIndex = _ExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 1),
    _ExtIndex_Type()
)
extIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extIndex.setStatus("current")
if mibBuilder.loadTexts:
    extIndex.setDescription("Reference Index for extensible scripts. Simply an integer row number.")
_ExtNames_Type = DisplayString
_ExtNames_Object = MibTableColumn
extNames = _ExtNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 2),
    _ExtNames_Type()
)
extNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extNames.setStatus("current")
if mibBuilder.loadTexts:
    extNames.setDescription("A Short, one name description of the extensible command.")
_ExtCommand_Type = DisplayString
_ExtCommand_Object = MibTableColumn
extCommand = _ExtCommand_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 3),
    _ExtCommand_Type()
)
extCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extCommand.setStatus("current")
if mibBuilder.loadTexts:
    extCommand.setDescription("The command line to be executed.")
_ExtResult_Type = Integer32
_ExtResult_Object = MibTableColumn
extResult = _ExtResult_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 100),
    _ExtResult_Type()
)
extResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extResult.setStatus("current")
if mibBuilder.loadTexts:
    extResult.setDescription("The result code (exit status) from the executed command.")
_ExtOutput_Type = DisplayString
_ExtOutput_Object = MibTableColumn
extOutput = _ExtOutput_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 101),
    _ExtOutput_Type()
)
extOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extOutput.setStatus("current")
if mibBuilder.loadTexts:
    extOutput.setDescription("The first line of output of the executed command.")
_ExtErrFix_Type = UCDErrorFix
_ExtErrFix_Object = MibTableColumn
extErrFix = _ExtErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 102),
    _ExtErrFix_Type()
)
extErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extErrFix.setStatus("current")
if mibBuilder.loadTexts:
    extErrFix.setDescription("Setting this to one will try to fix the problem if the agent has been configured with a script to call to attempt to fix problems automatically using remote snmp operations.")
_ExtErrFixCmd_Type = DisplayString
_ExtErrFixCmd_Object = MibTableColumn
extErrFixCmd = _ExtErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 103),
    _ExtErrFixCmd_Type()
)
extErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extErrFixCmd.setStatus("current")
if mibBuilder.loadTexts:
    extErrFixCmd.setDescription("The command that gets run when the extErrFix column is set to 1.")
_DskTable_Object = MibTable
dskTable = _DskTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9)
)
if mibBuilder.loadTexts:
    dskTable.setStatus("current")
if mibBuilder.loadTexts:
    dskTable.setDescription("Disk watching information. Partions to be watched are configured by the snmpd.conf file of the agent.")
_DskEntry_Object = MibTableRow
dskEntry = _DskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1)
)
dskEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "dskIndex"),
)
if mibBuilder.loadTexts:
    dskEntry.setStatus("current")
if mibBuilder.loadTexts:
    dskEntry.setDescription("An entry containing a disk and its statistics.")


class _DskIndex_Type(Integer32):
    """Custom type dskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DskIndex_Type.__name__ = "Integer32"
_DskIndex_Object = MibTableColumn
dskIndex = _DskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 1),
    _DskIndex_Type()
)
dskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskIndex.setStatus("current")
if mibBuilder.loadTexts:
    dskIndex.setDescription("Integer reference number (row number) for the disk mib.")
_DskPath_Type = DisplayString
_DskPath_Object = MibTableColumn
dskPath = _DskPath_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 2),
    _DskPath_Type()
)
dskPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPath.setStatus("current")
if mibBuilder.loadTexts:
    dskPath.setDescription("Path where the disk is mounted.")
_DskDevice_Type = DisplayString
_DskDevice_Object = MibTableColumn
dskDevice = _DskDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 3),
    _DskDevice_Type()
)
dskDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskDevice.setStatus("current")
if mibBuilder.loadTexts:
    dskDevice.setDescription("Path of the device for the partition")
_DskMinimum_Type = Integer32
_DskMinimum_Object = MibTableColumn
dskMinimum = _DskMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 4),
    _DskMinimum_Type()
)
dskMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinimum.setStatus("current")
if mibBuilder.loadTexts:
    dskMinimum.setDescription("Minimum space required on the disk (in kBytes) before the errors are triggered. Either this or dskMinPercent is configured via the agent's snmpd.conf file.")
_DskMinPercent_Type = Integer32
_DskMinPercent_Object = MibTableColumn
dskMinPercent = _DskMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 5),
    _DskMinPercent_Type()
)
dskMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinPercent.setStatus("current")
if mibBuilder.loadTexts:
    dskMinPercent.setDescription("Percentage of minimum space required on the disk before the errors are triggered. Either this or dskMinimum is configured via the agent's snmpd.conf file.")
_DskTotal_Type = Integer32
_DskTotal_Object = MibTableColumn
dskTotal = _DskTotal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 6),
    _DskTotal_Type()
)
dskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotal.setStatus("current")
if mibBuilder.loadTexts:
    dskTotal.setDescription("Total size of the disk/partion (kBytes). For large disks (>2Tb), this value will latch at INT32_MAX (2147483647).")
_DskAvail_Type = Integer32
_DskAvail_Object = MibTableColumn
dskAvail = _DskAvail_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 7),
    _DskAvail_Type()
)
dskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvail.setStatus("current")
if mibBuilder.loadTexts:
    dskAvail.setDescription("Available space on the disk. For large lightly-used disks (>2Tb), this value will latch at INT32_MAX (2147483647).")
_DskUsed_Type = Integer32
_DskUsed_Object = MibTableColumn
dskUsed = _DskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 8),
    _DskUsed_Type()
)
dskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsed.setStatus("current")
if mibBuilder.loadTexts:
    dskUsed.setDescription("Used space on the disk. For large heavily-used disks (>2Tb), this value will latch at INT32_MAX (2147483647).")
_DskPercent_Type = Integer32
_DskPercent_Object = MibTableColumn
dskPercent = _DskPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 9),
    _DskPercent_Type()
)
dskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercent.setStatus("current")
if mibBuilder.loadTexts:
    dskPercent.setDescription("Percentage of space used on disk")
_DskPercentNode_Type = Integer32
_DskPercentNode_Object = MibTableColumn
dskPercentNode = _DskPercentNode_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 10),
    _DskPercentNode_Type()
)
dskPercentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercentNode.setStatus("current")
if mibBuilder.loadTexts:
    dskPercentNode.setDescription("Percentage of inodes used on disk")
_DskTotalLow_Type = Unsigned32
_DskTotalLow_Object = MibTableColumn
dskTotalLow = _DskTotalLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 11),
    _DskTotalLow_Type()
)
dskTotalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotalLow.setStatus("current")
if mibBuilder.loadTexts:
    dskTotalLow.setDescription("Total size of the disk/partion (kBytes). Together with dskTotalHigh composes 64-bit number.")
_DskTotalHigh_Type = Unsigned32
_DskTotalHigh_Object = MibTableColumn
dskTotalHigh = _DskTotalHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 12),
    _DskTotalHigh_Type()
)
dskTotalHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotalHigh.setStatus("current")
if mibBuilder.loadTexts:
    dskTotalHigh.setDescription("Total size of the disk/partion (kBytes). Together with dskTotalLow composes 64-bit number.")
_DskAvailLow_Type = Unsigned32
_DskAvailLow_Object = MibTableColumn
dskAvailLow = _DskAvailLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 13),
    _DskAvailLow_Type()
)
dskAvailLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvailLow.setStatus("current")
if mibBuilder.loadTexts:
    dskAvailLow.setDescription("Available space on the disk (kBytes). Together with dskAvailHigh composes 64-bit number.")
_DskAvailHigh_Type = Unsigned32
_DskAvailHigh_Object = MibTableColumn
dskAvailHigh = _DskAvailHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 14),
    _DskAvailHigh_Type()
)
dskAvailHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvailHigh.setStatus("current")
if mibBuilder.loadTexts:
    dskAvailHigh.setDescription("Available space on the disk (kBytes). Together with dskAvailLow composes 64-bit number.")
_DskUsedLow_Type = Unsigned32
_DskUsedLow_Object = MibTableColumn
dskUsedLow = _DskUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 15),
    _DskUsedLow_Type()
)
dskUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsedLow.setStatus("current")
if mibBuilder.loadTexts:
    dskUsedLow.setDescription("Used space on the disk (kBytes). Together with dskUsedHigh composes 64-bit number.")
_DskUsedHigh_Type = Unsigned32
_DskUsedHigh_Object = MibTableColumn
dskUsedHigh = _DskUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 16),
    _DskUsedHigh_Type()
)
dskUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsedHigh.setStatus("current")
if mibBuilder.loadTexts:
    dskUsedHigh.setDescription("Used space on the disk (kBytes). Together with dskUsedLow composes 64-bit number.")
_DskErrorFlag_Type = UCDErrorFlag
_DskErrorFlag_Object = MibTableColumn
dskErrorFlag = _DskErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 100),
    _DskErrorFlag_Type()
)
dskErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    dskErrorFlag.setDescription("Error flag signaling that the disk or partition is under the minimum required space configured for it.")
_DskErrorMsg_Type = DisplayString
_DskErrorMsg_Object = MibTableColumn
dskErrorMsg = _DskErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 101),
    _DskErrorMsg_Type()
)
dskErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorMsg.setStatus("current")
if mibBuilder.loadTexts:
    dskErrorMsg.setDescription("A text description providing a warning and the space left on the disk.")
_LaTable_Object = MibTable
laTable = _LaTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10)
)
if mibBuilder.loadTexts:
    laTable.setStatus("current")
if mibBuilder.loadTexts:
    laTable.setDescription("Load average information.")
_LaEntry_Object = MibTableRow
laEntry = _LaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1)
)
laEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laEntry.setStatus("current")
if mibBuilder.loadTexts:
    laEntry.setDescription("An entry containing a load average and its values.")


class _LaIndex_Type(Integer32):
    """Custom type laIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LaIndex_Type.__name__ = "Integer32"
_LaIndex_Object = MibTableColumn
laIndex = _LaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 1),
    _LaIndex_Type()
)
laIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laIndex.setStatus("current")
if mibBuilder.loadTexts:
    laIndex.setDescription("reference index/row number for each observed loadave.")
_LaNames_Type = DisplayString
_LaNames_Object = MibTableColumn
laNames = _LaNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 2),
    _LaNames_Type()
)
laNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laNames.setStatus("current")
if mibBuilder.loadTexts:
    laNames.setDescription("The list of loadave names we're watching.")
_LaLoad_Type = DisplayString
_LaLoad_Object = MibTableColumn
laLoad = _LaLoad_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 3),
    _LaLoad_Type()
)
laLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoad.setStatus("current")
if mibBuilder.loadTexts:
    laLoad.setDescription("The 1,5 and 15 minute load averages (one per row).")
_LaConfig_Type = DisplayString
_LaConfig_Object = MibTableColumn
laConfig = _LaConfig_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 4),
    _LaConfig_Type()
)
laConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laConfig.setStatus("current")
if mibBuilder.loadTexts:
    laConfig.setDescription("The watch point for load-averages to signal an error. If the load averages rises above this value, the laErrorFlag below is set.")
_LaLoadInt_Type = Integer32
_LaLoadInt_Object = MibTableColumn
laLoadInt = _LaLoadInt_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 5),
    _LaLoadInt_Type()
)
laLoadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoadInt.setStatus("current")
if mibBuilder.loadTexts:
    laLoadInt.setDescription("The 1,5 and 15 minute load averages as an integer. This is computed by taking the floating point loadaverage value and multiplying by 100, then converting the value to an integer.")
_LaLoadFloat_Type = Float
_LaLoadFloat_Object = MibTableColumn
laLoadFloat = _LaLoadFloat_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 6),
    _LaLoadFloat_Type()
)
laLoadFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoadFloat.setStatus("current")
if mibBuilder.loadTexts:
    laLoadFloat.setDescription("The 1,5 and 15 minute load averages as an opaquely wrapped floating point number.")
_LaErrorFlag_Type = UCDErrorFlag
_LaErrorFlag_Object = MibTableColumn
laErrorFlag = _LaErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 100),
    _LaErrorFlag_Type()
)
laErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    laErrorFlag.setDescription("A Error flag to indicate the load-average has crossed its threshold value defined in the snmpd.conf file. It is set to 1 if the threshold is crossed, 0 otherwise.")
_LaErrMessage_Type = DisplayString
_LaErrMessage_Object = MibTableColumn
laErrMessage = _LaErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 101),
    _LaErrMessage_Type()
)
laErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laErrMessage.setStatus("current")
if mibBuilder.loadTexts:
    laErrMessage.setDescription("An error message describing the load-average and its surpased watch-point value.")
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 11)
)
_SsIndex_Type = Integer32
_SsIndex_Object = MibScalar
ssIndex = _SsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 1),
    _SsIndex_Type()
)
ssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIndex.setStatus("current")
if mibBuilder.loadTexts:
    ssIndex.setDescription("Bogus Index. This should always return the integer 1.")
_SsErrorName_Type = DisplayString
_SsErrorName_Object = MibScalar
ssErrorName = _SsErrorName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 2),
    _SsErrorName_Type()
)
ssErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssErrorName.setStatus("current")
if mibBuilder.loadTexts:
    ssErrorName.setDescription("Bogus Name. This should always return the string 'systemStats'.")
_SsSwapIn_Type = Integer32
_SsSwapIn_Object = MibScalar
ssSwapIn = _SsSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 3),
    _SsSwapIn_Type()
)
ssSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapIn.setStatus("current")
if mibBuilder.loadTexts:
    ssSwapIn.setUnits("kB")
if mibBuilder.loadTexts:
    ssSwapIn.setDescription("The average amount of memory swapped in from disk, calculated over the last minute.")
_SsSwapOut_Type = Integer32
_SsSwapOut_Object = MibScalar
ssSwapOut = _SsSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 4),
    _SsSwapOut_Type()
)
ssSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapOut.setStatus("current")
if mibBuilder.loadTexts:
    ssSwapOut.setUnits("kB")
if mibBuilder.loadTexts:
    ssSwapOut.setDescription("The average amount of memory swapped out to disk, calculated over the last minute.")
_SsIOSent_Type = Integer32
_SsIOSent_Object = MibScalar
ssIOSent = _SsIOSent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 5),
    _SsIOSent_Type()
)
ssIOSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssIOSent.setUnits("blocks/s")
if mibBuilder.loadTexts:
    ssIOSent.setDescription("The average amount of data written to disk or other block device, calculated over the last minute. This object has been deprecated in favour of 'ssIORawSent(57)', which can be used to calculate the same metric, but over any desired time period.")
_SsIOReceive_Type = Integer32
_SsIOReceive_Object = MibScalar
ssIOReceive = _SsIOReceive_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 6),
    _SsIOReceive_Type()
)
ssIOReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOReceive.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssIOReceive.setUnits("blocks/s")
if mibBuilder.loadTexts:
    ssIOReceive.setDescription("The average amount of data read from disk or other block device, calculated over the last minute. This object has been deprecated in favour of 'ssIORawReceived(58)', which can be used to calculate the same metric, but over any desired time period.")
_SsSysInterrupts_Type = Integer32
_SsSysInterrupts_Object = MibScalar
ssSysInterrupts = _SsSysInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 7),
    _SsSysInterrupts_Type()
)
ssSysInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysInterrupts.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssSysInterrupts.setUnits("interrupts/s")
if mibBuilder.loadTexts:
    ssSysInterrupts.setDescription("The average rate of interrupts processed (including the clock) calculated over the last minute. This object has been deprecated in favour of 'ssRawInterrupts(59)', which can be used to calculate the same metric, but over any desired time period.")
_SsSysContext_Type = Integer32
_SsSysContext_Object = MibScalar
ssSysContext = _SsSysContext_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 8),
    _SsSysContext_Type()
)
ssSysContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysContext.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssSysContext.setUnits("switches/s")
if mibBuilder.loadTexts:
    ssSysContext.setDescription("The average rate of context switches, calculated over the last minute. This object has been deprecated in favour of 'ssRawContext(60)', which can be used to calculate the same metric, but over any desired time period.")
_SsCpuUser_Type = Integer32
_SsCpuUser_Object = MibScalar
ssCpuUser = _SsCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 9),
    _SsCpuUser_Type()
)
ssCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuUser.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssCpuUser.setDescription("The percentage of CPU time spent processing user-level code, calculated over the last minute. This object has been deprecated in favour of 'ssCpuRawUser(50)', which can be used to calculate the same metric, but over any desired time period.")
_SsCpuSystem_Type = Integer32
_SsCpuSystem_Object = MibScalar
ssCpuSystem = _SsCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 10),
    _SsCpuSystem_Type()
)
ssCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuSystem.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssCpuSystem.setDescription("The percentage of CPU time spent processing system-level code, calculated over the last minute. This object has been deprecated in favour of 'ssCpuRawSystem(52)', which can be used to calculate the same metric, but over any desired time period.")
_SsCpuIdle_Type = Integer32
_SsCpuIdle_Object = MibScalar
ssCpuIdle = _SsCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 11),
    _SsCpuIdle_Type()
)
ssCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuIdle.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssCpuIdle.setDescription("The percentage of processor time spent idle, calculated over the last minute. This object has been deprecated in favour of 'ssCpuRawIdle(53)', which can be used to calculate the same metric, but over any desired time period.")
_SsCpuRawUser_Type = Counter32
_SsCpuRawUser_Object = MibScalar
ssCpuRawUser = _SsCpuRawUser_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 50),
    _SsCpuRawUser_Type()
)
ssCpuRawUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawUser.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawUser.setDescription("The number of 'ticks' (typically 1/100s) spent processing user-level code. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawNice_Type = Counter32
_SsCpuRawNice_Object = MibScalar
ssCpuRawNice = _SsCpuRawNice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 51),
    _SsCpuRawNice_Type()
)
ssCpuRawNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawNice.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawNice.setDescription("The number of 'ticks' (typically 1/100s) spent processing reduced-priority code. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawSystem_Type = Counter32
_SsCpuRawSystem_Object = MibScalar
ssCpuRawSystem = _SsCpuRawSystem_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 52),
    _SsCpuRawSystem_Type()
)
ssCpuRawSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSystem.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawSystem.setDescription("The number of 'ticks' (typically 1/100s) spent processing system-level code. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors). This object may sometimes be implemented as the combination of the 'ssCpuRawWait(54)' and 'ssCpuRawKernel(55)' counters, so care must be taken when summing the overall raw counters.")
_SsCpuRawIdle_Type = Counter32
_SsCpuRawIdle_Object = MibScalar
ssCpuRawIdle = _SsCpuRawIdle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 53),
    _SsCpuRawIdle_Type()
)
ssCpuRawIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawIdle.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawIdle.setDescription("The number of 'ticks' (typically 1/100s) spent idle. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawWait_Type = Counter32
_SsCpuRawWait_Object = MibScalar
ssCpuRawWait = _SsCpuRawWait_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 54),
    _SsCpuRawWait_Type()
)
ssCpuRawWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawWait.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawWait.setDescription("The number of 'ticks' (typically 1/100s) spent waiting for IO. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. This time may also be included within the 'ssCpuRawSystem(52)' counter. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawKernel_Type = Counter32
_SsCpuRawKernel_Object = MibScalar
ssCpuRawKernel = _SsCpuRawKernel_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 55),
    _SsCpuRawKernel_Type()
)
ssCpuRawKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawKernel.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawKernel.setDescription("The number of 'ticks' (typically 1/100s) spent processing kernel-level code. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. This time may also be included within the 'ssCpuRawSystem(52)' counter. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawInterrupt_Type = Counter32
_SsCpuRawInterrupt_Object = MibScalar
ssCpuRawInterrupt = _SsCpuRawInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 56),
    _SsCpuRawInterrupt_Type()
)
ssCpuRawInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawInterrupt.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawInterrupt.setDescription("The number of 'ticks' (typically 1/100s) spent processing hardware interrupts. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsIORawSent_Type = Counter32
_SsIORawSent_Object = MibScalar
ssIORawSent = _SsIORawSent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 57),
    _SsIORawSent_Type()
)
ssIORawSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawSent.setStatus("current")
if mibBuilder.loadTexts:
    ssIORawSent.setDescription("Number of blocks sent to a block device")
_SsIORawReceived_Type = Counter32
_SsIORawReceived_Object = MibScalar
ssIORawReceived = _SsIORawReceived_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 58),
    _SsIORawReceived_Type()
)
ssIORawReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawReceived.setStatus("current")
if mibBuilder.loadTexts:
    ssIORawReceived.setDescription("Number of blocks received from a block device")
_SsRawInterrupts_Type = Counter32
_SsRawInterrupts_Object = MibScalar
ssRawInterrupts = _SsRawInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 59),
    _SsRawInterrupts_Type()
)
ssRawInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawInterrupts.setStatus("current")
if mibBuilder.loadTexts:
    ssRawInterrupts.setDescription("Number of interrupts processed")
_SsRawContexts_Type = Counter32
_SsRawContexts_Object = MibScalar
ssRawContexts = _SsRawContexts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 60),
    _SsRawContexts_Type()
)
ssRawContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawContexts.setStatus("current")
if mibBuilder.loadTexts:
    ssRawContexts.setDescription("Number of context switches")
_SsCpuRawSoftIRQ_Type = Counter32
_SsCpuRawSoftIRQ_Object = MibScalar
ssCpuRawSoftIRQ = _SsCpuRawSoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 61),
    _SsCpuRawSoftIRQ_Type()
)
ssCpuRawSoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSoftIRQ.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawSoftIRQ.setDescription("The number of 'ticks' (typically 1/100s) spent processing software interrupts. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsRawSwapIn_Type = Counter32
_SsRawSwapIn_Object = MibScalar
ssRawSwapIn = _SsRawSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 62),
    _SsRawSwapIn_Type()
)
ssRawSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawSwapIn.setStatus("current")
if mibBuilder.loadTexts:
    ssRawSwapIn.setDescription("Number of blocks swapped in")
_SsRawSwapOut_Type = Counter32
_SsRawSwapOut_Object = MibScalar
ssRawSwapOut = _SsRawSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 63),
    _SsRawSwapOut_Type()
)
ssRawSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawSwapOut.setStatus("current")
if mibBuilder.loadTexts:
    ssRawSwapOut.setDescription("Number of blocks swapped out")
_SsCpuRawSteal_Type = Counter32
_SsCpuRawSteal_Object = MibScalar
ssCpuRawSteal = _SsCpuRawSteal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 64),
    _SsCpuRawSteal_Type()
)
ssCpuRawSteal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSteal.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawSteal.setDescription("The number of 'ticks' (typically 1/100s) spent by the hypervisor code to run other VMs even though the CPU in the current VM had something runnable. This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawGuest_Type = Counter32
_SsCpuRawGuest_Object = MibScalar
ssCpuRawGuest = _SsCpuRawGuest_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 65),
    _SsCpuRawGuest_Type()
)
ssCpuRawGuest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawGuest.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawGuest.setDescription("The number of 'ticks' (typically 1/100s) spent by the CPU to run a virtual CPU (guest). This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuRawGuestNice_Type = Counter32
_SsCpuRawGuestNice_Object = MibScalar
ssCpuRawGuestNice = _SsCpuRawGuestNice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 66),
    _SsCpuRawGuestNice_Type()
)
ssCpuRawGuestNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawGuestNice.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuRawGuestNice.setDescription("The number of 'ticks' (typically 1/100s) spent by the CPU to run a niced virtual CPU (guest). This object will not be implemented on hosts where the underlying operating system does not measure this particular CPU metric. On a multi-processor system, the 'ssCpuRaw*' counters are cumulative over all CPUs, so their sum will typically be N*100 (for N processors).")
_SsCpuNumCpus_Type = Integer32
_SsCpuNumCpus_Object = MibScalar
ssCpuNumCpus = _SsCpuNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 67),
    _SsCpuNumCpus_Type()
)
ssCpuNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuNumCpus.setStatus("current")
if mibBuilder.loadTexts:
    ssCpuNumCpus.setDescription("The number of processors, as counted by the agent. This object's value may be useful in the management of certain operating systems where notions such as load average do not take into account the number of processors in the system. For other objects in the systemStats group whose descriptions refer to 'N processors', this object's value is N.")
_UcdInternal_ObjectIdentity = ObjectIdentity
ucdInternal = _UcdInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 12)
)
_UcdExperimental_ObjectIdentity = ObjectIdentity
ucdExperimental = _UcdExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13)
)
_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("current")
if mibBuilder.loadTexts:
    fileTable.setDescription("Table of monitored files.")
_FileEntry_Object = MibTableRow
fileEntry = _FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1)
)
fileEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "fileIndex"),
)
if mibBuilder.loadTexts:
    fileEntry.setStatus("current")
if mibBuilder.loadTexts:
    fileEntry.setDescription("Entry of file")


class _FileIndex_Type(Integer32):
    """Custom type fileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FileIndex_Type.__name__ = "Integer32"
_FileIndex_Object = MibTableColumn
fileIndex = _FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 1),
    _FileIndex_Type()
)
fileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileIndex.setStatus("current")
if mibBuilder.loadTexts:
    fileIndex.setDescription("Index of file")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
if mibBuilder.loadTexts:
    fileName.setDescription("Filename")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 3),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileSize.setUnits("kB")
if mibBuilder.loadTexts:
    fileSize.setDescription("Size of file (kB)")
_FileMax_Type = Integer32
_FileMax_Object = MibTableColumn
fileMax = _FileMax_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 4),
    _FileMax_Type()
)
fileMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileMax.setStatus("current")
if mibBuilder.loadTexts:
    fileMax.setUnits("kB")
if mibBuilder.loadTexts:
    fileMax.setDescription("Limit of filesize (kB)")
_FileErrorFlag_Type = UCDErrorFlag
_FileErrorFlag_Object = MibTableColumn
fileErrorFlag = _FileErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 100),
    _FileErrorFlag_Type()
)
fileErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    fileErrorFlag.setDescription("Limit exceeded flag")
_FileErrorMsg_Type = DisplayString
_FileErrorMsg_Object = MibTableColumn
fileErrorMsg = _FileErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 101),
    _FileErrorMsg_Type()
)
fileErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileErrorMsg.setStatus("current")
if mibBuilder.loadTexts:
    fileErrorMsg.setDescription("Filesize error message")
_LogMatch_ObjectIdentity = ObjectIdentity
logMatch = _LogMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 16)
)
_LogMatchMaxEntries_Type = Integer32
_LogMatchMaxEntries_Object = MibScalar
logMatchMaxEntries = _LogMatchMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 1),
    _LogMatchMaxEntries_Type()
)
logMatchMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchMaxEntries.setStatus("current")
if mibBuilder.loadTexts:
    logMatchMaxEntries.setDescription("The maximum number of logmatch entries this snmpd daemon can support.")
_LogMatchTable_Object = MibTable
logMatchTable = _LogMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2)
)
if mibBuilder.loadTexts:
    logMatchTable.setStatus("current")
if mibBuilder.loadTexts:
    logMatchTable.setDescription("Table of monitored files.")
_LogMatchEntry_Object = MibTableRow
logMatchEntry = _LogMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1)
)
logMatchEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "logMatchIndex"),
)
if mibBuilder.loadTexts:
    logMatchEntry.setStatus("current")
if mibBuilder.loadTexts:
    logMatchEntry.setDescription("Entry of file")


class _LogMatchIndex_Type(Integer32):
    """Custom type logMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogMatchIndex_Type.__name__ = "Integer32"
_LogMatchIndex_Object = MibTableColumn
logMatchIndex = _LogMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 1),
    _LogMatchIndex_Type()
)
logMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchIndex.setStatus("current")
if mibBuilder.loadTexts:
    logMatchIndex.setDescription("Index of logmatch")
_LogMatchName_Type = DisplayString
_LogMatchName_Object = MibTableColumn
logMatchName = _LogMatchName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 2),
    _LogMatchName_Type()
)
logMatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchName.setStatus("current")
if mibBuilder.loadTexts:
    logMatchName.setDescription("logmatch instance name")
_LogMatchFilename_Type = DisplayString
_LogMatchFilename_Object = MibTableColumn
logMatchFilename = _LogMatchFilename_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 3),
    _LogMatchFilename_Type()
)
logMatchFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchFilename.setStatus("current")
if mibBuilder.loadTexts:
    logMatchFilename.setDescription("filename to be logmatched")
_LogMatchRegEx_Type = DisplayString
_LogMatchRegEx_Object = MibTableColumn
logMatchRegEx = _LogMatchRegEx_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 4),
    _LogMatchRegEx_Type()
)
logMatchRegEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchRegEx.setStatus("current")
if mibBuilder.loadTexts:
    logMatchRegEx.setDescription("regular expression")
_LogMatchGlobalCounter_Type = Counter32
_LogMatchGlobalCounter_Object = MibTableColumn
logMatchGlobalCounter = _LogMatchGlobalCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 5),
    _LogMatchGlobalCounter_Type()
)
logMatchGlobalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchGlobalCounter.setStatus("current")
if mibBuilder.loadTexts:
    logMatchGlobalCounter.setDescription("global count of matches")
_LogMatchGlobalCount_Type = Integer32
_LogMatchGlobalCount_Object = MibTableColumn
logMatchGlobalCount = _LogMatchGlobalCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 6),
    _LogMatchGlobalCount_Type()
)
logMatchGlobalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchGlobalCount.setStatus("current")
if mibBuilder.loadTexts:
    logMatchGlobalCount.setDescription("Description.")
_LogMatchCurrentCounter_Type = Counter32
_LogMatchCurrentCounter_Object = MibTableColumn
logMatchCurrentCounter = _LogMatchCurrentCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 7),
    _LogMatchCurrentCounter_Type()
)
logMatchCurrentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCurrentCounter.setStatus("current")
if mibBuilder.loadTexts:
    logMatchCurrentCounter.setDescription("Regex match counter. This counter will be reset with each logfile rotation.")
_LogMatchCurrentCount_Type = Integer32
_LogMatchCurrentCount_Object = MibTableColumn
logMatchCurrentCount = _LogMatchCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 8),
    _LogMatchCurrentCount_Type()
)
logMatchCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCurrentCount.setStatus("current")
if mibBuilder.loadTexts:
    logMatchCurrentCount.setDescription("Description.")
_LogMatchCounter_Type = Counter32
_LogMatchCounter_Object = MibTableColumn
logMatchCounter = _LogMatchCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 9),
    _LogMatchCounter_Type()
)
logMatchCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCounter.setStatus("current")
if mibBuilder.loadTexts:
    logMatchCounter.setDescription("Regex match counter. This counter will be reset with each read")
_LogMatchCount_Type = Integer32
_LogMatchCount_Object = MibTableColumn
logMatchCount = _LogMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 10),
    _LogMatchCount_Type()
)
logMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCount.setStatus("current")
if mibBuilder.loadTexts:
    logMatchCount.setDescription("Description.")
_LogMatchCycle_Type = Integer32
_LogMatchCycle_Object = MibTableColumn
logMatchCycle = _LogMatchCycle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 11),
    _LogMatchCycle_Type()
)
logMatchCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCycle.setStatus("current")
if mibBuilder.loadTexts:
    logMatchCycle.setDescription("time between updates (if not queried) in seconds")
_LogMatchErrorFlag_Type = UCDErrorFlag
_LogMatchErrorFlag_Object = MibTableColumn
logMatchErrorFlag = _LogMatchErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 100),
    _LogMatchErrorFlag_Type()
)
logMatchErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    logMatchErrorFlag.setDescription("errorflag: is this line configured correctly?")
_LogMatchRegExCompilation_Type = DisplayString
_LogMatchRegExCompilation_Object = MibTableColumn
logMatchRegExCompilation = _LogMatchRegExCompilation_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 101),
    _LogMatchRegExCompilation_Type()
)
logMatchRegExCompilation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchRegExCompilation.setStatus("current")
if mibBuilder.loadTexts:
    logMatchRegExCompilation.setDescription("message of regex precompilation")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 100)
)
_VersionIndex_Type = Integer32
_VersionIndex_Object = MibScalar
versionIndex = _VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 1),
    _VersionIndex_Type()
)
versionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionIndex.setStatus("current")
if mibBuilder.loadTexts:
    versionIndex.setDescription("Index to mib (always 0)")
_VersionTag_Type = DisplayString
_VersionTag_Object = MibScalar
versionTag = _VersionTag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 2),
    _VersionTag_Type()
)
versionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionTag.setStatus("current")
if mibBuilder.loadTexts:
    versionTag.setDescription("CVS tag keyword")
_VersionDate_Type = DisplayString
_VersionDate_Object = MibScalar
versionDate = _VersionDate_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 3),
    _VersionDate_Type()
)
versionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionDate.setStatus("current")
if mibBuilder.loadTexts:
    versionDate.setDescription("Date string from RCS keyword")
_VersionCDate_Type = DisplayString
_VersionCDate_Object = MibScalar
versionCDate = _VersionCDate_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 4),
    _VersionCDate_Type()
)
versionCDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionCDate.setStatus("current")
if mibBuilder.loadTexts:
    versionCDate.setDescription("Date string from ctime() ")
_VersionIdent_Type = DisplayString
_VersionIdent_Object = MibScalar
versionIdent = _VersionIdent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 5),
    _VersionIdent_Type()
)
versionIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionIdent.setStatus("current")
if mibBuilder.loadTexts:
    versionIdent.setDescription("Id string from RCS keyword")
_VersionConfigureOptions_Type = DisplayString
_VersionConfigureOptions_Object = MibScalar
versionConfigureOptions = _VersionConfigureOptions_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 6),
    _VersionConfigureOptions_Type()
)
versionConfigureOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionConfigureOptions.setStatus("current")
if mibBuilder.loadTexts:
    versionConfigureOptions.setDescription("Options passed to the configure script when this agent was built.")
_VersionClearCache_Type = Integer32
_VersionClearCache_Object = MibScalar
versionClearCache = _VersionClearCache_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 10),
    _VersionClearCache_Type()
)
versionClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionClearCache.setStatus("current")
if mibBuilder.loadTexts:
    versionClearCache.setDescription("Set to 1 to clear the exec cache, if enabled")
_VersionUpdateConfig_Type = Integer32
_VersionUpdateConfig_Object = MibScalar
versionUpdateConfig = _VersionUpdateConfig_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 11),
    _VersionUpdateConfig_Type()
)
versionUpdateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionUpdateConfig.setStatus("current")
if mibBuilder.loadTexts:
    versionUpdateConfig.setDescription("Set to 1 to read-read the config file(s).")
_VersionRestartAgent_Type = Integer32
_VersionRestartAgent_Object = MibScalar
versionRestartAgent = _VersionRestartAgent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 12),
    _VersionRestartAgent_Type()
)
versionRestartAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionRestartAgent.setStatus("current")
if mibBuilder.loadTexts:
    versionRestartAgent.setDescription("Set to 1 to restart the agent.")
_VersionSavePersistentData_Type = Integer32
_VersionSavePersistentData_Object = MibScalar
versionSavePersistentData = _VersionSavePersistentData_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 13),
    _VersionSavePersistentData_Type()
)
versionSavePersistentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionSavePersistentData.setStatus("current")
if mibBuilder.loadTexts:
    versionSavePersistentData.setDescription("Set to 1 to force the agent to save it's persistent data immediately.")
_VersionDoDebugging_Type = Integer32
_VersionDoDebugging_Object = MibScalar
versionDoDebugging = _VersionDoDebugging_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 20),
    _VersionDoDebugging_Type()
)
versionDoDebugging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionDoDebugging.setStatus("current")
if mibBuilder.loadTexts:
    versionDoDebugging.setDescription("Set to 1 to turn debugging statements on in the agent or 0 to turn it off.")
_Snmperrs_ObjectIdentity = ObjectIdentity
snmperrs = _Snmperrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 101)
)
_SnmperrIndex_Type = Integer32
_SnmperrIndex_Object = MibScalar
snmperrIndex = _SnmperrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 1),
    _SnmperrIndex_Type()
)
snmperrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrIndex.setStatus("current")
if mibBuilder.loadTexts:
    snmperrIndex.setDescription("Bogus Index for snmperrs (always 0).")
_SnmperrNames_Type = DisplayString
_SnmperrNames_Object = MibScalar
snmperrNames = _SnmperrNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 2),
    _SnmperrNames_Type()
)
snmperrNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrNames.setStatus("current")
if mibBuilder.loadTexts:
    snmperrNames.setDescription("snmp")
_SnmperrErrorFlag_Type = UCDErrorFlag
_SnmperrErrorFlag_Object = MibScalar
snmperrErrorFlag = _SnmperrErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 100),
    _SnmperrErrorFlag_Type()
)
snmperrErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrErrorFlag.setStatus("current")
if mibBuilder.loadTexts:
    snmperrErrorFlag.setDescription("A Error flag to indicate trouble with the agent. It goes to 1 if there is an error, 0 if no error.")
_SnmperrErrMessage_Type = DisplayString
_SnmperrErrMessage_Object = MibScalar
snmperrErrMessage = _SnmperrErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 101),
    _SnmperrErrMessage_Type()
)
snmperrErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrErrMessage.setStatus("current")
if mibBuilder.loadTexts:
    snmperrErrMessage.setDescription("An error message describing the problem (if one exists).")
_MrTable_Object = MibTable
mrTable = _MrTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102)
)
if mibBuilder.loadTexts:
    mrTable.setStatus("current")
if mibBuilder.loadTexts:
    mrTable.setDescription("A table displaying all the oid's registered by mib modules in the agent. Since the agent is modular in nature, this lists each module's OID it is responsible for and the name of the module")
_MrEntry_Object = MibTableRow
mrEntry = _MrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1)
)
mrEntry.setIndexNames(
    (1, "UCD-SNMP-MIB", "mrIndex"),
)
if mibBuilder.loadTexts:
    mrEntry.setStatus("current")
if mibBuilder.loadTexts:
    mrEntry.setDescription("An entry containing a registered mib oid.")
_MrIndex_Type = ObjectIdentifier
_MrIndex_Object = MibTableColumn
mrIndex = _MrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1, 1),
    _MrIndex_Type()
)
mrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrIndex.setStatus("current")
if mibBuilder.loadTexts:
    mrIndex.setDescription("The registry slot of a mibmodule.")
_MrModuleName_Type = DisplayString
_MrModuleName_Object = MibTableColumn
mrModuleName = _MrModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1, 2),
    _MrModuleName_Type()
)
mrModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrModuleName.setStatus("current")
if mibBuilder.loadTexts:
    mrModuleName.setDescription("The module name that registered this OID.")
_UcdSnmpAgent_ObjectIdentity = ObjectIdentity
ucdSnmpAgent = _UcdSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250)
)
_Hpux9_ObjectIdentity = ObjectIdentity
hpux9 = _Hpux9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 1)
)
_Sunos4_ObjectIdentity = ObjectIdentity
sunos4 = _Sunos4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 2)
)
_Solaris_ObjectIdentity = ObjectIdentity
solaris = _Solaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 3)
)
_Osf_ObjectIdentity = ObjectIdentity
osf = _Osf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 4)
)
_Ultrix_ObjectIdentity = ObjectIdentity
ultrix = _Ultrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 5)
)
_Hpux10_ObjectIdentity = ObjectIdentity
hpux10 = _Hpux10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 6)
)
_Netbsd1_ObjectIdentity = ObjectIdentity
netbsd1 = _Netbsd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 7)
)
_Freebsd_ObjectIdentity = ObjectIdentity
freebsd = _Freebsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 8)
)
_Irix_ObjectIdentity = ObjectIdentity
irix = _Irix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 9)
)
_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 10)
)
_Bsdi_ObjectIdentity = ObjectIdentity
bsdi = _Bsdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 11)
)
_Openbsd_ObjectIdentity = ObjectIdentity
openbsd = _Openbsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 12)
)
_Win32_ObjectIdentity = ObjectIdentity
win32 = _Win32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 13)
)
_Hpux11_ObjectIdentity = ObjectIdentity
hpux11 = _Hpux11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 14)
)
_Aix_ObjectIdentity = ObjectIdentity
aix = _Aix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 15)
)
_Macosx_ObjectIdentity = ObjectIdentity
macosx = _Macosx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 16)
)
_Dragonfly_ObjectIdentity = ObjectIdentity
dragonfly = _Dragonfly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 17)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 255)
)
_UcdTraps_ObjectIdentity = ObjectIdentity
ucdTraps = _UcdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 251)
)

# Managed Objects groups


# Notification objects

ucdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2021, 251, 1)
)
if mibBuilder.loadTexts:
    ucdStart.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ucdStart.setDescription("This trap could in principle be sent when the agent start")

ucdShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2021, 251, 2)
)
if mibBuilder.loadTexts:
    ucdShutdown.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ucdShutdown.setDescription("This trap is sent when the agent terminates")


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "UCD-SNMP-MIB",
    **{"Float": Float,
       "UCDErrorFlag": UCDErrorFlag,
       "UCDErrorFix": UCDErrorFix,
       "ucdavis": ucdavis,
       "prTable": prTable,
       "prEntry": prEntry,
       "prIndex": prIndex,
       "prNames": prNames,
       "prMin": prMin,
       "prMax": prMax,
       "prCount": prCount,
       "prErrorFlag": prErrorFlag,
       "prErrMessage": prErrMessage,
       "prErrFix": prErrFix,
       "prErrFixCmd": prErrFixCmd,
       "memory": memory,
       "memIndex": memIndex,
       "memErrorName": memErrorName,
       "memTotalSwap": memTotalSwap,
       "memAvailSwap": memAvailSwap,
       "memTotalReal": memTotalReal,
       "memAvailReal": memAvailReal,
       "memTotalSwapTXT": memTotalSwapTXT,
       "memAvailSwapTXT": memAvailSwapTXT,
       "memTotalRealTXT": memTotalRealTXT,
       "memAvailRealTXT": memAvailRealTXT,
       "memTotalFree": memTotalFree,
       "memMinimumSwap": memMinimumSwap,
       "memShared": memShared,
       "memBuffer": memBuffer,
       "memCached": memCached,
       "memUsedSwapTXT": memUsedSwapTXT,
       "memUsedRealTXT": memUsedRealTXT,
       "memTotalSwapX": memTotalSwapX,
       "memAvailSwapX": memAvailSwapX,
       "memTotalRealX": memTotalRealX,
       "memAvailRealX": memAvailRealX,
       "memTotalFreeX": memTotalFreeX,
       "memMinimumSwapX": memMinimumSwapX,
       "memSharedX": memSharedX,
       "memBufferX": memBufferX,
       "memCachedX": memCachedX,
       "memSwapError": memSwapError,
       "memSwapErrorMsg": memSwapErrorMsg,
       "extTable": extTable,
       "extEntry": extEntry,
       "extIndex": extIndex,
       "extNames": extNames,
       "extCommand": extCommand,
       "extResult": extResult,
       "extOutput": extOutput,
       "extErrFix": extErrFix,
       "extErrFixCmd": extErrFixCmd,
       "dskTable": dskTable,
       "dskEntry": dskEntry,
       "dskIndex": dskIndex,
       "dskPath": dskPath,
       "dskDevice": dskDevice,
       "dskMinimum": dskMinimum,
       "dskMinPercent": dskMinPercent,
       "dskTotal": dskTotal,
       "dskAvail": dskAvail,
       "dskUsed": dskUsed,
       "dskPercent": dskPercent,
       "dskPercentNode": dskPercentNode,
       "dskTotalLow": dskTotalLow,
       "dskTotalHigh": dskTotalHigh,
       "dskAvailLow": dskAvailLow,
       "dskAvailHigh": dskAvailHigh,
       "dskUsedLow": dskUsedLow,
       "dskUsedHigh": dskUsedHigh,
       "dskErrorFlag": dskErrorFlag,
       "dskErrorMsg": dskErrorMsg,
       "laTable": laTable,
       "laEntry": laEntry,
       "laIndex": laIndex,
       "laNames": laNames,
       "laLoad": laLoad,
       "laConfig": laConfig,
       "laLoadInt": laLoadInt,
       "laLoadFloat": laLoadFloat,
       "laErrorFlag": laErrorFlag,
       "laErrMessage": laErrMessage,
       "systemStats": systemStats,
       "ssIndex": ssIndex,
       "ssErrorName": ssErrorName,
       "ssSwapIn": ssSwapIn,
       "ssSwapOut": ssSwapOut,
       "ssIOSent": ssIOSent,
       "ssIOReceive": ssIOReceive,
       "ssSysInterrupts": ssSysInterrupts,
       "ssSysContext": ssSysContext,
       "ssCpuUser": ssCpuUser,
       "ssCpuSystem": ssCpuSystem,
       "ssCpuIdle": ssCpuIdle,
       "ssCpuRawUser": ssCpuRawUser,
       "ssCpuRawNice": ssCpuRawNice,
       "ssCpuRawSystem": ssCpuRawSystem,
       "ssCpuRawIdle": ssCpuRawIdle,
       "ssCpuRawWait": ssCpuRawWait,
       "ssCpuRawKernel": ssCpuRawKernel,
       "ssCpuRawInterrupt": ssCpuRawInterrupt,
       "ssIORawSent": ssIORawSent,
       "ssIORawReceived": ssIORawReceived,
       "ssRawInterrupts": ssRawInterrupts,
       "ssRawContexts": ssRawContexts,
       "ssCpuRawSoftIRQ": ssCpuRawSoftIRQ,
       "ssRawSwapIn": ssRawSwapIn,
       "ssRawSwapOut": ssRawSwapOut,
       "ssCpuRawSteal": ssCpuRawSteal,
       "ssCpuRawGuest": ssCpuRawGuest,
       "ssCpuRawGuestNice": ssCpuRawGuestNice,
       "ssCpuNumCpus": ssCpuNumCpus,
       "ucdInternal": ucdInternal,
       "ucdExperimental": ucdExperimental,
       "fileTable": fileTable,
       "fileEntry": fileEntry,
       "fileIndex": fileIndex,
       "fileName": fileName,
       "fileSize": fileSize,
       "fileMax": fileMax,
       "fileErrorFlag": fileErrorFlag,
       "fileErrorMsg": fileErrorMsg,
       "logMatch": logMatch,
       "logMatchMaxEntries": logMatchMaxEntries,
       "logMatchTable": logMatchTable,
       "logMatchEntry": logMatchEntry,
       "logMatchIndex": logMatchIndex,
       "logMatchName": logMatchName,
       "logMatchFilename": logMatchFilename,
       "logMatchRegEx": logMatchRegEx,
       "logMatchGlobalCounter": logMatchGlobalCounter,
       "logMatchGlobalCount": logMatchGlobalCount,
       "logMatchCurrentCounter": logMatchCurrentCounter,
       "logMatchCurrentCount": logMatchCurrentCount,
       "logMatchCounter": logMatchCounter,
       "logMatchCount": logMatchCount,
       "logMatchCycle": logMatchCycle,
       "logMatchErrorFlag": logMatchErrorFlag,
       "logMatchRegExCompilation": logMatchRegExCompilation,
       "version": version,
       "versionIndex": versionIndex,
       "versionTag": versionTag,
       "versionDate": versionDate,
       "versionCDate": versionCDate,
       "versionIdent": versionIdent,
       "versionConfigureOptions": versionConfigureOptions,
       "versionClearCache": versionClearCache,
       "versionUpdateConfig": versionUpdateConfig,
       "versionRestartAgent": versionRestartAgent,
       "versionSavePersistentData": versionSavePersistentData,
       "versionDoDebugging": versionDoDebugging,
       "snmperrs": snmperrs,
       "snmperrIndex": snmperrIndex,
       "snmperrNames": snmperrNames,
       "snmperrErrorFlag": snmperrErrorFlag,
       "snmperrErrMessage": snmperrErrMessage,
       "mrTable": mrTable,
       "mrEntry": mrEntry,
       "mrIndex": mrIndex,
       "mrModuleName": mrModuleName,
       "ucdSnmpAgent": ucdSnmpAgent,
       "hpux9": hpux9,
       "sunos4": sunos4,
       "solaris": solaris,
       "osf": osf,
       "ultrix": ultrix,
       "hpux10": hpux10,
       "netbsd1": netbsd1,
       "freebsd": freebsd,
       "irix": irix,
       "linux": linux,
       "bsdi": bsdi,
       "openbsd": openbsd,
       "win32": win32,
       "hpux11": hpux11,
       "aix": aix,
       "macosx": macosx,
       "dragonfly": dragonfly,
       "unknown": unknown,
       "ucdTraps": ucdTraps,
       "ucdStart": ucdStart,
       "ucdShutdown": ucdShutdown}
)
