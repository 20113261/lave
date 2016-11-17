#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

import hashlib
from common.class_common import Flight, EachFlight
from StopCommon import *

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlFlight(StopCommon):

    def __init__(self):
        pass
    
    def HtmlFlight(self, area, filename, list):
        
        Dict = defaultdict(dict)
        flight = Flight()
        for every in list:
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'currency')
                if con_res == 'error':
                    Dict[md5]['currency'] = flight.currency
                else:
                    Dict[md5]['currency'] = con_res 
            except Exception, e:
                Dict[md5]['currency'] = flight.currency
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'source')
                if con_res == 'error':
                    Dict[md5]['source'] = flight.source
                else:
                    Dict[md5]['source'] = con_res 
            except Exception, e:
                Dict[md5]['source'] = flight.source
        
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_day')
                if con_res == 'error':
                    Dict[md5]['dept_day'] = flight.dept_day
                else:
                    Dict[md5]['dept_day'] = con_res 
            except Exception, e:
                Dict[md5]['dept_day'] = flight.dept_day
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_time')
                if con_res == 'error':
                    Dict[md5]['dept_time'] = flight.dept_time
                else:
                    Dict[md5]['dept_time'] = con_res 
            except Exception, e:
                Dict[md5]['dept_time'] = flight.dept_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_id')
                if con_res == 'error':
                    Dict[md5]['dept_id'] = flight.dept_id
                else:
                    Dict[md5]['dept_id'] = con_res 
            except Exception, e:
                Dict[md5]['dept_id'] = flight.dept_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_id')
                if con_res == 'error':
                    Dict[md5]['dest_id'] = flight.dest_id
                else:
                    Dict[md5]['dest_id'] = con_res 
            except Exception, e:
                Dict[md5]['dest_id'] = flight.dest_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_time')
                if con_res == 'error':
                    Dict[md5]['dest_time'] = flight.dest_time
                else:
                    Dict[md5]['dest_time'] = con_res 
            except Exception, e:
                Dict[md5]['dest_time'] = flight.dest_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'seat_type')
                if con_res == 'error':
                    Dict[md5]['seat_type'] = flight.seat_type
                else:
                    Dict[md5]['seat_type'] = con_res 
            except Exception, e:
                Dict[md5]['seat_type'] = flight.seat_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'real_class')
                if con_res == 'error':
                    Dict[md5]['real_class'] = flight.real_class
                else:
                    Dict[md5]['real_class'] = con_res 
            except Exception, e:
                Dict[md5]['real_class'] = flight.real_class
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'package')
                if con_res == 'error':
                    Dict[md5]['package'] = flight.package
                else:
                    Dict[md5]['package'] = con_res 
            except Exception, e:
                Dict[md5]['package'] = flight.package
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stopid')
                if con_res == 'error':
                    Dict[md5]['stop_id'] = flight.stop_id
                else:
                    Dict[md5]['stop_id'] = con_res 
            except Exception, e:
                Dict[md5]['stop_id'] = flight.stop_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stoptime')
                if con_res == 'error':
                    Dict[md5]['stop_time'] = flight.stop_time
                else:
                    Dict[md5]['stop_time'] = con_res 
            except Exception, e:
                Dict[md5]['stop_time'] = flight.stop_time
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_no')
                if con_res == 'error':
                    Dict[md5]['flight_no'] = flight.flight_no
                else:
                    Dict[md5]['flight_no'] = con_res 
            except Exception, e:
                Dict[md5]['flight_no'] = flight.flight_no
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_corp')
                if con_res == 'error':
                    Dict[md5]['flight_corp'] = flight.flight_corp
                else:
                    Dict[md5]['flight_corp'] = con_res 
            except Exception, e:
                Dict[md5]['flight_corp'] = flight.flight_corp
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'daydiff')
                if con_res == 'error':
                    Dict[md5]['daydiff'] = flight.daydiff
                else:
                    Dict[md5]['daydiff'] = con_res 
            except Exception, e:
                Dict[md5]['daydiff'] = flight.daydiff
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'price')
                if con_res == 'error':
                    Dict[md5]['price'] = flight.price
                else:
                    Dict[md5]['price'] = con_res 
            except Exception, e:
                Dict[md5]['price'] = flight.price
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'tax')
                if con_res == 'error':
                    Dict[md5]['tax'] = flight.tax
                else:
                    Dict[md5]['tax'] = con_res 
            except Exception, e:
                Dict[md5]['tax'] = flight.tax
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'return_rule')
                if con_res == 'error':
                    Dict[md5]['return_rule'] = flight.return_rule
                else:
                    Dict[md5]['return_rule'] = con_res 
            except Exception, e:
                Dict[md5]['return_rule'] = flight.return_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dur')
                if con_res == 'error':
                    Dict[md5]['dur'] = flight.dur
                else:
                    Dict[md5]['dur'] = con_res 
            except Exception, e:
                Dict[md5]['dur'] = flight.dur
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'rest')
                if con_res == 'error':
                    Dict[md5]['rest'] = flight.rest
                else:
                    Dict[md5]['rest'] = con_res 
            except Exception, e:
                Dict[md5]['rest'] = flight.rest
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop')
                if con_res == 'error':
                    Dict[md5]['stop'] = flight.stop
                else:
                    Dict[md5]['stop'] = con_res 
            except Exception, e:
                Dict[md5]['stop'] = flight.stop
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'surcharge')
                if con_res == 'error':
                    Dict[md5]['surcharge'] = flight.surcharge
                else:
                    Dict[md5]['surcharge'] = con_res 
            except Exception, e:
                Dict[md5]['surcharge'] = flight.surcharge
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'promotion')
                if con_res == 'error':
                    Dict[md5]['promotion'] = flight.promotion
                else:
                    Dict[md5]['promotion'] = con_res 
            except Exception, e:
                Dict[md5]['promotion'] = flight.promotion
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'plane_type')
                if con_res == 'error':
                    Dict[md5]['plane_type'] = flight.plane_type
                else:
                    Dict[md5]['plane_type'] = con_res 
            except Exception, e:
                Dict[md5]['plane_type'] = flight.plane_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'change_rule')
                if con_res == 'error':
                    Dict[md5]['change_rule'] = flight.change_rule
                else:
                    Dict[md5]['change_rule'] = con_res 
            except Exception, e:
                Dict[md5]['change_rule'] = flight.change_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'share_flight')
                if con_res == 'error':
                    Dict[md5]['share_flight'] = flight.share_flight
                else:
                    Dict[md5]['share_flight'] = con_res 
            except Exception, e:
                Dict[md5]['share_flight'] = flight.share_flight
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stopby')
                if con_res == 'error':
                    Dict[md5]['stopby'] = flight.stopby
                else:
                    Dict[md5]['stopby'] = con_res 
            except Exception, e:
                Dict[md5]['stopby'] = flight.stopby
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'baggage')
                if con_res == 'error':
                    Dict[md5]['baggage'] = flight.baggage
                else:
                    Dict[md5]['baggage'] = con_res 
            except Exception, e:
                Dict[md5]['baggage'] = flight.baggage
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'transit_visa')
                if con_res == 'error':
                    Dict[md5]['transit_visa'] = flight.transit_visa
                else:
                    Dict[md5]['transit_visa'] = con_res 
            except Exception, e:
                Dict[md5]['transit_visa'] = flight.transit_visa
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'reimbursement')
                if con_res == 'error':
                    Dict[md5]['reimbursement'] = flight.reimbursement
                else:
                    Dict[md5]['reimbursement'] = con_res 
            except Exception, e:
                Dict[md5]['reimbursement'] = flight.reimbursement
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_meals')
                if con_res == 'error':
                    Dict[md5]['flight_meals'] = flight.flight_meals
                else:
                    Dict[md5]['flight_meals'] = con_res 
            except Exception, e:
                Dict[md5]['flight_meals'] = flight.flight_meals
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'ticket_type')
                if con_res == 'error':
                    Dict[md5]['ticket_type'] = flight.ticket_type
                else:
                    Dict[md5]['ticket_type'] = con_res 
            except Exception, e:
                Dict[md5]['ticket_type'] = flight.ticket_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'others_info')
                if con_res == 'error':
                    Dict[md5]['others_info'] = flight.others_info
                else:
                    Dict[md5]['others_info'] = con_res 
            except Exception, e:
                Dict[md5]['others_info'] = flight.others_info
            
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
 
