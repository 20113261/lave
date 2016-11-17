#!/usr/bin/python
#coding=utf-8
import re

class SeclectContent(object):

    def __init__(self):
        pass

    def selectneirong(s):
    
        s=s.decode('utf8')
        s=s.replace('<a>',' ')
        s=s.replace('</a>',' ')
        patten=re.compile(u"[\w\u4e00-\u9fa5]+")
        slist=patten.findall(s)
        str = ''
        for i in slist:
            str += i + ' '

        return  str

if __name__=='__main__':
    s='中国 任命<a>ac</a>'
    selectneirong(s)
