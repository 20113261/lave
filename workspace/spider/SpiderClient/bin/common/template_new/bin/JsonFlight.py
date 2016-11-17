#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

from confParser import *
import hashlib
from GetJoin import *
from common.class_common import Flight, EachFlight

reload(sys)
sys.setdefaultencoding('utf-8')

class JsonFlight(GetConfValues, GetJoin):

    def __init__(self):
        pass

    def JsonFlight(self, filename, list):
        
        Dict = defaultdict(dict)

        flight = Flight()
        
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()
            
            Dict[md5]['currency'] = self.GetConfValues(filename, 'section', 'currency')
            Dict[md5]['source'] = self.GetConfValues(filename, 'section', 'source')

            try:
                planetypepath = self.GetConfValues(filename, 'section', 'plane_type')
                Dict[md5]['plane_type'] = self.GetUnder(every, planetypepath)
            except Exception, e:
                Dict[md5]['plane_type'] = flight.plane_type
        
            
            try:
                flightnumberpath = self.GetConfValues(filename, 'section', 'flight_no')
                Dict[md5]['flight_no'] = self.GetUnder(every, flightnumberpath)
            except Exception, e:
                Dict[md5]['flight_no'] = flight.flight_no

            try:
                flight_corppath = self.GetConfValues(filename, 'section', 'flight_corp')
                Dict[md5]['flight_corp'] = self.GetUnder(every, flight_corppath)
            except Exception, e:
                Dict[md5]['flight_corp'] = flight.flight_corp

            try:
                daypath = self.GetConfValues(filename, 'section', 'dept_day')
                Dict[md5]['dept_day'] = self.GetJsonValues(every, daypath)
            except Exception, e:
                Dict[md5]['dept_day'] = flight.dept_day

            try:
                stoptimepath = self.GetConfValues(filename, 'section', 'stoptime')
                Dict[md5]['stoptime'] = self.GetVertical(every, stoptimepath)
            except Exception, e:
                Dict[md5]['stoptime'] = flight.stop_time

            try:
                stop_time_list = Dict[md5]['stoptime'].split('_')
                Dict[md5]['dept_time'] = stop_time_list[0]
                Dict[md5]['dest_time'] = stop_time_list[len(stop_time_list) - 1]
            except Exception, e:
                Dict[md5]['dept_time'] = flight.dept_time
                Dict[md5]['dest_time'] = flight.dest_time

            try:
                stopidpath = self.GetConfValues(filename, 'section', 'stopid')
                Dict[md5]['stop_id'] = self.GetVertical(every, stopidpath)
            except Exception, e:
                Dict[md5]['stop_id'] = flight.stop_id

            try:
                stop_list = Dict[md5]['stop_id'].split('_')
                Dict[md5]['dept_id'] = stop_list[0]
                Dict[md5]['dest_id'] = stop_list[len(stop_list) - 1]
            except Exception, e:
                Dict[md5]['dept_id'] = flight.dept_id
                Dict[md5]['dest_id'] = flight.dest_id

            try:
                durpath = self.GetConfValues(filename, 'section', 'dur')
                Dict[md5]['dur'] = self.GetUnder(every, durpath)
            except Exception, e:
                Dict[md5]['dur'] = flight.dur

            try:
                restpath = self.GetConfValues(filename, 'section', 'rest')
                Dict[md5]['rest'] = self.GetJsonValues(every, restpath)
            except Exception, e:
                Dict[md5]['rest'] = flight.rest

            try:
                stoppath = self.GetConfValues(filename, 'section', 'stop')
                Dict[md5]['stop'] = self.GetJsonValues(every, stoppath)
            except Exception, e:
                Dict[md5]['stop'] = flight.stop

            try:
                return_rulepath = self.GetConfValues(filename, 'section', 'return_rule')
                Dict[md5]['return_rule'] = self.GetUnder(every, return_rulepath)
            except Exception, e:
                Dict[md5]['return_rule'] = flight.return_rule

            try:
                seat_typepath = self.GetConfValues(filename, 'section', 'seat_type')
                Dict[md5]['seat_type'] = self.GetUnder(every, seat_typepath)
            except Exception, e:
                Dict[md5]['seat_type'] = flight.seat_type

            try:
                real_classpath = self.GetConfValues(filename, 'section', 'real_class')
                Dict[md5]['real_class'] = self.GetUnder(every, real_classpath)
            except Exception, e:
                Dict[md5]['real_class'] = flight.real_class

            try:
                surchargepath = self.GetConfValues(filename, 'section', 'surcharge')
                Dict[md5]['surcharge'] = self.GetJsonValues(every, surchargepath)
            except Exception, e:
                Dict[md5]['surcharge'] = flight.surcharge

            try:
                promotionpath = self.GetConfValues(filename, 'section', 'promotion')
                Dict[md5]['promotion'] = self.GetJsonValues(every, promotionpath)
            except Exception, e:
                Dict[md5]['promotion'] = flight.promotion

            try:
                packagepath = self.GetConfValues(filename, 'section', 'package')
                Dict[md5]['package'] = self.GetJsonValues(every, packagepath)
            except Exception, e:
                Dict[md5]['package'] = flight.package

            try:
                Dict[md5]['daydiff'] = flight.daydiff
            except Exception, e:
                Dict[md5]['daydiff'] = flight.daydiff

            try:
                pricepath = self.GetConfValues(filename, 'section', 'price')
                Dict[md5]['price'] = self.GetUnder(every, pricepath)
            except Exception, e:
                Dict[md5]['price'] = flight.price

            try:
                taxpath = self.GetConfValues(filename, 'section', 'tax')
                Dict[md5]['tax'] = self.GetUnder(every, taxpath)
            except Exception, e:
                Dict[md5]['tax'] = flight.tax

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

    gj = GetJsonContent()
    from public.PageTreeDict import *

    pt = PageTreeDict()
    with open('ceair_json', 'r') as f:
        page = f.read()

    dict0 = pt.PageTreeDict(page, 'json')
    list = gj.GetJsonValues(dict0, 'airResultDto|productUnits')
    jf = JsonFlight()
    res = jf.JsonFlight('ceair.ini', list)
    print res
