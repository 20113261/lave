#!/usr/bin/env python
#coding:utf-8

import sys

import re
import json
from lxml import html as HTML
from lxml import etree
from common.logger import logger
from GetContent import *

reload(sys)
sys.setdefaultencoding('utf-8')

#解析复杂XPATH路径获取子树列表
class GetUsedSubtree(GetContent):

    def __init__(self):
        pass

    def GetUsedSubtree(self, isTree, route):
           
        usedSubtree = []
        if route.find('$') > -1:
            route_list = route.split('$') 
            path = route_list[0].split('|att=./@')
            path_list = path[0].split('|')
            i = 1
            nodeinfo = isTree
            if route_list[1].find('|') == -1:
                for ele in path_list:
                    if i != len(path_list):
                        i = i + 1
                        if ele.find('id=') > -1:
                            res = self.GetNode(nodeinfo, ele)
                        else:
                            res = self.GetNode(nodeinfo, ele)[0]
                        nodeinfo = res
                    else:
                        list = self.GetNode(nodeinfo, ele) 
                        for every in list:
                            
                            try:
                                attrinfo = self.GetRegularContent(every, 'att=./@' + path[1]) 
                            except Exception, e:
                                continue
                            
                            if route_list[1][0] != '=':
                                if attrinfo.find(route_list[1]) > -1: 
                                    usedSubtree.append(every)
                                else:
                                    continue
                            else:
                                if attrinfo == route_list[1][1:]:
                                    usedSubtree.append(every)
                                else:
                                    continue
            
            else:
                temp_list = route_list[1].split('|')
                for ele in path_list:

                    if i != len(path_list):
                        i = i + 1
                        if ele.find('id=') > -1:
                            res = self.GetNode(nodeinfo, ele)
                        else:
                            res = self.GetNode(nodeinfo, ele)[0]
                        nodeinfo = res
                    else:
                        list = self.GetNode(nodeinfo, ele)
                        for every in list:
                            try:
                                attrinfo = self.GetRegularContent(every, 'att=./@' + path[1])
                            except Exception, e:
                                continue
                            
                            if temp_list[0][0] == '=' and attrinfo == temp_list[0][1:]:
                                s_node = every
                                j = 2
                                for each in temp_list[1:]:
                                    if j != len(temp_list):
                                        j = j + 1
                                        if each.find('id=') > -1:
                                            s_res = self.GetNode(s_node, each)
                                        else:
                                            s_res = self.GetNode(s_node, each)[0]
                                        s_node = s_res
                                    else:
                                        s_list = self.GetNode(s_node, each)
                                        usedSubtree = s_list
                            else:
                                continue

            return usedSubtree

        else:
            route_list = route.split('|')
            i = 1
            nodeinfo = isTree
            for ele in route_list:
                if i != len(route_list):
                    i = i + 1
                    if ele.find('id=') > -1:
                        res = self.GetNode(nodeinfo, ele)
                    else:
                        try:
                            res = self.GetNode(nodeinfo, ele)[0]
                        except Exception, e:
                            break
                    nodeinfo = res
                else:
                    usedSubtree = self.GetNode(nodeinfo, ele)
            return usedSubtree
        
        return usedSubtree


if __name__ == '__main__':
    
    '''
    with open('ebooks.html','r') as f:
        page = f.read()

    from PageTreeDict import *
    from GetContent import *
    from GetUsedSubtree import *

    gu = GetUsedSubtree()
    pagetree = PageTreeDict()
    html =pagetree.PageTreeDict(page, 'GBK', 0)
    getcontent = GetContent()
    root = getcontent.GetNode(html, 'id=contentContainer')
    every_root = gu.GetUsedSubtree(root, 'id=main|class=airResultsMod resultSetAir|class=airResultsCard')
    print every_root
    '''
    import os
    import sys
    sys.path.append('..')
    with open('../test/raileurope.html', 'r') as f:
        page = f.read()
    
    from coms.CommonParser import *

    cp = CommonParser()
    type = 'html_utf-8'
    root = 'id=packages'
    subtree = 'id=ptpresults-body|class=solutionRow'
    #content = 'class=r2-pkg|att=./@class$=r2-pkg|class=connectionDialog|class=ptpresult-solution-details clearfix|class=connection-details-item clearfix&class=connection-details-left|class=journey-info-segment-big first|xpath=./span'
    content = 'class=r2-pkg|att=./@class$=r2-pkg|class=connectionDialog|class=ptpresult-solution-details clearfix|class=connection-details-item clearfix&class=connection-details-left|class=journey-info-segment-big first&class=connection-details-left|class=journey-info-segment-small last$'     
    rest = cp.TestAPI(page, [type, root, subtree, content])


