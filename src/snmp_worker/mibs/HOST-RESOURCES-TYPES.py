# SNMP MIB module (HOST-RESOURCES-TYPES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/HOST-RESOURCES-TYPES
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

(hrDevice,
 hrMIBAdminInfo,
 hrStorage) = mibBuilder.import_symbols(
    "HOST-RESOURCES-MIB",
    "hrDevice",
    "hrMIBAdminInfo",
    "hrStorage")

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

hostResourcesTypesModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 4)
)
if mibBuilder.loadTexts:
    hostResourcesTypesModule.setRevisions(
        ("2000-03-06 00:00",)
    )
if mibBuilder.loadTexts:
    hostResourcesTypesModule.setLastUpdated("200003060000Z")
if mibBuilder.loadTexts:
    hostResourcesTypesModule.setOrganization("IETF Host Resources MIB Working Group")
if mibBuilder.loadTexts:
    hostResourcesTypesModule.setContactInfo("Steve Waldbusser Postal: Lucent Technologies, Inc. 1213 Innsbruck Dr. Sunnyvale, CA 94089 USA Phone: 650-318-1251 Fax: 650-318-1633 Email: waldbusser@ins.com In addition, the Host Resources MIB mailing list is dedicated to discussion of this MIB. To join the mailing list, send a request message to hostmib-request@andrew.cmu.edu. The mailing list address is hostmib@andrew.cmu.edu.")
if mibBuilder.loadTexts:
    hostResourcesTypesModule.setDescription("This MIB module registers type definitions for storage types, device types, and file system types. After the initial revision, this module will be maintained by IANA.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HrStorageTypes_ObjectIdentity = ObjectIdentity
hrStorageTypes = _HrStorageTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1)
)
_HrStorageOther_ObjectIdentity = ObjectIdentity
hrStorageOther = _HrStorageOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hrStorageOther.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageOther.setDescription("The storage type identifier used when no other defined type is appropriate.")
_HrStorageRam_ObjectIdentity = ObjectIdentity
hrStorageRam = _HrStorageRam_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hrStorageRam.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageRam.setDescription("The storage type identifier used for RAM.")
_HrStorageVirtualMemory_ObjectIdentity = ObjectIdentity
hrStorageVirtualMemory = _HrStorageVirtualMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hrStorageVirtualMemory.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageVirtualMemory.setDescription("The storage type identifier used for virtual memory, temporary storage of swapped or paged memory.")
_HrStorageFixedDisk_ObjectIdentity = ObjectIdentity
hrStorageFixedDisk = _HrStorageFixedDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hrStorageFixedDisk.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageFixedDisk.setDescription("The storage type identifier used for non-removable rigid rotating magnetic storage devices.")
_HrStorageRemovableDisk_ObjectIdentity = ObjectIdentity
hrStorageRemovableDisk = _HrStorageRemovableDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hrStorageRemovableDisk.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageRemovableDisk.setDescription("The storage type identifier used for removable rigid rotating magnetic storage devices.")
_HrStorageFloppyDisk_ObjectIdentity = ObjectIdentity
hrStorageFloppyDisk = _HrStorageFloppyDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hrStorageFloppyDisk.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageFloppyDisk.setDescription("The storage type identifier used for non-rigid rotating magnetic storage devices.")
_HrStorageCompactDisc_ObjectIdentity = ObjectIdentity
hrStorageCompactDisc = _HrStorageCompactDisc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hrStorageCompactDisc.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageCompactDisc.setDescription("The storage type identifier used for read-only rotating optical storage devices.")
_HrStorageRamDisk_ObjectIdentity = ObjectIdentity
hrStorageRamDisk = _HrStorageRamDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hrStorageRamDisk.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageRamDisk.setDescription("The storage type identifier used for a file system that is stored in RAM.")
_HrStorageFlashMemory_ObjectIdentity = ObjectIdentity
hrStorageFlashMemory = _HrStorageFlashMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hrStorageFlashMemory.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageFlashMemory.setDescription("The storage type identifier used for flash memory.")
_HrStorageNetworkDisk_ObjectIdentity = ObjectIdentity
hrStorageNetworkDisk = _HrStorageNetworkDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hrStorageNetworkDisk.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageNetworkDisk.setDescription("The storage type identifier used for a networked file system.")
_HrDeviceTypes_ObjectIdentity = ObjectIdentity
hrDeviceTypes = _HrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1)
)
_HrDeviceOther_ObjectIdentity = ObjectIdentity
hrDeviceOther = _HrDeviceOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hrDeviceOther.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceOther.setDescription("The device type identifier used when no other defined type is appropriate.")
_HrDeviceUnknown_ObjectIdentity = ObjectIdentity
hrDeviceUnknown = _HrDeviceUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hrDeviceUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceUnknown.setDescription("The device type identifier used when the device type is unknown.")
_HrDeviceProcessor_ObjectIdentity = ObjectIdentity
hrDeviceProcessor = _HrDeviceProcessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hrDeviceProcessor.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceProcessor.setDescription("The device type identifier used for a CPU.")
_HrDeviceNetwork_ObjectIdentity = ObjectIdentity
hrDeviceNetwork = _HrDeviceNetwork_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hrDeviceNetwork.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceNetwork.setDescription("The device type identifier used for a network interface.")
_HrDevicePrinter_ObjectIdentity = ObjectIdentity
hrDevicePrinter = _HrDevicePrinter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hrDevicePrinter.setStatus("current")
if mibBuilder.loadTexts:
    hrDevicePrinter.setDescription("The device type identifier used for a printer.")
_HrDeviceDiskStorage_ObjectIdentity = ObjectIdentity
hrDeviceDiskStorage = _HrDeviceDiskStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hrDeviceDiskStorage.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceDiskStorage.setDescription("The device type identifier used for a disk drive.")
_HrDeviceVideo_ObjectIdentity = ObjectIdentity
hrDeviceVideo = _HrDeviceVideo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hrDeviceVideo.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceVideo.setDescription("The device type identifier used for a video device.")
_HrDeviceAudio_ObjectIdentity = ObjectIdentity
hrDeviceAudio = _HrDeviceAudio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hrDeviceAudio.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceAudio.setDescription("The device type identifier used for an audio device.")
_HrDeviceCoprocessor_ObjectIdentity = ObjectIdentity
hrDeviceCoprocessor = _HrDeviceCoprocessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 12)
)
if mibBuilder.loadTexts:
    hrDeviceCoprocessor.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceCoprocessor.setDescription("The device type identifier used for a co-processor.")
_HrDeviceKeyboard_ObjectIdentity = ObjectIdentity
hrDeviceKeyboard = _HrDeviceKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 13)
)
if mibBuilder.loadTexts:
    hrDeviceKeyboard.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceKeyboard.setDescription("The device type identifier used for a keyboard device.")
_HrDeviceModem_ObjectIdentity = ObjectIdentity
hrDeviceModem = _HrDeviceModem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 14)
)
if mibBuilder.loadTexts:
    hrDeviceModem.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceModem.setDescription("The device type identifier used for a modem.")
_HrDeviceParallelPort_ObjectIdentity = ObjectIdentity
hrDeviceParallelPort = _HrDeviceParallelPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 15)
)
if mibBuilder.loadTexts:
    hrDeviceParallelPort.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceParallelPort.setDescription("The device type identifier used for a parallel port.")
_HrDevicePointing_ObjectIdentity = ObjectIdentity
hrDevicePointing = _HrDevicePointing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 16)
)
if mibBuilder.loadTexts:
    hrDevicePointing.setStatus("current")
if mibBuilder.loadTexts:
    hrDevicePointing.setDescription("The device type identifier used for a pointing device (e.g., a mouse).")
_HrDeviceSerialPort_ObjectIdentity = ObjectIdentity
hrDeviceSerialPort = _HrDeviceSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 17)
)
if mibBuilder.loadTexts:
    hrDeviceSerialPort.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceSerialPort.setDescription("The device type identifier used for a serial port.")
_HrDeviceTape_ObjectIdentity = ObjectIdentity
hrDeviceTape = _HrDeviceTape_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 18)
)
if mibBuilder.loadTexts:
    hrDeviceTape.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceTape.setDescription("The device type identifier used for a tape storage device.")
_HrDeviceClock_ObjectIdentity = ObjectIdentity
hrDeviceClock = _HrDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 19)
)
if mibBuilder.loadTexts:
    hrDeviceClock.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceClock.setDescription("The device type identifier used for a clock device.")
_HrDeviceVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceVolatileMemory = _HrDeviceVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 20)
)
if mibBuilder.loadTexts:
    hrDeviceVolatileMemory.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceVolatileMemory.setDescription("The device type identifier used for a volatile memory storage device.")
_HrDeviceNonVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceNonVolatileMemory = _HrDeviceNonVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 21)
)
if mibBuilder.loadTexts:
    hrDeviceNonVolatileMemory.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceNonVolatileMemory.setDescription("The device type identifier used for a non-volatile memory storage device.")
_HrFSTypes_ObjectIdentity = ObjectIdentity
hrFSTypes = _HrFSTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9)
)
_HrFSOther_ObjectIdentity = ObjectIdentity
hrFSOther = _HrFSOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 1)
)
if mibBuilder.loadTexts:
    hrFSOther.setStatus("current")
if mibBuilder.loadTexts:
    hrFSOther.setDescription("The file system type identifier used when no other defined type is appropriate.")
_HrFSUnknown_ObjectIdentity = ObjectIdentity
hrFSUnknown = _HrFSUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 2)
)
if mibBuilder.loadTexts:
    hrFSUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hrFSUnknown.setDescription("The file system type identifier used when the type of file system is unknown.")
_HrFSBerkeleyFFS_ObjectIdentity = ObjectIdentity
hrFSBerkeleyFFS = _HrFSBerkeleyFFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 3)
)
if mibBuilder.loadTexts:
    hrFSBerkeleyFFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSBerkeleyFFS.setDescription("The file system type identifier used for the Berkeley Fast File System.")
_HrFSSys5FS_ObjectIdentity = ObjectIdentity
hrFSSys5FS = _HrFSSys5FS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 4)
)
if mibBuilder.loadTexts:
    hrFSSys5FS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSSys5FS.setDescription("The file system type identifier used for the System V File System.")
_HrFSFat_ObjectIdentity = ObjectIdentity
hrFSFat = _HrFSFat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 5)
)
if mibBuilder.loadTexts:
    hrFSFat.setStatus("current")
if mibBuilder.loadTexts:
    hrFSFat.setDescription("The file system type identifier used for DOS's FAT file system.")
_HrFSHPFS_ObjectIdentity = ObjectIdentity
hrFSHPFS = _HrFSHPFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 6)
)
if mibBuilder.loadTexts:
    hrFSHPFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSHPFS.setDescription("The file system type identifier used for OS/2's High Performance File System.")
_HrFSHFS_ObjectIdentity = ObjectIdentity
hrFSHFS = _HrFSHFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 7)
)
if mibBuilder.loadTexts:
    hrFSHFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSHFS.setDescription("The file system type identifier used for the Macintosh Hierarchical File System.")
_HrFSMFS_ObjectIdentity = ObjectIdentity
hrFSMFS = _HrFSMFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 8)
)
if mibBuilder.loadTexts:
    hrFSMFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSMFS.setDescription("The file system type identifier used for the Macintosh File System.")
_HrFSNTFS_ObjectIdentity = ObjectIdentity
hrFSNTFS = _HrFSNTFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 9)
)
if mibBuilder.loadTexts:
    hrFSNTFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSNTFS.setDescription("The file system type identifier used for the Windows NT File System.")
_HrFSVNode_ObjectIdentity = ObjectIdentity
hrFSVNode = _HrFSVNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 10)
)
if mibBuilder.loadTexts:
    hrFSVNode.setStatus("current")
if mibBuilder.loadTexts:
    hrFSVNode.setDescription("The file system type identifier used for the VNode File System.")
_HrFSJournaled_ObjectIdentity = ObjectIdentity
hrFSJournaled = _HrFSJournaled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 11)
)
if mibBuilder.loadTexts:
    hrFSJournaled.setStatus("current")
if mibBuilder.loadTexts:
    hrFSJournaled.setDescription("The file system type identifier used for the Journaled File System.")
_HrFSiso9660_ObjectIdentity = ObjectIdentity
hrFSiso9660 = _HrFSiso9660_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 12)
)
if mibBuilder.loadTexts:
    hrFSiso9660.setStatus("current")
if mibBuilder.loadTexts:
    hrFSiso9660.setDescription("The file system type identifier used for the ISO 9660 File System for CD's.")
_HrFSRockRidge_ObjectIdentity = ObjectIdentity
hrFSRockRidge = _HrFSRockRidge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 13)
)
if mibBuilder.loadTexts:
    hrFSRockRidge.setStatus("current")
if mibBuilder.loadTexts:
    hrFSRockRidge.setDescription("The file system type identifier used for the RockRidge File System for CD's.")
_HrFSNFS_ObjectIdentity = ObjectIdentity
hrFSNFS = _HrFSNFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 14)
)
if mibBuilder.loadTexts:
    hrFSNFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSNFS.setDescription("The file system type identifier used for the NFS File System.")
_HrFSNetware_ObjectIdentity = ObjectIdentity
hrFSNetware = _HrFSNetware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 15)
)
if mibBuilder.loadTexts:
    hrFSNetware.setStatus("current")
if mibBuilder.loadTexts:
    hrFSNetware.setDescription("The file system type identifier used for the Netware File System.")
_HrFSAFS_ObjectIdentity = ObjectIdentity
hrFSAFS = _HrFSAFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 16)
)
if mibBuilder.loadTexts:
    hrFSAFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSAFS.setDescription("The file system type identifier used for the Andrew File System.")
_HrFSDFS_ObjectIdentity = ObjectIdentity
hrFSDFS = _HrFSDFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 17)
)
if mibBuilder.loadTexts:
    hrFSDFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSDFS.setDescription("The file system type identifier used for the OSF DCE Distributed File System.")
_HrFSAppleshare_ObjectIdentity = ObjectIdentity
hrFSAppleshare = _HrFSAppleshare_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 18)
)
if mibBuilder.loadTexts:
    hrFSAppleshare.setStatus("current")
if mibBuilder.loadTexts:
    hrFSAppleshare.setDescription("The file system type identifier used for the AppleShare File System.")
_HrFSRFS_ObjectIdentity = ObjectIdentity
hrFSRFS = _HrFSRFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 19)
)
if mibBuilder.loadTexts:
    hrFSRFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSRFS.setDescription("The file system type identifier used for the RFS File System.")
_HrFSDGCFS_ObjectIdentity = ObjectIdentity
hrFSDGCFS = _HrFSDGCFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 20)
)
if mibBuilder.loadTexts:
    hrFSDGCFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSDGCFS.setDescription("The file system type identifier used for the Data General DGCFS.")
_HrFSBFS_ObjectIdentity = ObjectIdentity
hrFSBFS = _HrFSBFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 21)
)
if mibBuilder.loadTexts:
    hrFSBFS.setStatus("current")
if mibBuilder.loadTexts:
    hrFSBFS.setDescription("The file system type identifier used for the SVR4 Boot File System.")
_HrFSFAT32_ObjectIdentity = ObjectIdentity
hrFSFAT32 = _HrFSFAT32_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 22)
)
if mibBuilder.loadTexts:
    hrFSFAT32.setStatus("current")
if mibBuilder.loadTexts:
    hrFSFAT32.setDescription("The file system type identifier used for the Windows FAT32 File System.")
_HrFSLinuxExt2_ObjectIdentity = ObjectIdentity
hrFSLinuxExt2 = _HrFSLinuxExt2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 23)
)
if mibBuilder.loadTexts:
    hrFSLinuxExt2.setStatus("current")
if mibBuilder.loadTexts:
    hrFSLinuxExt2.setDescription("The file system type identifier used for the Linux EXT2 File System.")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.export_symbols(
    "HOST-RESOURCES-TYPES",
    **{"hrStorageTypes": hrStorageTypes,
       "hrStorageOther": hrStorageOther,
       "hrStorageRam": hrStorageRam,
       "hrStorageVirtualMemory": hrStorageVirtualMemory,
       "hrStorageFixedDisk": hrStorageFixedDisk,
       "hrStorageRemovableDisk": hrStorageRemovableDisk,
       "hrStorageFloppyDisk": hrStorageFloppyDisk,
       "hrStorageCompactDisc": hrStorageCompactDisc,
       "hrStorageRamDisk": hrStorageRamDisk,
       "hrStorageFlashMemory": hrStorageFlashMemory,
       "hrStorageNetworkDisk": hrStorageNetworkDisk,
       "hrDeviceTypes": hrDeviceTypes,
       "hrDeviceOther": hrDeviceOther,
       "hrDeviceUnknown": hrDeviceUnknown,
       "hrDeviceProcessor": hrDeviceProcessor,
       "hrDeviceNetwork": hrDeviceNetwork,
       "hrDevicePrinter": hrDevicePrinter,
       "hrDeviceDiskStorage": hrDeviceDiskStorage,
       "hrDeviceVideo": hrDeviceVideo,
       "hrDeviceAudio": hrDeviceAudio,
       "hrDeviceCoprocessor": hrDeviceCoprocessor,
       "hrDeviceKeyboard": hrDeviceKeyboard,
       "hrDeviceModem": hrDeviceModem,
       "hrDeviceParallelPort": hrDeviceParallelPort,
       "hrDevicePointing": hrDevicePointing,
       "hrDeviceSerialPort": hrDeviceSerialPort,
       "hrDeviceTape": hrDeviceTape,
       "hrDeviceClock": hrDeviceClock,
       "hrDeviceVolatileMemory": hrDeviceVolatileMemory,
       "hrDeviceNonVolatileMemory": hrDeviceNonVolatileMemory,
       "hrFSTypes": hrFSTypes,
       "hrFSOther": hrFSOther,
       "hrFSUnknown": hrFSUnknown,
       "hrFSBerkeleyFFS": hrFSBerkeleyFFS,
       "hrFSSys5FS": hrFSSys5FS,
       "hrFSFat": hrFSFat,
       "hrFSHPFS": hrFSHPFS,
       "hrFSHFS": hrFSHFS,
       "hrFSMFS": hrFSMFS,
       "hrFSNTFS": hrFSNTFS,
       "hrFSVNode": hrFSVNode,
       "hrFSJournaled": hrFSJournaled,
       "hrFSiso9660": hrFSiso9660,
       "hrFSRockRidge": hrFSRockRidge,
       "hrFSNFS": hrFSNFS,
       "hrFSNetware": hrFSNetware,
       "hrFSAFS": hrFSAFS,
       "hrFSDFS": hrFSDFS,
       "hrFSAppleshare": hrFSAppleshare,
       "hrFSRFS": hrFSRFS,
       "hrFSDGCFS": hrFSDGCFS,
       "hrFSBFS": hrFSBFS,
       "hrFSFAT32": hrFSFAT32,
       "hrFSLinuxExt2": hrFSLinuxExt2,
       "hostResourcesTypesModule": hostResourcesTypesModule}
)
