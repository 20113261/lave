#!/usr/bin/env python
# coding=UTF-8
"""
    Created on 2014-03-08
    @author: devin
    @desc:
        数据访问
"""
try:
    import pymysql

    pymysql.install_as_MySQLdb()
except Exception:
    pass
import MySQLdb

import traceback
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
from logger import logger

# 建立数据库连接池
mysql_db_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=2, maxconnections=10,
                         host='10.10.154.38', port=3306, user='writer', passwd='miaoji1109',
                         db='crawl', charset='utf8', use_unicode=False)
mysql_spider_data_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=2, maxconnections=10,
                                  host='10.10.228.253', port=3306, user='writer', passwd='miaoji1109',
                                  db='spider_db', charset='utf8', use_unicode=False)


def get_uc_connection():
    return mysql_db_pool.connection()


def ExecuteSQL(sql, args=None):
    """
        执行SQL语句, 正常执行返回影响的行数，出错返回 False
    """
    try:
        conn = get_uc_connection()
        cur = conn.cursor()

        ret = cur.execute(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        logger.error("ExecuteSQL error: %s" % str(e))
        return False
    return ret


def execute_many_into_spider_db(sql, args):
    try:
        db = mysql_spider_data_pool.connection()
        cursor = db.cursor()
        cursor.executemany(sql, args)
        db.commit()
    except Exception as e:
        logger.warn(traceback.format_exc(e))
        return False
    return True


def close_db(db):
    if db:
        try:
            db.close()
        except Exception:
            pass


def ExecuteSQLs(sql, args=None):
    """
        执行多条SQL语句, 正常执行返回影响的行数，未影响返回 None，出错返回 False
    """
    try:
        uc_conn = get_uc_connection()
        uc_cur = uc_conn.cursor()
        uc_ret = uc_cur.executemany(sql, args)
        uc_conn.commit()

    except MySQLdb.Error, e:
        logger.error("ExecuteSQLs error: %s" % str(e))
        return False
    return uc_ret


def QueryBySQL(sql, args=None, size=None):
    """
        通过sql查询数据库，正常返回查询结果，否则返回None
    """
    results = []
    try:
        conn = get_uc_connection()
        cur = conn.cursor(cursorclass=DictCursor)

        cur.execute(sql, args)
        rs = cur.fetchall()
        for row in rs:
            results.append(row)
    except MySQLdb.Error, e:
        logger.error("QueryBySQL error: %s" % str(e))
        return None
    return results


if __name__ == '__main__':
    print ExecuteSQLs(['asdfasdf'])
    print execute_many_into_spider_db('asdfasdf', 'asdfasdfsdf')
