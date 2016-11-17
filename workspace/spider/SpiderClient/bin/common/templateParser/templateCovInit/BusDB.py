#!usr/env/python
#coding=UTF-8
from common.class_common import Bus

class BusDB():
    
    def __init__(self):
        self.bus = Bus()

    def busTupleList(self,ticket_list):

        result = []
        for edict in ticket_list:
            each_dict = eval(edict)
            self.bus.dept_city = each_dict['dept_city']
            self.bus.dest_city = each_dict['dest_city']
            self.bus.dept_station = each_dict['dept_station']
            self.bus.dest_station = each_dict['dest_station']
            self.bus.dept_day = each_dict['dept_day']
            self.bus.dept_time = each_dict['dept_time']
            self.bus.dest_time = each_dict['dest_time']
            self.bus.dur = each_dict['dur']
            self.bus.price = each_dict['price']
            self.bus.currency = each_dict['currency']
            self.bus.source = each_dict['source']
            self.bus.corp = each_dict['corp']
            self.bus.tax = each_dict['tax']
            self.bus.return_rule = each_dict['return_rule']
            self.bus.daydiff = each_dict['daydiff']
            self.bus.rest = each_dict['rest']
            self.bus.change_rule = each_dict['change_rule']
            self.bus.ticket_type = each_dict['ticket_type']

            bus_tuple = (self.bus.dept_city,self.bus.dest_city,self.bus.dept_station,self.bus.dest_station,self.bus.dept_day,self.bus.dept_time,self.bus.dest_time,\
                self.bus.dur,self.bus.price,self.bus.currency,self.bus.source,self.bus.corp,self.bus.corp,self.bus.tax,self.bus.return_rule,\
                self.bus.daydiff,self.bus.rest,self.bus.change_rule,self.bus.ticket_type)
            result.append(bus_tuple)

        return result
