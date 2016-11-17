#! /usr/bin/python
#coding=utf-8
from common import timezone
import datetime
from common import city_common
from common import airport_common
from common import station_common


class CalDate(object):

    def __init__(self):
        pass

    def get_time_zone_standard(self, para_type, params):
        
        para_list=['city','airport','station']
        para_type=para_type.lower()
        
        if para_type not in para_list:
            print "Wrong para_type"
            return -100

        if para_type=='airport':
            try:
                country_name=airport_common.Airport[params]['country'].encode('utf-8')
            except Exception,e:
                print "Wrong airport:"+params+str(e)
        
        elif para_type=='city':
            try:
                country_name=city_common.City[params]['country'].encode('utf-8')
            except Exception,e:
                print "Wrong city:"+params+str(e)

        else:
            try:
                country_name=station_common.Station[params].encode('utf-8')
            except Exception,e:
                print "Wrong station:"+params+str(e)
        
        try:
            country_info=timezone.TimeZone[country_name]
        except Exception,e:
            print 'Get country failed'+str(e)
            return -100
        
        timez=int(country_info['standard'])
        
        return timez


    def CalDate(self, paratype, dept_params, dept_time, duration, dest_params, dest_time):
        
        dept_timezone = timezone.get_time_zone(paratype, dept_params, dept_time)
        dest_timezone_standard = self.get_time_zone_standard(paratype, dest_params)
        
        if dept_timezone == -100:
            print('dept: %s::%s not exist in database' % (paratype.upper(), dept_params))
            
            return -100

        if dest_timezone_standard ==-100:
            print ('dest:%s::%s not exist in database' % (paratype.upper(), dest_params))
            
            return -100
        
        else:
            dept_time_tmp=datetime.datetime(int(dept_time[0:4]),int(dept_time[5:7]),int(dept_time[8:10]),\
                    int(dept_time[11:13]),int(dept_time[14:16]),int(dept_time[17:19]))

            dest_time_tmp = dept_time_tmp+datetime.timedelta(seconds=duration)
            dest_time_tmp1=dest_time_tmp+datetime.timedelta(hours=dest_timezone_standard-dept_timezone)
            dest_time1=(str(dest_time_tmp1)).strip().split()[1]
            dest_date1=(str(dest_time_tmp1)).strip().split()[0]
            
            if dest_time1 != dest_time:
                dest_time_tmp2=dest_time_tmp+datetime.timedelta(hours=dest_timezone_standard+1-dept_timezone)
                dest_time2=(str(dest_time_tmp2).strip()).split()[1]
                dest_date2=(str(dest_time_tmp2).strip()).split()[0]
            
            return dest_date1



if __name__=="__main__":
    
    cd = CalDate()
    result=cd.CalDate('airport','PEK','2015-04-20T13:20:00',37200,'TXL',"17:40:00")
    print result
