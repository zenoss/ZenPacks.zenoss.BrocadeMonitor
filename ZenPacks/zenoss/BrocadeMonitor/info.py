##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.ZenUtils.Utils import convToUnits

from ZenPacks.zenoss.StorageBase.interfaces import IFcPortInfo

class FcPortInfo(ComponentInfo):
    implements(IFcPortInfo)

    @property
    def portStatus(self):
        operStatusMap = {
            0:'Unknown',
            1:'Online',
            2:'Offline',
            3:'Testing',
            4:'Link Failure'
        }
        statusCode = self._object.operStatus()
        operStatus = operStatusMap.get(statusCode,
                'Unknown (%s)' % statusCode)

        adminStatusMap = {
            0:'Unknown',
            1:'Online',
            2:'Testing',
        }
        statusCode = self._object.adminStatus()
        adminStatus = adminStatusMap.get(statusCode,
                'Unknown (%s)' % statusCode)

        return adminStatus + ' / ' + operStatus

    @property
    def portType(self):
        return 0

    @property
    def peerPortId(self):
        return self._object.peerPortId

    @property
    def speed(self):
        return 0

    @property
    def module(self):
        return self._object.module

    @property
    def gbic(self):
        gbicType2name = {
            1:'Unknown',
            2:'Long wave laser',
            3:'Short wave laser',
            4:'Long wave LED',
            5:'Copper',
        }
        return gbicType2name.get(self._object.gbicType,
                'Unknown (%s)' % self._object.gbicType)
