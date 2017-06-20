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
        result = self.__client.get(url)
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
            rds.setex(task.redis_key, json.dumps(result), 600)
        except Exception, e:
            logger.info('writer redis fail. result:{0}'.format(proxy))
            logger.info('writer redis fail.' + str(task.redis_key) + '\t'
                        + task.redis_host + '\t' + str(task.redis_port)
                        + '\t' + str(task.redis_db) + '\t' + str(task.redis_passwd) + '\t' + str(e))

    def assign_workload(self):

        if self.tasks.qsize() <= 0:
            return None
        try:
            task = self.tasks.get()
        except Exception:
            return None
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

                url = 'http://{0}/?type={1}&qid={2}&uid={3}&query={4}' \
                    .format(task.host, task.callback_type, task.req_qid, task.req_uid, urllib.quote(json.dumps(query)))

                HttpClient(task.host).get(url)
                logger.info("[error_code 信息入库 http code: {0} url: {1}]".format(Error, url))
                return True

            len_key = 1
            if task in self.TaskingDict:
                len_key = self.TaskingDict.pop(task)

            while len_key > 0:
                task_status = {"id": task.id, "content": task.content, "source": task.source,
                               "workload_key": task.workload_key, "error": int(Error), 'proxy': "NULL",
                               "timeslot": task.timeslot}
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
            self.__client.get(
                "/complete_workload?q=" + urllib.quote(completed_task) + other_query)
            self.__tasks_status = self.__tasks_status[len_task:]
        except Exception, e:
            logger.info("complete task to master fail. task_count=" +
                        str(len_task) + ' err = ' + str(e))

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
