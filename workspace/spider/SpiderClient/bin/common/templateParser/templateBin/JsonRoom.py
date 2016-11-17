#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

from confParser import *
import hashlib
from GetJoin import *
from common.class_common import Room

reload(sys)
sys.setdefaultencoding('utf-8')

class JsonRoom(GetConfValues, GetJoin):

    def __init__(self):
        pass
    
    def JsonRoom(self,filename, list):
        
        Dict = defaultdict(dict)
        room = Room()
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         

            Dict[md5]['currency'] = self.GetConfValues(filename, 'section', 'currency')
            Dict[md5]['source'] = self.GetConfValues(filename, 'section', 'source')
            
            try:
                roomtypepath = self.GetConfValues(filename, 'section', 'room_type')
                Dict[md5]['room_type'] = self.GetUnder(every, roomtypepath)
            except Exception, e:
                Dict[md5]['room_type'] = room.room_type
            
            try:
                hotel_namepath = self.GetConfValues(filename, 'section', 'hotel_name')
                Dict[md5]['hotel_name'] = self.GetUnder(every, hotel_namepath)
            except Exception, e:
                Dict[md5]['hotel_name'] = room.hotel_name 
            
            try:
                citypath = self.GetConfValues(filename, 'section', 'city')
                Dict[md5]['city'] = self.GetUnder(every, citypath)
            except Exception, e:
                Dict[md5]['city'] = room.city 
            
            try:
                source_hotelidpath = self.GetConfValues(filename, 'section', 'source_hotelid')
                Dict[md5]['source_houtelid'] = self.GetUnder(every, source_hotelidpath)
            except Exception, e:
                Dict[md5]['source_houtelid'] = room.source_houtelid
            
            try:
                source_roomidpath = self.GetConfValues(filename, 'section', 'source_roomid')
                Dict[md5]['source_roomid'] = self.GetUnder(every, source_roomidpath)
            except Exception, e:
                Dict[md5]['source_roomid'] = room.source_roomid 
            
            try:
                real_sourcepath = self.GetConfValues(filename, 'section', 'real_source')
                Dict[md5]['real_source'] = self.GetUnder(every, real_sourcepath)
            except Exception, e:
                Dict[md5]['real_source'] = room.real_source
            
            try:
                occupancypath = self.GetConfValues(filename, 'section', 'occupancy')
                Dict[md5]['occupancy'] = self.GetUnder(every, occupancypath)
            except Exception, e:
                Dict[md5]['occupancy'] = room.occupancy
            
            try:
                bed_typepath = self.GetConfValues(filename, 'section', 'bed_type')
                Dict[md5]['bed_type'] = self.GetUnder(every, bed_typepath)
            except Exception, e:
                Dict[md5]['bed_type'] = room.bed_type 
            
            try:
                sizepath = self.GetConfValues(filename, 'section', 'size')
                Dict[md5]['size'] = self.GetUnder(every, sizepath)
            except Exception, e:
                Dict[md5]['size'] = room.size
            
            try:
                floorpath = self.GetConfValues(filename, 'section', 'floor')
                Dict[md5]['floor'] = self.GetUnder(every, floorpath)
            except Exception, e:
                Dict[md5]['floor'] = room.floor
            
            try:
                check_inpath = self.GetConfValues(filename, 'section', 'check_in')
                Dict[md5]['check_in'] = self.GetUnder(every, check_inpath)
            except Exception, e:
                Dict[md5]['check_in'] = room.check_in
            
            try:
                check_outpath = self.GetConfValues(filename, 'section', 'check_out')
                Dict[md5]['check_out'] = self.GetUnder(every, check_outpath)
            except Exception, e:
                Dict[md5]['check_out'] = room.check_out
            
            try:
                restpath = self.GetConfValues(filename, 'section', 'rest')
                Dict[md5]['rest'] = self.GetUnder(every, restpath)
            except Exception, e:
                Dict[md5]['rest'] = room.rest

            try:
                pricepath = self.GetConfValues(filename, 'section', 'price')
                Dict[md5]['price'] = self.GetUnder(every, pricepath)
            except Exception, e:
                Dict[md5]['price'] = room.price
            
            try: 
                taxpath = self.GetConfValues(filename, 'section', 'tax')
                Dict[md5]['tax'] = self.GetUnder(every, taxpath)
            except Exception, e:
                Dict[md5]['tax'] = room.tax
            
            try: 
                is_extrabedpath = self.GetConfValues(filename, 'section', 'is_extrabed')
                Dict[md5]['is_extrabed'] = self.GetUnder(every, is_extrabedpath)
            except Exception, e:
                Dict[md5]['is_extrabed'] = room.is_extrabed
            
            try: 
                is_extrabed_freepath = self.GetConfValues(filename, 'section', 'is_extrabed_free')
                Dict[md5]['is_extrabed_free'] = self.GetUnder(every, is_extrabed_freepath)
            except Exception, e:
                Dict[md5]['is_extrabed_free'] = room.is_extrabed_free
            
            try: 
                has_breakfastpath = self.GetConfValues(filename, 'section', 'has_breakfast')
                Dict[md5]['has_breakfast'] = self.GetUnder(every, has_breakfastpath)
            except Exception, e:
                Dict[md5]['has_breakfast'] = room.has_breakfast
            
            try: 
                is_extrabed_freepath = self.GetConfValues(filename, 'section', 'is_breakfast_free')
                Dict[md5]['is_breakfast_free'] = self.GetUnder(every, is_breakfast_freepath)
            except Exception, e:
                Dict[md5]['is_breakfast_free'] = room.is_breakfast_free
            
            try: 
                is_cancel_freepath = self.GetConfValues(filename, 'section', 'is_cancel_free')
                Dict[md5]['is_cancel_free'] = self.GetUnder(every, is_cancel_freepath)
            except Exception, e:
                Dict[md5]['is_cancel_free'] = room.is_cancel_free
            
            try:
                room_descpath = self.GetConfValues(filename, 'section', 'room_desc')
                Dict[md5]['room_desc'] = self.GetUnder(every, room_descpath)
            except Exception, e:
                Dict[md5]['room_desc'] = room.room_desc

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

