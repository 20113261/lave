#!/usr/bin/env python
#coding:utf-8

import sys
import re
#from common.logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')


def GetNum(str_temp):
    
    result = ''
    str_temp = str_temp.replace(',', '')
    pat = re.compile(r'(\d+.?\d+)',re.S)
    result = pat.findall(str_temp)[0]

    return result






