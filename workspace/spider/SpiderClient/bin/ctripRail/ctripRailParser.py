#!/usr/bin/python
#coding=UTF-8

import sys

import re
import json
import random
import traceback
import time
import datetime
import requests
import logging
from util.Browser2 import MechanizeCrawler as MC
from common.common import get_proxy
from common.logger import logger
from common.insert_db import InsertTrain2
from common.class_common import Train, EachTrain
from common.city_common import City
from common.station_common import Station
from common.task import Task
from common.city_common import City
reload(sys)
sys.setdefaultencoding('utf-8')

PROXY_NONE = 21
TASK_ERROR = 12
PROXY_INVALID = 22
PROXY_FORBIDDEN = 23
DATA_NONE = 24
UNKNOWN_TYPE = 25

def ctriprail_task_parser(task):
    content = task.content
    proxy_info = task.proxy_info
    ticket_info = task.ticket_info
    result = {'para': {'tickets': []}, 'error': 0, 'proxy':''}
    try:
        contentlist = content.split('&')
        dept_id = contentlist[0]
        dept_id_en = City[contentlist[0]]['city_name_en']
        dest_id = contentlist[1]
        dest_id_en = City[contentlist[1]]['city_name_en']
        dept_time =  contentlist[2]
        dept_day = dept_time[0:4] + '-' + str(int(dept_time[4:6])) + '-' + str(int(dept_time[6:8]))
    except Exception, e:
        traceback.print_exc(str(e))
        logger.error('ctripRail: tasl error: %s'% str(e))
        result['error'] = TASK_ERROR
        return result
    try:
        res0 = crawl(dept_id, dest_id, dept_id_en, dest_id_en, dept_day, adults=1, children=0, seniors=0, youth=0)
    except Exception, e:
        traceback.print_exc(e)
        result['error'] = res0['error']
        result['proxy'] = res0['proxy']
        return result
    if res0['error'] != 0:
        result['error'] = res0['error']
        result['proxy'] = res0['proxy']
        return result
    else:
        try:
            result = ctripRail_parser(res0['content'], contentlist[0], contentlist[1])
        except Exception,e:
            traceback.print_exc(e)
            result['error'] = 27
            return result
        result['proxy'] = res0['proxy']

    return result



def crawl(dept_id, dest_id, dept_city_en, dest_city_en, dept_day, adults=1, children=0, seniors=0, youth=0, proxy_info={}):
    result = {'proxy': '', 'error': 0, 'content': ''}
    if proxy_info != {}:
        p = get_proxy(source='ctripRail', proxy_info=proxy_info)
    else:
        p = get_proxy(source='ctripRail')
    if p == None or p == '':
        logger.error('ctripRail :: get proxy failed.')
        result['error'] = 21
        return result
    result['proxy'] = p

    mc = MC()
    mc.set_debug(True)
    mc.set_proxy(p)
    url = 'http://webresource.ctrip.com/ResTrainOnline/R9/Outie/JS/outiecity.js?2017_2_21_16_40_32.js'
    html, err = mc.req('get', url, html_flag=True)
    if err:
        raise Exception(err)
    try:
        dept_city = re.compile(r'\|[A-Z]{5}\|%s'%dept_city_en.upper()).findall(html)[0][1:6]
        dest_city = re.compile(r'\|[A-Z]{5}\|%s'%dest_city_en.upper()).findall(html)[0][1:6]
    except Exception,e:
        traceback.print_exc(e)
        result['error'] = 99
        return result
    headers={'Accept':'*/*', 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,ja;q=0.4,af;q=0.2,en;q=0.2,de;q=0.2', 'Cache-Control':'max-age=0', 'Connection':'keep-alive','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',\
             'Host':'rails.ctrip.com','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrom', 'Origin':'http://rails.ctrip.com'}
    referer = 'http://rails.ctrip.com/international/OutiePTPList.aspx?departureDate=%s&starttime=&adult=%s&child=%s&youth=%s&seniors=%s&searchType=0&pageStatus=0&passHolders=0&from=%s&to=%s&arriveDate=' % (dept_day, adults, children, seniors, youth, dept_city, dest_city)
    mc.add_referer(referer)
    data, err = mc.req('get', referer, html_flag=True)
    if err:
        raise Exception(err)
    PageLoadGUID = re.compile(r'id="PageLoadGUID".*/>').findall(data)[0][25:-4]

    url = 'http://rails.ctrip.com/international/Ajax/QueryOutiePTPProd.ashx'
    PassengerType = {'AdultCount':str(adults),
                     'YouthCount':str(youth),
                     'ChildCount':str(children),
                     'OldCount':'0'
                    }
    data = {'StartTime':'06:00',
            'StartDate':dept_day,
            'StartCityCode':dept_city,
            'ArriveCityCode':dest_city,
            'PassengerType':PassengerType,
            'PassHolders':'0',
            'LastStartDAte':'',
            #'StartCityName':dept_city_zh,
            #'ArrivalCityName':dest_city_zh,
            'TrvalType':1,
            'PageLoadGUID':PageLoadGUID
           }
    json_data = json.dumps(data)
    postdata = {'QueryParam': json_data}
    try:
        page, error = mc.req('post', url, headers=headers, paras=postdata, paras_type=2, html_flag=True)
        logger.debug("headers:%s", mc.resp.request.headers)
        if error:
            raise Exception(error)
    except Exception, e:
        result['error'] = 22
        return result
    result['content'] = page

    return result


def ctripRail_parser(page, dept_id, dest_id):
    trains = []
    result = {'para': {'tickets': trains}, 'error': 0, 'proxy':''}
    try:
        res = json.loads(page.decode("GBK", "ignore"))
    except Exception, e:
        traceback.print_exc(str(e))
        result['error'] = 24
        return result
    RstStatus = res['RstStatus']
    if RstStatus != 1:
        result['error'] = 29
        return result
    ProdectList = res['ProductList']
    for Product in ProdectList:
        train_info = Train()
        Class = []
        train_no = []
        train_corp = []
        DurationTime = Product['DurationTime']
        dur = re.compile(r'[0-9]{1,2}').findall(DurationTime)
        Trains = Product['Trains']
        for train in Trains:
            train_no.append(train['TrainName'])
            train_corp.append('NULL')
        Class.append(Product['FirstClass'] if Product.has_key('FirstClass') else {})
        Class.append(Product['SecondClass'] if Product.has_key('SecondClass') else {})
        for cla in Class:
            if cla:
                TrainPrice = cla['TrainPrice']
                for Trainprice in TrainPrice:
                    change_rule = []
                    return_rule = []
                    Sigments = Trainprice['Sigments']
                    for Sigment in Sigments:
                        change_rule.append(Sigment['ChangeRules'])
                        return_rule.append(Sigment['ChangeRulesDetail'])
                    seat_type = []

                    ProductInForOrder = json.loads(Trainprice['ProductInfoForOrder'])
                    productList = ProductInForOrder['productList']
                    for product in productList:
                        train_info.price = product['Price']
                        seat_type.append(product['PackageTypeName'])
                        #train_info.dept_station = product['FromCity'] + '站'
                        #train_info.dest_station = product['ToCity'] + '站'
                        train_info.dept_day = product['DepartureDate']
                        ptpSegmentList = product['ptpSegmentList']
                        train_type = []
                        stop_time = []
                        stop_id = []
                        for segment in ptpSegmentList:
                            train_type.append(segment['TrainModel'])
                            stop_id.append(Station[segment['StartCityCode']]+'_'+Station[segment['CityArrivedCode']])
                            #stop_id.append(segment['StartCityCode']+'_'+segment['CityArrivedCode'])
                            dept_time = segment['DepartureDateTime'].split(' ')
                            dest_time = segment['ArrivalDateTime'].split(' ')
                            stop_time.append('T'.join(dept_time)+':00_'+'T'.join(dest_time)+':00')

                        train_info.stop = len(stop_id) - 1
                        train_info.dept_city = dept_id
                        train_info.dest_city = dest_id
                        train_info.train_no = '_'.join(train_no)
                        train_info.train_corp = '_'.join(train_corp)
                        train_info.train_type = '_'.join(train_type)
                        train_info.stopid = '|'.join(stop_id)
                        train_info.stoptime = '|'.join(stop_time)
                        train_info.seat_type = '_'.join(seat_type * len(stop_id))
                        train_info.real_class = train_info.seat_type
                        train_info.change_rule = '_'.join(change_rule)
                        train_info.return_rule = '_'.join(return_rule)
                        train_info.dept_station = stop_id[0].split('_')[0]
                        train_info.dest_station = stop_id[-1].split('_')[-1]
                        train_info.dept_time = stop_time[0].split('_')[0]
                        train_info.dest_time = stop_time[-1].split('_')[-1]
                        train_info.dur = int(dur[0]) * 3600 + int(dur[1]) * 60
                        train_info.tax = 0
                        train_info.daydiff = '_'.join(['0'] * len(stop_id))
                        train_info.currency = 'CNY'
                        train_info.source = 'ctrip'
                        train_tuple = (train_info.train_no, train_info.train_type, \
                                       train_info.train_corp, train_info.dept_city, train_info.dept_station,\
                                       train_info.dest_city, train_info.dest_station, train_info.dept_day,\
                                       train_info.dept_time, train_info.dest_time, train_info.dur,\
                                       train_info.price, train_info.tax, train_info.currency, train_info.seat_type,\
                                       train_info.real_class, train_info.promotion, train_info.source,\
                                       train_info.return_rule, train_info.change_rule, train_info.stopid,\
                                       train_info.stoptime, train_info.daydiff, train_info.stop,\
                                       train_info.train_facilities, train_info.ticket_type,\
                                       train_info.electric_ticket, train_info.others_info, train_info.rest)
                        trains.append(train_tuple)
                        print train_tuple
    return result


