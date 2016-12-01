#!/usr/bin/env python
#coding=UTF-8
'''
    Overwrite on 2016-11-15
    @author: wyl
    @desc:
        作业管理
'''
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
from util.http_client import HttpClientPool,HttpClient
import redis
import sys

from gevent.queue import Queue, Empty
TASK_TIME_SPAN = 150
COMPLETE_TIME_SPAN = 2
TASK_COUNT = 1200
TaskQsize = 1000
MaxQsize = 85000
class ControllerWorkload(WorkloadStorable):
    '''
        通过Controller进行workload管理
    '''
    def __init__(self, host, sources,  forbide_section_str, recv_real_time_request = True):

        self.__client = HttpClientPool(host, timeout = 1000, maxsize = 500, block = True)

        self.__sources = sources
        self.__sem = threading.Semaphore()
        self.__complete_task_sem = threading.Semaphore()
        self.__tasks = Queue(maxsize = MaxQsize)
        self.__tasks_status = []
        self.__flag = recv_real_time_request
        self.__forbide_section_str = forbide_section_str

        #self.__timer = timer.Timer(TASK_TIME_SPAN, self.get_workloads)
        #self.__timer.start()
        self.__timer2 = timer.Timer(COMPLETE_TIME_SPAN, self.complete_workloads)
        self.__timer2.start()

    def add_workload(self, task):
        while self.__tasks.qsize() > (MaxQsize - 100):
            logger.info('request is full, please wait !')
            time.sleep(10)
        self.__tasks.put(task)

    def get_workloads(self):
        '''
            从master取一批workloads
            get every TASK_TIME_SPAN (s), up to TASK_COUNT
        '''

        task_length = TASK_COUNT - self.__tasks.qsize()

        if task_length <= 0 :
            return True

        logger.info('Need %d New Tasks'%task_length)
        url = "/workload?forbid="  + self.__forbide_section_str + "&count=" + str(task_length)
        result = self.__client.get(url)
        logger.info(result)
        if result == None or result == []:
            return False

        try:
            result = result.strip('\0').strip()
            tasks = eval(result)
        except Exception,e:
            logger.info('GET TASKS ERROR: '+str(e))
            return False
        for task in tasks:
            try:
                if not isinstance(task,dict):
                    logger.error('task is not a dict. task=' + str(task))
                    continue

                task_str = json.dumps(task)
                self.__tasks.put(Task.parse(task_str))
                while(self.__tasks.qsize() > TaskQsize):
                    time.sleep(0.5)
            except Exception,e:
                logger.info('add task from master to tasks fail. error = ' + str(e))
                return False

        return True



    def write_redis_ticket(self, task, proxy,Error ):
        try:
            rds = redis.Redis(host=task.redis_host, port=task.redis_port,  db=int(task.redis_db), password = task.redis_passwd)
            result = {"err_code":Error,"data":proxy }
            rds.setex(task.redis_key, json.dumps(result),600)
        except Exception,e:
            logger.info('writer redis fail.' + str(task.redis_key) + '\t' \
                    + task.redis_host + '\t' + str(task.redis_port) \
                    + '\t' + str(task.redis_db) + '\t' + str(task.redis_passwd) + '\t' + str(e))

    def assign_workload(self):

        if self.__tasks.qsize() <= 0:
            return None
        try:
            task = self.__tasks.get()
        except:
            logger.info('self.__tasks is not task ')
            return None
        return task

    def complete_workload(self, task, Error = 0, proxy='NULL'):
        if self.__flag:
            if proxy == 'NULL':  proxy = []

            logger.info('server is start! ')
            query = {"other_info":task.other_info}
            try:
                self.write_redis_ticket(task, proxy,Error)
            except Exception,e:
                logger.info('not redis con'+str(e))

            url = 'http://'+task.host+'/?type=scv100&qid='+task.req_qid+'&uid='+task.req_uid+'&query='+ urllib.quote(json.dumps(query))
            logger.info(url)

            HttpClient(task.host).get(url)
            return True

        task_status = {"id": task.id, "content": task.content, "source": task.source, \
                "workload_key": task.workload_key, "error": Error,'proxy' : proxy,"timeslot": task.timeslot}
        self.__tasks_status.append(task_status)

        return True

    def complete_workloads(self):
        if self.__flag:

            return True

        len_task = len(self.__tasks_status)
        if len_task > 50:
            len_task = 50
        logger.info('send complete workload finish.task = %s. get response: ' % str(len_task))
        if len_task <= 0:
            return True
        result = self.__client.get("/complete_workload?q=" + urllib.quote(jsonlib.write(self.__tasks_status[:len_task])))
        self.__tasks_status = self.__tasks_status[len_task:]
        return True
    def remove_workload(self, task):
        pass

    def update_workload(self, task, priority = 0):
        pass

    def clear(self):
        '''
            清空作业
        '''
        pass

    def add_workloads(self, tasks):
        '''
            添加作业
        '''
        pass

    def get_task_status(self, task):
        '''
            获得指定任务的状态
        '''
        pass

