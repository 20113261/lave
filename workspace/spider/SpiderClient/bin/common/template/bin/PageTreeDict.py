#!/usr/bin/env python
#coding:utf-8

import sys
from lxml import html as HTML
from lxml import etree
from common.logger import logger
import json

reload(sys)
sys.setdefaultencoding('utf-8')


class PageTreeDict(object):

    def __init__(self):
        pass
    
    def PageTreeDict(self, page, coding):
        
        content = ''
        try:
            if coding == 'json':
                content = json.loads(page[page.find('{'):])
            else:
                content = HTML.fromstring(page.decode(coding))
        except Exception, e:
            logger.info('%s',e )

        return content




if __name__ == '__main__':

    import os
    
    with open('../test/huifee.html', 'r') as f:
        page = f.read()
    
    get = PageTreeDict()
    res = get.PageTreeDict(page, 'utf-8')

    print res
    


