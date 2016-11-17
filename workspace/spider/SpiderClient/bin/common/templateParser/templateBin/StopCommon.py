#!/usr/bin/env python
#coding:utf-8

import sys

from StopContent import *
from GetJoin import * 
from confParser import *
from lxml import html as HTML

class StopCommon(GetConfValues, StopContent, GetJoin):

    def __init__(self):
        pass


    def com_Hfunc(self, every, filename, area, field):

        content = ''

        path = self.GetConfValues(filename, area, field)
        if path == 'error' or path == '':
            content = 'error'
            return content

        and_num = path.count('&')
        
        if and_num == 0:
            content = path
        elif and_num == 1:
            content = self.StopUnder(every, path)
        else:
            content = self.StopVertical(every, path)
        if content == '':
            content = 'error'
        return content
 
    def com_HDfunc(self, page, every, filename, area, field):
        
        import time
        content = ''
        path = self.GetConfValues(filename, area, field)
        if path == 'error' or path == '':
            content = 'error'
            return content
        
        type = self.GetConfValues(filename, area, 'coding')
        t = self.GetConfValues(filename, area, 'req')
        
        #stime = time.time()
        #rootTree = HTML.fromstring(page.decode(type))
        #etime = time.time()
        #print str(etime - stime), '**********'
        rootTree = page
        and_num = path.count('&')
        
        if and_num == 0:
            content = path
        elif and_num == 1:
            if path[:2] == 'g_':
                content = self.StopUnder(rootTree, path[2:])
            else:
                content = self.StopUnder(every, path)
        else:
            if path[:2] == 'g_':
                content = self.StopVertical(rootTree, path[2:])
            else:
                content = self.StopVertical(every, path)
        
        if content == '':
            content = 'error'

        return content
    
    
    def com_Jfunc(self, every, filename, area, field):

        content = ''
        
        path = self.GetConfValues(filename, area, field)
        if path == 'error':
            content = path
            return content

        and_num = path.count('&')
        
        if and_num == 0:
            content = path
        elif and_num == 1:
            content = self.GetUnder(every, path)
        else:
            content = self.GetVertical(every, path)

        return content


if __name__ == '__main__':
    
    print 'aaaaaaaaaaaaaaa'
