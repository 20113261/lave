#!/usr/bin/env python
# coding=utf-8
import gevent.monkey

gevent.monkey.patch_all()
import pika
import json
import logging
from mioji.common.logger import logger

# test
# HOST = '10.10.213.148'
# USER = 'hourong'
# PASSWD = '1220'

logging.getLogger("pika").setLevel(logging.WARNING)
logging.getLogger("pika").propagate = False

# online
HOST = '10.10.38.166'
USER = 'main'
PASSWD = 'main'


def insert_rabbitmq(args, queue_list, routing_key):
    logger.debug('[rabbitmq 入库开始]')
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

        # 此部分代码会修改 exchange 以及定义 queue
        # for q in queue_list:
        #     channel.queue_declare(queue=q, durable=True)
        #     channel.queue_bind(queue=q, exchange='TrafficDataPush', routing_key=routing_key)

        msg = json.dumps(args, ensure_ascii=False)

        res = channel.basic_publish(exchange='TrafficDataPush', routing_key=routing_key, body=msg,
                                    properties=pika.BasicProperties(
                                        delivery_mode=2))
        connection.close()
        if not res:
            raise Exception('RabbitMQ Result False')
        logger.debug('[rabbitmq 入库结束]')
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    a = [(1, 2, 3), (2, 3, 4)]
    q_list = ['dround_dev', 'dround_ol']
    for i in range(100):
        insert_rabbitmq(args=a, queue_list=q_list, routing_key='round')
