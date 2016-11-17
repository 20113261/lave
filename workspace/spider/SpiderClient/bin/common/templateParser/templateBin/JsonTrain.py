#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

from confParser import *
import hashlib
from GetJoin import *
from common.class_common import Train, EachTrain

reload(sys)
sys.setdefaultencoding('utf-8')

class JsonTrain(GetConfValues, GetJoin):

    def __init__(self):
        pass
    
    def JsonTrain(self,filename, list):
        
        Dict = defaultdict(dict)
        train = Train()
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         

            Dict[md5]['currency'] = self.GetConfValues(filename, 'section', 'currency')
            Dict[md5]['source'] = self.GetConfValues(filename, 'section', 'source')
            
            try:
                traintypepath = self.GetConfValues(filename, 'section', 'train_type')
                Dict[md5]['train_type'] = self.GetUnder(every, traintypepath)
            except Exception, e:
                Dict[md5]['train_type'] = train.train_type
            
            try:
                trainnumberpath = self.GetConfValues(filename, 'section', 'train_no')
                Dict[md5]['train_no'] = self.GetUnder(every, trainnumberpath)
            except Exception, e:
                Dict[md5]['train_no'] = train.train_no
                
            try:
                Dict[md5]['train_corp'] = self.GetUnder(every, trainnumberpath)
            except Exception, e:
                Dict[md5]['train_corp'] = train.train_corp
            
            try:
                daypath = self.GetConfValues(filename, 'section', 'dept_day')
                Dict[md5]['dept_day'] = self.GetUnder(every, daypath)
            except Exception, e:
                Dict[md5]['dept_day'] = train.dept_day
            
            try:
                stoptimepath = self.GetConfValues(filename, 'section', 'stoptime')
                Dict[md5]['stoptime'] = self.GetVertical(every, stoptimepath)
            except Exception, e:
                Dict[md5]['stoptime'] = train.stop_time
            
            try:
                stop_time_list = Dict[md5]['stoptime'].split('_')
                Dict[md5]['dept_time'] = stop_time_list[0]
                Dict[md5]['dest_time'] = stop_time_list[len(stop_time_list) - 1]
            except Exception, e:
                Dict[md5]['dept_time'] = train.dept_time
                Dict[md5]['dest_time'] = train.dest_time

            try:
                stopidpath = self.GetConfValues(filename, 'section', 'stopid')
                Dict[md5]['stopid'] = self.GetVertical(every, stopidpath)
            except Exception, e:
                Dict[md5]['stopid'] = train.stop_id
            
            try:
                stop_list = Dict[md5]['stopid'].split('_')
                Dict[md5]['dept_id'] = stop_list[0]
                Dict[md5]['dest_id'] = stop_list[len(stop_list) - 1]
            except Exception, e:
                Dict[md5]['dept_id'] = train.dept_id
                Dict[md5]['dest_id'] = train.dest_id
            
            try:
                durpath = self.GetConfValues(filename, 'section', 'dur')
                Dict[md5]['dur'] = self.GetUnder(every, durpath)
            except Exception, e:
                Dict[md5]['dur'] = train.dur
            
            try:
                stoppath = self.GetConfValues(filename, 'section', 'stop')
                Dict[md5]['stop'] = self.GetUnder(every, stoppath)
            except Exception, e:
                Dict[md5]['stop'] = train.stop
            
            try:
                return_rulepath = self.GetConfValues(filename, 'section', 'return_rule')
                Dict[md5]['return_rule'] = self.GetUnder(every, return_rulepath)
            except Exception, e:
                Dict[md5]['return_rule'] = train.return_rule
            
            try: 
                seat_typepath = self.GetConfValues(filename, 'section', 'seat_type')
                Dict[md5]['seat_type'] = self.GetUnder(every, seat_typepath)
            except Exception, e:
                Dict[md5]['seat_type'] = train.seat_type
            
            try:
                real_classpath = self.GetConfValues(filename, 'section', 'real_class')
                Dict[md5]['real_class'] = self.GetUnder(every, real_classpath)
            except Exception, e:
                Dict[md5]['real_class'] = train.real_class
            
            try:
                Dict[md5]['daydiff'] = train.daydiff 
            except Exception, e:
                Dict[md5]['daydiff'] = train.daydiff
            
            try:
                pricepath = self.GetConfValues(filename, 'section', 'price')
                Dict[md5]['price'] = self.GetUnder(every, pricepath)
            except Exception, e:
                Dict[md5]['price'] = train.price
            
            try: 
                taxpath = self.GetConfValues(filename, 'section', 'tax')
                Dict[md5]['tax'] = self.GetUnder(every, taxpath)
            except Exception, e:
                Dict[md5]['tax'] = train.tax


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


