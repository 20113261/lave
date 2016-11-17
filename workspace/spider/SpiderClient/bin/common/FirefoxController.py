#!/usr/bin/env python
# coding=utf-8

from FirefoxCrawler import get_browser, FirefoxCrawler
import sys
import time
import ConfigParser
import random
from logger import logger
import traceback
from common import get_proxy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

PROXY_NONE = 21
BROWSER_NONE = 26
PROXY_INVALID = 22
UNKNOWN_TYPE = 25
CONFIG_ERROR = 26
PROXTY_FORBIDDEN = 23

reload(sys)
sys.setdefaultencoding('utf-8')

WAIT_TIME1 = 3
WAIT_TIME2 = 5
WAIT_TIME3 = 10
WAIT_TIME4 = 30
WAIT_TIME5 = 45
WAIT_TIME6 = 60

MAX_PAGE = 10

class FirefoxController():

    def __init__(self, config_file, params = [], url = 'NULL', debug = False, use_proxy = True):
        self.__config = ConfigParser.ConfigParser()
        self.__config.read(config_file)
        self.__result = {'para':[], 'error':0, 'proxy':'NULL'}

        self.__para_list = params
        basic_data = self.parse_basic_info()
        self.__source = basic_data['source']
        self.__params = basic_data['para']
        self.__step_list = basic_data['step']
        self.__loop_list = []

        # get a proxy by proxy rule
        if use_proxy == True:
            self.__proxy = self.get_proxy_by_rule()
            if self.__proxy == '' or self.__proxy == 'NULL':
                self.__result['error'] = PROXY_NONE
                return self.__result
        else:
            self.__proxy = 'NULL'
        self.__result['proxy'] = self.__proxy

        self.__browser = get_browser(self.__proxy)
        if self.__browser == '' or self.__browser == 'NULL':
            self.__result['error'] = BROWSER_NONE

        self.__content = ''
        self.__url = url
        self.__debug = debug
        self.__firefox_crawler = FirefoxCrawler(self.__browser, self.__source, debug = self.__debug)


    def get_proxy_by_rule(self):
        try:
            allow_port_content = self.__config.get('proxy', 'allow_port').strip()
            allow_port_list = allow_port_content.split(' ')
            allow_port_list = [int(each_port) for each_port in allow_port_list]
        except:
            allow_port_list = []

        try:
            forbid_port_content = self.__config.get('proxy', 'forbid_port').strip()
            forbid_port_list = forbid_port_content.split(' ')
            forbid_port_list = [int(each_port) for each_port in forbid_port_list]
        except:
            forbid_port_list = []

        try:
            allow_region_content = self.__config.get('proxy', 'allow_region').strip()
            allow_region_list = allow_region_content.split(' ')
        except:
            allow_region_list = []

        try:
            forbid_region_content = self.__config.get('proxy', 'forbid_region').strip()
            forbid_region_list = forbid_region_content.split(' ')
        except:
            forbid_region_list = []

        p = get_proxy(source = self.__source, allow_ports = allow_port_list, \
                forbid_ports = forbid_port_list, allow_regions = allow_region_list, \
                forbid_regions = forbid_region_list)
        logger.info('Proxy : %s' % p)

        return p


    def parse_basic_info(self):

        basic_data = {'source':'', 'para':{}, 'step':[], 'loop':[]}

        try:
            _source = self.__config.get('basic', 'source').strip()
            basic_data['source'] = _source

            _para_name_content = self.__config.get('basic', 'params').strip()
            _para_name_list = _para_name_content.split(' ')
            _para_dict = {}
            for each_para_name in _para_name_list:
                para_index = _para_name_list.index(each_para_name)
                _para_dict[each_para_name] = self.__para_list[para_index]
            basic_data['para'] = _para_dict

            _step_content = self.__config.get('basic', 'step').strip()
            _step_list = _step_content.split(' ')
            basic_data['step'] = _step_list

            try:
                _loop_content = self.__config.get('basic', 'loop').strip()
                _loop_list = _loop_content.split(' ')
                basic_data['loop'] = _loop_list
            except:
                basic_data['loop'] = []

        except Exception, e:
            traceback.print_exc(e)
            logger.error('config error: parse config file failed with error, ' + str(e))

        return basic_data


    def parse(self):
        tmp_func = 'NULL'
        data_list = []
        result = ([], False, 0)
        try:
            parser_name = self.__config.get('parser', 'func_name').strip()
            file_path = self.__config.get('parser', 'file_path').strip()
            params_list = self.__config.get('parser', 'params').strip().split(' ')
            parser_params = []
            for each_para_key in params_list:
                if each_para_key == 'content':
                    parser_params.append(self.__content)
                else:
                    parser_params.append(self.__params[each_para_key])

            if file_path not in sys.path:
                sys.path.append(file_path)

            exec_func = parser_name + ' as tmp_func'
            exec(exec_func)
            result = tmp_func(parser_params)

        except Exception, e:
            traceback.print_exc(e)
            logger.error('Firefox config parser error, loading parser function failed. error : ' + str(e))

        return result



    def get(self, step_name):

        error_code = 0
        try:
            request_url = self.__url

            try:
                wait_flag = self.__config.get(step_name, 'flag').strip()
            except:
                wait_flag = 'NULL'

            try:
                wait_time = self.__config.get(step_name, 'wait_time').strip()
                wait_time = int(wait_time)
            except:
                wait_time = WAIT_TIME2

            try:
                page_length = self.__config.get(step_name, 'length').strip()
                page_length = int(page_length)
            except:
                page_length = 1000

            try:
                judge_flag = self.__config.get(step_name, 'judge_flag').strip()
            except:
                judge_flag = 'NULL'

            error_code = self.__firefox_crawler.get(request_url, wait_flag, \
                    wait_time, page_length, judge_flag)

        except Exception, e:
            #print 'Firefox get :: get %s failed. error : %s' % (request_url, str(e)))
            traceback.print_exc(e)
            return error_code

        return error_code



    def click(self, step_name):
        '''
        执行点击操作，传入的参数有需要点击的位置，需要点击的标志，等待时间
        '''
        error_code = 0

        try:
            click_path = self.__config.get(step_name, 'xpath').strip()
        except:
            click_path = 'NULL'
            error_code = CONFIG_ERROR
            return error_code

        try:
            click_flag = self.__config.get(step_name, 'flag').strip()
            click_flag = self.__params[click_flag]
        except Exception, e:
            logger.error('Firefox.click : get click flag error. %s' % str(e))
            click_flag = 'NULL'

        try:
            wait_time = self.__config.get(step_name, 'wait_time').strip()
            wait_time = int(wait_time)
        except:
            wait_time = WAIT_TIME1

        error_code = self.__firefox_crawler.click(click_path, click_flag, \
                wait_time)

        return error_code


    def send(self, step_name):

        error_code = 0

        try:
            send_path = self.__config.get(step_name, 'xpath').strip()
        except:
            send_path = 'NULL'
            error_code = CONFIG_ERROR
            return error_code

        try:
            send_value_key = self.__config.get(step_name, 'value').strip()
            send_value = self.__params[send_value_key]
            send_value = send_value.decode('utf-8')
        except Exception, e:
            logger.error('FirefoxContraller.send : send value error %s' % str(e))
            send_value = 'NULL'
            error_code = CONFIG_ERROR
            return error_code

        try:
            wait_time = self.__config.get(step_name, 'wait_time').strip()
            wait_time = int(wait_time)
        except:
            wait_time = WAIT_TIME1

        error_code = self.__firefox_crawler.send(send_path, send_value, \
                wait_time)

        return error_code


    def wait(self, step_name):

        try:
            wait_flag = self.__config.get(step_name, 'flag').strip()
        except:
            wait_flag = 'NULL'

        try:
            wait_time = self.__config.get(step_name, 'wait_time').strip()
            wait_time = int(wait_time)
        except:
            wait_time = WAIT_TIME5


        error_code = self.__firefox_crawler.wait(wait_flag, wait_time)

        return error_code


    def execute(self, step_name):
        '''
        通过调用 execute 函数，执行 jquery 代码对一些不能直接操作的元素赋值
        '''

        try:
            js_script_temp = self.__config.get(step_name, 'script').strip()
        except Exception, e:
            logger.info('Firefox.execute : parse jquery script failed with error %s.' % str(e))
            error_code = CONFIG_ERROR
            return error_code

        try:
            wait_time = self.__config.get(step_name, 'wait_time').strip()
            wait_time = int(wait_time)
        except:
            wait_time = WAIT_TIME1

        try:
            js_params_str = self.__config.get(step_name, 'params').strip()
            js_params_list = js_params_str.split(' ')
        except:
            js_params_list = []

        if js_params_list == []:
            js_script = js_script_temp
        else:
            try:
                for each_params_key in js_params_list:
                    each_params = self.__params[each_params_key]
                    js_script_temp = js_script_temp.replace('miaoji_params@[%s]' % each_params_key, \
                            '%s' % each_params)
                js_script = js_script_temp
            except Exception, e:
                logger.error('Firefox.execute : load js script error, %s.' % str(e))
                error_code = CONFIG_ERROR
                return error_code

        error_code = self.__firefox_crawler.execute(js_script, wait_time)

        return error_code


    def select(self, step_name):
        '''
        完成需要下拉点击的操作
        '''
        error_code = 0

        try:
            select_path = self.__config.get(step_name, 'xpath').strip()
        except Exception, e:
            logger.error('Firefox.select :: parse config file failed.' + \
                ' can\'t parse xpath in step :%s' % step_name)
            error_code = CONFIG_ERROR

        try:
            select_params_str = self.__config.get(step_name, 'params').strip()
            select_params_list = select_params_str.split(' ')
        except Exception, e:
            select_params_list = []

        try:
            select_flag_str = self.__config.get(step_name, 'flag').strip()
        except Exception, e:
            logger.error('Firefox.select :: parse config file failed.' + \
                ' can\'t parse flag in step : %s' % step_name)
            error_code = CONFIG_ERROR

        if select_params_list == []:
            select_flag = select_flag_str
        else:
            try:
                for each_params_key in select_params_list:
                    each_params = self.__params[each_params_key]
                    select_flag_str = select_flag_str.replace('miaoji_params@[%s]' % each_params_key, \
                        '%s' % each_params)
                select_flag = select_flag_str
            except Exception, e:
                logger.error('Firefox.select : parse config file failed')
                error_code = CONFIG_ERROR
                return error_code

        error_code = self.__firefox_crawler.select(select_path, select_flag)

        return error_code


    def crawl(self):
        try:
            if self.__step_list == []:
                self.__browser.quit()
                return self.__result

            for each_step in self.__step_list:
                logger.info('Firefox is crawling %s step' % each_step)
                step_action_name = self.__config.get(each_step, 'action')

                try:
                    content_flag = self.__config.get(each_step, \
                            'content_flag').strip()
                except:
                    content_flag = 'No'

                if step_action_name == 'click':
                    temp_value = self.click(each_step)
                elif step_action_name == 'send':
                    temp_value = self.send(each_step)
                elif step_action_name == 'get':
                    temp_value = self.get(each_step)
                elif step_action_name == 'execute':
                    temp_value = self.execute(each_step)
                elif step_action_name == 'wait':
                    temp_value = self.wait(each_step)
                elif step_action_name == 'select':
                    temp_value = self.select(each_step)

                if content_flag == 'Yes':
                    each_content = self.__browser.page_source.encode('utf-8')
                    self.__content = each_content
                    tmp_result, next_page_flag, error_code = self.parse()
                    self.__result['para'] += tmp_result
                    self.__result['error'] = error_code

                if temp_value != 0:
                    self.__result['error'] = temp_value
                    return self.__result

            debug_file_name = self.__source + '_' + each_step + '_' + \
                    str(int(time.time())) + '.html'
            if self.__debug == True:
                fout = open(debug_file_name, 'w')
                each_debug_content = self.__browser.page_source.encode('utf-8')
                fout.write(each_debug_content)
                fout.close()

            #开始进行翻页抓取
            if self.__loop_list == []:
                return self.__result
            else:
                crawl_time = 0
                while crawl_time < MAX_PAGE:

                    for each_step in self.__loop_list:
                        step_action_name = self.__config.get(each_step, 'action')

                        try:
                            content_flag = self.__config.get(each_step, \
                                    'content_flag').strip()
                        except:
                            content_flag = 'No'

                        if step_action_name == 'click':
                            temp_value = self.click(each_step)
                        elif step_action_name == 'send':
                            temp_value = self.send(each_step)
                        elif step_action_name == 'get':
                            temp_value = self.get(each_step)
                        elif step_action_name == 'execute':
                            temp_value = self.execute(each_step)
                        elif step_action_name == 'wait':
                            temp_value = self.wait(each_step)
                        elif step_action_name == 'select':
                            temp_value = self.select(each_step)

                        if content_flag == 'Yes':
                            each_content = self.__browser.page_source.encode('utf-8')
                            self.__content = each_content
                            tmp_result, next_page_flag, error_code = self.parse()
                            self.__result['para'] += tmp_result
                            self.__result['error'] = error_code

                        if temp_value != 0:
                            self.__result['error'] = temp_value
                            return self.__result

        except Exception, e:
            traceback.print_exc(e)
            logger.error('Firefox crawler :: crawl failed with error ' + str(e))
            traceback.print_exc(e)
            #self.__browser.quit()
        finally:
            self.__browser.quit()

        if self.__result['para'] == [] and self.__result['error'] == 0:
            self.__result['error'] = UNKNOWN_TYPE
        elif self.__result['para'] != [] and self.__result['error'] != 0:
            self.__result['error'] = 0

        return self.__result


if __name__ == '__main__':
    firefox = FirefoxCrawler()
