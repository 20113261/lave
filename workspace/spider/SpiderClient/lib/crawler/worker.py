#!/usr/bin/env python
# coding=UTF-8
"""
    Overwrite on 201-02-23
    @author: wyl
    @desc:
       抓取线程
"""
import gevent

import threading
import time
import gc
import os
import datetime
from util.logger import logger
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()


class Worker(threading.Thread):
    """
        工作线程
    """

    def __init__(self, workers, thread_name, greents_num, func, workload):
        self.__workers = workers
        self.__busy = False
        self.__pool = Pool(greents_num + 1)
        self.greents_num = greents_num
        self.thread_name = thread_name
        self.__func = func
        self.workload = workload
        threading.Thread.__init__(self, None, None, self.thread_name, (), {})
        logger.info("%s init complete" % self.thread_name)

    def task_entrance(self, task):
        try:
            with gevent.Timeout(self.workload.timeout):
                self.__func(task)
        except gevent.Timeout:
            self.workload.complete_workload(task, '52', 'NULL')
            logger.info('>>>>>>>>>>>>>> task timeout!' + str(task))

    def dojudge(self):

        r = os.popen('free -am').readlines()[1].split(' ')[-1].strip()

        if int(r) < 500:
            gc.collect()
            return False

        return True

    def run(self):

        self.__busy = True
        while self.__busy:
            task = self.workload.assign_workload()

            try:

                if task is None:
                    time.sleep(2)
                    continue
                self.__pool.spawn(self.task_entrance, task)
            except Exception:
                logger.info('get  assign task failed sleep 3s')
                time.sleep(3)

        self.__busy = False

        logger.info("%s stop" % self.thread_name)

    def is_busy(self):
        return self.__busy

    def stop(self):
        self.__busy = False
        time.sleep(0.5)


class Workers(object):
    def __init__(self, workload, func, thread_num=10, greents_num=100, recv_real_time_request=True):
        self.__workers = []  # 存放所有的workers
        self.__greents_num = greents_num
        self.__func = func
        self.__workload = workload

        self.__index = 0
        self.__flag = recv_real_time_request
        for i in range(thread_num):
            self.add_worker()

    def workload_run(self):
        while self.__workload.workload_restart_flag:
            try:
                self.__workload.get_workloads()
                time.sleep(5)
            except Exception, e:
                logger.info('from master get task thread is  killed , sleep 3s ' + str(e))
                time.sleep(8)

        logger.info('get task thread is killed')

    def start(self):
        """
            启动线程
        """
        # 由于在每个子线程中会使用到datetime.trrptime,而datetime.trrptime是线程不安全的
        # 因此在启动子线程之前先调用一次datetime.trrptime,保证线程在使用strptime之前已经得到相关的锁
        datetime.datetime.strptime('2016-08-21', '%Y-%m-%d')

        for worker in self.__workers:
            worker.start()
        logger.info(self.__flag)
        if not self.__flag:
            t = threading.Thread(target=self.workload_run, args=())
            t.start()

    def add_worker(self):
        """
            添加一个worker
        """
        self.__index += 1
        worker = Worker(self, "work_thread_" + str(self.__index), self.__greents_num, self.__func, self.__workload)
        self.__workers.append(worker)
        return worker

    @staticmethod
    def stop_worker(worker):
        """
            停止一个worker
        """
        worker.stop()

    def status(self):
        for worker in self.__workers:
            print str(datetime.datetime.now()), worker.thread_name, worker.is_busy(), worker.isAlive()

    def stop(self):
        """
            停止所有的workers线程
        """
        for worker in self.__workers:
            worker.stop()
        time.sleep(1)

    def check_alive_worker(self):
        """
            遍历所有线程，确认线程是否alive，对应不是alive的线程，从workers里面删除
        """
        self.__workers = filter(lambda w: w.isAlive() and w.is_busy(), self.__workers)

    def get_thread_num(self):
        """
            返回当前的线程数目，只统计运行的线程
        """
        self.check_alive_worker()
        return len(self.__workers)

    def set_thread_num(self, thread_num):
        """
            调整线程的个数
        """
        self.check_alive_worker()
        i = len(self.__workers)

        if i < thread_num:  # 线程数不够，增加线程
            while i < thread_num:
                i += 1
                worker = self.add_worker()
                worker.start()
        elif i > thread_num:  # 线程数过多，stop一些线程
            while i > thread_num:
                i -= 1
                worker = self.__workers.pop()
                worker.stop()
