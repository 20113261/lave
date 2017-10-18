#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2013-11-15
    @author: devin
    @desc:
        进程管理
'''
import os
import re
import time
from util import timer
import commands
from SendMail import send

PROCESS_TIME_SPAN = 20


class BossStatus(object):
    """
        管理salve
    """

    def __init__(self):
        self.__process_list = []
        self.__timer = timer.Timer(PROCESS_TIME_SPAN, self.update_process_status)
        self.__timer.start()
        self.__process_list = self.get_process_l()

    def getLocalIp(self, ifname='eth0'):
        import socket, fcntl, struct
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))

        ret = socket.inet_ntoa(inet[20:24])

        return ret

    def get_process_l(self):
        """
            获取启动的slave进程列表
        """
        cmd = "ps -ef | grep 'slave.py' | grep -v 'grep' | awk -F ' ' '{print $10}'"
        init_process_l = commands.getoutput(cmd).split('\n')
        return init_process_l

    def update_process_status(self):
        """
            检查slave进程是否被kill
        """
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        cur_process_list = []
        cur_process_list = []
        cur_process_list = self.get_process_l()
        restart_list = filter(lambda x: x not in cur_process_list, self.__process_list)
        content = ''
        if restart_list:
            for process in restart_list:
                abspath = '/home/SpiderClient/bin/start/boss_start.sh'
                pat = re.compile(r'\d+')
                number = pat.findall(process)[0]

                cmd = 'sh ' + abspath + ' ' + str(number)
                os.system(cmd)
                restart_time = time.strftime(ISOTIMEFORMAT, time.localtime())
                print '[' + restart_time + ']\t' + '[BOSS::restart]' + '\t' + process
                content += ' | ' + str(number)

        if content != '':
            print 'content is %s' % content
            print 'self.getLocalIp() is ' + self.getLocalIp()
            # send('[爬虫监控][爬虫 slave][进程被 kill]', self.getLocalIp() + ' :: ' + content,
            #      'dujun@mioji.com;changjing@mioji.com;hourong@mioji.com;shengweisong@mioji.com')


bs = BossStatus()
