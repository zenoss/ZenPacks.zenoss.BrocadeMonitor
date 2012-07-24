##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2008, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__="""BrocadeDeviceMap

BrocadeDeviceMap maps the device level information for Brocade switches.

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs

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
        om.setHWProductKey = MultiArgs('SAN Switch', 'Brocade')
        om.setOSProductKey = MultiArgs(
            'Fabric OS %s' % getdata['firmwareVersion'], 'Brocade')
        return om
