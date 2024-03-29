##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2008, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPack

class Menu:
    version = Version(2, 0, 3)

    def migrate(self, pack):
        dmd = pack.__primary_parent__.__primary_parent__
        id = 'brocadeDeviceDetail'
        # check to see if the menu exisits before trying to delete it
        menu = dmd.zenMenus.More._getOb(id, None)
        if menu is not None:
            dmd.zenMenus.More.manage_deleteZenMenuItem((id,))
        dmd.zenMenus.More.manage_addZenMenuItem(
            id,
            action=id,
            description='Brocade Details',
            allowed_classes=('BrocadeDevice',),
            ordering=5.0)

Menu()
