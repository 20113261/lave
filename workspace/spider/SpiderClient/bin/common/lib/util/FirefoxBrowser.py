#coding:utf-8


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from selenium.webdriver.remote.remote_connection import LOGGER
import logging
from common.user_agent_list import user_agent_list
import random

LOGGER.setLevel(logging.WARNING)
reload(sys)
sys.setdefaultencoding('utf-8')

user_agent_index = random.randint(1, 1000)
user_agent = user_agent_list[user_agent_index]
UserAgentList = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36']

def get_browser(myProxy):
    print myProxy

    
    ip, port = myProxy.split(':')[0], int(myProxy.split(':')[1])
    profile = webdriver.FirefoxProfile()
    #print dir(profile)
    # 使用代理
    profile.set_preference('network.proxy.type', 1)
    '''    
    # 设置代理，ip和port
    profile.set_preference('network.proxy.http', ip)
    profile.set_preference('network.proxy.http_port', port)
    '''
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': '' # set this value as desired
        }) 

    profile.set_proxy(proxy)
    profile.native_events_enabled = True
    # 设置user-agent
    ua_index = random.randint(0, len(UserAgentList) - 1)
    #ua = UserAgentList[ua_index]
    ua = user_agent
    print ua
    profile.set_preference('general.useragent.override', ua)

    # forbbiden cache
    profile.set_preference('network.http.use-cache', False)
    
    # forbbiden loading all images
    profile.set_preference('permissions.default.image', 2)
     
    profile.update_preferences()
    
    #set debug
    profile.set_preference('devtools.debugger.log', True)
    # 启动firefox
    try:
        br = webdriver.Firefox(profile)
        br.set_page_load_timeout(180)
        br.set_script_timeout(180)
    except Exception, e:
        print e
        return 'NULL'

    return br


def DestroyBrowser(br):
    try:
        br.quit()
    except Exception, e:
        print 'br quit error: ' + str(e)
        pass


if __name__ == '__main__':
    import time
    x = time.time()
    #from common.common import get_proxy
    #p = get_proxy()
    #print p
    p = '117.168.17.206:8123'
    br = get_browser(p)
    br.get('http://182.254.208.100/site/PrintHeader')
    print br.page_source.encode('utf-8')
    br.quite()
