#!/usr/bin/env python
#coding:utf-8


import os
import ConfigParser
import re
import json
from lxml import html as HTML
from GetJsonContent import *
#解析配置文件类
#获得配置文件的Key，并得到Values,
class GetConfValues(object):

    def __init__(self):
        pass

    def GetConfValues(self, filename, section, key):
        
        conf = ConfigParser.RawConfigParser()
        #path = os.path.split(os.path.realpath(__file__))[0] + '/' + filename
        path = filename
        conf.read(path)
        
        res = ''
        if conf.has_section(section):#检查配置文件是否包含此SECTION
            if conf.has_option(section, key):#获得SECTION中的KEY获取VALUES
                res = conf.get(section, key)
                return res
            else:
                res = 'error'
        else:
            res = 'error'

        return res

    def ch_section(self, page, filename, section, key):

        content = ''
        #coding = 'utf-8'
        type_list = self.GetConfValues(filename, section, 'type').split('_')
        type = type_list[0]
        coding = type_list[1].lower()
        if type == 'html':
            p_tree = HTML.fromstring(page.decode(coding))
        else:
            p_dict = json.loads(page[page.find('{'):])
        pat = re.compile(r'\d+')
        flag_dict = {}
        step_num = self.GetConfValues(filename, section, 'step').split(' ')
        
        if len(step_num) == 1:
            flag_dict['flag'] = 'section'
        else:
            i = 1
            for ele in step_num:
                if i == 1:
                    flag_dict['flag'] = ele
                else:    
                    num = pat.findall(ele)[0]
                    flag_dict['flag' + num] = ele
                i = i + 1
        
        for key in flag_dict:
            
            route = self.GetConfValues(filename, section, key)
            if route == '' or route == 'error' and len(flag_dict) == 1:
                content = flag_dict[key]
                return content

            if type == 'html':
                result = p_tree.xpath(route)
            else:
                result = GetJsonContent.GetJsonValues(p_dict, route)
            
            if result == []:
                continue
            else:
                content = flag_dict[key]

        return content


if __name__ == '__main__':

    gsk = GetConfValues()
    with open('../test/aeroflot2.html') as f:
        page = f.read()
    
    res = gsk.ch_section(page, 'aeroflot.ini', 'basic','step')

    print res


