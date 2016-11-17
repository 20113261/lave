#! /usr/bin/env python
#coding=utf-8

import sys
from city_common import City

def judge_error(tickets, taskcontent):
    error = 1

    try:
        infos = taskcontent.split('&')
        dept_id, dest_id = infos[0], infos[1]
    except Exception, e:
        print 'ebookerFlight :: parse taskcontent failed'
        return error

    try:
        for each_ticket in tickets:
            if each_ticket[3] == dept_id and each_ticket[4] == dest_id:
                error = 0
                break
    except:
        pass

    return error


def judge_train_error(tickets, taskcontent):
    error = 1
    city_dict = {}
        
    for each_city_code in City:
        city_dict[City[each_city_code]['city_name_zh'].encode('utf-8')] = \
                each_city_code
    
    try:
        infos = taskcontent.split('&')
        dept_id, dest_id = infos[0], infos[1]
    except Exception, e:
        print 'pare train taskcontent failed'
        return error

    try:
        for each_ticket in tickets:
            dept_city, dest_city = each_ticket[3].encode('utf-8'), \
                    each_ticket[5].encode('utf-8')
            if city_dict[dept_city] == dept_id and \
               city_dict[dest_city] == dest_id:
                error = 0
                break
    except:
        pass

    return error

if __name__ == '__main__':
    juage_train_error('','')
