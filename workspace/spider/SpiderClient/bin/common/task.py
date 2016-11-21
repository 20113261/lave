#!/usr/bin/env python
#coding=UTF-8
'''
    Created on 2014-03-22
    @author: devin
    @desc:

'''
import jsonlib
import json
class Task:
    '''
        抓取任务
    '''

    def __init__(self, **kws):
        self.id = 0
        self.task_data = ''
        self.content = None         # 任务内容，不同source的格式可以不同，各个抓取下自行定义
        self.source = None          # 任务来源，用来表明谁来负责处理该任务
        self.task_type = 3          # 任务类型，1表示小时级任务，2表示天级任务，3表示长期任务
        self.priority = 0           # 优先级
        self.crawl_day = None       # 抓取时间，对应长期任务表示再该时间之前处理
        self.crawl_hour = 0         # 抓取时间（小时）
        self.update_times = 0       # 抓取次数
        self.success_times = 0      # 抓取成功次数
        self.update_time = None     # 更新时间
        self.proxy_info = {}        # 代理信息
        self.ticket_info = {}
        self.timeslot = -1

    def init_ticket_info(self, source, ticket_info):
        if not ticket_info:
            return

        source = source.lower()
        if 'flight' in source:
            ticket_info.setdefault('v_seat_type', 'E')
            count = int(ticket_info.setdefault('v_count', 2))
            ticket_info.setdefault('v_age', '_'.join(['-1']*count))
            ticket_info.setdefault('v_hold_seat', '_'.join(['1']*count))

        elif 'hotel' in source:
            ticket_info.setdefault('room_info', [])
            ticket_info.setdefault('occ', 2)
            ticket_info.setdefault('room_count', 1)

        elif 'train' in source:
            ticket_info.setdefault('v_seat_type', '2nd')
            count = int(ticket_info.setdefault('v_count', 2))
            ticket_info.setdefault('v_age', '_'.join(['-1']*count))
            ticket_info.setdefault('v_hold_seat', '_'.join(['1']*count))

        elif 'bus' in source:
            ticket_info.setdefault('v_seat_type', '2nd')
            count = int(ticket_info.setdefault('v_count', 2))
            ticket_info.setdefault('v_age', '_'.join(['-1']*count))
            ticket_info.setdefault('v_hold_seat', '_'.join(['1']*count))

        self.ticket_info.update(ticket_info)

    def __str__(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def parse(s):
        '''
            从json字符串中解析初task
        '''
        if s == None:
            return None

        if s == None or len(s.strip()) == 0:
            return None

        data = None
        try:
            data = jsonlib.read(s)
        except jsonlib.ReadError, e:
            print "Parse json error. task_str = " + s
            return None

        if data == None:
            return None

        task = Task()
        for k, v in data.items():
            task.__dict__[k] = v

        task.task_data = s

        return task


class RequestTask:
    '''
        实时请求任务
    '''
    def __init__(self):
        self.content = None             # 任务内容
        self.source = None              # 任务来源，用来表明谁来负责处理该任务

    def __str__(self):
        return jsonlib.write(self.__dict__)

    @staticmethod
    def parse(s):
        '''
            从json字符串中解析初task
        '''
        if s == None or len(s.strip()) == 0:
            return None

        data = None
        try:
            data = jsonlib.read(s)
        except jsonlib.ReadError, e:
            print "Parse json error.  task_str = " + s
            return None

        if data == None:
            return None

        task = RequestTask()
        for k, v in data.items():
            task.__dict__[k] = v
        return task
