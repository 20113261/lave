#!/usr/bin/env python
#coding:utf-8

import sys
import re
#sys.path.append('../../')
import json
from common.currency_common import Currency_Dict 
reload(sys)
sys.setdefaultencoding('utf-8')


def getCurrency(cur_str):
    
    currency = ''
    for each_key in Currency_Dict:
        if cur_str == each_key:
            currency = Currency_Dict[cur_str]
            return currency
        else:
            #return 'NULL'
	    continue

if __name__ == '__main__':
    print getCurrency('CAD$')





