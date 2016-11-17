#!/usr/bin/env python
#coding:utf-8

import sys
from common.logger import logger
from common.station_common import Station

reload(sys)
sys.setdefaultencoding('utf-8')

class GetStationId(object):

    def __init__(self):
        pass

    def GetStationId(self,constation):

        station_id = ''
        station_list = constation.split('_')
        for every in station_list:
            if every.find('NULL') > -1:
                station_id += 'NULL_'
            else:
                if every.upper() in Station:
                    station_id += Station[every.upper()] + '_'
                else:
                    station_id += 'NULL_'

        return station_id[:-1]


if __name__ == '__main__':

    get = GetStationId()

    re = get.GetStationId('NULL_NULL')

    print re





