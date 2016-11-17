#!/usr/bin/env python
#coding:utf-8

import sys
import json
from GetJsonPath import *

reload(sys)
sys.setdefaultencoding('utf-8')


class GetJsonContent(GetJsonPath):
    
    #解析KEY序列
    def __init__(self):

        pass


    def GetJsonValues(self, dict, route):
        
        content = ''
        path = self.GetKeyPath(route)
        
        content = eval('dict' + path)
    
        return content


if __name__ == '__main__':

    gj = GetJsonContent()
    #res = gj.GetKeyPath('a|s|f|g&2|g')
    
    import sys
    sys.path.append('..')

    from public.PageTreeDict import *
    
    pt = PageTreeDict()
    import os 
    with open('../test/ceair_json', 'r') as f:
        page = f.read()

    try:
        dict = pt.PageTreeDict(page, 'json')
    except Exception, e:
        print str(e)
    ''' 
    res = gj.GetKeyPath('airResultDto|productUnits&1')
    print eval("dict" + res)
    '''
    
    res = gj.GetJsonValues(dict, 'airResultDto|productUnits&0|flightNoGroup')
    print res




