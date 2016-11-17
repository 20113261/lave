#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import sys

import hashlib
from common.class_common import RoundFlight
from StopCommon import *

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlRoundFlight(StopCommon):

    def __init__(self):
        pass
    
    def HtmlRoundFlight(self, area, filename, list):
        
        Dict = defaultdict(dict)
        round = RoundFlight()
        for every in list:
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()         
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'currency')
                if con_res == 'error':
                    Dict[md5]['currency'] = round.currency
                else:
                    Dict[md5]['currency'] = con_res 
            except Exception, e:
                Dict[md5]['currency'] = round.currency
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'source')
                if con_res == 'error':
                    Dict[md5]['source'] = round.source
                else:
                    Dict[md5]['source'] = con_res 
            except Exception, e:
                Dict[md5]['source'] = round.source
        
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_day')
                if con_res == 'error':
                    Dict[md5]['dept_day'] = round.dept_day
                else:
                    Dict[md5]['dept_day'] = con_res 
            except Exception, e:
                Dict[md5]['dept_day'] = round.dept_day
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_day')
                if con_res == 'error':
                    Dict[md5]['dest_day'] = round.dest_day
                else:
                    Dict[md5]['dest_day'] = con_res 
            except Exception, e:
                Dict[md5]['dest_day'] = round.dest_day
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_time_A')
                if con_res == 'error':
                    Dict[md5]['dept_time_A'] = round.dept_time_A
                else:
                    Dict[md5]['dept_time_A'] = con_res 
            except Exception, e:
                Dict[md5]['dept_time_A'] = round.dept_time_A
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_time_B')
                if con_res == 'error':
                    Dict[md5]['dept_time_B'] = round.dept_time_B
                else:
                    Dict[md5]['dept_time_B'] = con_res 
            except Exception, e:
                Dict[md5]['dept_time_B'] = round.dept_time_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_time_A')
                if con_res == 'error':
                    Dict[md5]['dest_time_A'] = round.dest_time_A
                else:
                    Dict[md5]['dest_time_A'] = con_res 
            except Exception, e:
                Dict[md5]['dest_time_A'] = round.dest_time_A
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_time_B')
                if con_res == 'error':
                    Dict[md5]['dest_time_B'] = round.dest_time_B
                else:
                    Dict[md5]['dest_time_B'] = con_res 
            except Exception, e:
                Dict[md5]['dest_time_B'] = round.dest_time_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_id_A')
                if con_res == 'error':
                    Dict[md5]['stop_id_A'] = round.stop_id_A
                else:
                    Dict[md5]['stop_id_A'] = con_res 
            except Exception, e:
                Dict[md5]['stop_id_A'] = round.stop_id_A
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_id_B')
                if con_res == 'error':
                    Dict[md5]['stop_id_B'] = round.stop_id_B
                else:
                    Dict[md5]['stop_id_B'] = con_res 
            except Exception, e:
                Dict[md5]['stop_id_B'] = round.stop_id_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_time_A')
                if con_res == 'error':
                    Dict[md5]['stop_time_A'] = round.stop_time_A
                else:
                    Dict[md5]['stop_time_A'] = con_res 
            except Exception, e:
                Dict[md5]['stop_time_A'] = round.stop_time_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_time_B')
                if con_res == 'error':
                    Dict[md5]['stop_time_B'] = round.stop_time_B
                else:
                    Dict[md5]['stop_time_B'] = con_res 
            except Exception, e:
                Dict[md5]['stop_time_B'] = round.stop_time_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_no_A')
                if con_res == 'error':
                    Dict[md5]['flight_no_A'] = round.flight_no_A
                else:
                    Dict[md5]['flight_no_A'] = con_res 
            except Exception, e:
                Dict[md5]['flight_no_A'] = round.flight_no_A
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_no_B')
                if con_res == 'error':
                    Dict[md5]['flight_no_B'] = round.flight_no_B
                else:
                    Dict[md5]['flight_no_B'] = con_res 
            except Exception, e:
                Dict[md5]['flight_no_B'] = round.flight_no_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'airline_A')
                if con_res == 'error':
                    Dict[md5]['airline_A'] = round.airline_A
                else:
                    Dict[md5]['airline_A'] = con_res 
            except Exception, e:
                Dict[md5]['airline_A'] = round.airline_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'airline_B')
                if con_res == 'error':
                    Dict[md5]['airline_B'] = round.airline_B
                else:
                    Dict[md5]['airline_B'] = con_res 
            except Exception, e:
                Dict[md5]['airline_B'] = round.airline_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'daydiff_A')
                if con_res == 'error':
                    Dict[md5]['daydiff_A'] = round.daydiff_A
                else:
                    Dict[md5]['daydiff_A'] = con_res 
            except Exception, e:
                Dict[md5]['daydiff_A'] = round.daydiff_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'daydiff_B')
                if con_res == 'error':
                    Dict[md5]['daydiff_B'] = round.daydiff_B
                else:
                    Dict[md5]['daydiff_B'] = con_res 
            except Exception, e:
                Dict[md5]['daydiff_B'] = round.daydiff_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'price')
                if con_res == 'error':
                    Dict[md5]['price'] = round.price
                else:
                    Dict[md5]['price'] = con_res 
            except Exception, e:
                Dict[md5]['price'] = round.price
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'tax')
                if con_res == 'error':
                    Dict[md5]['tax'] = round.tax
                else:
                    Dict[md5]['tax'] = con_res 
            except Exception, e:
                Dict[md5]['tax'] = round.tax
            try:
                con_res = self.com_Hfunc(every, filename, area, 'seat_type_A')
                if con_res == 'error':
                    Dict[md5]['seat_type_A'] = round.seat_type_A
                else:
                    Dict[md5]['seat_type_A'] = con_res 
            except Exception, e:
                Dict[md5]['seat_type_A'] = round.seat_type_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'seat_type_B')
                if con_res == 'error':
                    Dict[md5]['seat_type_B'] = round.seat_type_B
                else:
                    Dict[md5]['seat_type_B'] = con_res 
            except Exception, e:
                Dict[md5]['seat_type_B'] = round.seat_type_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'real_class_A')
                if con_res == 'error':
                    Dict[md5]['real_class_A'] = round.real_class_A
                else:
                    Dict[md5]['real_class_A'] = con_res 
            except Exception, e:
                Dict[md5]['real_class_A'] = round.real_class_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'real_class_B')
                if con_res == 'error':
                    Dict[md5]['real_class_B'] = round.real_class_B
                else:
                    Dict[md5]['real_class_B'] = con_res 
            except Exception, e:
                Dict[md5]['real_class_B'] = round.real_class_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'return_rule')
                if con_res == 'error':
                    Dict[md5]['return_rule'] = round.return_rule
                else:
                    Dict[md5]['return_rule'] = con_res 
            except Exception, e:
                Dict[md5]['return_rule'] = round.return_rule
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dur_A')
                if con_res == 'error':
                    Dict[md5]['dur_A'] = round.dur_A
                else:
                    Dict[md5]['dur_A'] = con_res 
            except Exception, e:
                Dict[md5]['dur_A'] = round.dur_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dur_B')
                if con_res == 'error':
                    Dict[md5]['dur_B'] = round.dur_B
                else:
                    Dict[md5]['dur_B'] = con_res 
            except Exception, e:
                Dict[md5]['dur_B'] = round.dur_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'rest')
                if con_res == 'error':
                    Dict[md5]['rest'] = round.rest
                else:
                    Dict[md5]['rest'] = con_res 
            except Exception, e:
                Dict[md5]['rest'] = round.rest
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_A')
                if con_res == 'error':
                    Dict[md5]['stop_A'] = round.stop_A
                else:
                    Dict[md5]['stop_A'] = con_res 
            except Exception, e:
                Dict[md5]['stop_A'] = round.stop_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stop_B')
                if con_res == 'error':
                    Dict[md5]['stop_B'] = round.stop_B
                else:
                    Dict[md5]['stop_B'] = con_res 
            except Exception, e:
                Dict[md5]['stop_B'] = round.stop_B
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dept_id')
                if con_res == 'error':
                    Dict[md5]['dept_id'] = round.dept_id
                else:
                    Dict[md5]['dept_id'] = con_res 
            except Exception, e:
                Dict[md5]['dept_id'] = round.dept_id
            try:
                con_res = self.com_Hfunc(every, filename, area, 'dest_id')
                if con_res == 'error':
                    Dict[md5]['dest_id'] = round.dest_id
                else:
                    Dict[md5]['dest_id'] = con_res 
            except Exception, e:
                Dict[md5]['dest_id'] = round.dest_id
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'surcharge')
                if con_res == 'error':
                    Dict[md5]['surcharge'] = round.surcharge
                else:
                    Dict[md5]['surcharge'] = con_res 
            except Exception, e:
                Dict[md5]['surcharge'] = round.surcharge
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'promotion')
                if con_res == 'error':
                    Dict[md5]['promotion'] = round.promotion
                else:
                    Dict[md5]['promotion'] = con_res 
            except Exception, e:
                Dict[md5]['promotion'] = round.promotion
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'plane_no_A')
                if con_res == 'error':
                    Dict[md5]['plane_no_A'] = round.plane_no_A
                else:
                    Dict[md5]['plane_no_A'] = con_res 
            except Exception, e:
                Dict[md5]['plane_no_A'] = round.plane_no_A
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'plane_no_B')
                if con_res == 'error':
                    Dict[md5]['plane_no_B'] = round.plane_no_B
                else:
                    Dict[md5]['plane_no_B'] = con_res 
            except Exception, e:
                Dict[md5]['plane_no_B'] = round.plane_no_B
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'change_rule')
                if con_res == 'error':
                    Dict[md5]['change_rule'] = round.change_rule
                else:
                    Dict[md5]['change_rule'] = con_res 
            except Exception, e:
                Dict[md5]['change_rule'] = round.change_rule

            try:
                con_res = self.com_Hfunc(every, filename, area, 'share_flight')
                if con_res == 'error':
                    Dict[md5]['share_flight'] = round.share_flight
                else:
                    Dict[md5]['share_flight'] = con_res 
            except Exception, e:
                Dict[md5]['share_flight'] = round.share_flight
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'stopby')
                if con_res == 'error':
                    Dict[md5]['stopby'] = round.stopby
                else:
                    Dict[md5]['stopby'] = con_res 
            except Exception, e:
                Dict[md5]['stopby'] = round.stopby
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'baggage')
                if con_res == 'error':
                    Dict[md5]['baggage'] = round.baggage
                else:
                    Dict[md5]['baggage'] = con_res 
            except Exception, e:
                Dict[md5]['baggage'] = round.baggage
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'transit_visa')
                if con_res == 'error':
                    Dict[md5]['transit_visa'] = round.transit_visa
                else:
                    Dict[md5]['transit_visa'] = con_res 
            except Exception, e:
                Dict[md5]['transit_visa'] = round.transit_visa
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'reimbursement')
                if con_res == 'error':
                    Dict[md5]['reimbursement'] = round.reimbursement
                else:
                    Dict[md5]['reimbursement'] = con_res 
            except Exception, e:
                Dict[md5]['reimbursement'] = round.reimbursement
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'flight_meals')
                if con_res == 'error':
                    Dict[md5]['flight_meals'] = round.flight_meals
                else:
                    Dict[md5]['flight_meals'] = con_res 
            except Exception, e:
                Dict[md5]['flight_meals'] = round.flight_meals
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'ticket_type')
                if con_res == 'error':
                    Dict[md5]['ticket_type'] = round.ticket_type
                else:
                    Dict[md5]['ticket_type'] = con_res 
            except Exception, e:
                Dict[md5]['ticket_type'] = round.ticket_type
            
            try:
                con_res = self.com_Hfunc(every, filename, area, 'others_info')
                if con_res == 'error':
                    Dict[md5]['others_info'] = round.others_info
                else:
                    Dict[md5]['others_info'] = con_res 
            except Exception, e:
                Dict[md5]['others_info'] = round.others_info
            
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
 
