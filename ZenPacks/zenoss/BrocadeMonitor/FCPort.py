######################################################################
#
# Copyright 2008 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

__doc__="""FCPort

FCPort is a fibre channel port on a Brocade fibre channel switch

"""

import locale

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenUtils.Utils import convToUnits
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import prepId


class FCPort(DeviceComponent, ManagedEntity):
    """Fibre Channel Port"""

    portal_type = meta_type = 'FcPort'
    
    module = ""
    port = ""
    gbicType = 0


    _properties = (
        {'id':'module', 'type':'string', 'mode':''},
        {'id':'port', 'type':'string', 'mode':''},
        {'id':'gbicType', 'type':'int', 'mode':''},
        )

    _relations = (
        ("fcswitch", ToOne(ToManyCont,
            "ZenPacks.zenoss.BrocadeMonitor.BrocadeDevice", "fcports")),
        )
    

    factory_type_information = ( 
        { 
            'id'             : 'FCPort',
            'meta_type'      : 'FCPort',
            'description'    : """Arbitrary device grouping class""",
            'icon'           : 'FCPort_icon.gif',
            'product'        : 'BrocadeMonitor',
            'factory'        : 'manage_addFCPort',
            'immediate_view' : 'viewFCPort',
            'actions'        :
            ( 
                { 'id'            : 'perfServer'
                , 'name'          : 'Graphs'
                , 'action'        : 'viewDevicePerformance'
                , 'permissions'   : (ZEN_VIEW, )
                },

                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'viewFCPort'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
                },                
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
          },
        )
        

    def viewName(self):
        return "%s/%s" % (self.module, self.port)
    name = viewName


    def primarySortKey(self):
        return int(self.module) * int(self.port)


    def device(self):
        return self.fcswitch()


    def adminStatus(self, default=None):
        value = self.cacheRRDValue('adminStatus', default)
        if value is None:
            value = 0
        return value

        

    adminStatusMap = ("unknown", "online", "testing")
    def adminStatusString(self):
        a_s = self.adminStatus()
        return a_s is None and "unknown" or self.adminStatusMap[int(a_s)]
        

    def operStatus(self, default=None):
        value = self.cacheRRDValue('operStatus', default)
        if value is None:
            value = 0
        return value

    operStatusMap = ("unknown", "online", "offline", "testing", "linkFailure")
    def operStatusString(self):
        os = self.operStatus()
        return os is None and "unknown" or self.operStatusMap[int(os)]


    def getRRDNames(self):
        return [
            'adminStatus_adminStatus',
            'operStatus_operStatus',
            
            'linkFailures_linkFailures',
            'syncLosses_syncLosses',
            'sigLosses_sigLosses',
            'primSeqProtoErrors_primSeqProtoErrors',
            'invalidTxWords_invalidTxWords'
            'invalidCrcs_invalidCrcs',
            'delimiterErrors_delimiterErrors',
            'addressIdErrors_addressIdErrors',
            'linkResetIns_linkResetIns',
            'linkResetOuts_linkResetOuts',
            'olsIns_olsIns',
            'olsOuts_oldOuts',
            
            'c1InFrames_c1InFrames',
            'c1OutFrames_c1OutFrames',
            'c1InOctets_c1InOctets',
            'c1OutOctets_c1OutOctets',
            'c1Discards_c1Discards',
            'c1FbsyFrames_c1FbsyFrames',
            'c1FrjtFrames_c1FrjtFrames',
            'c1InConnections_c1InConnections',
            'c1OutConnections_c1OutConnections',
            'c1ConnTime_c1ConnTime',
            
            'c2InFrames_c2InFrames',
            'c2OutFrames_c2OutFrames',
            'c2InOctets_c2InOctets',
            'c2OutOctets_c2OutOctets',
            'c2Discards_c2Discards',
            'c2FbsyFrames_c2FbsyFrames',
            'c2FrjtFrames_c2FrjtFrames',
            
            'c3InFrames_c3InFrames',
            'c3OutFrames_c3OutFrames',
            'c3InOctets_c3InOctets',
            'c3OutOctets_c3OutOctets',
            'c3Discards_c3Discards',
            ]

InitializeClass(FCPort)
