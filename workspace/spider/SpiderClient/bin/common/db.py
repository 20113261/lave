#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2014-03-08
    @author: devin
    @desc:
        数据访问
'''
import sys
import traceback
from slave import UCConnection
from MySQLdb.cursors import DictCursor
import datetime
from logger import logger

# try:
#     import pymysql
#     pymysql.install_as_MySQLdb()
# except Exception:
#     pass
import pymysql
import MySQLdb


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


def execute_many_bypymsql(sql, args):
    host = '10.10.154.38'
    user = 'writer'
    passwd = 'miaoji1109'
    db_name = 'crawl'
    # 打开数据库连接
    try:
        db = pymysql.connect(host, user, passwd, db_name, charset='utf8')
        cursor = db.cursor()
        cursor.executemany(sql, args)
        db.commit()
    except:
        logger.warn(traceback.format_exc())
        return False
    finally:
        close_db(db)
    return True


def execute_many_into_spider_db(sql, args):
    host = '10.10.228.253'
    user = 'writer'
    passwd = 'miaoji1109'
    db_name = 'spider_db'
    db = None
    # 打开数据库连接
    try:
        db = pymysql.connect(host, user, passwd, db_name, charset='utf8')
        cursor = db.cursor()
        cursor.executemany(sql, args)
        db.commit()
    except Exception as e:
        logger.warn(traceback.format_exc(e))
        return False
    finally:
        close_db(db)
    return True


def close_db(db):
    if db:
        try:
            db.close()
        except Exception:
            pass


def ExecuteSQLs(sql, args=None):
    '''
        执行多条SQL语句, 正常执行返回影响的行数，出错返回Flase 
    '''
    # ret = 0
    uc_ret = 0
    try:
        # conn = GetConnection()
        # cur = conn.cursor()
        # ret = cur.executemany(sql, args)
        # conn.commit()

        uc_conn = GetUCConnection()
        uc_cur = uc_conn.cursor()
        uc_ret = uc_cur.executemany(sql, args)
        uc_conn.commit()

    except MySQLdb.Error, e:
        logger.error("ExecuteSQLs error: %s" % str(e))
        return False
    finally:
        pass
        # cur.close()
        # conn.close()

    return uc_ret


def QueryBySQL(sql, args=None, size=None):
    '''
        通过sql查询数据库，正常返回查询结果，否则返回None
    '''
    results = []
    try:
        conn = GetConnection()
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
