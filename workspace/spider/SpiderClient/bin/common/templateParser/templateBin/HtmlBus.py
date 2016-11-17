#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

import hashlib
from common.class_common import Bus
from StopCommon import *

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlBus(StopCommon):

    def __init__(self):
        pass
    
    def HtmlBus(self, page, area, filename, list):
        
        Dict = defaultdict(dict)
        bus = Bus()
        for every in list:
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'currency')
                if con_res == 'error':
                    Dict[md5]['currency'] = bus.currency
                else:
                    Dict[md5]['currency'] = con_res 
            except Exception, e:
                Dict[md5]['currency'] = bus.currency
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'source')
                if con_res == 'error':
                    Dict[md5]['source'] = bus.source
                else:
                    Dict[md5]['source'] = con_res 
            except Exception, e:
                Dict[md5]['source'] = bus.source
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_city')
                if con_res == 'error':
                    Dict[md5]['dept_city'] = bus.dept_city
                else:
                    Dict[md5]['dept_city'] = con_res 
            except Exception, e:
                Dict[md5]['dept_city'] = bus.dept_city
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_city')
                if con_res == 'error':
                    Dict[md5]['dest_city'] = bus.dest_city
                else:
                    Dict[md5]['dest_city'] = con_res 
            except Exception, e:
                Dict[md5]['dest_city'] = bus.dest_city
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_station')
                if con_res == 'error':
                    Dict[md5]['dept_station'] = bus.dept_station
                else:
                    Dict[md5]['dept_station'] = con_res 
            except Exception, e:
                Dict[md5]['dept_station'] = bus.dept_station
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_station')
                if con_res == 'error':
                    Dict[md5]['dest_station'] = bus.dest_station
                else:
                    Dict[md5]['dest_station'] = con_res 
            except Exception, e:
                Dict[md5]['dest_station'] = bus.dest_station
        
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_day')
                if con_res == 'error':
                    Dict[md5]['dept_day'] = bus.dept_day
                else:
                    Dict[md5]['dept_day'] = con_res 
            except Exception, e:
                Dict[md5]['dept_day'] = bus.dept_day
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_time')
                if con_res == 'error':
                    Dict[md5]['dept_time'] = bus.dept_time
                else:
                    Dict[md5]['dept_time'] = con_res 
            except Exception, e:
                Dict[md5]['dept_time'] = bus.dept_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_time')
                if con_res == 'error':
                    Dict[md5]['dest_time'] = bus.dest_time
                else:
                    Dict[md5]['dest_time'] = con_res 
            except Exception, e:
                Dict[md5]['dest_time'] = bus.dest_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'corp')
                if con_res == 'error':
                    Dict[md5]['corp'] = bus.corp
                else:
                    Dict[md5]['corp'] = con_res 
            except Exception, e:
                Dict[md5]['corp'] = bus.corp
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'daydiff')
                if con_res == 'error':
                    Dict[md5]['daydiff'] = bus.daydiff
                else:
                    Dict[md5]['daydiff'] = con_res 
            except Exception, e:
                Dict[md5]['daydiff'] = bus.daydiff
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'price')
                if con_res == 'error':
                    Dict[md5]['price'] = bus.price
                else:
                    Dict[md5]['price'] = con_res 
            except Exception, e:
                Dict[md5]['price'] = bus.price
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'rest')
                if con_res == 'error':
                    Dict[md5]['rest'] = bus.rest
                else:
                    Dict[md5]['rest'] = con_res 
            except Exception, e:
                Dict[md5]['rest'] = bus.rest
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'return_rule')
                if con_res == 'error':
                    Dict[md5]['return_rule'] = bus.return_rule
                else:
                    Dict[md5]['return_rule'] = con_res 
            except Exception, e:
                Dict[md5]['return_rule'] = bus.return_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'change_rule')
                if con_res == 'error':
                    Dict[md5]['change_rule'] = bus.change_rule
                else:
                    Dict[md5]['change_rule'] = con_res 
            except Exception, e:
                Dict[md5]['change_rule'] = bus.change_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'ticket_type')
                if con_res == 'error':
                    Dict[md5]['ticket_type'] = bus.ticket_type
                else:
                    Dict[md5]['ticket_type'] = con_res 
            except Exception, e:
                Dict[md5]['ticket_type'] = bus.ticket_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'tax')
                if con_res == 'error':
                    Dict[md5]['tax'] = bus.tax
                else:
                    Dict[md5]['tax'] = con_res 
            except Exception, e:
                Dict[md5]['tax'] = bus.tax
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dur')
                if con_res == 'error':
                    Dict[md5]['dur'] = bus.dur
                else:
                    Dict[md5]['dur'] = con_res 
            except Exception, e:
                Dict[md5]['dur'] = bus.dur
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'other_0')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_0'] = con_res 
            except Exception, e:
                Dict[md5]['other_0'] = 'NULL'
            try:
                con_res = self.com_Hfunc(every, filename, area, 'other_1')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_1'] = con_res 
            except Exception, e:
                Dict[md5]['other_1'] = 'NULL'
            try:
                con_res = self.com_Hfunc(every, filename, area, 'other_2')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_2'] = con_res 
            except Exception, e:
                Dict[md5]['other_2'] = 'NULL'
            try:
                con_res = self.com_Hfunc(every, filename, area, 'other_3')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_3'] = con_res 
            except Exception, e:
                Dict[md5]['other_3'] = 'NULL'
            try:
                con_res = self.com_Hfunc(every, filename, area, 'other_4')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_4'] = con_res 
            except Exception, e:
                Dict[md5]['other_4'] = 'NULL'
        
        
        return Dict


       
