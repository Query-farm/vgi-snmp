# SNMP MIB module (NET-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/NET-SNMP-AGENT-MIB
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

(netSnmpGroups,
 netSnmpModuleIDs,
 netSnmpNotifications,
 netSnmpObjects) = mibBuilder.import_symbols(
    "NET-SNMP-MIB",
    "netSnmpGroups",
    "netSnmpModuleIDs",
    "netSnmpNotifications",
    "netSnmpObjects")

(SnmpAdminString,) = mibBuilder.import_symbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 NotificationType,
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
    "NotificationType",
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
 TextualConvention,
 TruthValue) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netSnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 2)
)
if mibBuilder.loadTexts:
    netSnmpAgentMIB.setRevisions(
        ("2010-03-17 00:00",
         "2005-02-07 00:00",
         "2002-02-09 00:00")
    )
if mibBuilder.loadTexts:
    netSnmpAgentMIB.setLastUpdated("201003170000Z")
if mibBuilder.loadTexts:
    netSnmpAgentMIB.setOrganization("www.net-snmp.org")
if mibBuilder.loadTexts:
    netSnmpAgentMIB.setContactInfo("postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts:
    netSnmpAgentMIB.setDescription("Defines control and monitoring structures for the Net-SNMP agent.")


# Types definitions


# TEXTUAL-CONVENTIONS



class NetsnmpCacheStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("enabled", 1),
          ("disabled", 2),
          ("empty", 3),
          ("cached", 4),
          ("expired", 5))
    )

    if mibBuilder.loadTexts:
        description = "an indication of the status of data caching entries"


# MIB Managed Objects in the order of their OIDs

_NsVersion_ObjectIdentity = ObjectIdentity
nsVersion = _NsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 1)
)
_NsMibRegistry_ObjectIdentity = ObjectIdentity
nsMibRegistry = _NsMibRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2)
)
_NsModuleTable_Object = MibTable
nsModuleTable = _NsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nsModuleTable.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleTable.setDescription("A table displaying all the oid's registered by mib modules in the agent. Since the agent is modular in nature, this lists each module's OID it is responsible for and the name of the module")
_NsModuleEntry_Object = MibTableRow
nsModuleEntry = _NsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1)
)
nsModuleEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsmContextName"),
    (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPoint"),
    (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPriority"),
)
if mibBuilder.loadTexts:
    nsModuleEntry.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleEntry.setDescription("An entry containing a registered mib oid.")
_NsmContextName_Type = SnmpAdminString
_NsmContextName_Object = MibTableColumn
nsmContextName = _NsmContextName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 1),
    _NsmContextName_Type()
)
nsmContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmContextName.setStatus("current")
if mibBuilder.loadTexts:
    nsmContextName.setDescription("The context name the module is registered under.")
_NsmRegistrationPoint_Type = ObjectIdentifier
_NsmRegistrationPoint_Object = MibTableColumn
nsmRegistrationPoint = _NsmRegistrationPoint_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 2),
    _NsmRegistrationPoint_Type()
)
nsmRegistrationPoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmRegistrationPoint.setStatus("current")
if mibBuilder.loadTexts:
    nsmRegistrationPoint.setDescription("The registry OID of a mib module.")


class _NsmRegistrationPriority_Type(Integer32):
    """Custom type nsmRegistrationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NsmRegistrationPriority_Type.__name__ = "Integer32"
_NsmRegistrationPriority_Object = MibTableColumn
nsmRegistrationPriority = _NsmRegistrationPriority_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 3),
    _NsmRegistrationPriority_Type()
)
nsmRegistrationPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmRegistrationPriority.setStatus("current")
if mibBuilder.loadTexts:
    nsmRegistrationPriority.setDescription("The priority of the registered mib module.")
_NsModuleName_Type = DisplayString
_NsModuleName_Object = MibTableColumn
nsModuleName = _NsModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 4),
    _NsModuleName_Type()
)
nsModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleName.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleName.setDescription("The module name that registered this OID.")


class _NsModuleModes_Type(Bits):
    """Custom type nsModuleModes based on Bits"""
    namedValues = NamedValues(
        *(("getAndGetNext", 0),
          ("set", 1),
          ("getBulk", 2))
    )

_NsModuleModes_Type.__name__ = "Bits"
_NsModuleModes_Object = MibTableColumn
nsModuleModes = _NsModuleModes_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 5),
    _NsModuleModes_Type()
)
nsModuleModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleModes.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleModes.setDescription("The modes that the particular lower level handler can cope with directly.")
_NsModuleTimeout_Type = Integer32
_NsModuleTimeout_Object = MibTableColumn
nsModuleTimeout = _NsModuleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 6),
    _NsModuleTimeout_Type()
)
nsModuleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleTimeout.setDescription("The registered timeout. This is only meaningful for handlers that expect to return results at a later date (subagents, etc)")
_NsExtensions_ObjectIdentity = ObjectIdentity
nsExtensions = _NsExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3)
)
_NsDLMod_ObjectIdentity = ObjectIdentity
nsDLMod = _NsDLMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 4)
)
_NsCache_ObjectIdentity = ObjectIdentity
nsCache = _NsCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5)
)


class _NsCacheDefaultTimeout_Type(Integer32):
    """Custom type nsCacheDefaultTimeout based on Integer32"""
    defaultValue = 5


_NsCacheDefaultTimeout_Type.__name__ = "Integer32"
_NsCacheDefaultTimeout_Object = MibScalar
nsCacheDefaultTimeout = _NsCacheDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 1),
    _NsCacheDefaultTimeout_Type()
)
nsCacheDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheDefaultTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheDefaultTimeout.setDescription("Default cache timeout value (unless overridden for a particular cache entry).")


class _NsCacheEnabled_Type(TruthValue):
    """Custom type nsCacheEnabled based on TruthValue"""
    defaultValue = 1


_NsCacheEnabled_Type.__name__ = "TruthValue"
_NsCacheEnabled_Object = MibScalar
nsCacheEnabled = _NsCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 2),
    _NsCacheEnabled_Type()
)
nsCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheEnabled.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheEnabled.setDescription("Whether data caching is active overall.")
_NsCacheTable_Object = MibTable
nsCacheTable = _NsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3)
)
if mibBuilder.loadTexts:
    nsCacheTable.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheTable.setDescription("A table of individual MIB module data caches.")
_NsCacheEntry_Object = MibTableRow
nsCacheEntry = _NsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1)
)
nsCacheEntry.setIndexNames(
    (1, "NET-SNMP-AGENT-MIB", "nsCachedOID"),
)
if mibBuilder.loadTexts:
    nsCacheEntry.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheEntry.setDescription("A conceptual row within the cache table.")
_NsCachedOID_Type = ObjectIdentifier
_NsCachedOID_Object = MibTableColumn
nsCachedOID = _NsCachedOID_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 1),
    _NsCachedOID_Type()
)
nsCachedOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCachedOID.setStatus("current")
if mibBuilder.loadTexts:
    nsCachedOID.setDescription("The root OID of the data being cached.")
_NsCacheTimeout_Type = Integer32
_NsCacheTimeout_Object = MibTableColumn
nsCacheTimeout = _NsCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 2),
    _NsCacheTimeout_Type()
)
nsCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheTimeout.setDescription("The length of time (?in seconds) for which the data in this particular cache entry will remain valid.")
_NsCacheStatus_Type = NetsnmpCacheStatus
_NsCacheStatus_Object = MibTableColumn
nsCacheStatus = _NsCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 3),
    _NsCacheStatus_Type()
)
nsCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheStatus.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheStatus.setDescription("The current status of this particular cache entry. Acceptable values for Set requests are 'enabled(1)', 'disabled(2)' or 'empty(3)' (to clear all cached data). Requests to read the value of such an object will return 'disabled(2)' through to 'expired(5)'.")
_NsErrorHistory_ObjectIdentity = ObjectIdentity
nsErrorHistory = _NsErrorHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 6)
)
_NsConfiguration_ObjectIdentity = ObjectIdentity
nsConfiguration = _NsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7)
)
_NsConfigDebug_ObjectIdentity = ObjectIdentity
nsConfigDebug = _NsConfigDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1)
)


class _NsDebugEnabled_Type(TruthValue):
    """Custom type nsDebugEnabled based on TruthValue"""
    defaultValue = 2


_NsDebugEnabled_Type.__name__ = "TruthValue"
_NsDebugEnabled_Object = MibScalar
nsDebugEnabled = _NsDebugEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 1),
    _NsDebugEnabled_Type()
)
nsDebugEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugEnabled.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugEnabled.setDescription("Whether the agent is configured to generate debugging output")


class _NsDebugOutputAll_Type(TruthValue):
    """Custom type nsDebugOutputAll based on TruthValue"""
    defaultValue = 2


_NsDebugOutputAll_Type.__name__ = "TruthValue"
_NsDebugOutputAll_Object = MibScalar
nsDebugOutputAll = _NsDebugOutputAll_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 2),
    _NsDebugOutputAll_Type()
)
nsDebugOutputAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugOutputAll.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugOutputAll.setDescription("Whether the agent is configured to display all debugging output rather than filtering on individual debug tokens. Nothing will be generated unless nsDebugEnabled is also true(1)")


class _NsDebugDumpPdu_Type(TruthValue):
    """Custom type nsDebugDumpPdu based on TruthValue"""
    defaultValue = 2


_NsDebugDumpPdu_Type.__name__ = "TruthValue"
_NsDebugDumpPdu_Object = MibScalar
nsDebugDumpPdu = _NsDebugDumpPdu_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 3),
    _NsDebugDumpPdu_Type()
)
nsDebugDumpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugDumpPdu.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugDumpPdu.setDescription("Whether the agent is configured to display raw packet dumps. This is unrelated to the nsDebugEnabled setting.")
_NsDebugTokenTable_Object = MibTable
nsDebugTokenTable = _NsDebugTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    nsDebugTokenTable.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugTokenTable.setDescription("A table of individual debug tokens, used to control the selection of what debugging output should be produced. This table is only effective if nsDebugOutputAll is false(2), and nothing will be generated unless nsDebugEnabled is also true(1)")
_NsDebugTokenEntry_Object = MibTableRow
nsDebugTokenEntry = _NsDebugTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1)
)
nsDebugTokenEntry.setIndexNames(
    (1, "NET-SNMP-AGENT-MIB", "nsDebugTokenPrefix"),
)
if mibBuilder.loadTexts:
    nsDebugTokenEntry.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugTokenEntry.setDescription("A conceptual row within the debug token table.")
_NsDebugTokenPrefix_Type = DisplayString
_NsDebugTokenPrefix_Object = MibTableColumn
nsDebugTokenPrefix = _NsDebugTokenPrefix_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 2),
    _NsDebugTokenPrefix_Type()
)
nsDebugTokenPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsDebugTokenPrefix.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugTokenPrefix.setDescription("A token prefix for which to generate the corresponding debugging output. Note that debug output will be generated for all registered debug statements sharing this prefix (rather than an exact match). Nothing will be generated unless both nsDebuggingEnabled is set true(1) and the corresponding nsDebugTokenStatus value is active(1).")
_NsDebugTokenStatus_Type = RowStatus
_NsDebugTokenStatus_Object = MibTableColumn
nsDebugTokenStatus = _NsDebugTokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 4),
    _NsDebugTokenStatus_Type()
)
nsDebugTokenStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsDebugTokenStatus.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugTokenStatus.setDescription("Whether to generate debug output for the corresponding debug token prefix. Nothing will be generated unless both nsDebuggingEnabled is true(1) and this instance is active(1). Note that is valid for an instance to be left with the value notInService(2) indefinitely - i.e. the meaning of 'abnormally long' (see RFC 2579, RowStatus) for this table is infinite.")
_NsConfigLogging_ObjectIdentity = ObjectIdentity
nsConfigLogging = _NsConfigLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2)
)
_NsLoggingTable_Object = MibTable
nsLoggingTable = _NsLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nsLoggingTable.setStatus("current")
if mibBuilder.loadTexts:
    nsLoggingTable.setDescription("A table of individual logging output destinations, used to control where various levels of output from the agent should be directed.")
_NsLoggingEntry_Object = MibTableRow
nsLoggingEntry = _NsLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1)
)
nsLoggingEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsLogLevel"),
    (1, "NET-SNMP-AGENT-MIB", "nsLogToken"),
)
if mibBuilder.loadTexts:
    nsLoggingEntry.setStatus("current")
if mibBuilder.loadTexts:
    nsLoggingEntry.setDescription("A conceptual row within the logging table.")


class _NsLogLevel_Type(Integer32):
    """Custom type nsLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_NsLogLevel_Type.__name__ = "Integer32"
_NsLogLevel_Object = MibTableColumn
nsLogLevel = _NsLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 1),
    _NsLogLevel_Type()
)
nsLogLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsLogLevel.setStatus("current")
if mibBuilder.loadTexts:
    nsLogLevel.setDescription("The (minimum) priority level for which this logging entry should be applied.")
_NsLogToken_Type = DisplayString
_NsLogToken_Object = MibTableColumn
nsLogToken = _NsLogToken_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 2),
    _NsLogToken_Type()
)
nsLogToken.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsLogToken.setStatus("current")
if mibBuilder.loadTexts:
    nsLogToken.setDescription("A token for which to generate logging entries. Depending on the style of logging, this may either be simply an arbitrary token, or may have some particular meaning (such as the filename to log to).")


class _NsLogType_Type(Integer32):
    """Custom type nsLogType based on Integer32"""
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
        *(("stdout", 1),
          ("stderr", 2),
          ("file", 3),
          ("syslog", 4),
          ("callback", 5))
    )


_NsLogType_Type.__name__ = "Integer32"
_NsLogType_Object = MibTableColumn
nsLogType = _NsLogType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 3),
    _NsLogType_Type()
)
nsLogType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogType.setStatus("current")
if mibBuilder.loadTexts:
    nsLogType.setDescription("The type of logging for this entry.")


class _NsLogMaxLevel_Type(Integer32):
    """Custom type nsLogMaxLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_NsLogMaxLevel_Type.__name__ = "Integer32"
_NsLogMaxLevel_Object = MibTableColumn
nsLogMaxLevel = _NsLogMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 4),
    _NsLogMaxLevel_Type()
)
nsLogMaxLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogMaxLevel.setStatus("current")
if mibBuilder.loadTexts:
    nsLogMaxLevel.setDescription("The maximum priority level for which this logging entry should be applied.")
_NsLogStatus_Type = RowStatus
_NsLogStatus_Object = MibTableColumn
nsLogStatus = _NsLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 5),
    _NsLogStatus_Type()
)
nsLogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogStatus.setStatus("current")
if mibBuilder.loadTexts:
    nsLogStatus.setDescription("Whether to generate logging output for this entry. Note that is valid for an instance to be left with the value notInService(2) indefinitely - i.e. the meaning of 'abnormally long' (see RFC 2579, RowStatus) for this table is infinite.")
_NsTransactions_ObjectIdentity = ObjectIdentity
nsTransactions = _NsTransactions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8)
)
_NsTransactionTable_Object = MibTable
nsTransactionTable = _NsTransactionTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1)
)
if mibBuilder.loadTexts:
    nsTransactionTable.setStatus("current")
if mibBuilder.loadTexts:
    nsTransactionTable.setDescription("Lists currently outstanding transactions in the net-snmp agent. This includes requests to AgentX subagents, or proxied SNMP agents.")
_NsTransactionEntry_Object = MibTableRow
nsTransactionEntry = _NsTransactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1)
)
nsTransactionEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsTransactionID"),
)
if mibBuilder.loadTexts:
    nsTransactionEntry.setStatus("current")
if mibBuilder.loadTexts:
    nsTransactionEntry.setDescription("A row describing a given transaction.")


class _NsTransactionID_Type(Unsigned32):
    """Custom type nsTransactionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NsTransactionID_Type.__name__ = "Unsigned32"
_NsTransactionID_Object = MibTableColumn
nsTransactionID = _NsTransactionID_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 1),
    _NsTransactionID_Type()
)
nsTransactionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsTransactionID.setStatus("current")
if mibBuilder.loadTexts:
    nsTransactionID.setDescription("The internal identifier for a given transaction.")
_NsTransactionMode_Type = Integer32
_NsTransactionMode_Object = MibTableColumn
nsTransactionMode = _NsTransactionMode_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 2),
    _NsTransactionMode_Type()
)
nsTransactionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTransactionMode.setStatus("current")
if mibBuilder.loadTexts:
    nsTransactionMode.setDescription("The mode number for the current operation being performed.")
_NsConfigGroups_ObjectIdentity = ObjectIdentity
nsConfigGroups = _NsConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7)
)

# Managed Objects groups

nsModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 2)
)
nsModuleGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsModuleName"),
        ("NET-SNMP-AGENT-MIB", "nsModuleModes"),
        ("NET-SNMP-AGENT-MIB", "nsModuleTimeout"))
)
if mibBuilder.loadTexts:
    nsModuleGroup.setStatus("current")
if mibBuilder.loadTexts:
    nsModuleGroup.setDescription("The objects relating to the list of MIB modules registered with the Net-SNMP agent.")

nsCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 4)
)
nsCacheGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsCacheDefaultTimeout"),
        ("NET-SNMP-AGENT-MIB", "nsCacheEnabled"),
        ("NET-SNMP-AGENT-MIB", "nsCacheTimeout"),
        ("NET-SNMP-AGENT-MIB", "nsCacheStatus"))
)
if mibBuilder.loadTexts:
    nsCacheGroup.setStatus("current")
if mibBuilder.loadTexts:
    nsCacheGroup.setDescription("The objects relating to data caching in the Net-SNMP agent.")

nsDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 1)
)
nsDebugGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsDebugEnabled"),
        ("NET-SNMP-AGENT-MIB", "nsDebugOutputAll"),
        ("NET-SNMP-AGENT-MIB", "nsDebugDumpPdu"),
        ("NET-SNMP-AGENT-MIB", "nsDebugTokenStatus"))
)
if mibBuilder.loadTexts:
    nsDebugGroup.setStatus("current")
if mibBuilder.loadTexts:
    nsDebugGroup.setDescription("The objects relating to debug configuration in the Net-SNMP agent.")

nsLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 2)
)
nsLoggingGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsLogType"),
        ("NET-SNMP-AGENT-MIB", "nsLogMaxLevel"),
        ("NET-SNMP-AGENT-MIB", "nsLogStatus"))
)
if mibBuilder.loadTexts:
    nsLoggingGroup.setStatus("current")
if mibBuilder.loadTexts:
    nsLoggingGroup.setDescription("The objects relating to logging configuration in the Net-SNMP agent.")

nsTransactionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 8)
)
nsTransactionGroup.setObjects(
    ("NET-SNMP-AGENT-MIB", "nsTransactionMode")
)
if mibBuilder.loadTexts:
    nsTransactionGroup.setStatus("current")
if mibBuilder.loadTexts:
    nsTransactionGroup.setDescription("The objects relating to transaction monitoring in the Net-SNMP agent.")


# Notification objects

nsNotifyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 1)
)
if mibBuilder.loadTexts:
    nsNotifyStart.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    nsNotifyStart.setDescription("An indication that the agent has started running.")

nsNotifyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 2)
)
if mibBuilder.loadTexts:
    nsNotifyShutdown.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    nsNotifyShutdown.setDescription("An indication that the agent is in the process of being shut down.")

nsNotifyRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 3)
)
if mibBuilder.loadTexts:
    nsNotifyRestart.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    nsNotifyRestart.setDescription("An indication that the agent has been restarted. This does not imply anything about whether the configuration has changed or not (unlike the standard coldStart or warmStart traps)")


# Notifications groups

nsAgentNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 9)
)
nsAgentNotifyGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsNotifyStart"),
        ("NET-SNMP-AGENT-MIB", "nsNotifyShutdown"),
        ("NET-SNMP-AGENT-MIB", "nsNotifyRestart"))
)
if mibBuilder.loadTexts:
    nsAgentNotifyGroup.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    nsAgentNotifyGroup.setDescription("The notifications relating to the basic operation of the Net-SNMP agent.")


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "NET-SNMP-AGENT-MIB",
    **{"NetsnmpCacheStatus": NetsnmpCacheStatus,
       "nsVersion": nsVersion,
       "nsMibRegistry": nsMibRegistry,
       "nsModuleTable": nsModuleTable,
       "nsModuleEntry": nsModuleEntry,
       "nsmContextName": nsmContextName,
       "nsmRegistrationPoint": nsmRegistrationPoint,
       "nsmRegistrationPriority": nsmRegistrationPriority,
       "nsModuleName": nsModuleName,
       "nsModuleModes": nsModuleModes,
       "nsModuleTimeout": nsModuleTimeout,
       "nsExtensions": nsExtensions,
       "nsDLMod": nsDLMod,
       "nsCache": nsCache,
       "nsCacheDefaultTimeout": nsCacheDefaultTimeout,
       "nsCacheEnabled": nsCacheEnabled,
       "nsCacheTable": nsCacheTable,
       "nsCacheEntry": nsCacheEntry,
       "nsCachedOID": nsCachedOID,
       "nsCacheTimeout": nsCacheTimeout,
       "nsCacheStatus": nsCacheStatus,
       "nsErrorHistory": nsErrorHistory,
       "nsConfiguration": nsConfiguration,
       "nsConfigDebug": nsConfigDebug,
       "nsDebugEnabled": nsDebugEnabled,
       "nsDebugOutputAll": nsDebugOutputAll,
       "nsDebugDumpPdu": nsDebugDumpPdu,
       "nsDebugTokenTable": nsDebugTokenTable,
       "nsDebugTokenEntry": nsDebugTokenEntry,
       "nsDebugTokenPrefix": nsDebugTokenPrefix,
       "nsDebugTokenStatus": nsDebugTokenStatus,
       "nsConfigLogging": nsConfigLogging,
       "nsLoggingTable": nsLoggingTable,
       "nsLoggingEntry": nsLoggingEntry,
       "nsLogLevel": nsLogLevel,
       "nsLogToken": nsLogToken,
       "nsLogType": nsLogType,
       "nsLogMaxLevel": nsLogMaxLevel,
       "nsLogStatus": nsLogStatus,
       "nsTransactions": nsTransactions,
       "nsTransactionTable": nsTransactionTable,
       "nsTransactionEntry": nsTransactionEntry,
       "nsTransactionID": nsTransactionID,
       "nsTransactionMode": nsTransactionMode,
       "netSnmpAgentMIB": netSnmpAgentMIB,
       "nsNotifyStart": nsNotifyStart,
       "nsNotifyShutdown": nsNotifyShutdown,
       "nsNotifyRestart": nsNotifyRestart,
       "nsModuleGroup": nsModuleGroup,
       "nsCacheGroup": nsCacheGroup,
       "nsConfigGroups": nsConfigGroups,
       "nsDebugGroup": nsDebugGroup,
       "nsLoggingGroup": nsLoggingGroup,
       "nsTransactionGroup": nsTransactionGroup,
       "nsAgentNotifyGroup": nsAgentNotifyGroup}
)
