#!/usr/bin/env python
#coding=utf8

'''
    @author: zhangbin
    @date: 2014-07-30
    @desc: read config
            crawl url and parse data
'''

import re
import os
import json
from lxml import html
import random
import time
import urllib
import ConfigParser
from util.logger import logger
from common import get_proxy, invalid_proxy
from util.Browser2 import MechanizeCrawler

import sys
reload(sys)
sys.setdefaultencoding='utf8'

PROXY_NONE = 21
PROXY_INVALID = 22
CRAWL_ERROR = 27
DATA_NONE = 24
CONFIGFILE_ERROR = 26
UNKNOWN_ERROR = 25

def get_random():
    #between 0 and 1, 0.63125677756 for example
    return str(random.random())

def get_time():
    #timestamp at current, 140748467786 for example
    return str(int(float(time.time()) * 100))

# Crawl Page By Steps
class Crawler():
    def __init__(self, config_file, parser_name, params = [], postdata = [], \
        headers = {}, source = '', allow_ports = [], forbid_ports = [], \
        allow_regions = [], forbid_regions = [], user = 'realtime', \
        passwd = 'realtime', use_proxy = True, proxy = ''):

        self.__config = ConfigParser.ConfigParser()
        self.__iter_times = 1
        self.__params = {}
        self.__params['random'] = get_random()
        self.__params['time'] = get_time()
        self.__headers = headers
        #self.__postdata = {}
        self.__parser_name = parser_name
        self.__source = source
        self.__steps = []
        self.__crawler = ''
        self.__use_proxy = use_proxy
        '''
        # 强行不使用代理   for validation
        if self.__parser_name.find('ctripFlight') != -1 or self.__parser_name.find('expedia') != -1 or self.__parser_name.find('ebookers') != -1 or self.__parser_name.find('hotelclub') != -1 or self.__parser_name.find('cheaptickets') != -1 or self.__parser_name.find("sncf") != -1 or self.__parser_name.find("theTrainLine") != -1 or self.__parser_name.find("easyjet") != -1 or self.__parser_name.find("ceair") != -1 or self.__parser_name.find("csair") != -1 or self.__parser_name.find("agoda") != -1 or self.__parser_name.find("budgetair") != -1 or self.__parser_name.find("cheapoair") != -1:
            self.__use_proxy = True
            print "CRAWL PROXY:  USE PROXY"
        else:
            self.__use_proxy = False
            print "CRAWL PROXY: DONOT USE PROXY"
        if self.__parser_name.find('travelgenio') != -1 or source.find('priceline') != -1 or source.find('sncfen') != -1 or source.find('budgetair') != -1 or self.__parser_name.find('airfrance') != -1 or self.__parser_name.find('ctripFlight') != -1 or self.__parser_name.find('vuelingFlight') != -1:
            self.__use_proxy = True
        '''
        self.__allow_ports = allow_ports
        self.__forbid_ports = forbid_ports
        self.__allow_regions = allow_regions
        self.__forbid_regions = forbid_regions
        self.__user = user
        self.__passwd = passwd
        self.__proxy = proxy
        self.__proxy = self.proxy(self.__source)
        self.__result = []
        self.__error = 0
        self.__url_of_response = ''
        self.config_parser(config_file, params, postdata)

    # get a proxy
    def proxy(self, source):

        if not self.__use_proxy:
            return ''

        if self.__proxy != '':
            return self.__proxy

        try:
            p = get_proxy(source,self.__allow_ports,self.__forbid_ports, self.__allow_regions, self.__forbid_regions, self.__user, self.__passwd)
        except Exception,e:
            time.sleep(random.randint(5,10))
            self.__error = PROXY_NONE
            return ''

        if p == None:
            self.__error = PROXY_NONE
            return ''

        return p

    def config_parser(self, config_file, params, postdata):

        #get basic_info: name, crawler
        try:
            self.__config.read(config_file)

            name = self.__config.get('basic','name')

            self.__crawler = self.__config.get('basic','crawler')

        except Exception,e:
            print 'ConfigParser Error: read/name/crawler Error ' + str(e)
            logger.error('ConfigParser Error: read/name/crawler Error ' + str(e))
            self.__error = CONFIGFILE_ERROR
            return False

        #validate name info
        if name != self.__parser_name:
            print 'ConfigParser Error: Wrong Parser Name'
            logger.error('ConfigParser Error: Wrong Parser Name')
            self.__error = CONFIGFILE_ERROR
            return False

        #get params, postdata, steps
        try:
            try:
                params_keystr = self.__config.get('basic','params').strip()
            except:
                params_keystr = ''
            if params_keystr.lower() != 'none' and params_keystr != '':
                params_keys = self.__config.get('basic','params').strip().split(' ')
                for i in range(0, len(params_keys)):
                    self.__params[params_keys[i]] = params[i]

            steps = self.__config.get('basic','steps').strip().split(' ')
            self.__steps.extend(steps)

            try:
                postdata_keystr = self.__config.get('basic', 'postdata').strip()
            except:
                postdata_keystr = ''
            if postdata_keystr.lower() != 'none' and postdata_keystr != '':
                postdata_keys = postdata_keystr.split(' ')
                for i in range(0, len(postdata_keys)):
                    self.__params[postdata_keys[i]] = postdata[i]

        except Exception, e:
            print 'ConfigParser Error: params/postdata/steps Error: ' + str(e)
            logger.error('ConfigParser Error: params/postdata/steps Error: ' + str(e))
            self.__error = CONFIGFILE_ERROR
            return False

    #crawl pages, if failed, re do n times at most, n = self.__iter_times
    def crawl(self):

        if self.__error:
            return None

        while self.__iter_times > 0:
            self.__error = 0
            self.__proxy = self.proxy(self.__source)
            status = self.single_crawl()
            if status:
                break
            else:
                self.__iter_times -= 1
                continue

        return None
    #crawl pages
    def single_crawl(self):

        #initialize mc, set proxy, headers
        if self.__crawler.strip().lower() == 'mc':
            crawler = MechanizeCrawler(p = self.__proxy, headers = self.__headers)
            crawler.set_debug(flag = True)
        else:
            print 'ConfigParser Error: crawler Error: '
            logger.error('ConfigParser Error: crawler Error: ')
            self.__error = CONFIGFILE_ERROR
            return False

        #crawl page by step
        for step in self.__steps:

            if self.__error:
                return False

            # if not crawl, parse a page, get search_id, token etc
            if step[0:5] == 'parse':
                self.parse(step)
                continue

            # validate
            if step[0:5] == 'judge':
                self.judge(step)
                continue

            if step[0:5] == 'outer':
                self.outer(step)
                continue

            #get crawl method, params
            try:
                url = self.__config.get(step, 'url')
                method = self.__config.get(step, 'method')

                try:
                    response_key =  self.__config.get(step, 'response')
                except:
                    response_key = 'none'
                if response_key.lower() == 'none':
                    response_key = None

                try:
                    params_keys = self.__config.get(step, 'params').strip().split(' ')
                except:
                    params_keys = []

                try:
                    html_flag = self.__config.get(step, 'html')
                except:
                    html_flag = False

                try:
                    target = self.__config.get(step, 'target')
                except:
                    target = 'htmlpage'

            except Exception, e:
                print 'ConfigParser Error: ' + step + ': url/response/method/params/target Error ' + str(e)
                logger.error('ConfigParser Error: ' + step + ': url/response/method/params/target Error ' + str(e))
                self.__error = CONFIGFILE_ERROR
                return False

            try:
                referer = self.__config.get(step, 'referer')
            except:
                referer = ''

            # get postdata for post method
            params_type = 0
            postdata = {}
            if method.strip().lower() == 'post':
                try:
                    postdata = self.__params[self.__config.get(step, 'postdata')]
                except Exception, e:
                    print 'ConfigParser Error: ' + step + ': postdata Error ' + str(e)
                    logger.error('ConfigParser Error: ' + step + ': postdata Error ' + str(e))
                    self.__error = CONFIGFILE_ERROR
                    return False

                try:
                    params_type = self.__config.getint(step, 'post_type')
                except:
                    pass

            #crawl page
            if method.strip().lower() in ['get','post']:
                try:
                    #get params
                    for params_key in params_keys:
                        this_param = self.__params[params_key]

                        if type(this_param) is str or type(this_param) is unicode:
                            url = url.replace('miaoji_params@[' + params_key + ']', this_param)
                            referer = referer.replace('miaoji_params@[' + params_key + ']', this_param)
                        elif type(this_param) is list:
                            param_index = 0
                            for each_this_param in this_param:
                                url = url.replace('miaoji_params@[' + params_key + '[%s]]' % str(param_index),each_this_param) 
                                url = url.replace('miaoji_params@[' + params_key + '[%s]]' % str(param_index),each_this_param)
                                param_index += 1

                except Exception, e:
                    print 'ConfigParser Error: ' + step + ': params Error ' + str(e)
                    logger.error('ConfigParser Error: ' + step + ': params Error ' + str(e))
                    self.__error = CONFIGFILE_ERROR
                    return False

                if referer != '':
                    crawler.add_referer(url = referer)

                #if page in null, redo for at most 1 times
                #crawl_error != '': PROXY_INVALID
                #crawl_error == '': DATA_NONE
                if target == 'jumpurl':
                    page, crawl_error = crawler.get_url(method, url, paras = postdata, paras_type = params_type)
                elif target == 'cookie':
                    #get_cookie returns a dict
                    page, crawl_error = crawler.get_cookie(method, url, paras = postdata, paras_type = params_type)
                else:
                    page, crawl_error = crawler.req(method, url, paras = postdata, paras_type = params_type, html_flag = True)

                if page == None or page == '':
                    if crawl_error == 'Crawl Error With Proxy':
                        self.__error = PROXY_INVALID
                        invalid_proxy(proxy = self.__proxy, source = self.__source)
                        return False
                    else:
                        #DATA_NONE means page is null while proxy is valid
                        self.__error = DATA_NONE
                        return False

                #need to get some params from this page?
                if response_key != None:
                    self.__params[response_key] = page

                #is a result page?
                if html_flag == 'True' or html_flag == True:
                    self.__result.append(page)

                self.__url_of_response = crawler.get_url_of_response()
        return True

    def get_url_of_response(self):
        '''
        @return the url of final page
        '''
        return self.__url_of_response

    #parse a page, get some params from this page, such as token, search_id etc, only regex, json, lxml temporary
    def parse(self, parse_step):

        try:
            data = self.__params[self.__config.get(parse_step, 'data')]
            method = self.__config.get(parse_step, 'method')

            method_str = self.__config.get(parse_step, method)
            response = self.__config.get(parse_step, 'response')

        except Exception, e:
            print 'ConfigParser Error: ' + parse_step + ': params Error ' + str(e)
            logger.error('ConfigParser Error: ' + parse_step + ': params Error ' + str(e))
            self.__error = CONFIGFILE_ERROR
            return False

        try:
            if method == 'regex':
                try:
                    index = int(self.__config.get(parse_step, 'index'))
                except:
                    index = 0
                self.__params[response] = eval(method_str).findall(data)[index]
                #self.__postdata[response] = eval(method_str).findall(data)[0]
            elif method == 'json':
                self.__params[response] = eval('str(json.loads(data)' + method_str+ ')')
            elif method == 'xpath':
                pass
            elif method == 'define':
                self.__params[response] = eval(method_str.replace('miaoji_params@[data]','data'))
                print self.__params[response]
            else:
                pass
        except Exception, e:
            print 'ConfigParser Error: ' + parse_step + ': method Error ' + str(e)
            logger.error('ConfigParser Error: ' + parse_step + ': method Error ' + str(e))
            self.__error = UNKNOWN_ERROR
            return False

        return True

    # given a specific string, if found in page, break; else, continue
    # regex only temporary
    def judge(self, judge_step):

        try:
            data = self.__params[self.__config.get(judge_step, 'data').strip()]
            identifier = self.__config.get(judge_step, 'identifier').strip()
            reason = self.__config.get(judge_step, 'reason').strip()

        except Exception, e:
            print 'ConfigParser Error: ' + judge_step + ': params Error ' + str(e)
            logger.error('ConfigParser Error: ' + parse_step + ': method Error ' + str(e))
            self.__error = CONFIGFILE_ERROR
            return False

        try:
            if data.find(identifier) != -1:
                if reason.lower() == 'proxy':
                    self.__error = PROXY_INVALID
                    invalid_proxy(proxy = self.__proxy, source = self.__source)
                elif reason.lower() == 'data':
                    self.__error = DATA_NONE
                else:
                    pass
            else:
                return True
        except Exception, e:
            print 'ConfigParser Error: ' + judge_step + ': judge Error ' + str(e)
            logger.error('ConfigParser Error: ' + judge_step + ': judge Error ' + str(e))
            self.__error = CONFIGFILE_ERROR
            return False

        return True

    # exec a func from outer module
    def outer(self, outer_step):

        try:
            path = self.__config.get(outer_step, 'path').strip()
            func = self.__config.get(outer_step, 'func').strip()
            params_keys = self.__config.get(outer_step, 'params').strip().split(' ')
            params = []
            for key in params_keys:
                params.append(self.__params[key])
            response = self.__config.get(outer_step, 'response')

            if path not in sys.path:
                sys.path.append(path)

            exec_func = func + ' as tmp_func'
            exec(exec_func)
            self.__params[response] = tmp_func(params)

        except Exception, e:
            logger.error('ConfigParser Error: ' + outer_step + ': exec outer func Error ' + str(e))
            print 'ConfigParser Error: ' + outer_step + ': exec outer func Error ' + str(e)
            self.__error = CONFIGFILE_ERROR
            return False

        return True

    # get result, return a list including all html_pages where [crawl][html] = True
    def result(self):
        self.__result.append(self.__proxy)

        return self.__result

    #get flag, if self.__error != 0, stop crawling
    def flag(self):

        return self.__error

#parse a single page
class Parser():

    def __init__(self, config_file, parser_name = '', html_str = ''):
        self.__config = ConfigParser.ConfigParser()
        self.__parser_name = parser_name
        self.__datas = {}
        self.__result = []
        self.__steps = []
        self.__error = 0
        self.config_parser(config_file, html_str)

    def config_parser(self, config_file, html_str):

        try:
            self.__config.read(config_file)

            name = self.__config.get('basic','name')

            steps = self.__config.get('basic','steps').strip().split(' ')

            self.__datas[self.__config.get('basic','data')] = html_str

        except Exception, e:
            print 'CONFIGFILR ERROR: name/steps/data Error ' + str(e)
            self.__error = CONFIGFILE_ERROR
            return False

        if self.__parser_name != name:
            print 'ConfigParser Error: Wrong Parser Name'
            self.__error = CONFIGFILE_ERROR
            return False

        self.__steps.extend(steps)

        return True

    def parse(self):

        if self.__error:
            return False

        # get one params every time
        for step in self.__steps:
            try:
                data_key = self.__config.get(step, 'data')
                method = self.__config.get(step, 'method')
                method_str = self.__config.get(step, method)
                response = self.__config.get(step, 'response')
                result = self.__config.get(step, 'result')
                if result == 'True':
                    result == True
                else:
                    result = False

            except Exception, e:
                print 'CONFIGFILR ERROR: data/method/method_str/response/result Error ' + str(e)
                self.__error = CONFIGFILE_ERROR
                return False

            try:
                if method == 'regex':
                    self.__datas[response] = eval(method_str).findall(self.__datas[data_key])[0]
                elif method == 'json':
                    self.__datas[response] = str(json.loads(self.__datas[data_key])[method_str])
                elif method == 'xpath':
                    pass
                else:
                    pass

                if result:
                    self.__result.append(self.__datas[response])
            except Exception, e:
                print 'ConfigParser Error: ' + step + ': method Error ' + str(e)
                self.__error = UNKNOWN_ERROR
                return False

        return True

    def result(self):
        
        return self.__result

    def flag(self):

        return self.__error

if __name__ == '__main__':

    pass