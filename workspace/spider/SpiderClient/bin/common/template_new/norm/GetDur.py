#!/usr/bin/env python
#coding:utf-8

import sys
import time
import re
from lxml import html as HTML
from lxml import etree
from common.logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')

def GetDur(self, durstr):
    
    '''
        @durstr:dur的原始字符串
        @格式:A_A_A_A.....
    '''
    durstr_list = durstr.split('_')
    dur = 0
    for every in durstr_list:
        pat = re.compile(r'(\d+)',re.S)
        if every.find(':') != -1:
            dur_list = every.split(':')
            dur_dur = int(dur_list[0]) * 3600 + int(dur_list[1]) * 60
            dur = dur + dur_dur
        else:
            dur_list = pat.findall(every)
            dur_dur = int(dur_list[0]) * 3600 + int(dur_list[1]) * 60
            dur = dur + dur_dur

    return dur
