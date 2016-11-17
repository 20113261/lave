#!/usr/bin/env python
#coding:utf-8


import os
import re
import time
import sys
#from common.station_common import Station #调用common文件下得相关文件
from GetNumber import  GetNum
from getCurr import getCurrency
from getCorp import GetAirline
from GetStationId import GetStationId
from getStopTime import gStopTime
from Daydiff import *
from common.class_common import *

class Typeinstance():
    def __init__(self, type):
        class_name = type[0].upper() + type[1:].lower() + '()'
	self.type = eval(class_name)
    def default_v(self, field):
	con = 'self.type.' + field
	return  eval(con)


class NormFunc(object):

    def __init__(self):
        self.result = ''

    def chmode(self, type_name, field, model, content):

        '''
            model:c0, c1, c2预留公共模式，其他模式model从1，2......
                    此model比较有针对性, 0为初始化模式
        '''
	default_value = Typeinstance(type_name)
        if model == '0':#0初始化模式全为NULL
            self.result = content#default_value.default_v(field)
        elif model == 'c1':#price, tax, rest(get number)
            self.result = GetNum(content)
        elif model == 'c2':#currency
            #$567.98(the string of including currency token)
            self.result = getCurrency(content)
        elif mode == 'c3':
            pass
        else:
            if field == 'flight_no':
                self.result = getFNo(flight_nostr, model)
            elif field == 'flight_corp':#SU123_MU9090_CA675
                self.result = getAirline(content, model)
            elif type_name.lower() == 'train' or type_name.lower() == 'bus':
                if field == 'dept_id' or field == 'dest_id' or field == 'stop_id':
                    #TRAIN and BUS:------>dept_id,dest_id, stop_id
                    self.result = GetStationId(content, type_name, model) 
                else:
                    pass
            elif field.find('time') > -1:
                #dept_time, dest_time, stop_time
                self.result = gStopTime(content, model) 
            elif field == 'dur':
                #计算dur
                self.result = dur(content) 
            elif type_name.lower() == 'flight':
                #FLIGHT:----->dept_id, dest_id, stop_id
                self.result = getId(idstr, model)
            else:
                pass
            
        return self.result



