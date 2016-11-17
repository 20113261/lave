#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('../../')
from common.logger import logger
from airport_common import Airport
from airport_cn import Airport_cn_Dict 

reload(sys)
sys.setdefaultencoding('utf-8')

def getId(idStr, model):
    
    result = ''
    if model == '1':#不需处理
        result = idstr
    elif model == '2':#处理中文机场
        pass
    elif model == '3':#处理英文机场
        pass
    else:
        pass

    return result




