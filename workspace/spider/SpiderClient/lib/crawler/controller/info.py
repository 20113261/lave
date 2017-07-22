#!/usr/bin/env python
#coding=UTF8
'''
    @author: devin
    @time: 2014-02-22
    @desc:
        保存slave的相关信息
'''
import json

class SlaveInfo:
    def __init__(self, name='raffle', local_ip=None, port=-1, recv_real_time_request=False):
        self.name = name            # slave名称
        self.local_ip = local_ip          # 所在机器的IP地址
        self.port = port
        self.recv_real_time_request = recv_real_time_request # 是否接收实时请求
        self.path = None            # 所在机器路径
        self.start_time = None      # 开始运行时间
        self.thread_num = 0         # 运行的线程数目
        self.process_task_num = 0   # 总共处理task个数
        self.error_task_num = 0     # 出错task个数
        self.type = None            # slave类型
        self.last_heartbeat = None  # 最后一次上报心跳信息时间
        self.status = 0             # 状态, 1表示正常，-1表示丢失连接
        self.request_task_num = 0   # 实时请求次数

    @property
    def service_address(self):
        '''
        return service address
        '''
        return "{0}:{1}".format(self.local_ip, self.port)

    def __str__(self):
        return json.dumps(self.__dict__)
