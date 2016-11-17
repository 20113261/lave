#!/usr/bin/env python
#coding:utf-8
from common.class_common import Train

class TrainDB(object):
    def __init__(self):
        self.train = Train()

    def trainTupleList(self, dictList):
        result = []
        for edict in dictList:
            each_dict = eval(edict)
            self.train.train_no = each_dict['train_no']
            self.train.train_type = each_dict['train_type']
            self.train.train_corp = each_dict['train_corp']
            self.train.dept_city = each_dict['dept_city']
            self.train.dest_city = each_dict['dest_city']
            self.train.dest_station = each_dict['dest_station']
            self.train.dept_time = each_dict['dept_time']
            self.train.dest_time = each_dict['dest_time']
            self.train.dur = each_dict['dur']
            self.train.price = each_dict['price']
            self.train.tax = each_dict['tax']
            self.train.currency = each_dict['currency']
            self.train.seat_type = each_dict['seat_type']
            self.train.source = each_dict['source']
            self.train.return_rule = each_dict['return_rule']
            self.train.stop = each_dict['stop']
            self.train.stop_station = each_dict['stop_station']
            self.train.dept_day = each_dict['dept_day']
            self.train.real_class = each_dict['real_class']
            self.train.stopid = each_dict['stopid']
            self.train.stoptime = each_dict['stoptime']
            self.train.daydiff = each_dict['daydiff']
            self.train.dept_id = each_dict['dept_id']
            self.train.dest_id = each_dict['dest_id']
            self.train.change_rule = each_dict['change_rule']
            self.train.train_facilities = each_dict['train_facilities']
            self.train.ticket_info = each_dict['ticket_info']
            self.train.electric_ticket = each_dict['electric_ticket']
            self.train.promotion = each_dict['promotion']
            self.train.others_info = each_dict['others_info']
            self.train.facilities = each_dict['facilities']
            self.train.ticket_type = each_dict['ticket_type']
            result.append(tuple(self.train.train_no, self.train.train_type, self.train.train_corp, self.train.dept_city, self.train.dept_id, 
                self.train.dest_city, self.train.dest_id, self.train.dept_day, self.train.dept_time, self.train.dest_time, self.train.dur, 
                self.train.price, self.train.tax, self.train.currency, self.train.seat_type, self.train.real_class, self.train.promotion, 
                self.train.source, self.train.return_rule, self.train.change_rule, self.train.stopid, self.train.stoptime, self.train.daydiff, 
                self.train.stop, self.train.train_facilities, self.train.ticket_type, self.train.electric_ticket, self.train.others_info))
            return result


if __name__ == '__main__':
    a = TrainDB([])
    a.process()
