#!/usr/bin/env python
#coding:utf-8

import sys
import re
from lxml import html as HTML
from lxml import etree
from common.logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')


class GetFloatValues(object):

    def __init__(self):
        pass

    def GetFloatValues(self, pricestr):
        
        price_tmp = pricestr.replace(',', '')
        price = ''
        if price_tmp.find('.') > -1:
            pat = re.compile(r'(\d+.\d+)',re.S)
            price = pat.findall(price_tmp)
        else:
            pat = re.compile(r'(\d+)',re.S)
            price = pat.findall(price_tmp)

        return price


if __name__ == '__main__':

    get = GetFloatValues()

    re = get.GetFloatValues('54,642')

    print re





