##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2007, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device


class BrocadeDevice(Device):
    "A Brocade Fibre Channel Switch"

    _relations = Device._relations + (
        ('fcports', ToManyCont(ToOne,
            'ZenPacks.zenoss.BrocadeMonitor.FCPort', 'fcswitch')),
        )


    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()


InitializeClass(BrocadeDevice)
