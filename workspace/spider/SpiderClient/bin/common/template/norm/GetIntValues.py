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


class GetIntValues(object):

    def __init__(self):
        pass

    def GetIntValues(self, durstr):

        rest = ''
        pat = re.compile(r'(\d+)',re.S)
        rest = pat.findall(durstr)[0]

        return rest


if __name__ == '__main__':

    getdur = GetIntValues()
    res = getdur.GetIntValues('中转1次')
    print res
