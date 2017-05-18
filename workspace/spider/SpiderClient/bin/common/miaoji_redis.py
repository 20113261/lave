#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2014-11-13
    @author: zy
    @desc:
        访问redis
'''
import sys
import redis
from logger import logger
from conf_manage import ConfigHelper


uc_redis_pool = redis.ConnectionPool()
config_helper = ConfigHelper()

def get_connection(db=0, redis_host=None, redis_port=None):
    if redis_host != None and redis_port != None:
        return redis_connection(db, redis_host, redis_port)
    else:
        return redis_connection(db)


def redis_connection(redis_host=config_helper.redis_host, redis_port=config_helper.redis_port, db=0):
    r = redis.Redis(host=redis_host, port=redis_port,
                    db=db, connection_pool=uc_redis_pool)
    return r


def SetKey(key, value, expire_time=259200, db=0, redis_host=None, redis_port=None):
    '''
        单独key set
    '''
    try:
        r = get_connection(db, redis_host, redis_port)
        r.set(key, value)
        if expire_time != -1:
            r.expire(key, expire_time)
        return True
    except Exception, e:
        logger.error("SetKey error: %s" % str(e))
        return False


def SetKeys(args, expire_time=259200, db=0, redis_host=None, redis_port=None):
    '''
        批量处理set操作
    '''
    if not isinstance(args, dict):
        logger.error("SetKeys error: args needs dictionary")
    try:
        r = get_connection(db, redis_host, redis_port)
        # 设置管道
        pipe = r.pipeline()
        for k, v in args.iteritems():
            pipe.set(k, v)
            if expire_time != -1:
                pipe.expire(k, expire_time)
        return pipe.execute()
    except Exception, e:
        logger.error("SetKeys error: %s" % str(e))
        return False


def HsetKeys(workload_key, args, db, expire_time=604800):
    '''
        hset
    '''
    if not isinstance(args, dict):
        logger.error("HsetKeys error: args needs dictionary")
    if workload_key == "NULL":
        logger.error("HsetKeys error: null workload_key")

    try:
        r = get_connection(db)
        r.delete(workload_key)
        pipe = r.pipeline()
        for k, v in args.iteritems():
            pipe.hset(workload_key, k, v)
        # if expire_time != -1:
        #    pipe.expire(workload_key, expire_time)
        return pipe.execute()
    except Exception, e:
        logger.error("HsetKeys error: %s" % str(e))
        return False
