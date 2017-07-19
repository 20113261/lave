#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2014-03-08
    @author: devin
    @desc:
        数据访问
'''

from slave import UCConnection
from MySQLdb.cursors import DictCursor
from logger import logger
import MySQLdb


# pymysql pool
import pymysql
from DBUtils.PooledDB import PooledDB


def INIT_SQLPOOL(host='10.10.228.253', user='mioji_admin', passwd='mioji1109', db='crawl', maxconnections=20):
    mysql_db_pool = PooledDB(creator=pymysql, mincached=1, maxcached=2, maxconnections=maxconnections,
                             host=host, port=3306, user=user, passwd=passwd,
                             db=db, charset='utf8', use_unicode=False, blocking=True)
    return mysql_db_pool

PY_POOL = INIT_SQLPOOL()
DATA_PY_POOL = INIT_SQLPOOL(host='10.10.228.253', user='writer', passwd='miaoji1109', db='spider_db')


def close_db(db):
    if db:
        try:
            db.close()
        except:
            pass


def GetUCConnection():
    return UCConnection()


def ExecuteSQL(sql, args=None):
    '''
        执行SQL语句, 正常执行返回影响的行数，出错返回Flase 
    '''
    ret = 0
    try:
        conn = GetUCConnection()
        cur = conn.cursor()

        ret = cur.execute(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        logger.error("ExecuteSQL error: %s" % str(e))
        return False
    finally:
        pass
        # cur.close()
        # conn.close()

    return ret


def execute_into_spider_db(sql, args):
    uc_conn = None
    try:
        uc_conn = DATA_PY_POOL.connection()
        cursor = uc_conn.cursor()
        cursor.executemany(sql, args)
        uc_conn.commit()
        cursor.close()
    except Exception, e:
        logger.error("ExecuteSQLs error: %s" % str(e))
        return False
    finally:
        close_db(uc_conn)

    return True


def ExecuteSQLs(sql, args=None):
    """
          执行多条SQL语句, 正常执行返回影响的行数，出错返回Flase 
    """
    uc_ret = 0
    uc_conn = None

    try:
        uc_conn = PY_POOL.connection()
        cursor = uc_conn.cursor()
        uc_ret = cursor.executemany(sql, args)
        uc_conn.commit()
        cursor.close()

    except Exception, e:
        logger.error("ExecuteSQLs error: %s" % str(e))
        return False
    finally:
        close_db(uc_conn)

    return uc_ret


def QueryBySQL(sql, args=None, size=None):
    '''
        通过sql查询数据库，正常返回查询结果，否则返回None
    '''
    results = []
    try:
        conn = GetUCConnection()
        cur = conn.cursor(cursorclass=DictCursor)

        cur.execute(sql, args)
        rs = cur.fetchall()
        for row in rs:
            results.append(row)
    except MySQLdb.Error, e:
        logger.error("QueryBySQL error: %s" % str(e))
        return None
    finally:
        cur.close()
        # conn.close()

    return results


if __name__ == '__main__':
    if pymysql:
        print 'ss'
