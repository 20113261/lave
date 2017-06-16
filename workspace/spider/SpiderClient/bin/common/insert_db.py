#!/usr/bin/env python
# coding=utf-8
'''

'''

import sys
import db  # 222:crawl
import json
import pika
import MySQLdb
from logger import logger
from insert_rabbitmq import insert_rabbitmq


def insert_hotel_base_data_task_info(args):
    sql = "REPLACE INTO hotel_base_data_task (source, source_id, city_id, hotel_url) VALUES (%s, %s, %s, %s)"
    try:
        db.execute_many_into_spider_db(sql=sql, args=args)
    except Exception:
        logger.exception("Insert Task Data Error")


def InsertFlight(args):
    # sql = "INSERT INTO flight" + table_name_date + " (flight_no,plane_no,airline,dept_id,dest_id,dept_day,dept_time," + \
    # "dest_time,dur,price,tax,surcharge,currency,seat_type,source,return_rule," + \
    # "stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql = "INSERT INTO flight (flight_no,plane_no,airline,dept_id,dest_id,dept_day,dept_time," + \
          "dest_time,dur,price,tax,surcharge,currency,seat_type,source,return_rule," + \
          "stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    return db.ExecuteSQLs(sql, args)


# 新增 change rule、baggage 等字段
def InsertNewFlight(args):
    sql = 'INSERT INTO flight_new (flight_no, plane_type, flight_corp, dept_id,' + \
          'dest_id, dept_day, dept_time, dest_time, dur, rest, price, tax, surcharge,' + \
          'promotion, currency, seat_type, real_class, package, stop_id, stop_time,' + \
          'daydiff, source, return_rule, change_rule, stop, share_flight, stopby,' + \
          'baggage, transit_visa, reimbursement, flight_meals, ticket_type, others_info) VALUES' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    routing_key = 'flight'
    q_list = ['dflight_dev', 'dflight_ol', 'sflight']
    # q_list = ['dflight_dev']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


# 新增了一列package
def InsertNewFlight2(args):
    # InsertFlightInfo(args)
    sql = 'INSERT INTO flight_new (flight_no,plane_type,flight_corp,dept_id,dest_id,dept_day,dept_time,' + \
          'dest_time,dur,rest,price,tax,surcharge,promotion,currency,seat_type,real_class,package,stop_id,stop_time,daydiff,' + \
          'source,return_rule,stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    return db.ExecuteSQLs(sql, args)


# 新增 change rule、baggage 等字段
def InsertNewFlight3(args):
    sql = 'INSERT INTO flight_new (flight_no, plane_type, flight_corp, dept_id,' + \
          'dest_id, dept_day, dept_time, dest_time, dur, rest, price, tax, surcharge,' + \
          'promotion, currency, seat_type, real_class, package, stop_id, stop_time,' + \
          'daydiff, source, return_rule, change_rule, stop, share_flight, stopby,' + \
          'baggage, transit_visa, reimbursement, flight_meals, others_info) VALUES' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertMultiFlight(args):
    sql = 'INSERT INTO flight_multi (flight_no, plane_type, flight_corp, dept_id,' + \
          'dest_id, dept_day, dept_time, dest_time, dur, rest, price, tax, surcharge,' + \
          'promotion, currency, seat_type, real_class, package, stop_id, stop_time,' + \
          'daydiff, source, return_rule, change_rule, stop, share_flight, stopby,' + \
          'baggage, transit_visa, reimbursement, flight_meals, ticket_type, others_info) VALUES' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    routing_key = 'interline'
    # q_list = ['dflight_dev', 'dflight_ol', 'sflight']
    q_list = ['dinterline_dev', 'dinterline_ol']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


def InsertFlightInfo(args):
    new_args = []
    for arg in args:
        flight_no = arg[0]
        plane_type = arg[1]
        flight_corp = arg[2]
        dept_id = arg[3]
        dest_id = arg[4]
        dept_time = arg[6][-8:]
        dest_time = arg[7][-8:]
        during = arg[8]
        stop_id = arg[-6]
        stop_time = arg[-5]
        daydiff = arg[-4]
        new_args.append((flight_no, plane_type, flight_corp, dept_id, dest_id, dept_time, dest_time, during, stop_id,
                         stop_time, daydiff))
    sql = 'REPLACE INTO flight_info (flight_no, plane_type, flight_corp, dept_id, dest_id, dept_time, dest_time, during, stop_id, stop_time, daydiff) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    db.ExecuteSQLs(sql, new_args)


def InsertRoundFlight(args):
    sql = 'INSERT INTO flight_round (dept_id, dest_id, dept_day, dest_day, price, tax, surcharge,promotion, currency, source, return_rule,' + \
          'flight_no_A, airline_A, plane_no_A, dept_time_A, dest_time_A, dur_A, seat_type_A,real_class_A,stop_id_A,stop_time_A,daydiff_A,stop_A, flight_no_B, airline_B, plane_no_B,' + \
          'dept_time_B, dest_time_B, dur_B, seat_type_B,real_class_B,stop_id_B,stop_time_B,daydiff_B,stop_B) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    routing_key = 'round'
    q_list = ['dround_dev', 'dround_ol']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


def InsertRoundFlight2(args):
    sql = 'INSERT INTO flight_round (dept_id, dest_id, dept_day, dest_day, price, ' + \
          'tax, surcharge, promotion, currency, source, return_rule, flight_no_A, ' + \
          'airline_A, plane_no_A, dept_time_A, dest_time_A, dur_A, seat_type_A, ' + \
          'real_class_A,stop_id_A,stop_time_A,daydiff_A,stop_A, flight_no_B, ' + \
          'airline_B, plane_no_B, dept_time_B, dest_time_B, dur_B, seat_type_B, ' + \
          'real_class_B,stop_id_B,stop_time_B,daydiff_B,stop_B, change_rule, ' + \
          'share_flight_A, share_flight_B, stopby_A, stopby_B, baggage, transit_visa, ' + \
          'reimbursement, flight_meals, ticket_type, others_info, rest) VALUES ( %s, %s, ' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s,  %s, %s, %s, %s, %s, %s)'

    routing_key = 'round'
    q_list = ['dround_dev', 'dround_ol']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


def InsertExtraFlight(args):
    sql = 'INSERT INTO flight_extra (flight_no,plane_type,flight_corp,dept_id,dest_id,dept_day,dept_time,' + \
          'dest_time,dur,rest,price,tax,surcharge,promotion,currency,seat_type,real_class,stop_id,stop_time,daydiff,' + \
          'source,return_rule,stop,extra_flight_no,extra_plane_type,extra_flight_corp,extra_dept_id,extra_dest_id,extra_dept_day,' + \
          'extra_dept_time,extra_dest_time,extra_dur,extra_seat_type,extra_real_class,extra_stop_id,extra_stop_time,extra_daydiff,' + \
          'extra_stop) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql, args)


def InsertExtraFlight2(args):
    sql = 'INSERT INTO flight_extra2 (flight_no,plane_type,flight_corp,dept_id,dest_id,dept_day,dept_time,dest_time,dur,rest,price,tax,surcharge,promotion,currency,seat_type,real_class,stop_id,stop_time,daydiff,source,return_rule,change_rule,stop,share_flight,stopby,baggage,transit_visa,reimbursement,flight_meals,others_info,ticket_type,extra_flight_no,extra_plane_type,extra_flight_corp,extra_dept_id,extra_dest_id,extra_dept_day,' + \
          'extra_dept_time,extra_dest_time,extra_dur,extra_seat_type,extra_real_class,extra_stop_id,extra_stop_time,extra_daydiff,extra_stop,extra_share_flight) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    return db.ExecuteSQLs(sql, args)


def InsertHotel(args):
    sql = 'INSERT INTO hotel (hotel_name,hotel_name_en,source,source_id,brand_name,map_info,address,city,' + \
          'country,city_id,postal_code,star,grade,has_wifi,is_wifi_free,has_parking,is_parking_free,service,' + \
          'img_items, description, accepted_cards, check_in_time, check_out_time, hotel_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql, args)


def InsertHotel_room(args):
    sql = 'INSERT INTO room (hotel_name, city, source, source_hotelid,source_roomid,real_source,room_type,' + \
          'occupancy, bed_type, size, floor, check_in, check_out, price, tax, currency, is_extrabed, is_extrabed_free,has_breakfast,' + \
          'is_breakfast_free,is_cancel_free, room_desc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql, args)


def InsertHotel_room2(args):
    sql = 'INSERT INTO room (hotel_name, city, source, source_hotelid,source_roomid,real_source,room_type,' + \
          'occupancy, bed_type, size, floor, check_in, check_out, rest, price, tax, currency, is_extrabed, is_extrabed_free,has_breakfast,' + \
          'is_breakfast_free,is_cancel_free, room_desc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    return db.ExecuteSQLs(sql, args)


def InsertHotel_room3(args):
    sql = 'INSERT INTO room (hotel_name, city, source, source_hotelid,' + \
          'source_roomid, real_source, room_type, occupancy, bed_type, size, ' + \
          'floor, check_in, check_out, rest, price, tax, currency, pay_method, ' + \
          'is_extrabed, is_extrabed_free, has_breakfast, is_breakfast_free, ' + \
          'is_cancel_free, extrabed_rule, return_rule, change_rule, room_desc, ' + \
          'others_info,guest_info) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertHotel_room4(args):
    sql = 'INSERT INTO room (hotel_name, city, source, source_hotelid,' + \
          'source_roomid, real_source, room_type, occupancy, bed_type, size, ' + \
          'floor, check_in, check_out, rest, price, tax, currency, pay_method, ' + \
          'is_extrabed, is_extrabed_free, has_breakfast, is_breakfast_free, ' + \
          'is_cancel_free, extrabed_rule, return_rule, change_rule, room_desc, ' + \
          'others_info,guest_info, hotel_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    insert_hotel_base_data_task_info(list(map(lambda x: (x[2], x[3], x[1], x[-1]), args)))

    return db.ExecuteSQLs(sql, args)


def InsertHotel_comment(args):
    sql = 'INSERT INTO hotel_comment (hotel_name, city, source, source_hotelid, title, comment, comment_user)' + \
          ' VALUES( %s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql, args)


def InsertTask(args):
    sql = "INSERT INTO workload (task,source,task_type,priority,crawl_day,crawl_hour,update_times,success_times,batch_id)" + \
          "VALUES (%s, %s, %s ,%s, %s, %s, %s, %s, %s)"

    return db.ExecuteSQLs(sql, args)


def InsertTrain(args):
    sql = 'INSERT INTO train (train_no, train_type, train_corp, dept_city, dept_id, dest_city, dest_id,' + \
          'dept_time, dest_time, dur, price, tax, currency, seat_type, source, return_rule, stop, stop_station)' + \
          'VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertTrain2(args):
    sql = 'INSERT INTO train_new (train_no, train_type, train_corp, dept_city, dept_id, dest_city, dest_id, ' + \
          'dept_day, dept_time, dest_time, dur, price, tax, currency, seat_type, real_class, source, ' + \
          'return_rule, stopid, stoptime, daydiff, stop)' + \
          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql, args)


def InsertTrain3(args):
    sql = 'INSERT INTO train_new (train_no, train_type, train_corp, dept_city,' + \
          'dept_id, dest_city, dest_id, dept_day, dept_time, dest_time, dur,' + \
          'price, tax, currency, seat_type, real_class,promotion, source, return_rule,' + \
          'change_rule, stopid, stoptime, daydiff, stop, train_facilities, ' + \
          'ticket_type, electric_ticket, others_info) VALUES ' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertNewTrain(args):
    sql = 'INSERT INTO train_new (train_no, train_type, train_corp, dept_city,' + \
          'dept_id, dest_city, dest_id, dept_day, dept_time, dest_time, dur,' + \
          'price, tax, currency, seat_type, real_class,promotion, source, return_rule,' + \
          'change_rule, stopid, stoptime, daydiff, stop, train_facilities, ' + \
          'ticket_type, electric_ticket, others_info, rest) VALUES ' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    routing_key = 'train'
    q_list = ['dtrain_dev', 'dtrain_ol', 'strain']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


def InsertTrainTMP(args):
    sql = 'INSERT INTO train_tmp (train_no, train_type, train_corp, dept_city,' + \
          'dept_id, dest_city, dest_id, dept_day, dept_time, dest_time, dur,' + \
          'price, tax, currency, seat_type, real_class,promotion, source, return_rule,' + \
          'change_rule, stopid, stoptime, daydiff, stop, train_facilities, ' + \
          'ticket_type, electric_ticket, others_info) VALUES ' + \
          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' + \
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertTieyou(args):
    sql1 = 'INSERT INTO train_tieyou (train_no, train_type, train_corp, dept_city, dept_id, dest_city, dest_id, ' + \
           'dept_day, dept_time, dest_time, dur, price, tax, currency, seat_type, real_class, source, ' + \
           'return_rule, stopid, stoptime, daydiff, stop)' + \
           'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return db.ExecuteSQLs(sql1, args)


def InsertEachTrain(args):
    sql = 'INSERT INTO eachtrain (train_no, train_corp, train_type, dept_station, dest_station, dept_time,' + \
          'dest_time, dur) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertFlight2(args):
    sql = "INSERT INTO flight (flight_no,plane_no,airline,dept_id,dest_id,dept_day,dept_time," + \
          "dest_time,dur,price,tax,surcharge,currency,seat_type,real_class,stop_airport,source,return_rule," + \
          "stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    return db.ExecuteSQLs(sql, args)


def InsertFlight3(args):
    sql = "INSERT INTO flight (flight_no,plane_no,airline,dept_id,dest_id,dept_day,dept_time," + \
          "dest_time,dur,rest,price,tax,surcharge,currency,seat_type,real_class,stop_airport,stop_dur,source,return_rule," + \
          "stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    return db.ExecuteSQLs(sql, args)


def InsertEachFlight(args):
    sql = 'REPLACE INTO flight_info (flight_no, airline, plane_no, dept_id, dest_id, dept_time, ' + \
          'dest_time, daydiff, stop, cost, schedule, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


def InsertStation(args):
    sql = 'insert into station_temp (station) values ( %s)'

    return db.ExecuteSQLs(sql, args)


def InsertCar(args):
    sql = 'INSERT INTO car (source, company, car_type, car_desc, car_image, price,' + \
          'list_price, rest, currency, rent_city, return_city, rent_store, return_store,' + \
          'rent_time, return_time, rent_area, return_area, is_automatic, baggages, ' + \
          'passengers, pay_method, insurance, fuel_strategy, promotion, license, ' + \
          'return_rule, diff_location_fee, door_num, mile_limit, extra_driver, zone_desc, package) ' + \
          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    return db.ExecuteSQLs(sql, args)


def InsertBus(args):
    sql = 'INSERT INTO bus (dept_city, dest_city, dept_station, dest_station, dept_day, dept_time, ' + \
          'dest_time, dur, price, currency, source, corp, tax, return_rule, daydiff, rest, change_rule, ticket_type, bus_type, ' + \
          'insurance, service_fee, stop, bus_no, stop_id, stop_time, transfer_interval, has_wifi, has_charge, ' + \
          'has_extended_seat, free_baggage_num, free_baggage_weight, has_meals, has_wc, arrive_gate' + \
          ') VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)'

    routing_key = 'bus'
    q_list = ['dbus_dev', 'dbus_ol', 'sbus']
    insert_rabbitmq_ok = False
    insert_db_ok = False
    try:
        insert_rabbitmq(args=args, queue_list=q_list, routing_key=routing_key)
        insert_rabbitmq_ok = True
    except Exception:
        logger.exception('[rabbitmq 入库异常]')

    try:
        res = db.ExecuteSQLs(sql, args)
        if res:
            insert_db_ok = True
        else:
            raise Exception('mysql 入库失败')
    except Exception:
        logger.exception('[mysql 入库异常]')

    return insert_rabbitmq_ok, insert_db_ok


def InsertPickup(args):
    sql = 'INSERT INTO pickup (source, pattren_type, airport_code, dept_addr, dept_lat, dept_lng, ' \
          'dest_addr, dest_lat, dest_lng, use_time, car_type_id, car_title, car_desc, car_seat_num, ' \
          'car_luggage_num, price, currency, price_mark, is_support_card, card_fee, is_support_child_seat, ' \
          'child_seat_fee, is_has_car_wifi, car_wifi_fee, is_must_child_seat, is_support_chinese) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    return db.ExecuteSQLs(sql, args)


if __name__ == '__main__':
    InsertFlightInfo([('KL231', '320', 'british air', 'PEK', 'CDG', '15:00:00', '16:00:00', 20000, 'PEK_LHR|LHR_CDG',
                       'dfdfdf', '1_0')])
