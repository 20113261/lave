#!/usr/bin/env python
#coding:utf-8

import sys
import re
import json
from lxml import html as HTML
from lxml import etree
from common.logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')


class GetContent(object):

    def __init__(self):
        pass
    
    def GetNode(self, isTree, rootNode):

        if rootNode.find('=') == -1:
            root = []
            root_list = rootNode.split('_')
            if len(root_list) == 2:
                temp = isTree.getchildren()[int(root_list[1])]
                root.append(temp)
            else:
                root = isTree.getchildren()
        else:
            attr = rootNode.split('=')
            flag = attr[0]
            para = attr[1]
            
            if flag == 'class':
                root = isTree.find_class(para)
            elif flag == 'id':
                root = isTree.get_element_by_id(para)
            else:
                root = isTree.xpath(para)
        #return List type
        return root

    def GetRegularContent(self, isTree, rootNode):
        
        content = ''
        attr = rootNode.split('=')
        flag = attr[0]
        para = attr[1]
        if flag == 'class':
            content_tmp = isTree.find_class(para)[0].text_content()
            content_list = content_tmp.split('\n')
            for ele in content_list:
                content += ele.encode('utf-8').strip().rstrip()
        elif flag == 'id':
            content_tmp = isTree.get_element_by_id(para).text_content()
            content_list = content_tmp.split('\n')
            for ele in content_list:
                content += ele.encode('utf-8').strip().rstrip()
        elif flag == 'att': #get attr values
            content = isTree.xpath(para)[0].encode('utf-8').strip().rstrip()
        else:
            if para.find('text()') > -1:
                content_list = isTree.xpath(para)
                for ele in content_list:
                    content += ele.encode('utf-8').strip().rstrip().replace('\r', '').replace('\n', '')
            else:
                content_tmp = isTree.xpath(para)[0].text_content()
                content_list = content_tmp.split('\n')
                for ele in content_list:
                    content += ele.encode('utf-8').strip().rstrip()
        # return string type
        return content


if __name__ == '__main__':

    get = GetAirline()

    re = get.GetAirline('BA323_CA546_NULL_IZ5465')

    print re





