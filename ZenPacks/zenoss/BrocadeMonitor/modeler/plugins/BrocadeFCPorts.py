##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2008, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__="""BrocadeFCPorts

BrocadeFCPorts maps fibre channel ports on Brocade switches

"""

import re

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, \
        GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap


class BrocadeFCPorts(SnmpPlugin):

    relname = "fcports"
    modname = "ZenPacks.zenoss.BrocadeMonitor.FCPort"

    snmpGetTableMaps = (
        GetTableMap(
            'statusTable', '.1.3.6.1.2.1.75.1.2.1.1', {
                '.1': 'portId',
                }),
    )

    indexMatch = re.compile('(\d+)\.(\d+)').search


    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        status = tabledata.get("statusTable")
        rm = self.relMap()
        for snmpindex, data in status.items():
            match = self.indexMatch(snmpindex)
            if not match: continue
            module, port = match.groups()

            om = self.objectMap()
            om.id = self.prepId("%s_%s" % (module, port))
            om.snmpindex = snmpindex
            om.module = module
            om.port = port
            rm.append(om)
        return rm
