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
#from slave import Connection
from MySQLdb.cursors import DictCursor
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
#from logger import logger

# MySQL 连接信息
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'jiangzongjin'
MYSQL_PWD = 'jiangzongjin'
MYSQL_DB = 'jiangzongjin'


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





def insertTable(args):

    #sql = 'INSERT INTO bus (station_id, station, alias, city, city_id, country, map_info, Program, name_en, online_name) VALUES (%s,%s,%s,%s,%s, %s,%s, %s, %s, %s)'
    train_sql = 'INSERT INTO station (station_id, station, alias, city, city_id, country, map_info, time_zone, time2city_center,ori_map_info,name_en, online_name) VALUES (%s,%s,%s,%s,%s, %s,%s, %s, %s, %s, %s, %s)'

    #return ExecuteSQLs(sql, args)
    return ExecuteSQLs(train_sql, args)


import csv
def indb():
    cf = file('../csvSet/20160426_train_ing.csv', 'r')
    readcsv = csv.reader(cf)
    id = 102037
    l = []
    for each_l in readcsv:
        station = each_l[0].encode('utf-8').lower()
        city_id = each_l[1].encode('utf-8')
        #station_id = each_l[2].encode('utf-8')
        map_info = each_l[3].encode('utf-8').split(',')[1] + ',' + each_l[3].encode('utf-8').split(',')[0]
        city = each_l[4].encode('utf-8')
        
        new_station_id = 'stt' + str(id)
        id = id + 1
        print station, city_id, new_station_id, map_info, city
        station_id = new_station_id
        alias = 'NULL'
        country = 'NULL'
        Program = 'N'
        name_en = 'NULL'
        online_name = 'NULL'
        time_zone = '-100'
        time2city_center = '-100'
        ori_map_info = 'NULL'
        t = (station_id, station, alias, city, city_id, country, map_info, time_zone, time2city_center,ori_map_info,name_en, online_name)
        l.append(t)    

    insertTable(l)


def updateTable():
    cf = file('../csvSet/20160426_train_done.csv', 'r')
    readcsv = csv.reader(cf)
    for ele in readcsv:
        station = ele[0].lower()
        station_id = ele[2].lower()
        alias = 'NULL'
        r_sql = 'select alias from station where station_id = "%s"' % (station_id)
        res = QueryBySQL(r_sql)
        if res[0]['alias'] == 'NULL':
            alias = station.lower()
        else:
            alias = res[0]['alias'] + '&&' + station.lower()
        w_sql = 'update station set alias = "%s" where station_id = "%s"' % (alias, station_id)
        print w_sql
        ExecuteSQL(w_sql)

#updateTable()
#indb()

