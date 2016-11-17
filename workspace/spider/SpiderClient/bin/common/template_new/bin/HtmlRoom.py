#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

from confParser import *
import hashlib
from StopCommon import *
from common.class_common import Room

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlRoom(StopCommon):

    def __init__(self):
        pass
    
    def HtmlRoom(self, page, area, filename, list):
        
        Dict = defaultdict(dict)
        room = Room()
        for every in list:
            
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'hotel_name') 
                if con_res == 'error':
                    Dict[md5]['hotel_name'] = room.hotel_name
                else:
                    Dict[md5]['hotel_name'] = con_res
            except Exception, e:
                Dict[md5]['hotel_name'] = room.hotel_name

            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'city') 
                if con_res == 'error':
                    Dict[md5]['city'] = room.city
                else:
                    Dict[md5]['city'] = con_res
            except Exception, e:
                Dict[md5]['city'] = room.city
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'source') 
                if con_res == 'error':
                    Dict[md5]['source'] = room.source 
                else:
                    Dict[md5]['source'] = con_res
            except Exception, e:
                Dict[md5]['source'] = room.source
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'source_hotelid') 
                if con_res == 'error':
                    Dict[md5]['source_hotelid'] = room.source_hotelid 
                else:
                    Dict[md5]['source_hotelid'] = con_res
            except Exception, e:
                Dict[md5]['source_hotelid'] = room.source_hotelid
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'source_roomid') 
                if con_res == 'error':
                    Dict[md5]['source_roomid'] = room.source_roomid 
                else:
                    Dict[md5]['source_roomid'] = con_res
            except Exception, e:
                Dict[md5]['source_roomid'] = room.source_roomid
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'real_source') 
                if con_res == 'error':
                    Dict[md5]['real_source'] = room.real_source 
                else:
                    Dict[md5]['real_source'] = con_res
            except Exception, e:
                Dict[md5]['real_source'] = room.real_source
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'room_type') 
                if con_res == 'error':
                    Dict[md5]['room_type'] = room.room_type 
                else:
                    Dict[md5]['room_type'] = con_res
            except Exception, e:
                Dict[md5]['room_type'] = room.room_type
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'occupancy') 
                if con_res == 'error':
                    Dict[md5]['occupancy'] = room.occupancy 
                else:
                    Dict[md5]['occupancy'] = con_res
            except Exception, e:
                Dict[md5]['occupancy'] = room.occupancy
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'bed_type') 
                if con_res == 'error':
                    Dict[md5]['bed_type'] = room.bed_type 
                else:
                    Dict[md5]['bed_type'] = con_res
            except Exception, e:
                Dict[md5]['bed_type'] = room.bed_type
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'size') 
                if con_res == 'error':
                    Dict[md5]['size'] = room.size 
                else:
                    Dict[md5]['size'] = con_res
            except Exception, e:
                Dict[md5]['size'] = room.size
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'floor') 
                if con_res == 'error':
                    Dict[md5]['floor'] = room.floor 
                else:
                    Dict[md5]['floor'] = con_res
            except Exception, e:
                Dict[md5]['floor'] = room.floor
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'check_in') 
                if con_res == 'error':
                    Dict[md5]['check_in'] = room.check_in 
                else:
                    Dict[md5]['check_in'] = con_res
            except Exception, e:
                Dict[md5]['check_in'] = room.check_in
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'check_out') 
                if con_res == 'error':
                    Dict[md5]['check_out'] = room.check_out 
                else:
                    Dict[md5]['check_out'] = con_res
            except Exception, e:
                Dict[md5]['check_out'] = room.check_out
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'rest') 
                if con_res == 'error':
                    Dict[md5]['rest'] = room.rest 
                else:
                    Dict[md5]['rest'] = con_res
            except Exception, e:
                Dict[md5]['rest'] = room.rest
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'price') 
                if con_res == 'error':
                    Dict[md5]['price'] = room.price 
                else:
                    Dict[md5]['price'] = con_res
            except Exception, e:
                Dict[md5]['price'] = room.price
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'tax') 
                if con_res == 'error':
                    Dict[md5]['tax'] = room.tax 
                else:
                    Dict[md5]['tax'] = con_res
            except Exception, e:
                Dict[md5]['tax'] = room.tax
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'currency') 
                if con_res == 'error':
                    Dict[md5]['currency'] = room.currency 
                else:
                    Dict[md5]['currency'] = con_res
            except Exception, e:
                Dict[md5]['currency'] = room.currency
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'pay_method') 
                if con_res == 'error':
                    Dict[md5]['pay_method'] = room.pay_method 
                else:
                    Dict[md5]['pay_method'] = con_res
            except Exception, e:
                Dict[md5]['pay_method'] = room.pay_method
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'is_extrabed') 
                if con_res == 'error':
                    Dict[md5]['is_extrabed'] = room.is_extrabed 
                else:
                    Dict[md5]['is_extrabed'] = con_res
            except Exception, e:
                Dict[md5]['is_extrabed'] = room.is_extrabed
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'is_extrabed_free') 
                if con_res == 'error':
                    Dict[md5]['is_extrabed_free'] = room.is_extrabed_free 
                else:
                    Dict[md5]['is_extrabed_free'] = con_res
            except Exception, e:
                Dict[md5]['is_extrabed_free'] = room.is_extrabed_free
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'has_breakfast') 
                if con_res == 'error':
                    Dict[md5]['has_breakfast'] = room.has_breakfast 
                else:
                    Dict[md5]['has_breakfast'] = con_res
            except Exception, e:
                Dict[md5]['has_breakfast'] = room.has_breakfast
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'is_breakfast_free') 
                if con_res == 'error':
                    Dict[md5]['is_breakfast_free'] = room.is_breakfast_free
                else:
                    Dict[md5]['is_breakfast_free'] = con_res
            except Exception, e:
                Dict[md5]['is_breakfast_free'] = room.is_breakfast_free
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'is_cancel_free') 
                if con_res == 'error':
                    Dict[md5]['is_cancel_free'] = room.is_cancel_free
                else:
                    Dict[md5]['is_cancel_free'] = con_res
            except Exception, e:
                Dict[md5]['is_cancel_free'] = room.is_cancel_free
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'extrabed_rule') 
                if con_res == 'error':
                    Dict[md5]['extrabed_rule'] = room.extrabed_rule
                else:
                    Dict[md5]['extrabed_rule'] = con_res
            except Exception, e:
                Dict[md5]['extrabed_rule'] = room.extrabed_rule
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'return_rule') 
                if con_res == 'error':
                    Dict[md5]['return_rule'] = room.return_rule
                else:
                    Dict[md5]['return_rule'] = con_res
            except Exception, e:
                Dict[md5]['return_rule'] = room.return_rule
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'change_rule') 
                if con_res == 'error':
                    Dict[md5]['change_rule'] = room.change_rule
                else:
                    Dict[md5]['change_rule'] = con_res
            except Exception, e:
                Dict[md5]['change_rule'] = room.change_rule
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'room_desc') 
                if con_res == 'error':
                    Dict[md5]['room_desc'] = room.room_desc
                else:
                    Dict[md5]['room_desc'] = con_res
            except Exception, e:
                Dict[md5]['room_desc'] = room.room_desc
            
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'others_info') 
                if con_res == 'error':
                    Dict[md5]['others_info'] = room.others_info
                else:
                    Dict[md5]['others_info'] = con_res
            except Exception, e:
                Dict[md5]['others_info'] = room.others_info

            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'req')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['req'] = con_res
            except Exception, e:
                Dict[md5]['req'] = 'NULL'

            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'other_0')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_0'] = con_res
            except Exception, e:
                Dict[md5]['other_0'] = 'NULL'
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'other_1')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_1'] = con_res
            except Exception, e:
                Dict[md5]['other_1'] = 'NULL'
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'other_2')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_2'] = con_res
            except Exception, e:
                Dict[md5]['other_2'] = 'NULL'
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'other_3')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_3'] = con_res
            except Exception, e:
                Dict[md5]['other_3'] = 'NULL'
            try:
                con_res = self.com_HDfunc(page, every, filename, area, 'other_4')
                if con_res == 'error':
                    continue
                else:
                    Dict[md5]['other_4'] = con_res
            except Exception, e:
                Dict[md5]['other_4'] = 'NULL'


        return Dict


