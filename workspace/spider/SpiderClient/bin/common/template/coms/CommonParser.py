#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('..')

from bin.ClassInit import *
from lxml import html
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class CommonParser(ClassInit):

    def __init__(self):
        pass

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
            if type_list[1].lower() == 'flight':
                #flight one-way 
                Dict = self.HtmlFlight(area, filename, subtree_list)
                
            elif type_list[1].lower() == 'train':
                #train one-way
                Dict = self.HtmlTrain(area, filename, subtree_list)

            elif type_list[1].lower() == 'bus':
                #bus
                Dict = self.HtmlBus(page, area, filename, subtree_list)

            elif type_list[1].lower() == 'room':
                #Hotel
                Dict = self.HtmlRoom(page, area, filename, subtree_list)
            
            elif type_list[1].lower() == 'car':
                #Zuche
                Dict = self.HtmlCar(page, area, filename, subtree_list)
                
            elif type_list[1].lower() == 'roundflight':
                #Round flight
                Dict = self.HtmlRoundFlight(area, filename, subtree_list)

            else:
                pass

        elif type_list[0].lower() == 'json':
            #JSON TYPE
            temp_dict = self.PageTreeDict(page, type_list[0].lower())

            dict_path = self.GetConfValues(filename, area, 'subtree')
            subtree_list = self.GetJsonValues(temp_dict, dict_path)
               
            if type_list[1].lower() == 'flight':
                Dict = self.JsonFlight(area, filename, subtree_list)

            elif type_list[1].lower() == 'train':
                Dict = self.JsonTrain(area, filename, subtree_list)

            elif type_list[1].lower() == 'bus':
                Dict = self.JsonBus(area, filename, subtree_list)

            elif type_list[1].lower() == 'room':
                Dict = self.JsonRoom(area, filename, subtree_list)
            
            elif type_list[1].lower() == 'car':
                Dict = self.JsonCar(area, filename, subtree_list)

            else:
                pass

        else:
            pass
        
        return Dict
        
    
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

