#!/usr/bin/env python
#coding:utf-8


from common.class_common import Flight


class FlightDB(object):
    def __init__(self):
        self.flight = Flight()

    def flightTupleList(self, dictList):
        result = []
        for edict in dictList:
            each_dict = eval(edict)
            self.flight.flight_no = each_dict['flight_no']
            self.flight.plane_type = each_dict['plane_type']
            self.flight.flight_corp = each_dict['flight_corp']
            self.flight.dept_id = each_dict['dept_id']
            self.flight.dest_id = each_dict['dest_id']
            self.flight.dept_day = each_dict['dept_day']
            self.flight.dept_time = each_dict['dept_time']
            self.flight.dest_time = each_dict['dest_time']
            self.flight.dur = each_dict['dur']
            self.flight.rest = each_dict['rest']
            self.flight.price = each_dict['price']
            self.flight.tax = each_dict['tax']
            self.flight.surcharge = each_dict['surcharge']
            self.flight.promotion = each_dict['promotion']
            self.flight.currency = each_dict['currency']
            self.flight.seat_type = each_dict['seat_type']
            self.flight.real_class = each_dict['real_class']
            self.flight.package = each_dict['package']			
            self.flight.stop_id = each_dict['stop_id']
            self.flight.stop_time = each_dict['stop_time']
            self.flight.dur = each_dict['dur']
            self.flight.daydiff = each_dict['daydiff']
            self.flight.source = each_dict['source']
            self.flight.return_rule = each_dict['return_rule']
            self.flight.stop = each_dict['stop']
            self.flight.flight_corp = each_dict['flight_corp']
            self.flight.change_rule = each_dict['change_rule']
            self.flight.share_flight = each_dict['share_flight']
            self.flight.stopby = each_dict['stopby']
            self.flight.baggage = each_dict['baggage']
            self.flight.transit_visa = each_dict['transit_visa']
            self.flight.reimbursement = each_dict['reimbursement']
            self.flight.flight_meals = each_dict['flight_meals']
            self.flight.others_info = each_dict['others_info']
            self.flight.ticket_type = each_dict['ticket_type']

            flight_tuple = (self.flight.flight_no, self.flight.plane_type, self.flight.flight_corp, self.flight.dept_id,\
                    self.flight.dest_id, self.flight.dept_day, self.flight.dept_time, self.flight.dest_time, self.flight.dur,\
                    self.flight.rest,self.flight.price, self.flight.tax, self.flight.surcharge, self.flight.promotion,\
                    self.flight.currency, self.flight.seat_type, self.flight.real_class, self.flight.package, self.flight.stop_id,\
                    self.flight.stop_time, self.flight.daydiff, self.flight.source, self.flight.return_rule, self.flight.change_rule,\
                    self.flight.stop, self.flight.share_flight, self.flight.stopby, self.flight.baggage, self.flight.transit_visa,\
                    self.flight.reimbursement, self.flight.flight_meals, self.flight.ticket_type, self.flight.others_info)
            result.append(flight_tuple)
        
        return result
