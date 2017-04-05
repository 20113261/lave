#!/usr/bin/env python
import pika
import json

# test
# HOST = '10.10.213.148'
# USER = 'hourong'
# PASSWD = '1220'


# online
HOST = '10.10.38.166'
USER = 'master'
PASSWD = 'master'


def insert_rabbitmq(args, queue_list, routing_key):
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
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    a = [(1, 2, 3), (2, 3, 4)]
    q_list = ['dround_dev', 'dround_ol', 'sround']
    insert_rabbitmq(args=a, queue_list=q_list, routing_key='round')
