#!/usr/bin/env python
#coding=UTF-8
'''
    Created on 2013-11-15
    @author: devin
    @desc:
        进程管理
'''
import sys
sys.path.append('/home/workspace/spider/SpiderClient/lib/')
import os
import re
import time
from util import timer
import commands

PROCESS_TIME_SPAN = 10

class BossStatus():
    '''
        管理salve
    '''
    def __init__(self):
        self.__process_list = []
        self.__timer = timer.Timer(PROCESS_TIME_SPAN, self.update_process_status)
        self.__timer.start()
        self.__process_list = self.get_process_l()


    def get_process_l(self):
        '''
            获取启动的slave进程列表
        '''
        init_process_l = []
        #cmd = "ps -ef | grep 'slave.py' | grep -v 'grep' | awk -F'/conf/' '{print $2}'"
        cmd = "ps -ef | grep 'slave.py' | grep -v 'grep' | awk -F ' ' '{print $10}'"
        init_process_l = commands.getoutput(cmd).split('\n')

        #print init_process_l
        return init_process_l


    def update_process_status(self):
        '''
            检查slave进程是否被kill
        '''
        ISOTIMEFORMAT='%Y-%m-%d %X'
        cur_process_list = []
        restart_list = []
        cur_process_list = []
        cur_process_list = self.get_process_l()
        restart_list = filter(lambda x:x not in cur_process_list, self.__process_list)

        print restart_list

        if restart_list != []:
            for process in restart_list:
                #abspath = os.path.abspath(__file__)
                #confdir = os.path.abspath(__file__, os.pardir)
                #abspath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
                #confdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
                abspath = '/home/workspace/spider/SpiderClient/bin/start/start.sh'
                pat = re.compile(r'\d+')
                number = pat.findall(process)[0]

                cmd = 'sh ' + abspath + ' ' + str(number)
                os.system(cmd)
                restartTime = time.strftime(ISOTIMEFORMAT, time.localtime())
                print '[' + restartTime + ']\t' + '[BOSS::restart]' + '\t'+process


bs = BossStatus()
