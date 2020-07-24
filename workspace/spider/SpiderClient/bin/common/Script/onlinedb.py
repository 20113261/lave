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
#from subordinate import Connection
from MySQLdb.cursors import DictCursor
import datetime
#from logger import logger
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
# MySQL 连接信息
MYSQL_HOST = '10.10.87.87'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'miaoji@2014!'
MYSQL_DB = 'devdb'


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

def instation(args):
     sql = 'INSERT INTO station (station_id, station, alias, city, city_id, country, map_info, time_zone, time2city_center,ori_map_info,name_en, online_name, belong_city_id, source, status, online_name_en) VALUES (%s,%s,%s,%s,%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
     return ExecuteSQLs(sql, args)


from CoordDist import getDist 
def travelfusion():
    
    from Dict import ndict
    import csv
    cf = file('./station_list1.csv', 'r')
    readcsv = csv.reader(cf)
    ID = 102235
    l = []
    for line in readcsv:
        code = line[0]
        station = line[1].lower()
        country = line[4]
        map_info = line[6] + ',' + line[5]
        source = line[7]
        country_table = 'select name from country where country_code = "%s"' % (country)
        try:
            country_zh = QueryBySQL(country_table)[0]['name']
        except:
            continue
        if code in ndict:
            stationid = ndict[code]
            sql = 'select alias from station where station_id = "%s"' % (stationid)
            alias = QueryBySQL(sql)[0]['alias'] + '&&' + station
            updatesql = 'update station set alias = "%s" where station_id = "%s"' % (alias.replace('NULL&&', ''), stationid)
            print updatesql
            ExecuteSQL(updatesql)
        else:
            station_id = 'stt' + str(ID)
            ID = ID + 1
            city = 'NULL'
            time_zone = -100
            time2city_center = -100
            name_en = station
            online_name = station
            belong_city_id = 'NULL'
            status = 'Open'
            online_name_en = station
            alias = 'NULL'
            city_id = 'NULL'
            ori_map_info = map_info
            t = (station_id, station, alias, city, city_id, country_zh, map_info, time_zone, time2city_center,ori_map_info,name_en, online_name, belong_city_id, source, status, online_name_en)
            print t
            l.append(t)
    instation(l)
        #tablesql = 'select * from station where country = "%s"' % (country_zh) 
        #res = QueryBySQL(tablesql)
        #for l in res:
        #    try:
        #        inmap = l['map_info']
        #        if inmap == None or inmap == 'NULL':
        #            continue
        #        dis = getDist(float(line[6]), float(line[5]), float(inmap.split(',')[0]), float(inmap.split(',')[1]))
        #        if int(dis) <= 100:
        #            print code, l['station_id']
        #    except:
        #        continue
#travelfusion()

