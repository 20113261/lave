#!/usr/bin/env python
#coding=UTF8

'''
    修改conf.ini文件
'''

def add_parser_info(filename, parser_info):
    '''
        新加一个parser详细信息,加在文件结尾
    '''

    afile = open(filename,'a')
    afile.write('\n')
    for item in parser_info:
        afile.write('\n' + item)

    afile.close()

def fix_config(config_dir, source, class_name, file_path):

    filelist = os.listdir(config_dir)
    from ConfigParser import ConfigParser

    for file in filelist:
        print file
        config = ConfigParser()
        config.read(config_dir + '/' + file)
        if not config.has_section(source):
            config.add_section(source)
            config.set(source, 'class_name', class_name)
            config.set(source, 'file_path', file_path)
            config.write(open(config_dir + '/' + file, 'w'))
    


if __name__ == "__main__":

    import os
    import sys

    if len(sys.argv) < 3:
        print 'Usage: %s conf_dir [parser_info] '%sys.argv[0]
        sys.exit(-1)

    config_dir = sys.argv[1]
    source = sys.argv[2]
    class_name = sys.argv[3]
    file_path = sys.argv[4]
    fix_config(config_dir, source, class_name, file_path)
