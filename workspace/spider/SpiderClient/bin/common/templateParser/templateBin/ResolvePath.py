#!/usr/bin/env python
#coding:utf-8

import sys

from GetContent import *
from PageTreeDict import *
from common.logger import logger
from lxml import html

class ResolvePath(GetContent):

    def __init__(self):
        pass
    
    def ResolvePath(self, subTree, Route):

        content = ''
        path_list = Route.split('|')
        i = 1
        NodeInfo = subTree
        for ele in path_list:
            if i != len(path_list):
                i = i + 1
                if ele.find('id=') > -1:
                    res = res = self.GetNode(NodeInfo, ele)
                try:
                    res = self.GetNode(NodeInfo, ele)[0]
                except Exception, e:
                    continue
                NodeInfo = res
            else:
                try:
                    content = self.GetRegularContent(NodeInfo, ele).replace('\t','')
                except Exception, e:
                    continue
        return content

