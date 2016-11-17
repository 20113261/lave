#!/usr/bin/env python
#coding:utf-8

import sys

from ResolvePath import *
from PageTreeDict import *
from GetUsedSubtree import *

class StopContent(ResolvePath,  GetUsedSubtree):

    def __init__(self):
        pass

    def StopVertical(self, subTree, Route):
        
        path_list = Route.split('&')
        content = ''
        tempList = []
        usedList = self.GetUsedSubtree(subTree, path_list[0])
        for ele in usedList:

            fcontent = self.ResolvePath(ele, path_list[1])
            scontent = self.ResolvePath(ele, path_list[2])
            str = fcontent + '_' + scontent
            tempList.append(str)

        content = '|'.join(tempList)

        return content

    
    def StopUnder(self, subTree, Route):

        path_list = Route.split('&')
        content = ''
        tempList = []
        usedList = []
        if path_list[0] != '':
            try:
                usedList = self.GetUsedSubtree(subTree, path_list[0])
            except Exception, e:
                pass
            for ele in usedList:
            
                fcontent = self.ResolvePath(ele, path_list[1])
                tempList.append(fcontent)
        
            content = '_'.join(tempList)
        else:
            content = self.ResolvePath(subTree, path_list[1])

        return content


