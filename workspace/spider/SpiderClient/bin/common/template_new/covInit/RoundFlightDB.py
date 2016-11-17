#!/usr/bin/env python
#coding:utf-8
from common.class_common import RoundFlight

class RoundFlightDB(object):
    def __init__(self):
        self.roundflight = RoundFlight()

    def roundflightTupleList(self, dictList):
        result = []
        for edict in dictList:
            each_dict = eval(edict)
            self.roundflight.dept_id = each_dict['dept_id']
            self.roundflight.dest_id = each_dict['dest_id']
            self.roundflight.dept_day = each_dict['dept_day']
            self.roundflight.dest_day = each_dict['dest_day']
            self.roundflight.price = each_dict['price']
            self.roundflight.tax = each_dict['tax']
            self.roundflight.surcharge = each_dict['surcharge']
            self.roundflight.promotion = each_dict['promotion']
            self.roundflight.currency = each_dict['currency']
            self.roundflight.source = each_dict['source']
            self.roundflight.return_rule = each_dict['return_rule']
            self.roundflight.flight_no_A = each_dict['flight_no_A']
            self.roundflight.airline_A = each_dict['airline_A']
            self.roundflight.plane_no_A = each_dict['plane_no_A']
            self.roundflight.dept_time_A = each_dict['dept_time_A']
            self.roundflight.dest_time_A = each_dict['dest_time_A']
            self.roundflight.dur_A = each_dict['dur_A']
            self.roundflight.seat_type_A = each_dict['seat_type_A']
            self.roundflight.real_class_A = each_dict['real_class_A']
            self.roundflight.stop_id_A = each_dict['stop_id_A']
            self.roundflight.stop_time_A = each_dict['stop_time_A']
            self.roundflight.daydiff_A = each_dict['daydiff_A']
            self.roundflight.stop_A = each_dict['stop_A']
            self.roundflight.flight_no_B = each_dict['flight_no_B']
            self.roundflight.airline_B = each_dict['airline_B']
            self.roundflight.plane_no_B = each_dict['plane_no_B']
            self.roundflight.dept_time_B = each_dict['dept_time_B']
            self.roundflight.dest_time_B = each_dict['dest_time_B']
            self.roundflight.dur_B = each_dict['dur_B']
            self.roundflight.seat_type_B = each_dict['seat_type_B']
            self.roundflight.real_class_B = each_dict['real_class_B']
            self.roundflight.stop_id_B = each_dict['stop_id_B']
            self.roundflight.stop_time_B = each_dict['stop_time_B']
            self.roundflight.daydiff_B = each_dict['daydiff_B']
            self.roundflight.stop_B = each_dict['stop_B']
            self.roundflight.change_rule = each_dict['change_rule']
            self.roundflight.share_flight_A = each_dict['share_flight_A']
            self.roundflight.share_flight_B = each_dict['share_flight_B']
            self.roundflight.stopby_A = each_dict['stopby_A']
            self.roundflight.stopby_B= each_dict['stopby_B']
            self.roundflight.baggage = each_dict['baggage']
            self.roundflight.transit_visa = each_dict['transit_visa']
            self.roundflight.reimbursement = each_dict['reimbursement']
            self.roundflight.flight_meals = each_dict['flight_meals']
            self.roundflight.ticket_type = each_dict['ticket_type']
            self.roundflight.others_info = each_dict['others_info']

            flight_tuple = (self.roundflight.dept_id, self.roundflight.dest_id, self.roundflight.dept_day, self.roundflight.dest_day, 
                self.roundflight.price, self.roundflight.tax, self.roundflight.surcharge, self.roundflight.promotion, self.roundflight.currency,
                self.roundflight.source, self.roundflight.return_rule, self.roundflight.flight_no_A, self.roundflight.airline_A,
                self.roundflight.plane_no_A, self.roundflight.dept_time_A, self.roundflight.dest_time_A, self.roundflight.dur_A,
                self.roundflight.seat_type_A, self.roundflight.real_class_A, self.roundflight.stop_id_A, self.roundflight.stop_time_A,
                self.roundflight.daydiff_A, self.roundflight.stop_A, self.roundflight.flight_no_B, self.roundflight.airline_B, self.roundflight.plane_no_B,
                self.roundflight.dept_time_B, self.roundflight.dest_time_B, self.roundflight.dur_B, self.roundflight.seat_type_B,
                self.roundflight.real_class_B, self.roundflight.stop_id_B, self.roundflight.stop_time_B, self.roundflight.daydiff_B,
                self.roundflight.stop_B, self.roundflight.change_rule, self.roundflight.share_flight_A, self.roundflight.share_flight_B,
                self.roundflight.stopby_A, self.roundflight.stopby_B, self.roundflight.baggage, self.roundflight.transit_visa,
                self.roundflight.reimbursement,self.roundflight.flight_meals, self.roundflight.ticket_type, self.others_info)
            result.append(flight_tuple)
        return result

if __name__ == '__main__':
    a = RoundFlightDB([])
    a.roundflightTupleList()
