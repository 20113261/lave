#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2013-11-15
    @author: devin
    @desc:
        作业管理
'''

import abc


class Task(object):
    """
        保存一个作业
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass


class WorkloadStorable(object):
    """
        作业管理接口
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_workload(self, task):
        """
            添加作业
        """
        pass

    @abc.abstractmethod
    def add_workloads(self, tasks):
        """
            添加作业
        """
        pass

    @abc.abstractmethod
    def assign_workload(self):
        """
            获取一个未处理的作业
        """
        pass

    @abc.abstractmethod
    def complete_workload(self, task, isError=False):
        """
            完成一个作业，isError用来标识处理过程是否出错
        """
        pass

    @abc.abstractmethod
    def remove_workload(self, task):
        """
            删除一个task
        """
        pass

    @abc.abstractmethod
    def update_workload(self, task):
        """
            更新task
        """
        pass

    @abc.abstractmethod
    def clear(self):
        """
            清空作业
        """
        pass

    @abc.abstractmethod
    def get_task_status(self, task):
        """
            获得指定任务的状态
        """
        pass
