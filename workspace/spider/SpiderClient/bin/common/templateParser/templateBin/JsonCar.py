#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

from confParser import *
import hashlib
from GetJoin import *
from common.class_common import Car

reload(sys)
sys.setdefaultencoding('utf-8')

class JsonCar(GetConfValues, GetJoin):

    def __init__(self):
        pass
    
    def JsonCar(self,filename, list):
        
        Dict = defaultdict(dict)
        car = Car()
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         

            Dict[md5]['currency'] = self.GetConfValues(filename, 'section', 'currency')
            Dict[md5]['source'] = self.GetConfValues(filename, 'section', 'source')
            
            try:
                companypath = self.GetConfValues(filename, 'section','company')
                Dict[md5]['company'] = self.GetUnder(every, companypath)
            except Exception, e:
                Dict[md5]['company'] = car.company
            
            try:
                car_typepath = self.GetConfValues(filename, 'section','car_type')
                Dict[md5]['car_type'] = self.GetUnder(every, car_typepath)
            except Exception, e:
                Dict[md5]['car_type'] = car.car_type
            
            try:
                car_descpath = self.GetConfValues(filename, 'section','car_desc')
                Dict[md5]['car_desc'] = self.GetUnder(every, car_descpath)
            except Exception, e:
                Dict[md5]['car_desc'] = car.car_desc
            
            try:
                car_imagepath = self.GetConfValues(filename, 'section','car_image')
                Dict[md5]['car_image'] = self.GetUnder(every, car_imagepath)
            except Exception, e:
                Dict[md5]['car_image'] = car.car_image
            
            try:
                list_pricepath = self.GetConfValues(filename, 'section','list_price')
                Dict[md5]['list_price'] = self.GetUnder(every, list_pricepath)
            except Exception, e:
                Dict[md5]['list_price'] = car.list_price
            
            try:
                restpath = self.GetConfValues(filename, 'section','rest')
                Dict[md5]['rest'] = self.GetUnder(every, restpath)
            except Exception, e:
                Dict[md5]['rest'] = car.rest
            
            try:
                rent_citypath = self.GetConfValues(filename, 'section','rent_city')
                Dict[md5]['rent_city'] = self.GetUnder(every, rent_citypath)
            except Exception, e:
                Dict[md5]['rent_city'] = car.rent_city
            
            try:
                return_citypath = self.GetConfValues(filename, 'section','return_city')
                Dict[md5]['return_city'] = self.GetUnder(every, return_citypath)
            except Exception, e:
                Dict[md5]['return_city'] = car.return_city
            
            try:
                rent_storepath = self.GetConfValues(filename, 'section','rent_store')
                Dict[md5]['rent_store'] = self.GetUnder(every, rent_storepath)
            except Exception, e:
                Dict[md5]['rent_store'] = car.rent_store
            
            try:
                return_storepath = self.GetConfValues(filename, 'section','return_store')
                Dict[md5]['return_store'] = self.GetUnder(every, return_storepath)
            except Exception, e:
                Dict[md5]['return_store'] = car.return_store
            
            try:
                rent_timepath = self.GetConfValues(filename, 'section','rent_time')
                Dict[md5]['rent_time'] = self.GetUnder(every, rent_timepath)
            except Exception, e:
                Dict[md5]['rent_time'] = car.rent_time
            
            try:
                return_timepath = self.GetConfValues(filename, 'section','return_time')
                Dict[md5]['return_time'] = self.GetUnder(every, return_timepath)
            except Exception, e:
                Dict[md5]['return_time'] = car.return_time
            
            try:
                rent_areapath = self.GetConfValues(filename, 'section','rent_area')
                Dict[md5]['rent_area'] = self.GetUnder(every, rent_areapath)
            except Exception, e:
                Dict[md5]['rent_area'] = car.rent_area
            
            try:
                return_areapath = self.GetConfValues(filename, 'section','return_area')
                Dict[md5]['return_area'] = self.GetUnder(every, return_areapath)
            except Exception, e:
                Dict[md5]['return_area'] = car.return_area
            
            try:
                is_automaticpath = self.GetConfValues(filename, 'section','is_automatic')
                Dict[md5]['is_automatic'] = self.GetUnder(every, is_automaticpath)
            except Exception, e:
                Dict[md5]['is_automatic'] = car.is_automatic
            
            try:
                path = self.GetConfValues(filename, 'section','baggages')
                Dict[md5]['baggages'] = self.GetUnder(every, baggagespath)
            except Exception, e:
                Dict[md5]['baggages'] = car.baggages
            
            try:
                passengerspath = self.GetConfValues(filename, 'section','passengers')
                Dict[md5]['passengers'] = self.GetUnder(every, passengerspath)
            except Exception, e:
                Dict[md5]['passengers'] = car.passengers
            
            try:
                pay_methodpath = self.GetConfValues(filename, 'section','pay_method')
                Dict[md5]['pay_method'] = self.GetUnder(every, pay_methodpath)
            except Exception, e:
                Dict[md5]['pay_method'] = car.pay_method
            
            try:
                insurancepath = self.GetConfValues(filename, 'section','insurance')
                Dict[md5]['insurance'] = self.GetUnder(every, insurancepath)
            except Exception, e:
                Dict[md5]['insurance'] = car.insurance
            
            try:
                fuel_strategypath = self.GetConfValues(filename, 'section','fuel_strategy')
                Dict[md5]['fuel_strategy'] = self.GetUnder(every, fuel_strategypath)
            except Exception, e:
                Dict[md5]['fuel_strategy'] = car.fuel_strategy
            
            try:
                promotionpath = self.GetConfValues(filename, 'section','promotion')
                Dict[md5]['promotion'] = self.GetUnder(every, promotionpath)
            except Exception, e:
                Dict[md5]['promotion'] = car.promotion
            
            try:
                licensepath = self.GetConfValues(filename, 'section','license')
                Dict[md5]['license'] = self.GetUnder(every, licensepath)
            except Exception, e:
                Dict[md5]['license'] = car.license
            
            try:
                pricepath = self.GetConfValues(filename, 'section', 'price')
                Dict[md5]['price'] = self.GetUnder(every, pricepath)
            except Exception, e:
                Dict[md5]['price'] = car.price
            
            try: 
                taxpath = self.GetConfValues(filename, 'section', 'tax')
                Dict[md5]['tax'] = self.GetUnder(every, taxpath)
            except Exception, e:
                Dict[md5]['tax'] = car.tax

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


