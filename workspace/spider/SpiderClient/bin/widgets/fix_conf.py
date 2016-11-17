#!/usr/bin/env python
#coding=UTF8

'''
    修改conf.ini文件
'''

def add_parser(filename, parser):
    '''
        在parser中加入一个parser使之可以爬取对应的workload，前提是下面的parser信息列表中存在该parser
        parser@line11
    '''

    rfile = open(filename,'r')
    
    lines = []
    for line in rfile:
        lines.append(line)
    
    rfile.close()

    lines[10] = lines[10].strip() + ' ' + parser + '\n'

    wfile = open(filename,'w')

    for line in lines:
        wfile.write(line)

    wfile.close()

def add_source(filename, source):
    '''
        在source中加入一个source使之可以爬取对应的workload，前提是下面parser信息列表中存在该parser
        source@line12
    '''

    rfile = open(filename,'r')


    lines = []
    for line in rfile:
        lines.append(line)

    rfile.close()

    lines[11] = lines[11].strip() + ' ' + source + '\n'

    wfile = open(filename,'w')

    for line in lines:
        wfile.write(line)

    wfile.close()

def add_parser_info(filename, parser_info):
    '''
        新加一个parser详细信息,加在文件结尾
    '''

    afile = open(filename,'a')
    afile.write('\n')
    for item in parser_info:
        afile.write('\n' + item)

    afile.close()

def temp(filename):

    rfile = open(filename,'r')

    lines = []
    for line in rfile:
        lines.append(line)

    lines[8] = 'host = 42.96.128.153' + '\n'

    wfile = open(filename,'w')
    for line in lines:
        wfile.write(line)

    wfile.close()

if __name__ == "__main__":

    import os
    import sys

    if len(sys.argv) < 5:
        print 'Usage: %s parser source conf_dir [parser_info] '%sys.argv[0]
        sys.exit(-1)

    parser = sys.argv[1]
    source = sys.argv[2]
    parser_info = sys.argv[4:]
    dir = sys.argv[3]

    #dir = os.getcwd()

    filelist = os.listdir(dir)

    for file in filelist:
        print file
        add_parser(dir + file, parser)
        add_source(dir + file, source)    
        add_parser_info(dir + file, parser_info)

