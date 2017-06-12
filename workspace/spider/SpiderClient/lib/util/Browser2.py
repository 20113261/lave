#coding=utf8
import urllib
import json
import httplib
import requests
from UserAgent import  GetUserAgent
from common.common import get_proxy
SOCKS_PROXY = '10.10.7.155|10.10.239.141|10.10.214.26|10.10.120.163|10.10.128.62|10.10.137.138|10.10.119.18|10.10.'
#SOCKS_PROXY = '139.129.231.218'
#SOCKS_PROXY = '106.75.30.126'
class MechanizeCrawler(object):

    def __init__(self, retry_flag=False, source='', referer='', headers={}, p='', md5 = '', qid = '',**kw):

        self.proxy = p
        self.md5 = md5
        self.qid = qid
        self.headers = headers
        self.br = requests.Session()
        self.br.keep_alive = False
        self.Userproxy = False
        headers['User-Agent'] = GetUserAgent()
        self.br.headers.update(headers)
        self.resp = ''
        self.times = 0
        self.html = ''
        self.error = ''
        self.flag = retry_flag
        self.source = source
        if  p:
            self.set_proxy(p)

    def set_debug(self, flag = True):
        pass
        '''
        if flag:
            httplib.HTTPConnection.debuglevel=1
            httplib.HTTPSConnection.debuglevel=1
        '''

    def retry(func):
        def wrapper(self, *args, **kw):
            if not self.flag:
                return func(self, *args, **kw)
            else:
                while self.times < 3:
                    print "重试次数 %d " % self.times
                    self.html, self.error = func(self, *args, **kw)
                    if self.error == '':
                        break
                    else:
                        p = get_proxy(source=self.source)
                        self.set_proxy(p)
                        self.times += 1
                return self.html, self.error

        return wrapper

    @retry
    def req(self, mechod, url, paras = {}, paras_type=1, html_flag=False, time_out=(60, 180),**kw):

        html, error = '', ''
        try:
            if mechod.lower() == 'get':
                url = url + urllib.urlencode(paras)
                self.resp = self.br.get(url,timeout=time_out, **kw)
            else:
                if paras_type == 0:
                    self.resp = self.br.post(url,json=paras,timeout = time_out, **kw)
                elif paras_type == 1:
                    paras = json.dumps(paras)
                    self.resp = self.br.post(url,data=paras,timeout = time_out, **kw)
                else:
                    self.resp = self.br.post(url,data=paras,timeout = time_out, **kw)

            if html_flag:
                html = self.resp.content
        except Exception,e:
            error = str(e)
            #print error
            #error = 'Crawl Error With Proxy'

        return html, error

    def set_proxy(self, p, https = False):
        if p != None and p != "REALTIME":
            # socks都是内网socks服务转发，所以以 10. 开头判断
            if p.startswith('10.'):
            # if p.split(':')[0] in SOCKS_PROXY:
                print 'socks --- '+p
                self.br.proxies = {
                        'http':'socks5://'+p,
                        'https':'socks5://'+p
                }
            else:
                self.br.proxies = {
                        'https':'http://'+p,
                        'http':'http://'+p,
                }


    def get_url_of_response(self):
        return self.resp.url

    def get_cookie_str(self):
        return self.resp.cookies

    def add_cookie(self, cookie = {}):
        self.br.cookies.update(cookie)

    def get_response(self):
        self.resp.code = self.resp.status_code
        return self.resp

    def add_referer(self,url):
        self.br.headers.update({'Referer':url})

    def add_header(self, headers={}):
        return self.br.headers.update(headers)

    def get_cookie_handle(self):
        pass
    def get_cookie(self, method, url_base, paras = {}, paras_type = 1, **kw):
        page,_ = self.req(method, url_base, paras = {}, paras_type = 1, **kw)
        dcookie = requests.utils.dict_from_cookiejar(self.resp.cookies)
        return dcookie,_

    def get_url(self, method, url_base, paras = {}, paras_type = 1, **kw):
        page,_error = self.req(method, url_base, paras = {}  , paras_type = 1, **kw)

        return self.get_url_of_response(),_error


if __name__ == '__main__':
    mc = MechanizeCrawler()
    mc.set_debug(True)
    print mc.get_cookie('get', 'http://www.ebookers.com')
    pass
