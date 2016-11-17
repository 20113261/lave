#!/usr/bin/env python
#coding:utf-8


import os
import sys
from ConfigParser import ConfigParser
import pdb

def fixConfig():

    conf = ConfigParser()
    conf_name = ['conf.ini'] 
    for i in range(1, 40):
        conf_name.append('conf' + str(i) + '.ini')

    for each in conf_name:
        conf.read(each)
        sections = conf.sections()
        #if each == 'conf1.ini':
        #    pdb.set_trace()
        
        conf.remove_option('slave', 'parsers')
        conf.remove_option('slave', 'sources')
        sections = conf.sections()

        sections.remove('slave')
        sections.remove('proxy')
        sections.remove('master')

        for ele in sections:
            try:
                res = dict(conf.items(ele))
                conf.remove_section(ele)
                if res['source'] == 'britishairRound':
                    res['source'] = 'britishairRoundFlight'
                conf.add_section(res['source'])
                conf.set(res['source'], 'class_name', res['class_name'])
                conf.set(res['source'], 'file_path', res['file_path'].split('../')[1])
                conf.write(open(each, 'w'))
            except Exception, e:
                print str(e)
                continue

fixConfig()
