#!/usr/bin/env python  
import os
import requests
import time

os.system(" ps -ef | grep 'bossStatus.py' | grep -v 'grep' | awk '{print $2}' | xargs kill -9 ")

pid_list = os.listdir('./slavepid')

for i in len(pid_list):
    url = 'http://127.0.0.1:{0}/restart_process'.format(str(8089+i))
    print url
    try:
        r = requests.get(url)
    except:
        pass

time.sleep(15)

for pid in pid_list:
    os.system("kill -9 {0}".format(pid))
