#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 下午2:24
# @Author  : Hou Rong
# @Site    :
# @File    : test_insert_rabbitmq.py
# @Software: PyCharm

# !/usr/bin/env python
# coding=utf-8
import gevent.monkey
from gevent.event import Event

gevent.monkey.patch_all()
import pika
import json
import logging
import functools
from mioji.common.spider import logger

# test
HOST = '10.10.213.148'
USER = 'hourong'
PASSWD = '1220'

logging.getLogger("pika").setLevel(logging.WARNING)
logging.getLogger("pika").propagate = False


# online
# HOST = '10.10.38.166'
# USER = 'master'
# PASSWD = 'master'


def insert_rabbitmq(args, queue_list, routing_key, test_key=0):
    logger.debug('[rabbitmq 入库开始][test_key][%s]' % test_key)
    try:
        credentials = pika.PlainCredentials(username=USER, password=PASSWD)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=HOST, virtual_host='TrafficDataPush', credentials=credentials
            )
        )
        channel = connection.channel()

        channel.exchange_declare(exchange='TrafficDataPush',
                                 # exchange_type='fanout',
                                 durable=True,
                                 auto_delete=False)
        for q in queue_list:
            channel.queue_declare(queue=q, durable=True)
            channel.queue_bind(queue=q, exchange='TrafficDataPush', routing_key=routing_key)

        msg = json.dumps(args, ensure_ascii=False)

        res = channel.basic_publish(exchange='TrafficDataPush', routing_key=routing_key, body=msg,
                                    properties=pika.BasicProperties(
                                        delivery_mode=2))
        connection.close()
        if not res:
            raise Exception('RabbitMQ Result False')
        logger.debug('[rabbitmq 入库结束][test_key][%s]' % test_key)
    except Exception as exc:
        raise exc


def task_wrapper(func):
    """
    apply_async 是在结果成功时调用 callback 中的函数，通过此方法将异常返回
    :param func: task 函数，例如：self.__single_crawl
    :return: 返回 函数结果 或 函数异常，以及为哪一者
    """

    @functools.wraps(func)
    def call(*args, **kwargs):
        try:
            return func(*args, **kwargs), True
        except Exception as exc:
            logger.exception('[新框架][页面解析异常][ {0} ]'.format(traceback.format_exc().replace('\n', '\t')))
            return (args, kwargs, exc), False

    return call


def block_async(pool, func, params):
    """
    通过 Event Lock 完成
    :param pool: 进程／线程／协程池
    :param func: 任务函数
    :param params: 可遍历项
    :return: 结果列表，由于被 task_wrapper 封装，返回值为 list [(res, is_data), ...]
    """
    result = []
    lock = Event()

    def callback(r):
        result.append(r)
        if len(result) == len(params):
            lock.set()

    for p in params:
        pool.apply_async(task_wrapper(func), p, callback=callback)

    lock.wait()
    return result


if __name__ == '__main__':
    import gevent.pool

    a = [(1, 2, 3), (2, 3, 4)]
    q_list = ['dround_dev', 'dround_ol', 'sround']

    # Group Function Test

    # group = []
    # pool = gevent.pool.Pool(50)
    # for i in range(50):
    #     group.append(
    #         pool.apply_async(insert_rabbitmq, kwds=dict(args=a, queue_list=q_list, routing_key='round', test_key=i)))
    # gevent.joinall(group)

    # block_async Function Test

    pool = gevent.pool.Pool()
    block_async(pool, insert_rabbitmq, [(a, q_list, 'round', i) for i in range(50)])
