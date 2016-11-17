#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('../../')
from datetime import datetime

try:
    from pytz import timezone
    import pytz
except Exception, e:
    import os
    os.system('yum -y install pytz')

try:
    from HTMLParser import HTMLParser
except Exception, e:
    import os
    os.system('yum -y install htmlparser')

from common.airport_common import Airport
from city_2_country import City_2_country

def date_to_std(str_time):
    
    Str_time = ''
    if str_time.find('T') > -1:
        str_time = str_time.replace('T',' ')
        std_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    else:
        std_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    return std_time


def isDaydiff(dept_time, dept_id, dest_time, dest_id, para_type):
    if dept_time == 'NULL' or dept_id == 'NULL' or dest_time == 'NULL' or dest_id == 'NULL':
        return str(-1)
    dept_time = date_to_std(dept_time)
    dest_time = date_to_std(dest_time)
    if para_type == 'airport':
        dept_country = Airport[dept_id]['country_code']
        dest_country = Airport[dest_id]['country_code']
    elif para_type == 'city':
        dept_country = City_2_country[dept_id]
        dest_country = City_2_country[dest_id]

    std = datetime(dept_time.year, dept_time.month, dept_time.day+1, 0)
    dept_tz = timezone(pytz.country_timezones[dept_country][0])
    dest_tz = timezone(pytz.country_timezones[dest_country][0])
    
    std = dept_tz.normalize(dept_tz.localize(std)).astimezone(pytz.utc)
    arrive = dest_tz.normalize(dest_tz.localize(dest_time)).astimezone(pytz.utc)
    start = dept_tz.normalize(dept_tz.localize(dept_time)).astimezone(pytz.utc)
    
    if arrive > std:
        return str(1)
    return str(0)


def dur(dept_time, dept_id, dest_time, dest_id, para_type):
    if dept_time == 'NULL' or dept_id == 'NULL' or dest_time == 'NULL' or dest_id == 'NULL':
        return -1
    dept_time = date_to_std(dept_time)
    dest_time = date_to_std(dest_time)
    if para_type == 'airport':
        dept_country = Airport[dept_id]['country_code']
        dest_country = Airport[dest_id]['country_code']
    elif para_type == 'city':
        dept_country = City_2_country[dept_id]
        dest_country = City_2_country[dest_id]

    std = datetime(dept_time.year, dept_time.month, dept_time.day+1, 0)
    dept_tz = timezone(pytz.country_timezones[dept_country][0])
    dest_tz = timezone(pytz.country_timezones[dest_country][0])
    
    std = dept_tz.normalize(dept_tz.localize(std)).astimezone(pytz.utc)
    end = dest_tz.normalize(dest_tz.localize(dest_time)).astimezone(pytz.utc)
    start = dept_tz.normalize(dept_tz.localize(dept_time)).astimezone(pytz.utc)

    dur_time = end - start#.seconds
    if dur_time.days > 0:
        dur_time = dur_time.days * 3600 * 24 + dur_time.seconds
    else:
        dur_time = dur_time.seconds
    return dur_time

    


dp = '2015-10-22T20:45:00'
ds = '2015-09-23T05:15:00'
#dp = '2016-01-05T09:55:00'
#ds = '2016-01-05T16:25:00'
#ds = datetime(2015,10,1,9,30)
#print dur(dp,'PEK',ds,'JFK','airport')
#print date_to_std(dp)
