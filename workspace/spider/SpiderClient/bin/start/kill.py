#!/usr/bin/env python  
import os
import requests
import time 
import sys

os.system(" ps -ef | grep 'bossStatus.py' | grep -v 'grep' | awk '{print $2}' | xargs kill -9 ")

for i in range(int(sys.argv[1])): 

    url = 'http://127.0.0.1:{0}/restart_process'.format(str(8089+i))
    print url
    try:
        r = requests.get(url)
    except:
        pass

time.sleep(20)


os.system("ps -ef | grep 'slave' | grep -v 'grep' | awk '{print $2}' | xargs kill -9 ")