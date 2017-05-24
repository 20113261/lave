#!/usr/bin/env python
#coding=utf-8
'''

'''

import hashlib
import miaoji_redis
import datetime
import time
from logger import logger
from city_common import city_name_dict
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')


def InsertFlight(tickets):
    '''
        插入航班价格
        redis数据库为0
    '''
    #飞机例行数据不再入redis,飞机预测已经不再使用
    return

    result = {}
    for ticket in tickets:
        try:
            if len(ticket) == 22:
                # 都大于22
                flight_no = ticket[0]
                dept_id = ticket[3]
                dest_id = ticket[4]
                dept_day = ticket[5]
                source = ticket[19]
                dept_time = ticket[6]
                dest_time = ticket[7]
                seat_type = ticket[14]
                real_class = ticket[15]
                promotion = 'NULL'
                return_rule = ticket[20]
                price = ticket[10]
                tax = ticket[11]
                surcharge = ticket[12]
                currency = ticket[13]
                updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            elif len(ticket) == 23:
                # 无套餐
                flight_no = ticket[0]
                plane_type = ticket[1]
                flight_corp = ticket[2]
                dept_id = ticket[3]
                dest_id = ticket[4]
                dept_day = ticket[5]
                source = ticket[20]
                dept_time = ticket[6]
                dest_time = ticket[7]
                during = ticket[8]
                seat_type = ticket[15]
                real_class = ticket[16]
                stop_id = ticket[17]
                stop_time = ticket[18]
                day_diff = ticket[19]
                promotion = ticket[13]
                return_rule = ticket[21]
                rest = ticket[9]
                price = ticket[10]
                tax = ticket[11]
                surcharge = ticket[12]
                currency = ticket[14]
                package = "NULL"
                updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            elif len(ticket) > 24:
                # 有套餐
                flight_no = ticket[0]
                plane_type = ticket[1]
                flight_corp = ticket[2]
                dept_id = ticket[3]
                dest_id = ticket[4]
                dept_day = ticket[5]
                source = ticket[21]
                dept_time = ticket[6]
                dest_time = ticket[7]
                during = ticket[8]
                seat_type = ticket[15]
                real_class = ticket[16]
                package = ticket[17]
                stop_id = ticket[18]
                stop_time = ticket[19]
                day_diff = ticket[20]
                promotion = ticket[13]
                return_rule = ticket[22]
                rest = ticket[9]
                price = ticket[10]
                tax = ticket[11]
                surcharge = ticket[12]
                currency = ticket[14]
                updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            source = source.split('::')[0]+'Flight'
            if rest == -10:
                logger.info("REDIS REST is -10")
                continue
            key = '|'.join( ("flight", flight_no, dept_day, dept_id, dest_id, source, seat_type.encode("utf8"), real_class.encode("utf8"), promotion.encode("utf8"), package.encode("utf8")) )
            if len(ticket) > 24:
                logger.info("NEW REDIS: %s" % key)
            result[key] = '\t'.join( (updatetime, str(price), str(tax), str(surcharge), currency) )


        except Exception,e:
            logger.error("%s" % str(e))

    #插入redis
    try:
        miaoji_redis.SetKeys(result, expire_time=604800, db=0)
        pass
    except Exception, e:
        logger.error("%s" % str(e))

    InsertFlightNo(tickets)


def InsertFlightNo(tickets):
    return
    result = {}
    result1 = {}
    for ticket in tickets:
        flight_no = ticket[0]
        dept_id = ticket[3]
        dest_id = ticket[4]
        dept_day = ticket[5]
        source = ticket[21]
        source = source.split('::')[0]+'Flight'
        seat_type = ticket[15]
        real_class = ticket[16]
        promotion = ticket[13]
        package = ticket[17]
        flight_key = '|'.join( (dept_id, dest_id, source, dept_day) )
        flight_value = '|'.join( ('flight', flight_no, dept_day, dept_id, dest_id, source, seat_type, real_class, promotion, package) )
        if flight_key not in result:
            result[flight_key] = list()
        else:
            result[flight_key].append(flight_value)

    for key, value in result.iteritems():
        result1[key] = '||'.join(value)

    try:
        miaoji_redis.SetKeys(result1, expire_time = 604800, db=0, redis_host = '10.10.69.158', redis_port = 6379)
        print result1
    except Exception, e:
        logger.error("%s" % str(e))



def InsertFlightInfo(flight_no, plane_type, flight_corp, dept_id, dest_id, dept_time, dest_time, during, stop_id, stop_time, day_diff):
    '''
        插入航班信息
    '''
    try:
        key = "flightInfo|" + flight_no
        value = '\t'.join( (plane_type, flight_corp.encode("utf8"), dept_id, dest_id, dept_time, dest_time, str(during), stop_id, stop_time, day_diff) )
    except Exception,e:
        logger.error("%s" % str(e))

    try:
        #miaoji_redis.SetKey(key, value, 10, db=2)
        pass
    except Exception, e:
        logger.error("%s" % str(e))


def InsertTrain(tickets):
    return
    # redis数据库为2
    result = {}
    for ticket in tickets:
        try:
            if len(ticket) == 28:
                train_no = ticket[0]
                dept_id = ticket[4]
                dest_id = ticket[6]
                dept_day = ticket[7]
                source = ticket[17]
                dept_time = ticket[8]
                dest_time = ticket[9]
                seat_type = ticket[14]
                real_class = ticket[15]
                return_rule = ticket[18]
                price = ticket[11]
                tax = ticket[12]
                currency = ticket[13]
                stopid = ticket[20]
                stoptime = ticket[21]
                daydiff = ticket[22]
                dept_city = ticket[3].encode("utf8")
                dest_city = ticket[5].encode("utf8")
            else:
                train_no = ticket[0]
                dept_id = ticket[4]
                dest_id = ticket[6]
                dept_day = ticket[7]
                source = ticket[16]
                dept_time = ticket[8]
                dest_time = ticket[9]
                seat_type = ticket[14]
                real_class = ticket[15]
                return_rule = ticket[17]
                price = ticket[11]
                tax = ticket[12]
                currency = ticket[13]
                stopid = ticket[18]
                stoptime = ticket[19]
                daydiff = ticket[20]
                dept_city = ticket[3].encode("utf8")

            updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            source = source + 'Rail'
            key = '|'.join( ("rail", train_no, dept_day, source, dept_id.encode("utf8"), dest_id.encode("utf8"), seat_type.encode("utf8"), real_class.encode("utf8")) )
            result[key] = '\t'.join( (updatetime, str(price), str(tax), currency) )

            '''
            key = '_'.join( ("train", train_no, dept_id, dest_id, dept_day, source, stopid, dept_time, dest_time, seat_type,real_class) )
            #logger.info("TRAIN REDIS: train_no %s, dept_id %s, dest_id %s, dept_day %s, source %s" % (train_no, dept_id, dest_id, dept_day, source) )
            md5_key = hashlib.md5(key.encode('utf8')).hexdigest()
            md5_key = "orig_train_" + md5_key
            judge = real_class.find('NULL')
            if  return_rule == "NULL" and judge > -1:
                result[md5_key]  = '\t'.join( (updatetime, str(price), str(tax), currency) )
            else:
                md5_key += "_special"
                return_rule = 'NULL'
                result[md5_key]  = '\t'.join( (updatetime, str(price), str(tax), currency, str(real_class), str(return_rule)) )
            '''
        except Exception,e:
            logger.error("%s" % str(e))

    #插入redis
    try:
        miaoji_redis.SetKeys(result, db=2)
        pass
    except Exception, e:
        logger.error("%s" % str(e))

def InsertTrain1(tickets):
    return
    #redis数据库为1
    result = {}

    for ticket in tickets:
        try:
            if len(ticket) == 28 or len(ticket) == 29:
                train_no = ticket[0]
                dept_id = ticket[4]
                dest_id = ticket[6]
                dept_day = ticket[7]
                source = ticket[17]
                dept_time = ticket[8]
                dest_time = ticket[9]
                seat_type = ticket[14]
                real_class = ticket[15]
                return_rule = ticket[18]
                price = ticket[11]
                tax = ticket[12]
                currency = ticket[13]
                stopid = ticket[20]
                stoptime = ticket[21]
                daydiff = ticket[22]
                dept_city = ticket[3].encode("utf8")
                dest_city = ticket[5].encode("utf8")
            else:
                train_no = ticket[0]
                dept_id = ticket[4]
                dest_id = ticket[6]
                dept_day = ticket[7]
                source = ticket[16]
                dept_time = ticket[8]
                dest_time = ticket[9]
                seat_type = ticket[14]
                real_class = ticket[15]
                return_rule = ticket[17]
                price = ticket[11]
                tax = ticket[12]
                currency = ticket[13]
                stopid = ticket[18]
                stoptime = ticket[19]
                daydiff = ticket[20]
                dept_city = ticket[3].encode("utf8")
                dest_city = ticket[5].encode("utf8")

            updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            source = source + 'Rail'
            key = '||'.join( ("rail", train_no, dept_day, source, dept_id.encode("utf8"), dest_id.encode("utf8"), seat_type.encode("utf8"), real_class.encode("utf8"), stopid.encode("utf8"), stoptime.encode("utf8"), daydiff.encode("utf8")) )
            result[key] = '\t'.join( (updatetime, str(price), str(tax), currency) )

        except Exception,e:
            logger.error("%s" % str(e))
    '''
    dept_city = '巴黎'
    dest_city = '里昂'
    source = 'sncfenRail'
    dept_day = '2015-05-21'
    '''
    try:
        logger.info("source %s, dept_day %s" % (source, dept_day))
        workload_key = '_'.join( (city_name_dict[dept_city], city_name_dict[dest_city], source, datetime.datetime.strptime(dept_day,"%Y-%m-%d").strftime("%Y%m%d")) )
    except Exception,e:
        logger.error("HSET, %s" % str(e))
        workload_key = "NULL"

    #插入redis
    try:
        logger.info("INSERT REDIS, HSET, workload_key is %s", workload_key)
        if len(result) < 1:
            return
        miaoji_redis.HsetKeys(workload_key, result, 1)
    except Exception, e:
        logger.error("%s" % str(e))


def InsertRoom(rooms):
    #例行数据不再入redis
    return

    #redis数据库为3
    result = {}
    for room in rooms:
        try:
            hotel_name = room[0]
            source = room[2]
            source_hotelid = room[3]
            source_roomid = room[4]
            roomtype = room[6]
            bed_type = room[8]
            check_in = room[11]
            check_out = room[12]
            price = room[14]
            tax = room[15]
            currency = room[16]
            updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            source += "Hotel"
            if source_roomid != "NULL":
                key = '|'.join( ("hotel", source, source_hotelid, source_roomid, check_in, check_out) )
                result[key] = '\t'.join( (updatetime, str(price), str(tax), currency) )

        except Exception,e:
            logger.error("%s" % str(e))

    #插入redis
    try:
        if len(result) > 0:
            miaoji_redis.SetKeys(result, db=3)
    except Exception, e:
        logger.error("%s" % str(e))



def InsertCars(cars):
    return
    #redis数据库为4
    result = {}
    for car in cars:
        try:
            source = car[0]
            company = car[1].encode('utf-8')
            car_type = car[2].encode('utf-8')
            car_desc = car[3].encode('utf-8')
            car_image = car[4]
            price = car[5]
            list_price = car[6]
            rest = car[7]
            currency = car[8].encode('utf-8')
            rent_city = car[9].encode('utf-8')
            return_city = car[10].encode('utf-8')
            rent_store = car[11].encode('utf-8')
            return_store = car[12].encode('utf-8')
            rent_time = car[13].encode('utf-8')
            return_time = car[14].encode('utf-8')
            rent_area = car[15].encode('utf-8')
            return_area = car[16].encode('utf-8')
            is_automatic = car[17].encode('utf-8')
            baggages = car[18].encode('utf-8')
            passengers = car[19]
            pay_method = car[20]
            insurance = car[21].encode('utf-8')
            fuel_strategy = car[22].encode('utf-8')
            promotion = car[23].encode('utf-8')
            license = car[24].encode('utf-8')
            updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            #key = '_'.join(("car",source,company, rent_city, return_city, rent_store, return_store, rent_area, return_area, rent_time, return_time, promotion))
            key = '_'.join( ("car", source, company, car_type,car_desc,is_automatic, rent_city, return_city, rent_store, return_store, rent_area, return_area, rent_time, return_time, promotion,fuel_strategy,str(price), insurance))
            print key
            md5_key = hashlib.md5(key.encode('utf8')).hexdigest()
            md5_key = "orig_" + md5_key

            if  promotion == "NULL":
                result[md5_key]  = '\t'.join( (updatetime, str(price),  currency) )
            else:
                md5_key += "special"
                result[md5_key]  = '\t'.join( (updatetime, str(price), promotion,currency))

        except Exception,e:
            logger.error("%s" % str(e))

    #插入redis
    try:
        miaoji_redis.SetKeys(result, db=4)
    except Exception, e:
        logger.error("%s" % str(e))



def InsertFlightMonitor(result):
    return
    '''
    插入监控信息
    redis key: workload_key
    redis value: updatetime1\terror_code1\nupdatetime2\terror_code2\nupdatetime3\terror_code3
    '''
    error_code = result['error']
    tickets = result['para']
    if tickets == [] or tickets == None:
        pass
    else:
        for ticket in tickets:
            dept_id = ticket[3]
            dest_id = ticket[4]
            source = ticket[19].split('::')[0]+'Flight'
            dept_day = ticket[5].replace('-','')
            workload_key = dept_id+'_'+dest_id+'_'+source+'_'+dept_day
            updatetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            value = updatetime + '\t' + error_code+'\n'
            try:
                miaoji_redis.SetKey(workload_key,value)
            except Exception, e:
                logger.error("%s" % str(e))
def InsertRealtimeResult(workload_key, result):
    '''
        插入实时查询信息，和爬虫信息只存储价格不同，此处存储全部信息
    '''
    pass


if __name__ == '__main__':
    InsertTrain1(1)
