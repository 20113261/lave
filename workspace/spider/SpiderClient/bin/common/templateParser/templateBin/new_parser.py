#!/usr/bin/env python
#coding:utf-8

from collections import defaultdict
import hashlib
from StopCommon import *
from confParser import *
from common.class_common import *
import time
from lxml import html as HTML 

reload(sys)
sys.setdefaultencoding('utf-8')


class Parser(object):

    def __init__(self):
        self.__conf = GetConfValues()
        self.__sc = StopCommon()

    def __default(self, field, Type):
        
        class_name = Type[0].upper() + Type[1:].lower() + '()'
        self_type = eval(class_name)
        try:
            con = 'self_type.' + field
            return  eval(con)
        except Exception, e:
            return 'NULL'

    def HParser(self, page, area, filename, sub_list):
        
        basefield = ['coding', 'root', 'type','subtree']
        Dict = defaultdict(dict)
        
        type = self.__conf.GetConfValues(filename, area, 'type').split('_')[1] 
        page_type = self.__conf.GetConfValues(filename, area, 'type').split('_')[0]
        coding_type = self.__conf.GetConfValues(filename, 'basic', 'type').split('_')[1]
        
        rootTree = HTML.fromstring(page.decode(coding_type))
        
        import ConfigParser
        conf = ConfigParser.ConfigParser()
        conf.read(filename)
        key_v = conf.options(area)
        
        field_list = list(set(key_v).difference(set(basefield)))
        for every in sub_list:
            md5 = hashlib.md5(str(every).encode('utf-8')).hexdigest()
            for field in field_list:
                if page_type.lower() == 'html':
                    con_res = self.__sc.com_HDfunc(rootTree, every, filename, area, field)
                else:
                    con_res = self.__sc.com_Jfunc(every, filename, area, field)
                try:
                    if con_res == 'error':
                        Dict[md5][field] = self.__default(field, type)
                    else:
                        Dict[md5][field] = con_res
                except Exception, e:
                    Dict[md5][field] = self.__default(field, type)

        return Dict

