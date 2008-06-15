######################################################################
#
# Copyright 2008 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

__doc__="""BrocadeDeviceMap

BrocadeDeviceMap maps the device level information for Brocade switches.

$ID: $"""

__version__ = '$Revision: $'[11:-2]

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap

class BrocadeDeviceMap(SnmpPlugin):

    maptype = "BrocadeDeviceMap"

    snmpGetMap = GetMap({
        '.1.3.6.1.2.1.1.2.0': 'sysObjectID',
        '.1.3.6.1.4.1.1588.2.1.1.1.1.6.0': 'firmwareVersion',
        })

    def process(self, device, results, log):
        log.info("processing %s for device %s", self.name(), device.id)
        getdata, tabledata = results
        if not getdata['sysObjectID'].startswith('.1.3.6.1.4.1.1588.2.1.1.1'):
            return None
            
        om = self.objectMap()
        om.setHWProductKey = 'Brocade SAN Switch'
        om.setOSProductKey = 'Brocade Fabric OS ' + \
            getdata['firmwareVersion']
        return om
