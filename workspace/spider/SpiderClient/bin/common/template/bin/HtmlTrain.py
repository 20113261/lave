#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

import hashlib
from common.class_common import Train
from StopCommon import *

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlTrain(StopCommon):

    def __init__(self):
        pass
    
    def HtmlTrain(self, area, filename, list):
        
        Dict = defaultdict(dict)
        train = Train()
        for every in list:
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'currency')
                if con_res == 'error':
                    Dict[md5]['currency'] = train.currency
                else:
                    Dict[md5]['currency'] = con_res 
            except Exception, e:
                Dict[md5]['currency'] = train.currency
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'source')
                if con_res == 'error':
                    Dict[md5]['source'] = train.source
                else:
                    Dict[md5]['source'] = con_res 
            except Exception, e:
                Dict[md5]['source'] = train.source
        
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_day')
                if con_res == 'error':
                    Dict[md5]['dept_day'] = train.dept_day
                else:
                    Dict[md5]['dept_day'] = con_res 
            except Exception, e:
                Dict[md5]['dept_day'] = train.dept_day
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_time')
                if con_res == 'error':
                    Dict[md5]['dept_time'] = train.dept_time
                else:
                    Dict[md5]['dept_time'] = con_res 
            except Exception, e:
                Dict[md5]['dept_time'] = train.dept_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_time')
                if con_res == 'error':
                    Dict[md5]['dest_time'] = train.dest_time
                else:
                    Dict[md5]['dest_time'] = con_res 
            except Exception, e:
                Dict[md5]['dest_time'] = train.dest_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_city')
                if con_res == 'error':
                    Dict[md5]['dept_city'] = train.dept_city
                else:
                    Dict[md5]['dept_city'] = con_res 
            except Exception, e:
                Dict[md5]['dept_city'] = train.dept_city
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_city')
                if con_res == 'error':
                    Dict[md5]['dest_city'] = train.dest_city
                else:
                    Dict[md5]['dest_city'] = con_res 
            except Exception, e:
                Dict[md5]['dest_city'] = train.dest_city
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'real_class')
                if con_res == 'error':
                    Dict[md5]['real_class'] = train.real_class
                else:
                    Dict[md5]['real_class'] = con_res 
            except Exception, e:
                Dict[md5]['real_class'] = train.real_class
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'promotion')
                if con_res == 'error':
                    Dict[md5]['promotion'] = train.promotion
                else:
                    Dict[md5]['promotion'] = con_res 
            except Exception, e:
                Dict[md5]['promotion'] = train.promotion
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stopid')
                if con_res == 'error':
                    Dict[md5]['stopid'] = train.stopid
                else:
                    Dict[md5]['stopid'] = con_res 
            except Exception, e:
                Dict[md5]['stopid'] = train.stopid
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stoptime')
                if con_res == 'error':
                    Dict[md5]['stoptime'] = train.stoptime
                else:
                    Dict[md5]['stoptime'] = con_res 
            except Exception, e:
                Dict[md5]['stoptime'] = train.stoptime
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'train_no')
                if con_res == 'error':
                    Dict[md5]['train_no'] = train.train_no
                else:
                    Dict[md5]['train_no'] = con_res 
            except Exception, e:
                Dict[md5]['train_no'] = train.train_no
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'train_corp')
                if con_res == 'error':
                    Dict[md5]['train_corp'] = train.train_corp
                else:
                    Dict[md5]['train_corp'] = con_res 
            except Exception, e:
                Dict[md5]['train_corp'] = train.train_corp
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'daydiff')
                if con_res == 'error':
                    Dict[md5]['daydiff'] = train.daydiff
                else:
                    Dict[md5]['daydiff'] = con_res 
            except Exception, e:
                Dict[md5]['daydiff'] = train.daydiff
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'price')
                if con_res == 'error':
                    Dict[md5]['price'] = train.price
                else:
                    Dict[md5]['price'] = con_res 
            except Exception, e:
                Dict[md5]['price'] = train.price
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'tax')
                if con_res == 'error':
                    Dict[md5]['tax'] = train.tax
                else:
                    Dict[md5]['tax'] = con_res 
            except Exception, e:
                Dict[md5]['tax'] = train.tax
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'return_rule')
                if con_res == 'error':
                    Dict[md5]['return_rule'] = train.return_rule
                else:
                    Dict[md5]['return_rule'] = con_res 
            except Exception, e:
                Dict[md5]['return_rule'] = train.return_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'change_rule')
                if con_res == 'error':
                    Dict[md5]['change_rule'] = train.change_rule
                else:
                    Dict[md5]['change_rule'] = con_res 
            except Exception, e:
                Dict[md5]['change_rule'] = train.change_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dur')
                if con_res == 'error':
                    Dict[md5]['dur'] = train.dur
                else:
                    Dict[md5]['dur'] = con_res 
            except Exception, e:
                Dict[md5]['dur'] = train.dur
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'seat_type')
                if con_res == 'error':
                    Dict[md5]['seat_type'] = train.seat_type
                else:
                    Dict[md5]['seat_type'] = con_res 
            except Exception, e:
                Dict[md5]['seat_type'] = train.seat_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop')
                if con_res == 'error':
                    Dict[md5]['stop'] = train.stop
                else:
                    Dict[md5]['stop'] = con_res 
            except Exception, e:
                Dict[md5]['stop'] = train.stop
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_id')
                if con_res == 'error':
                    Dict[md5]['dept_id'] = train.dept_id
                else:
                    Dict[md5]['dept_id'] = con_res 
            except Exception, e:
                Dict[md5]['dept_id'] = train.dept_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_id')
                if con_res == 'error':
                    Dict[md5]['dest_id'] = train.dest_id
                else:
                    Dict[md5]['dest_id'] = con_res 
            except Exception, e:
                Dict[md5]['dest_id'] = train.dest_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'train_type')
                if con_res == 'error':
                    Dict[md5]['train_type'] = train.train_type
                else:
                    Dict[md5]['train_type'] = con_res 
            except Exception, e:
                Dict[md5]['train_type'] = train.train_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'train_facilities')
                if con_res == 'error':
                    Dict[md5]['train_facilities'] = train.train_facilities
                else:
                    Dict[md5]['train_facilities'] = con_res 
            except Exception, e:
                Dict[md5]['train_facilities'] = train.train_facilities

            try:
                con_res = self.com_Hfunc(every, filename, area, 'electric_ticket')
                if con_res == 'error':
                    Dict[md5]['electric_ticket'] = train.electric_ticket
                else:
                    Dict[md5]['electric_ticket'] = con_res 
            except Exception, e:
                Dict[md5]['electric_ticket'] = train.electric_ticket
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'ticket_type')
                if con_res == 'error':
                    Dict[md5]['ticket_type'] = train.ticket_type
                else:
                    Dict[md5]['ticket_type'] = con_res 
            except Exception, e:
                Dict[md5]['ticket_type'] = train.ticket_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'others_info')
                if con_res == 'error':
                    Dict[md5]['others_info'] = train.others_info
                else:
                    Dict[md5]['others_info'] = con_res 
            except Exception, e:
                Dict[md5]['others_info'] = train.others_info
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'req')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['req'] = con_res 
            except Exception, e:
                Dict[md5]['req'] = 'NULL'
            
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

 
