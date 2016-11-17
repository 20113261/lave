#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('../../')
from common.logger import logger
from common.station_common import Station
from common.bus_common import Bus_Dict

reload(sys)
sys.setdefaultencoding('utf-8')


def GetStationId(self,constation, ttype, model):

    station_id = ''
    station_list = constation.split('_')
    if model == '0':
        for every in station_list:
            if every.upper().find('NULL') > -1:
                station_id += 'NULL_'
            else:
                if ttype.lower() == 'train':
                    if every.upper() in Station:
                        station_id += Station[every.upper()] + '_'
                    else:
                        station_id += 'NULL_'
                elif ttype.lower() == 'bus':
                    if every.upper() in Bus_Dict:
                        station_id += Bus_Dict[every.upper()] + '_'
                    else:
                        station_id += 'NULL_'
                else:
                    pass
    else:
        pass

    return station_id[:-1]





