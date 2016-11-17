#!/usr/bin/env python
#coding:utf-8

import sys
import os
from common.class_common import *
import new

class Typeinstance(object):

    def __init__(self, type):
        class_name = type[0].upper() + type[1:].lower() + '()'
        self._type = eval(class_name)
    
    def default(self, field):
        try:
            con = 'self._type.' + field
            return  eval(con)
        except Exception, e:
            return 'NULL'

if __name__ == '__main__':

    iss = Typeinstance('train')
    price = iss.default('price')

     
