#!/usr/bin/env python
#coding:utf-8

import sys
import json


reload(sys)
sys.setdefaultencoding('utf-8')


class GetJsonPath(object):

    def __init__(self):

        pass


    def GetKeyPath(self, route):

        content = ''
        route_list = route.split('|')
        
        for key in route_list:
            
            if key.find('@') > -1:
                key_list = key.split('@')
                content += "['" + key_list[0] + "']" + '[' + key_list[1] + ']'
            elif key.find('@-') > -1:
                key_list = key.split('@')
                content += "['" + key_list[0] + "']" + '[' + key_list[1] + ']'
                print content
            else:
                content += "['" + key + "']"
    
        return content


if __name__ == '__main__':

    gj = GetJsonPath()
    #res = gj.GetKeyPath('a|s|f|g@2|g')
    
    import sys
    sys.path.append('..')

    from PageTreeDict import *
    
    pt = PageTreeDict()
    import os    
    with open('../test/ceair_json', 'r') as f:
        page = f.read()

    try:
        dict = pt.PageTreeDict(page, 'json')
    except Exception, e:
        print str(e)
    
    res = gj.GetKeyPath('airResultDto|productUnits@-1')
    print eval("dict" + res)
