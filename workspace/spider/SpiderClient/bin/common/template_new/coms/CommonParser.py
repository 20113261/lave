#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('..')

from bin.ClassInit import *
from lxml import html
from bin.new_parser import Parser
from norm.normClass import Norm 
from covInit.GinDBList import GinDBList
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class CommonParser(ClassInit):

    def __init__(self):
        self.new_parser_tem = Parser()
        self.new_norm = Norm()
        self.new_idbl = GinDBList()
    
    def ListInput(self, page, area, filename, subtree_list):
        '''
            子树列表输入
        '''
        return self.new_parser_tem.HParser(page, area, filename, subtree_list)

    def GetNormData(self, filename, eDict):
        '''
            返回标准数据词典列表
        '''
        return self.new_norm.getLastResult(filename, eDict) 

    def GinDBList(self, type, dictList):
        '''
            返回入库列表
        '''
        return self.new_idbl.GetInDBList(type, dictList)

    def CommonParser(self, filename, page):
        '''
        filename:config_name
        page: 待解析网页
        '''
        Dict = ''
        Result = []
        f_result = []
         
        #parser config file
        area = self.ch_section(page, filename, 'basic', 'step')
        type = self.GetConfValues(filename, area, 'type')
        type_list = type.split('_')
        if type_list[0].lower() == 'html':
            #Html page
            code = self.GetConfValues(filename, area, 'coding')
            html = self.PageTreeDict(page, code)
            try: 
                root = self.GetConfValues(filename, area, 'root')
                if root.find('id=') > -1:
                    root_node = self.GetNode(html, root)
                else:
                    root_node = self.GetNode(html, root)[0]
            except Exception, e:
                root_node = html
    
            every_root = self.GetConfValues(filename, area, 'subtree')
            subtree_list = self.GetUsedSubtree(root_node, every_root)
            try: 
                Dict = self.new_parser_tem.HParser(page, area, filename, subtree_list)
            except Exception, e:
                Dict = self.new_parser_tem.oldHParser(area, filename, subtree_list)
            
            
        elif type_list[0].lower() == 'json':
            #JSON TYPE
            temp_dict = self.PageTreeDict(page, type_list[0].lower())

            dict_path = self.GetConfValues(filename, area, 'subtree')
            subtree_list = self.GetJsonValues(temp_dict, dict_path)
            try:   
                Dict = self.new_parser_tem.HParser(area, filename, subtree_list)
            except Exception, e:
                Dict = self.new_parser_tem.oldHParser(area, filename, subtree_list)

        else:
            pass
        
        return Dict


    def NormTestAPI(self, filename, eDict, field):
        
        temp = self.new_norm.getLastResult(filename, eDict)
        return temp[0][field]
        
    
    def TestAPI(self, page, testList):
        '''
        测试接口
        page：待解析网页
        testList：参数列表
        '''
        listlen = len(testList)
        content = ''

        if listlen == 1:
            type_list = testList[0].split('_')
            result = self.PageTreeDict(page, type_list[1])
            content = result
            print 
            print 'SUCCESSFULLY OBTAINED CONTENT : ' , content
            print 

        elif listlen == 2:
            type_list = testList[0].split('_')
            result = self.PageTreeDict(page, type_list[1])
            if type_list[0].lower() == 'json':
                content = self.GetJsonValues(result, testList[1])
            else:
                if testList[1] == '':
                    content = result
                else:
                    if testList[1].find('id=') > -1:
                        root = self.GetNode(result, testList[1])
                    else:
                        root = self.GetNode(result, testList[1])[0]
                    content = root
            print 
            print 'SUCCESSFULLY OBTAINED CONTENT : ' , content
            print 

        elif listlen == 3:
            type_list = testList[0].split('_')
            result = self.PageTreeDict(page, type_list[1])
            
            if type_list[0].lower() == 'html':
                if testList[1] == '':
                    root = result
                else:
                    if testList[1].find('id=') > -1:
                        root = self.GetNode(result, testList[1])
                    elif testList[1].find('=') == -1:
                        subtree = result.getchildren()
                    
                    else:
                        root = self.GetNode(result, testList[1])[0]
                subtree = self.GetUsedSubtree(root, testList[2])
                content = subtree
            else:
                root = self.GetJsonValues(result, testList[1]) 
                
                if testList[2][len(testList[2]) - 1] == '$':
                    objcontent = self.GetVertical(root[0], testList[2][:-1])
                else:
                    objcontent = self.GetUnder(root[0], testList[2])
                content = objcontent
            print 
            print 'SUCCESSFULLY OBTAINED CONTENT : ', content
            print 
        else:
            type_list = testList[0].split('_')
            result = self.PageTreeDict(page, type_list[1])
            if type_list[0].lower() == 'html':
                if testList[1] == '':
                    root = result
                else:
                    if testList[1].find('id=') > -1:
                        root = self.GetNode(result, testList[1])
                    else:
                        root = self.GetNode(result, testList[1])[0]
            subtree = self.GetUsedSubtree(root, testList[2])
            if testList[3][len(testList[3]) - 1] == '$':
                if testList[3][:2] != 'g_':
                    objcontent = self.StopVertical(subtree[0], testList[3][:-1])
                else:
                    objcontent = self.StopVertical(subtree[0], testList[3][:-1][2:])
                    print objcontent
            else:
                if testList[3][:2] != 'g_':
                    objcontent = self.StopUnder(result, testList[3])
                else:
                    objcontent = self.StopUnder(result, testList[3][2:])

            content = objcontent
            print
            print 'SUCCESSFULLY OBTAINED CONTENT : ', content
            print

        return content

