#!/usr/bin/env python
#coding:utf-8

import sys
import re
import json
from lxml import html as HTML
from common.logger import logger
from common.airline_common import *#Airline

reload(sys)
sys.setdefaultencoding('utf-8')


def GetAirline(flight_no, model):

    Aircorp = ''
    if model == '1':
        #根据航班号获取航空公司 MU123_CA123_HU123---->中国东风航空_中国国际航空_海南航空
        if flight_no.find('NULL') > -1:
            nullnum = flight_no.count('NULL')
            linenum = flight_no.count('_')
            if nullnum > linenum:
                Aircorp = flight_no + '_'    
            else:
                airline_list = flight_no.split('_')
                for every in airline_list:
                    if every.find('NULL') > -1:
                        Aircorp += 'NULL_'
                    else:
                        try:
                            Aircorp += Airline[every[:2]] + '_'
                        except Exception, e:
                            Aircorp += 'NULL_'
        else:
            airline_list = flight_no.split('_')
            for every in airline_list:
                if every.find('NULL') > -1:
                    Aircorp += 'NULL_'
                else:
                    try:
                        Aircorp += Airline[every[:2]] + '_'
                    except Exception, e:
                        Aircorp += 'NULL_'
    else:
        pass

    return Aircorp[:-1]





