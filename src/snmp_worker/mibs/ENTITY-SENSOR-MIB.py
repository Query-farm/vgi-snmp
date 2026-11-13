# SNMP MIB module (ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/ENTITY-SENSOR-MIB
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

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.import_symbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

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
 TextualConvention,
 TimeStamp) = mibBuilder.import_symbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

entitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 99)
)
if mibBuilder.loadTexts:
    entitySensorMIB.setRevisions(
        ("2002-12-16 00:00",)
    )
if mibBuilder.loadTexts:
    entitySensorMIB.setLastUpdated("200212160000Z")
if mibBuilder.loadTexts:
    entitySensorMIB.setOrganization("IETF Entity MIB Working Group")
if mibBuilder.loadTexts:
    entitySensorMIB.setContactInfo(" Andy Bierman Cisco Systems, Inc. Tel: +1 408-527-3711 E-mail: abierman@cisco.com Postal: 170 West Tasman Drive San Jose, CA USA 95134 Dan Romascanu Avaya Inc. Tel: +972-3-645-8414 Email: dromasca@avaya.com Postal: Atidim technology Park, Bldg. #3 Tel Aviv, Israel, 61131 K.C. Norseth L-3 Communications Tel: +1 801-594-2809 Email: kenyon.c.norseth@L-3com.com Postal: 640 N. 2200 West. Salt Lake City, Utah 84116-0850 Send comments to <entmib@ietf.org> Mailing list subscription info: http://www.ietf.org/mailman/listinfo/entmib ")
if mibBuilder.loadTexts:
    entitySensorMIB.setDescription("This module defines Entity MIB extensions for physical sensors. Copyright (C) The Internet Society (2002). This version of this MIB module is part of RFC 3433; see the RFC itself for full legal notices.")


# Types definitions


# TEXTUAL-CONVENTIONS



class EntitySensorDataType(TextualConvention, Integer32):
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
          ("unknown", 2),
          ("voltsAC", 3),
          ("voltsDC", 4),
          ("amperes", 5),
          ("watts", 6),
          ("hertz", 7),
          ("celsius", 8),
          ("percentRH", 9),
          ("rpm", 10),
          ("cmm", 11),
          ("truthvalue", 12))
    )

    if mibBuilder.loadTexts:
        description = "An object using this data type represents the Entity Sensor measurement data type associated with a physical sensor value. The actual data units are determined by examining an object of this type together with the associated EntitySensorDataScale object. An object of this type SHOULD be defined together with objects of type EntitySensorDataScale and EntitySensorPrecision. Together, associated objects of these three types are used to identify the semantics of an object of type EntitySensorValue. Valid values are: other(1): a measure other than those listed below unknown(2): unknown measurement, or arbitrary, relative numbers voltsAC(3): electric potential voltsDC(4): electric potential amperes(5): electric current watts(6): power hertz(7): frequency celsius(8): temperature percentRH(9): percent relative humidity rpm(10): shaft revolutions per minute cmm(11),: cubic meters per minute (airflow) truthvalue(12): value takes { true(1), false(2) } "


class EntitySensorDataScale(TextualConvention, Integer32):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9),
          ("kilo", 10),
          ("mega", 11),
          ("giga", 12),
          ("tera", 13),
          ("exa", 14),
          ("peta", 15),
          ("zetta", 16),
          ("yotta", 17))
    )

    if mibBuilder.loadTexts:
        description = "An object using this data type represents a data scaling factor, represented with an International System of Units (SI) prefix. The actual data units are determined by examining an object of this type together with the associated EntitySensorDataType object. An object of this type SHOULD be defined together with objects of type EntitySensorDataType and EntitySensorPrecision. Together, associated objects of these three types are used to identify the semantics of an object of type EntitySensorValue."
    if mibBuilder.loadTexts:
        reference = "The International System of Units (SI), National Institute of Standards and Technology, Spec. Publ. 330, August 1991."


class EntitySensorPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )

    if mibBuilder.loadTexts:
        description = "An object using this data type represents a sensor precision range. An object of this type SHOULD be defined together with objects of type EntitySensorDataType and EntitySensorDataScale. Together, associated objects of these three types are used to identify the semantics of an object of type EntitySensorValue. If an object of this type contains a value in the range 1 to 9, it represents the number of decimal places in the fractional part of an associated EntitySensorValue fixed- point number. If an object of this type contains a value in the range -8 to -1, it represents the number of accurate digits in the associated EntitySensorValue fixed-point number. The value zero indicates the associated EntitySensorValue object is not a fixed-point number. Agent implementors must choose a value for the associated EntitySensorPrecision object so that the precision and accuracy of the associated EntitySensorValue object is correctly indicated. For example, a physical entity representing a temperature sensor that can measure 0 degrees to 100 degrees C in 0.1 degree increments, +/- 0.05 degrees, would have an EntitySensorPrecision value of '1', an EntitySensorDataScale value of 'units(9)', and an EntitySensorValue ranging from '0' to '1000'. The EntitySensorValue would be interpreted as 'degrees C * 10'."


class EntitySensorValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )

    if mibBuilder.loadTexts:
        description = "An object using this data type represents an Entity Sensor value. An object of this type SHOULD be defined together with objects of type EntitySensorDataType, EntitySensorDataScale and EntitySensorPrecision. Together, associated objects of those three types are used to identify the semantics of an object of this data type. The semantics of an object using this data type are determined by the value of the associated EntitySensorDataType object. If the associated EntitySensorDataType object is equal to 'voltsAC(3)', 'voltsDC(4)', 'amperes(5)', 'watts(6), 'hertz(7)', 'celsius(8)', or 'cmm(11)', then an object of this type MUST contain a fixed point number ranging from -999,999,999 to +999,999,999. The value -1000000000 indicates an underflow error. The value +1000000000 indicates an overflow error. The EntitySensorPrecision indicates how many fractional digits are represented in the associated EntitySensorValue object. If the associated EntitySensorDataType object is equal to 'percentRH(9)', then an object of this type MUST contain a number ranging from 0 to 100. If the associated EntitySensorDataType object is equal to 'rpm(10)', then an object of this type MUST contain a number ranging from -999,999,999 to +999,999,999. If the associated EntitySensorDataType object is equal to 'truthvalue(12)', then an object of this type MUST contain either the value 'true(1)' or the value 'false(2)'. If the associated EntitySensorDataType object is equal to 'other(1)' or unknown(2)', then an object of this type MUST contain a number ranging from -1000000000 to 1000000000."


class EntitySensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unavailable", 2),
          ("nonoperational", 3))
    )

    if mibBuilder.loadTexts:
        description = "An object using this data type represents the operational status of a physical sensor. The value 'ok(1)' indicates that the agent can obtain the sensor value. The value 'unavailable(2)' indicates that the agent presently cannot obtain the sensor value. The value 'nonoperational(3)' indicates that the agent believes the sensor is broken. The sensor could have a hard failure (disconnected wire), or a soft failure such as out- of-range, jittery, or wildly fluctuating readings."


# MIB Managed Objects in the order of their OIDs

_EntitySensorObjects_ObjectIdentity = ObjectIdentity
entitySensorObjects = _EntitySensorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 1)
)
_EntPhySensorTable_Object = MibTable
entPhySensorTable = _EntPhySensorTable_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1)
)
if mibBuilder.loadTexts:
    entPhySensorTable.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorTable.setDescription("This table contains one row per physical sensor represented by an associated row in the entPhysicalTable.")
_EntPhySensorEntry_Object = MibTableRow
entPhySensorEntry = _EntPhySensorEntry_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1)
)
entPhySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entPhySensorEntry.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorEntry.setDescription("Information about a particular physical sensor. An entry in this table describes the present reading of a sensor, the measurement units and scale, and sensor operational status. Entries are created in this table by the agent. An entry for each physical sensor SHOULD be created at the same time as the associated entPhysicalEntry. An entry SHOULD be destroyed if the associated entPhysicalEntry is destroyed.")
_EntPhySensorType_Type = EntitySensorDataType
_EntPhySensorType_Object = MibTableColumn
entPhySensorType = _EntPhySensorType_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1),
    _EntPhySensorType_Type()
)
entPhySensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorType.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorType.setDescription("The type of data returned by the associated entPhySensorValue object. This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation.")
_EntPhySensorScale_Type = EntitySensorDataScale
_EntPhySensorScale_Object = MibTableColumn
entPhySensorScale = _EntPhySensorScale_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2),
    _EntPhySensorScale_Type()
)
entPhySensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorScale.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorScale.setDescription("The exponent to apply to values returned by the associated entPhySensorValue object. This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation.")
_EntPhySensorPrecision_Type = EntitySensorPrecision
_EntPhySensorPrecision_Object = MibTableColumn
entPhySensorPrecision = _EntPhySensorPrecision_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3),
    _EntPhySensorPrecision_Type()
)
entPhySensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorPrecision.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorPrecision.setDescription("The number of decimal places of precision in fixed-point sensor values returned by the associated entPhySensorValue object. This object SHOULD be set to '0' when the associated entPhySensorType value is not a fixed-point type: e.g., 'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'. This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation.")
_EntPhySensorValue_Type = EntitySensorValue
_EntPhySensorValue_Object = MibTableColumn
entPhySensorValue = _EntPhySensorValue_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4),
    _EntPhySensorValue_Type()
)
entPhySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValue.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValue.setDescription("The most recent measurement obtained by the agent for this sensor. To correctly interpret the value of this object, the associated entPhySensorType, entPhySensorScale, and entPhySensorPrecision objects must also be examined.")
_EntPhySensorOperStatus_Type = EntitySensorStatus
_EntPhySensorOperStatus_Object = MibTableColumn
entPhySensorOperStatus = _EntPhySensorOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5),
    _EntPhySensorOperStatus_Type()
)
entPhySensorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorOperStatus.setDescription("The operational status of the sensor.")
_EntPhySensorUnitsDisplay_Type = SnmpAdminString
_EntPhySensorUnitsDisplay_Object = MibTableColumn
entPhySensorUnitsDisplay = _EntPhySensorUnitsDisplay_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6),
    _EntPhySensorUnitsDisplay_Type()
)
entPhySensorUnitsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorUnitsDisplay.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorUnitsDisplay.setDescription("A textual description of the data units that should be used in the display of entPhySensorValue.")
_EntPhySensorValueTimeStamp_Type = TimeStamp
_EntPhySensorValueTimeStamp_Object = MibTableColumn
entPhySensorValueTimeStamp = _EntPhySensorValueTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7),
    _EntPhySensorValueTimeStamp_Type()
)
entPhySensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValueTimeStamp.setDescription("The value of sysUpTime at the time the status and/or value of this sensor was last obtained by the agent.")
_EntPhySensorValueUpdateRate_Type = Unsigned32
_EntPhySensorValueUpdateRate_Object = MibTableColumn
entPhySensorValueUpdateRate = _EntPhySensorValueUpdateRate_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8),
    _EntPhySensorValueUpdateRate_Type()
)
entPhySensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setUnits("milliseconds")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setDescription("An indication of the frequency that the agent updates the associated entPhySensorValue object, representing in milliseconds. The value zero indicates: - the sensor value is updated on demand (e.g., when polled by the agent for a get-request), - the sensor value is updated when the sensor value changes (event-driven), - the agent does not know the update rate. ")
_EntitySensorConformance_ObjectIdentity = ObjectIdentity
entitySensorConformance = _EntitySensorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3)
)
_EntitySensorCompliances_ObjectIdentity = ObjectIdentity
entitySensorCompliances = _EntitySensorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 1)
)
_EntitySensorGroups_ObjectIdentity = ObjectIdentity
entitySensorGroups = _EntitySensorGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 2)
)

# Managed Objects groups

entitySensorValueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 99, 3, 2, 1)
)
entitySensorValueGroup.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"),
        ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
)
if mibBuilder.loadTexts:
    entitySensorValueGroup.setStatus("current")
if mibBuilder.loadTexts:
    entitySensorValueGroup.setDescription("A collection of objects representing physical entity sensor information.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entitySensorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 99, 3, 1, 1)
)
entitySensorCompliance.setObjects(
      *(("ENTITY-SENSOR-MIB", "entitySensorValueGroup"),
        ("ENTITY-MIB", "entityPhysicalGroup"))
)
if mibBuilder.loadTexts:
    entitySensorCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    entitySensorCompliance.setDescription("Describes the requirements for conformance to the Entity Sensor MIB module.")


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "ENTITY-SENSOR-MIB",
    **{"EntitySensorDataType": EntitySensorDataType,
       "EntitySensorDataScale": EntitySensorDataScale,
       "EntitySensorPrecision": EntitySensorPrecision,
       "EntitySensorValue": EntitySensorValue,
       "EntitySensorStatus": EntitySensorStatus,
       "entitySensorMIB": entitySensorMIB,
       "entitySensorObjects": entitySensorObjects,
       "entPhySensorTable": entPhySensorTable,
       "entPhySensorEntry": entPhySensorEntry,
       "entPhySensorType": entPhySensorType,
       "entPhySensorScale": entPhySensorScale,
       "entPhySensorPrecision": entPhySensorPrecision,
       "entPhySensorValue": entPhySensorValue,
       "entPhySensorOperStatus": entPhySensorOperStatus,
       "entPhySensorUnitsDisplay": entPhySensorUnitsDisplay,
       "entPhySensorValueTimeStamp": entPhySensorValueTimeStamp,
       "entPhySensorValueUpdateRate": entPhySensorValueUpdateRate,
       "entitySensorConformance": entitySensorConformance,
       "entitySensorCompliances": entitySensorCompliances,
       "entitySensorCompliance": entitySensorCompliance,
       "entitySensorGroups": entitySensorGroups,
       "entitySensorValueGroup": entitySensorValueGroup}
)
