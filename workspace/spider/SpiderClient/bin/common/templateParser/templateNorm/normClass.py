#!/usr/bin/env python
#coding:utf-8
import ConfigParser
from common.fieldNorm.onlineNorm import NormFunc
from common.class_common import *
from collections import defaultdict

class Typeinstance(object):
    def __init__(self, type):
	class_name = type[0].upper() + type[1:].lower() + '()'
	self.type = eval(class_name)

    def default(self, field):
	con = 'self.type.' + field[0]
	return  eval(con)


class Norm(object):

    def __init__(self):
        self._conf = ConfigParser.ConfigParser()
        self._nc = NormFunc()
        self.result = {}
        self.result_list = []

    def Pretreatment(self, filename, eDict):
        self._conf.read(filename)
        fieldtype = self._conf.get('section', 'type').split('_')[1]
	default_value = Typeinstance(fieldtype)
        mode_list = self._conf.get('basic', 'norm_mode').strip().split(' ')
        for mode in mode_list:
	    if mode == '':
		continue
            set_list = mode.split('&') 
	    if set_list[0] in eDict:
                try:
                    if eDict[set_list[0]].find('|') > -1:
                        con_list = eDict[set_list[0]].split('|')
                        result_temp = ''
                        for eroutine in con_list:
                            se_conetnt = eroutine.split('_')
                            first = self._nc.chmode(fieldtype, set_list[0], set_list[1], se_content[0]) 
                            second = self._nc.chmode(fieldtype, set_list[0], set_list[1], se_content[1]) 
                            result_temp += first + '_' + second + '|'
                        self.result[set_list[0]] = result_temp[:-1]
                    else:
                        con_list = eDict[set_list[0]].split('_')
                        result_temp = ''
                        for eContent in con_list:
                            result_temp += self._nc.chmode(fieldtype, set_list[0], set_list[1], eContent) + '_'
                        self.result[set_list[0]] = result_temp[:-1] 
                except Exception, e:
                    self.result[set_list[0]] = default_value.default([set_list[0]])
	    else:
		self.result[set_list[0]] = default_value.default([set_list[0]])
        return self.result #返回一张票相关所有字段的词典


    def getLastResult(self, filename, Dict_list):
        
        for ele_ticket in Dict_list:
            #key 为md5
            eDict = {}
            eDict = self.Pretreatment(filename, ele_ticket)
            self.result_list.append(str(eDict))

        return self.result_list #返回词典列表


if __name__ == '__main__':
    
    norm = Norm()
    norm.Pretreatment('test')


        
