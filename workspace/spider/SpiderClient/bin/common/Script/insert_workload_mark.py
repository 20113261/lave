#!/usr/bin/env python
#coding=UTF-8
'''
    Created on 2014-03-08
    @author: devin
    @desc:
        数据访问
'''
import sys
import MySQLdb
from MySQLdb.cursors import DictCursor
import datetime
import time
import os
reload(sys)
sys.setdefaultencoding('utf-8')

# MySQL 连接信息
MYSQL_HOST = '10.10.86.250'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'miaoji@2014!'
MYSQL_DB = 'workload'


def GetConnection():
    conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PWD, \
                           db=MYSQL_DB, charset="utf8")
    return conn
    #return Connection()


def Connect():
    conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PWD, \
            db=MYSQL_DB, charset="utf8")

    return conn

def ExecuteSQL(sql, args = None):
    '''
        执行SQL语句, 正常执行返回影响的行数，出错返回Flase 
    '''
    ret = 0
    try:
        conn = GetConnection()
        cur = conn.cursor()

        ret = cur.execute(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        #logger.error("ExecuteSQL error: %s" %str(e))
        return False
    finally:
        cur.close()
        #conn.close()

    return ret

def ExecuteSQLs(sql, args = None):
    '''
        执行多条SQL语句, 正常执行返回影响的行数，出错返回Flase 
    '''
    ret = 0
    try:
        conn = GetConnection()
        cur = conn.cursor()

        ret = cur.executemany(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        #logger.error("ExecuteSQLs error: %s" %str(e))
        return False
    finally:
        cur.close()
        #conn.close()

    return ret

def QueryBySQL(sql, args = None, size = None):
    '''
        通过sql查询数据库，正常返回查询结果，否则返回None
    '''
    results = []
    try:
        conn = GetConnection()
        cur = conn.cursor(cursorclass = DictCursor)
        
        cur.execute(sql, args)
        rs = cur.fetchall()
        for row in rs : 
            results.append(row)
    except MySQLdb.Error, e:
        #logger.error("QueryBySQL error: %s" %str(e))
        return None
    finally:
        cur.close()
        #conn.close()

    return results

def InsertBusMark(args):

    sql = 'INSERT INTO bus_station_mark (station, inBus, sameNameID, city, city_id, country, map_info, distance, addDate, source, knowledge_confirm) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return ExecuteSQLs(sql,args)

def InsertTrainMark(args):

    sql = 'INSERT INTO train_station_mark (station, inTrain, sameNameID, city, city_id, country, map_info, distance, addDate, source, knowledge_confirm) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return ExecuteSQLs(sql,args)


import db

def insertBusMark():
    '''
        标注后的文档插入bus_mark
    '''

    todayStr = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday)
    queryStr = 'select city, station, source from extractBus  where station != "NULL" group by city, station'
    res = db.QueryBySQL(queryStr)
    l = []
    for ele in res:
        city = ele['city']
        station = ele['station'].lower()
        source = ele['source']
        inBus = 'NULL'
        sameNameID = 'NULL'
        city_id = 'NULL'
        country = 'NULL'
        map_info = 'NULL'
        distance = '-1.0'
        addDate = todayStr
        knowledge_confirm = 'N'
        t = (station, inBus, sameNameID, city, city_id, country, map_info, distance, addDate, source, knowledge_confirm)
        l.append(t)
    InsertBusMark(l)

def traversalbus():
    '''
        遍历bus表，检查此站是否已经存在
    '''
    busSQL = 'select city, station, alias, station_id from bus'
    res = QueryBySQL(busSQL)
    for ele in res:
        station_id = ele['station_id'].encode('utf-8')
        station = ele['station'].encode('utf-8')
        alias = ele['alias'].encode('utf-8')
        station_t = [station]
        if alias == '' or alias == None or alias == 'NULL':
            pass
        else:
            for e in alias.split('&&'):
                station_t.append(e.encode('utf-8'))
        city = ele['city'].encode('utf-8')
        updatemark = 'update bus_station_mark set sameNameID = "%s" where staion in "%s" and city != "%s"' % (station_id, str(tuple(station_t)).encode('utf-8'), city)
        updatemarkin = 'update bus_station_mark set inBus = "%s" where station in "%s" and city = "%s"' % (station_id, str(tuple(station_t)).encode('utf-8'), city)
        print updatemarkin
        print updatemark
        ExecuteSQL(updatemark)
        ExecuteSQL(updatemarkin)

def traversaltrain():
    '''
        遍历station表，检查此站是否已经存在
    '''
    trainSQL = 'select city_id, station, alias, station_id from station'
    res = QueryBySQL(trainSQL)
    for ele in res:
        station_id = ele['station_id'].encode('utf-8')
        station = ele['station'].encode('utf-8')
        alias = ele['alias']#.encode('utf-8')
        station_t = [station]
        if alias == '' or alias == None or alias == 'NULL':
            pass
        else:
            for e in alias.split('&&'):
                station_t.append(e.encode('utf-8'))

        city = ele['city_id'].encode('utf-8')
        todayStr = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday)
        updatemark = 'update train_station_mark set sameNameID = "%s" where station in "%s" and city_id != "%s" and addDate = "%s"' % (station_id, str(tuple(station_t)).encode('utf-8'),city, todayStr)
        updatemarkin = 'update train_station_mark set inTrain = "%s" where station in "%s" and city_id = "%s" and addDate = "%s"' % (station_id, str(tuple(station_t)).encode('utf-8'),city, todayStr)
        print updatemarkin
        print updatemark
        ExecuteSQL(updatemark)
        ExecuteSQL(updatemarkin)

def insertTrainMark():
    '''
        标注后的车站整理入train_mark表
    '''

    todayStr = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday)
    queryStr = 'select city, station, source from extractTrain  where station != "NULL" group by city, station'
    res = db.QueryBySQL(queryStr)
    l = []
    for ele in res:
        city = ele['city']
        station = ele['station'].lower()
        source = ele['source']
        inTrain = 'NULL'
        sameNameID = 'NULL'
        city_id = 'NULL'
        country = 'NULL'
        map_info = 'NULL'
        distance = '-1.0'
        addDate = todayStr
        knowledge_confirm = 'N'
        t = (station, inTrain, sameNameID, city, city_id, country, map_info, distance, addDate, source, knowledge_confirm)
        l.append(t)
    InsertTrainMark(l)
'''
import csv
def genBusCSV():
    todayStr = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday)
    queryStr = 'select * from bus_station_mark'
    res = QueryBySQL(queryStr)
    for ele in res:


    filename = 'bus_station_mark.csv'
    csvfile1 = file(filename, 'wb')
    writer = csv.writer(csvfile1)
    writer.writerows(final_result_lst)
    csvfile1.close()
'''

if __name__ == '__main__':

    import sys
    Type = sys.argv[1]
    if Type.lower() == 'bus':
        insertBusMark()
        traversalbus()
    elif Type.lower() == 'train':
        #insertTrainMark()
        traversaltrain()
    else:
        pass
