#!/usr/bin/env python
# encoding: utf-8

import sys
import os.path
import time

time_diff = 1*60*60 #1 hour

cand_file = 'request_validation.py'
cand_file = 'a.xx'

file_dir='/home/workspace/spider/SpiderClient/bin/start/'

for file_name in os.listdir(file_dir):
    cand_file = file_dir + file_name
    if not os.path.isfile(cand_file):
        print 'not file ' + cand_file
        continue

    if len(file_name) == 32:
        statinfo=os.stat(cand_file)

        modify_time = statinfo.st_mtime

        modify_timespan = time.time() - statinfo.st_mtime

        if modify_timespan >= time_diff:
            os.remove(cand_file)
