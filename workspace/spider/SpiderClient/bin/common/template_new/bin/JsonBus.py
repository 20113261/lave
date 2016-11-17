#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys
sys.path.append('..')

from confParser import *
import hashlib
from GetJoin import *
from common.class_common import Bus

reload(sys)
sys.setdefaultencoding('utf-8')

class JsonBus(GetConfValues, GetJoin):

    def __init__(self):
        pass
    
    def JsonBus(self,filename, list):
        
        Dict = defaultdict(dict)
        bus = Bus()
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         

            Dict[md5]['currency'] = self.GetConfValues(filename, 'section', 'currency')
            Dict[md5]['source'] = self.GetConfValues(filename, 'section', 'source')
            
            try:
                dept_citypath = self.GetConfValues(filename, 'section', 'dept_city')
                Dict[md5]['dept_city'] = self.GetUnder(every, dept_citypath)
            except Exception, e:
                Dict[md5]['dept_city'] = bus.dept_city
            
            try:
                dest_citypath = self.GetConfValues(filename, 'section', 'dest_city')
                Dict[md5]['dest_city'] = self.GetUnder(every, dest_citypath)
            except Exception, e:
                Dict[md5]['dest_city'] = bus.dest_city
            
            try:
                dept_stationpath = self.GetConfValues(filename, 'section', 'dept_station')
                Dict[md5]['dept_station'] = self.GetUnder(every, dept_stationpath)
            except Exception, e:
                Dict[md5]['dept_station'] = bus.dept_station
            
            try:
                dest_stationpath = self.GetConfValues(filename, 'section', 'dept_station')
                Dict[md5]['dest_station'] = self.GetUnder(every, dest_stationpath)
            except Exception, e:
                Dict[md5]['dest_station'] = bus.dest_station
            
            try:
                dept_daypath = self.GetConfValues(filename, 'section', 'dept_day')
                Dict[md5]['dept_day'] = self.GetUnder(every, dept_daypath)
            except Exception, e:
                Dict[md5]['dept_day'] = bus.dept_day
            
            try:
                dept_timepath = self.GetConfValues(filename, 'section', 'dept_time')
                Dict[md5]['dept_time'] = self.GetUnder(every, dept_timepath)
            except Exception, e:
                Dict[md5]['dept_time'] = bus.dept_time
            
            try:
                dest_timepath = self.GetConfValues(filename, 'section', 'dest_time')
                Dict[md5]['dest_time'] = self.GetUnder(every, dest_timepath)
            except Exception, e:
                Dict[md5]['dest_time'] = bus.dest_time

            try:
                durpath = self.GetConfValues(filename, 'section', 'dur')
                Dict[md5]['dur'] = self.GetUnder(every, durpath)
            except Exception, e:
                Dict[md5]['dur'] = bus.dur
            
            try:
                pricepath = self.GetConfValues(filename, 'section', 'price')
                Dict[md5]['price'] = self.GetUnder(every, pricepath)
            except Exception, e:
                Dict[md5]['price'] = bus.price
            
            try:
                corppath = self.GetConfValues(filename, 'section', 'corp')
                Dict[md5]['corp'] = self.GetUnder(every, corppath)
            except Exception, e:
                Dict[md5]['corp'] = bus.corp
            
            try:
                taxpath = self.GetConfValues(filename, 'section', 'tax')
                Dict[md5]['tax'] = self.GetUnder(every, taxpath)
            except Exception, e:
                Dict[md5]['tax'] = bus.tax
            
            try:
                return_rulepath = self.GetConfValues(filename, 'section', 'return_rule')
                Dict[md5]['return_rule'] = self.GetUnder(every, return_rulepath)
            except Exception, e:
                Dict[md5]['return_rule'] = bus.return_rule
            
            try:
                daydiffpath = self.GetConfValues(filename, 'section', 'daydiff')
                Dict[md5]['daydiff'] = self.GetUnder(every, daydiffpath)
            except Exception, e:
                Dict[md5]['daydiff'] = bus.daydiff
            
            other_0path = self.GetConfValues(filename, 'section', 'other_0')
            if other_0path == 'error':
                continue
            else:
                try:
                    Dict[md5]['other_0'] = self.GetUnder(every, other_0path)
                except Exception, e:
                    Dict[md5]['other_0'] = 'NULL'
                
            other_1path = self.GetConfValues(filename, 'section', 'other_1')
            if other_1path == 'error':
                continue
            else:
                try:
                    Dict[md5]['other_1'] = self.GetUnder(every, other_1path)
                except Exception, e:
                    Dict[md5]['other_1'] = 'NULL'
            
            other_2path = self.GetConfValues(filename, 'section', 'other_2')
            if other_2path == 'error':
                continue
            else:
                try:
                    Dict[md5]['other_2'] = self.GetUnder(every, other_2path)
                except Exception, e:
                    Dict[md5]['other_2'] = 'NULL'
        
        return Dict




if __name__ == '__main__':

    import os

    with open('../test/ebooks.html', 'r') as f:
        page = f.read()


