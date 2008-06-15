######################################################################
#
# Copyright 2007 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

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
