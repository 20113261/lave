#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict

from common.class_common import Flight, EachFlight
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#处理为插入数据库格式

class DictTuple(object):

    def __init__(self):
        pass
    
    def DictTuple(self,Dict_list):
        
        tickets = []
        flight = Flight()
        for every in Dict_list:
            
            flight.plane_type = every['plane_type']
            
            flight.flight_no = every['flight_no']
                
            flight.flight_corp = every['flight_corp']
            
            flight.dept_day = every['dept_day']
            
            flight.stop_time = every['stoptime']
            
            flight.dept_time = every['dept_time']
            
            flight.dest_time = every['dest_time']

            flight.stop_id = every['stop_id']
            
            flight.dept_id = every['dept_id']
            
            flight.dest_id = every['dest_id']
            
            flight.dur = every['dur']
           
            flight.rest = every['rest']
            
            flight.stop = every['stop']
            
            flight.return_rule = every['return_rule']
            
            flight.seat_type = every['seat_type']
            
            flight.real_class = every['real_class']
            
            flight.surcharge = every['surcharge']
            
            flight.promotion = every['promotion']
            
            flight.package = every['package']
            
            flight.daydiff = every['daydiff']
            
            flight.price = every['price']
            
            flight.tax = every['tax']
            
            flight_tuple = (flight.flight_no,flight.plane_type,flight.flight_corp,flight.dept_id,flight.dest_id,flight.dept_day,\
                    flight.dept_time,flight.dest_time,flight.dur,flight.rest,flight.price,flight.tax,flight.surcharge,\
                    flight.promotion,flight.currency,flight.seat_type,flight.real_class,flight.stop_id,flight.stop_time,\
                    flight.daydiff,flight.source,flight.return_rule,flight.stop)

            tickets.append(flight_tuple)

        return tickets





if __name__ == '__main__':

    import os

    with open('../test/ebooks.html', 'r') as f:
        page = f.read()


    from public.PageTreeDict import *
    from public.GetContent import *
    from public.GetUsedSubtree import *
    gu = GetUsedSubtree()
    pagetree = PageTreeDict()
    html =pagetree.PageTreeDict(page, 'GBK')
    getcontent = GetContent()
    root = getcontent.GetNode(html, 'id=contentContainer')
    every_root = gu.GetUsedSubtree(root, 'id=main|class=airResultsMod resultSetAir|class=airResultsCard')
    ps = HtmlFlight()
    res = ps.HtmlFlight(every_root)
    print res
