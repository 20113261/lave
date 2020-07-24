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
import os
#from subordinate import Connection
from MySQLdb.cursors import DictCursor
import datetime
import commands
#from logger import logger
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


def bus():
    sql = 'select station_id, station, alias from bus'
    res = QueryBySQL(sql)
    result = """#/usr/bin/env python\n#coding:utf-8\nimport os\nimport sys\n\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nBus_Dict = {\n"""
    with open('bus_common.py','w') as new_file:
        new_file.write(result)
    temp = ''
    for ele in res:
        station = ele['station'].encode('utf-8').upper()
        station_id = ele['station_id'].encode('utf-8')
        try:
            alias_l = ele['alias'].encode('utf-8').split('&&')
        except:
            alias_l = ['NULL']
        if alias_l != [] or alias_l != ['NULL']:
            for e in alias_l:
                if e == 'NULL':
                    continue
                aname = e.encode('utf-8').upper()
                temp += '"' + aname + '":"' + station_id + '",\n' 
        else:
            pass
        temp += '"' + station + '":"' + station_id + '",\n' 
    with open('temp', 'w') as f:
        f.write(temp)
    cmd = 'cat /search/Sextract/Script/temp | sort | uniq >> /search/Sextract/Script/bus_common.py'
    t = os.system(cmd)
    with open('bus_common.py', 'r') as fread:
        new_dict = fread.read()
    with open('bus_common.py', 'w') as new_file:
        new_file.write(new_dict[:-2] + '}')

def train():
    sql = 'select station_id, station, alias from station'
    res = QueryBySQL(sql)
    result = """#/usr/bin/env python\n#coding:utf-8\nimport os\nimport sys\n\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nStation = {\n"""
    with open('station_common.py','w') as new_file:
        new_file.write(result)
    temp = ''
    for ele in res:
        station = ele['station'].encode('utf-8').upper()
        station_id = ele['station_id'].encode('utf-8')
        try:
            alias_l = ele['alias'].encode('utf-8').split('&&')
        except:
            alias_l = ['NULL']
        if alias_l != [] or alias_l != ['NULL']:
            for e in alias_l:
                if e == 'NULL':
                    continue
                aname = e.encode('utf-8').upper()
                temp +='"' + aname + '":"' + station_id + '",\n' 
        else:
            pass
        temp +='"' + station + '":"' + station_id + '",\n' 
    with open('temp', 'w') as f:
        f.write(temp)
    cmd = 'cat /search/Sextract/Script/temp | sort | uniq >> /search/Sextract/Script/station_common.py'
    t = os.system(cmd)
    with open('station_common.py', 'r') as fread:
        new_dict = fread.read()
    with open('station_common.py', 'w') as new_file:
        new_file.write(new_dict[:-2] + '}')

if __name__ == '__main__':
    import sys

    Type = sys.argv[1]
    if Type.lower() == 'bus':
        bus()
    elif Type.lower() == 'train':
        train()
    else:
        pass
