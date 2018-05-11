#!/usr/bin/env python
# coding=UTF-8
"""
    Overwrite on 2016-11-15
    @author: wyl
    @desc:
        作业管理
"""
import os
import random
import json
import urllib
import jsonlib
import time
from util import timer
from common.task import Task
import threading
from common.logger import logger
from crawler.workload import WorkloadStorable
from util.http_client import HttpClientPool, HttpClient
import redis
import requests
import pika
import traceback

from gevent.queue import Queue, Empty

TASK_TIME_SPAN = 150
COMPLETE_TIME_SPAN = 2
TASK_COUNT = 600
TaskQsize = 1000
MaxQsize = 1000


class ControllerWorkload(WorkloadStorable):
    """
        通过Controller进行workload管理
    """

    def __init__(self, host, sources, data_type_str, recv_real_time_request=True):

        self.__client = HttpClientPool(
            host, timeout=1000, maxsize=500, block=True)
        self.__test_client = HttpClientPool(
            '10.10.239.46:12345', timeout=1000, maxsize=500, block=True)
        self.timeout = 2395
        self.__sources = sources
        self.__sem = threading.Semaphore()
        self.__complete_task_sem = threading.Semaphore()
        self.tasks = Queue(maxsize=MaxQsize)
        self.__tasks_status = []
        self.TaskingDict = {}
        self.new_tasks = []
        self.__flag = recv_real_time_request
        self.data_type_str = data_type_str
        self.workload_restart_flag = True
        self.__timer2 = timer.Timer(
            COMPLETE_TIME_SPAN, self.complete_workloads)
        self.__timer2.start()

    def add_workload(self, task):
        while self.tasks.qsize() > (MaxQsize - 100):
            logger.info('request is full, please wait !')
            time.sleep(10)
        self.tasks.put(task)
        logger.info('workload task queue size: {0}'.format(self.tasks.qsize()))

    def get_workloads(self):
        """
            从master取一批workloads
            get every TASK_TIME_SPAN (s), up to TASK_COUNT
        """
        task_length = TASK_COUNT - self.tasks.qsize()
        need_task = task_length
        if need_task <= 0:
            return True

        logger.info('Need %d New Tasks' % task_length)

        url = "/workload?count={0}&qid={1}&type=routine001&data_type={2}".format(need_task, int(1000 * time.time()),
                                                                                 self.data_type_str)
        # if self.data_type_str in ["RoundFlight", "ListHotel", "Flight"]:
        result = self.__test_client.get(url)
        # else:
            # result = self.__client.get(url)
        if result is None or result == []:
            return False

        try:
            result = result.strip('\0').strip()
            self.new_tasks = eval(result)
            logger.info(
                'from master get task count is : {0} / {1}'.format(len(self.new_tasks), need_task))

        except Exception, e:
            logger.info('GET TASKS ERROR: ' + str(e))
            return False

        get_task_count = 0
        for task in self.new_tasks:
            try:
                if not isinstance(task, dict):
                    logger.error('task is not a dict. task=' + str(task))
                    continue

                task_str = json.dumps(task)
                task_strs = Task.parse(task_str)
                self.tasks.put(task_strs)
                if task_strs not in self.TaskingDict:
                    self.TaskingDict[task_strs] = 0
                self.TaskingDict[task_strs] += 1

                get_task_count += 1

            except Exception, e:
                logger.info(
                    'add task from master to tasks fail. error = ' + str(e))
                break

        if get_task_count > 0:
            logger.info("get new task from master: " + str(get_task_count))

        return True

    def write_redis_ticket(self, task, proxy, Error):
        try:
            rds = redis.Redis(host=task.redis_host, port=task.redis_port, db=int(
                task.redis_db), password=task.redis_passwd)
            result = {"err_code": Error, "data": proxy}
            rds.setex(task.redis_key, json.dumps(result), 1800)
        except Exception, e:
            logger.info('writer redis fail. result:{0}'.format(proxy))
            logger.info('writer redis fail.' + str(task.redis_key) + '\t'
                        + task.redis_host + '\t' + str(task.redis_port)
                        + '\t' + str(task.redis_db) + '\t' + str(task.redis_passwd) + '\t' + str(e))

    def assign_workload(self):
        # 使用队列block分配任务
        task = self.tasks.get(block=True)
        return task

    def complete_workload(self, task, Error=0, proxy='NULL'):
        try:
            if self.__flag:
                if proxy == 'NULL':
                    proxy = []

                task.other_info['parser_error'] = int(Error)
                query = {"other_info": task.other_info}
                try:
                    try:
                        logger.info("[error_code 信息入库 redis error:%s, task:%s]".format(Error, task))
                    except Exception:
                        try:
                            logger.info("[error_code 信息入库 redis error:%s task:%s ]".format(Error,
                                                                                           str(task).decode(
                                                                                               'gbk').encode('utf8')))
                        except Exception:
                            pass
                    self.write_redis_ticket(task, proxy, Error)
                except Exception, e:
                    logger.exception('not redis con' + str(e))

                # 临时兼容，有mq配置使用mq推送
                if task.master_info.get('spider_mq_host', None):
                    call_back_toservice(task, query)
                else:
                    url = 'http://{0}/?type={1}&qid={2}&uid={3}&query={4}' \
                        .format(task.host, task.callback_type, task.req_qid, task.req_uid, urllib.quote(json.dumps(query)))
                    HttpClient(task.host).get(url)
                    logger.info("[error_code 信息入库 http code: {0} url: {1}]".format(Error, url))
                return True

            len_key = 1
            if task in self.TaskingDict:
                len_key = self.TaskingDict.pop(task)

            while len_key > 0:
                # # if self.data_type_str not in ["RoundFlight", "ListHotel", "Flight"]:
                # task_status = {"id": task.id, "content": task.content, "source": task.source,
                #                 "workload_key": task.workload_key, "error": int(Error), 'proxy': "NULL",
                #                 "timeslot": task.timeslot}
                # else:
                task_status = {"id": task.id, "content": task.content, "source": task.source,"feedback_times":task.feedback_times,
                                "workload_key": task.workload_key, "error": int(Error), 'proxy': "NULL",
                                "timeslot": task.timeslot,"used_times": task.used_times, "collection_name": task.collection_name,'tid':task.tid}
                self.__tasks_status.append(task_status)

                len_key -= 1

        except Exception, e:
            logger.exception("complete a task fail. error = " + str(e))

        return True

    def complete_workloads(self):
        if self.__flag:
            return True

        len_task = len(self.__tasks_status)
        if len_task > 400:
            len_task = 400

        if len_task <= 0:
            return True

        logger.info(
            'send complete workload finish.task = %s. get response: ' % str(len_task))
        try:
            completed_task = json.dumps(self.__tasks_status[:len_task])
            other_query = '&type=routine002&qid={0}&cur_id=&'.format(int(1000 * time.time()))
            data = {
                "q": urllib.quote(completed_task),
                "type": "routine002",
                "qid": int(1000 * time.time()),
                "cur_id": "",
            }
            # if self.data_type_str in ["RoundFlight", "ListHotel", "Flight"]:
            url = "http://10.10.239.46:12345/complete_workload"
            requests.post(url, data=data, timeout=1000)
            # else:
            #     self.__client.get(
            #     "/complete_workload?q=" + urllib.quote(completed_task) + other_query)
            self.__tasks_status = self.__tasks_status[len_task:]
        except Exception, e:
            logger.error('complete task: {0}'.format(self.__tasks_status[:len_task]))
            logger.error("complete task to master fail. task_count=" +
                        str(len_task) + ' err = ' + traceback.format_exc())

        return True

    def remove_workload(self, task):
        pass

    def update_workload(self, task, priority=0):
        pass

    def clear(self):
        """
            清空作业
        """
        pass

    def add_workloads(self, tasks):
        """
            添加作业
        """
        pass

    def get_task_status(self, task):
        """
            获得指定任务的状态
        """
        pass


def call_back_toservice(task, query):
    logger.debug('[callback a verifytask by rabbitmq]')
    try:
        credentials = pika.PlainCredentials(username=task.master_info['spider_mq_user']
                                            , password=task.master_info['spider_mq_passwd'])
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=task.master_info['spider_mq_host'], virtual_host=task.master_info['spider_mq_vhost'], credentials=credentials
            )
        )
        channel = connection.channel()

        msg = json.dumps({
            'qid': task.req_qid, 'type': task.callback_type,
            'uid': task.req_uid, 'query': json.dumps(query)
        })

        res = channel.basic_publish(
            exchange=task.master_info['spider_mq_exchange'],
            routing_key=task.master_info['spider_mq_routerKey'],
            properties=pika.BasicProperties(delivery_mode=2),
            body=msg,
        )
        connection.close()
        if not res:
            raise Exception('RabbitMQ Result False')
        logger.debug('[callback a verifytask done]')
    except Exception as exc:
        logger.exception("callback a task fail. error = {0}".format(traceback.format_exc()))


if __name__ == '__main__':
    task = Task()
    a= {"content":"MXP&FCO&20170827|FCO&VCE&20170830","csuid":"","master_info":{"master_addr":"10.10.155.146:48067","redis_addr":"10.10.173.116:6379","redis_db":0,"redis_passwd":"MiojiRedisOrzSpiderVerify","spider_mq_exchange":"spiderToVerify","spider_mq_exchangeType":"direct","spider_mq_host":"10.19.131.242","spider_mq_passwd":"miaoji1109","spider_mq_port":"5672","spider_mq_queue":"spider_callback_data","spider_mq_routerKey":"scv101","spider_mq_user":"writer","spider_mq_vhost":"test"},"other_info":{"cache_key":"preflightmulti|10005|10002|20170827|10002|10003|20170830|travelocity|E","callback_type":"scv101","csuid":"","data_type":"flightmulti_new_pre_verify","machine_ip":"10.10.231.156","machine_port":8089,"ptid":"ptid","qid":"1504250930338","redis_key":["flightmulti_new_pre_verify|MXP&FCO&20170827|FCO&VCE&20170830|travelocity|E|10.10.231.156:8089|1504250930338|388325ab112e52427ce4819764c54294|0"],"req_type":"v107","request_begin_time":"1504250930374","result_source_redis_key":"flightmulti_new_pre_verify_1504250930338_ptid_388325ab112e52427ce4819764c54294|travelocity|E_10.10.231.156:8089","source":"travelocityMultiFlight","src":"travelocity","ticket_info":{"csuid":"","env_name":"offline","md5":"388325ab112e52427ce4819764c54294","ptid":"ptid","qid":"1504250930338","tid":"","uid":"test","v_seat_type":"E","verify_type":"pre_verify"},"ticket_md5":"388325ab112e52427ce4819764c54294","tid":"","uid":"test"},"ptid":"ptid","qid":"1504250930338","source":"travelocityMultiFlight","ticket_info":{"csuid":"","env_name":"offline","md5":"388325ab112e52427ce4819764c54294","ptid":"ptid","qid":"1504250930338","tid":"","uid":"test","v_seat_type":"E","verify_type":"pre_verify"},"tid":"","uid":"test"}
    task.parse('''''')
    task.req_qid = '1'
    task.req_uid = '22'
    task.callback_type = 'scv101'
    task.master_info = a['master_info']
    print task.master_info
    call_back_toservice(task, {'code': 1000})
