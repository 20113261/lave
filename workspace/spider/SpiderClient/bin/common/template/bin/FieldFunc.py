#!/usr/bin/env python
#coding:utf-8

import sys
from common.logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')


class FieldFunc(object):

    def __init__(self, re_flag = False):

        self.__re_flag = Flase

    
    def __FieldFunc(self,each_dict):

        f_dict = {}
        
        if self.__re_flag = True:

            pass
        else:
            f_dict = each_dict

        return f_dict


    def source_func(self,self.__FieldFunc(each_dict)):
        
        content = ''
        content  = self.__FieldFunc(each_dict)['source']
        
        return content


    def currency_func(self,self.__FieldFunc(each_dict)):

        if 'currency' in self.__FieldFunc(each_dict):
            content = self.__FieldFunc(each_dict)['currency']
        else:
            content = 'NULL'

        return content
    

    def _func(self,self.__FieldFunc(each_dict)):

        if '' in self.__FieldFunc(each_dict):
            content = self.__FieldFunc(each_dict)['']
        else:
            content = 'NULL'

        return content










