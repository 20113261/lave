#!/usr/bin/env python
# coding=UTF8
'''
    @author: devin
    @time: 2014-02-23
    @desc:
        slave
'''
import os
import threading
import json
import urllib
import redis

from info import SlaveInfo
from util import http_client, http_server, timer
from util.logger import logger

HEARTBEAT_TIME_SPAN = 10


class Slave(object):
    def __init__(self, host, port, master_host, workers, env, recv_real_time_request=False):
        '''
            初始化
            @param host: 接收实时请求的ip，当recv_real_time_request为True的时候才使用
            @param port: 接收实时请求的端口，当recv_real_time_request为True的时候才使用
            @param master_host: master的ip和端口
            @param workers: 线程组
            @param recv_real_time_request: 是否能接收实时请求，True表示可以接收，其它表示不能
        '''

        self.__server = http_server.HttpServer('0.0.0.0', port)

        self.__client = http_client.HttpClient(master_host)
        self.__master_host = master_host
        # 保存slave的相关信息
        self.info = SlaveInfo(local_ip=host, port=port,
                              recv_real_time_request=recv_real_time_request)
        self.info.path = os.getcwd()
        # timer，用来定时发送heartbeat状态
        self.env = env
        self.redis = redis.Redis(host='10.10.173.116', port=6379,
                                 password='MiojiRedisOrzSpiderVerify', db=1)
        self.__timer = timer.Timer(HEARTBEAT_TIME_SPAN, self.heartbeat)
        self.__timer_new = timer.Timer(HEARTBEAT_TIME_SPAN, self.__heartbeat)
        # 互斥信号量
        self.__sem = threading.Semaphore()
        self.__workers = workers

    def run(self):
        '''
            启动slave
        '''
        # register
        try:
            self.register("/modify_thread_num", self.modify_thread_num)
        except:
            pass

        # register to master
        try:
            if not self.register_in_master():
                logger.error("Can't register to master.")
        except:
            pass

        # start the timer
        self.__timer.start()
        self.__timer_new.start()

        # start the workers
        self.__workers.start()

        # start the server
        self.__server.run()

    def register(self, path, func):
        '''
            注册http服务
            @param path: http服务的地址
            @param func: 响应请求的函数
        '''
        self.__server.register(path, func)


    def heartbeat(self):
        '''
            向master发起心跳请求，上报目前状态
        '''
        query_json = {"server_ip":self.info.service_address}
        query_json_str = json.dumps(query_json)
        data = {"name": self.info.name,
                "server": self.info.local_ip,
                "path": self.info.path,
                "server_ip": self.info.service_address,
                "query": query_json_str,
                "type": "heartbeat",
                'recv_real_time_request': self.info.recv_real_time_request}

        path = "/heartbeat?" + urllib.urlencode(data)
        try:
            ###test for router
            #try:
            #    router_test_host = '10.10.244.26:48068'
            #    http_client.HttpClient(router_test_host).get(path)
            #except Exception,e:
            #    print 'heartbeat for eouter test fail'
            #test for router done

            http_client.HttpClient(self.__master_host).get(path)
        except Exception, e:
            import traceback
            error_info = str(traceback.format_exc().split('\n'))
            print 'heartbeat_error:' + error_info


    def __heartbeat(self):
        '''
            put signal in a redis to let router know this process is alive
        '''
        key = "{0}_{1}".format(self.info.service_address, self.env)
        return self.redis.set(key, 1, ex=HEARTBEAT_TIME_SPAN)

    def register_in_master(self):
        '''
            向master注册，并获得master分配的id
        '''
        query_json = {"server_ip": self.info.service_address}
        query_json_str = json.dumps(query_json)

        data = {"name": self.info.name,
                "server": self.info.local_ip,
                "path": self.info.path,
                "server_ip": self.info.service_address,
                "query": query_json_str,
                "type": "register_slave",
                'recv_real_time_request': self.info.recv_real_time_request}
        path = "/register_slave?" + urllib.urlencode(data)
        try:
            logger.info('slave register to host:{0}'.format(
                self.__client.host))
            res = self.__client.get(path).strip()
            logger.info('slave register to host:{0} res:{1}'.format(
                self.__client.host, res))
            if json.loads(res)['error']['error_id'] != 0:
                return False
        except Exception as e:
            logger.info(str(e))
        logger.info('slave register to host:%s success', self.__client.host)
        return True

    def modify_thread_num(self, params):
        '''
            响应用户或者master的修改线程请求
        '''
        thread_num = params.get("thread_num")
        if thread_num == None or not thread_num.isdigit():
            return False
        thread_num = int(thread_num)
        self.__workers.set_thread_num(thread_num)

        return True
