#!/usr/bin/env python
#coding:utf-8


"""
>>> 功能：配置文件出现错误时，删除指定的section
"""

def delete_section(source):

    config_dir = '/home/workspace/spider/SpiderClient/conf/'

    filelist = os.listdir(config_dir)
    from ConfigParser import ConfigParser
    for file in filelist:
        print file
        config = ConfigParser()
        config.read(config_dir + '/' + file)
        config.remove_section(source)

        with open(config_dir + '/' + file,"w+") as config_file:
            config.write(config_file)


if __name__ == "__main__":

    import os
    import sys

    if len(sys.argv) < 2:
        print 'Usage: %s conf_dir [parser_info] '%sys.argv[0]
        sys.exit(-1)

    source = sys.argv[1]
    delete_section(source)
