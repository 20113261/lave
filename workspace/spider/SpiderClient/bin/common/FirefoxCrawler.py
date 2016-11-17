#!/usr/bin/env python
# coding=utf-8

#from util.FirefoxCrawler import get_browser
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
from util.FirefoxBrowser import get_browser

PROXY_INVALID = 22
UNKNOWN_TYPE = 25

reload(sys)
sys.setdefaultencoding('utf-8')


class FirefoxCrawler():
    
    def __init__(self, config_file, browser, params = [], url = '', ):
        self.__config = ConfigParser.ConfigParser()
        self.__config_file = config_file
        self.__para_list = params
        self.__browser = browser
        basic_data = self.parse_basic_info()
        self.__request_url = basic_data['url']
        self.__source = basic_data['source']
        self.__params = basic_data['para']
        self.__step_list = basic_data['step']
        self.__loop_list = []
        self.__proxy_rule = basic_data['proxy_rule']
        self.__multi = basic_data['multi']
        self.__result = {'para':[], 'error':0}
        self.__content = ''
        self.__url = url


    def parse_basic_info(self):
        self.__config.read(self.__config_file)
        
        basic_data = {'url':'', 'source':'', 'para':{}, \
                'step':[], 'multi':[], 'proxy_rule':''}

        try:
            _request_url = self.__config.get('basic', 'url').strip()
            basic_data['url'] = _request_url

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
                _multi_content = self.__config.get('basic', 'multi').strip()
                _multi_list = _multi_content.split(' ')
                basic_data['multi'] = _multi_list
            except:
                basic_data['multi'] = []
        except Exception, e:
            self.__browser.quit()
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
            logger.error('Firefox config parser error, loading parser function failed. error : ' + str(e))

        return result


    def click(self, step_name):
        try:
           ele_path = self.__config.get(step_name, 'xpath')

           try:
               multiable = self.__config.get(step_name, 'multiable')
               multiable = bool(multiable)
               times = self.__config.get(step, 'times')
               times = int(times)
           except:
               multiable = False
               times = 0
        except Exception, e:
            logger.error('Parse config file failed. error : ' + str(e))
            return -1

        try:
            if multiable == False:
                logger.info('Firefox click :: click the elememt at %s ' % ele_path)
                self.__browser.find_element_by_xpath('%s' % ele_path).click()

            elif multiable == True:
                click_eles = self.__browser.find_elements_by_xpath('%s' % ele_path)
                logger.info('Firefox click :: click the %s elememts at %s ' % (str(times),ele_path))
                for each_ele in click_ele[:times]:
                    each_ele.click()
                    time.sleep(1)
        except Exception, e:
            logger.error('Execute click action failed. error : ' + str(e))
            return -1

        return 0


    def send(self, step_name):

        try:
            ele_path = self.__config.get(step_name, 'xpath').strip()
            value_key = self.__config.get(step_name, 'value').strip()
            value = self.__params[value_key]
            
            try:
                wait_flag = self.__config.get(step_name, 'flag_path').strip()
            except:
                wait_flag = None 

            try:
                wait_time = self.__config.get(step_name, 'time').strip()
                wait_time = int(wait_time)
            except:
                wait_time = 3

            send_ele = self.__browser.find_element_by_xpath('%s' % ele_path)
            send_ele.clear()
            logger.info('Firefox send :: sending %s at %s ' % (value.encode('utf-8'), ele_path))
            value = value.decode('utf-8')
            send_ele.send_keys(value)
            
            if wait_flag == None:
                time.sleep(wait_time)
            else:
                try:
                    self.wait_func(wait_flag, wait_time)
                except:
                    pass
        except Exception, e:
            logger.error(' Firefox send :: send action failed. error : ' + str(e))
            return -1

        return 0 


    def find(self, step_name):
        try:
            ele_path = self.__config.get(step_name, 'xpath').strip()
            flag_key = self.__config.get(step_name, 'flag').strip()
            flag = self.__params[flag_key]
            flag_path = self.__config.get(step_name, 'flag_path').strip()
            
            ele_list = self.__browser.find_elements_by_xpath('%s' % ele_path)
            for each_ele in ele_list:
                if flag in each_ele.text.encode('utf-8'):
                    click_ele = each_ele.find_element_by_xpath('%s' % flag_path)
                    click_ele.click()
                    break
            time.sleep(5)
        except Exception, e:
            traceback.print_exc(e)
            logger.error(' Execute find action failed. error : ' + str(e))
            return -1

        return 0 


    def wait(self, step_name):
        try:
            br = self.__browser
            ele_flag = self.__config.get(step_name, 'flag').strip()
            wait_time = self.__config.get(step_name, 'time').strip()
            wait_time = int(wait_time)
            
            #WebDriverWait(self.__browser, wait_time).until(lambda br: br.find_element_by_xpath('%s' % ele_flag))
            content_ele = br.find_element_by_xpath('//*[@id="searchLoading"]')
            WebDriverWait(self.__browser, wait_time).until(lambda br: br.find_element_by_xpath('//*[@id="searchLoading"]').get_attribute('style') == 'height: 160px; text-align: center; display: none;')
        except Exception, e:
            logger.error(' Execute wait action failed. error : ' + str(e))
            return -1
        #open('ctrip.html','w').write(self.__browser.page_source.encode('utf-8'))
        return 0

    def wait2(self, step_name):
        try:
            br = self.__browser
            ele_flag = self.__config.get(step_name, 'flag').strip()

            try:
                wait_time = self.__config.get(step_name, 'time').strip()
                wait_time = int(wait_time)
            except:
                wait_time = 60
            #time.sleep(wait_time)

            for i in range(1):
                try:
                    try:
                        WebDriverWait(self.__browser, wait_time).until(lambda br: br.find_element_by_xpath('%s' % ele_flag))
                    except Exception, e:
                        logger.info('Firefox wait :: wait {0} element failed {1} time. error : {2}.'.format(ele_flag, str(i), str(e)))
                        #self.__browser.refresh()
                        logger.info('Firefox wait :: refreshing')
                except Exception, e:
                    print str(e)
                    continue
                content = self.__browser.page_source.encode('utf-8')
                print 'page length', len(content)
                if (len(content) > 700000) or (len(content) > 1000 and len(content) < 10000):
                    break

        except Exception, e:
            logger.error('Firefox get :: get final page failed. error :' + str(e))

        return 0


    def refresh(self, step_name):
        try:
            wait_time = self.__config.get(step_name, 'time').strip()
            wait_time = int(wait_time)
        except:
            wait_time = 30

        try:
            ele_flag = self.__config.get(step_name, 'flag').strip()
        except:
            wait_flag = '.'

        try:
            times = self.__config.get(step_name, 'times').strip()
            times = int(times)
        except:
            times = 3
        time.sleep(3)
        for i in range(times):
            logger.info('Firefox refresh :: the {0} time refresh the page'.format(str(i)))
            try:
                self.__browser.refresh()
                WebDriverWait(self.__browser, wait_time).until(lambda br: self.__browser.find_element_by_xpath('%s' % ele_flag))
            except Exception, e:
                print str(e)
                continue

        content = self.__browser.page_source.encode('utf-8')
        return 0 
        

    
    def judge(self, step_name):
        try:
            #flag_value = self.__config.get(step_name, 'flag').strip()
            flag_path = self.__config.get(step_name, 'flag_path').strip()
            flag_name = self.__config.get(step_name, 'flag_name').strip()
            try:
                script = self.__config.get(step_name, 'script').strip()
            except:
                script = 'NULL'

            if script != 'NULL':
                try:
                    self.__browser.execute_script('%s' % script)
                except Exception, e:
                    logger.info('Firefox crawler :: execute script %s at action judge failed. error : %s' % (script, str(e)))
                    return -1

            judge_value = self.__browser.find_element_by_xpath('%s' % flag_path).get_attribute('%s' % flag_name)
            logger.info('Firefox judge :: %s at position is %s ' % (judge_value, flag_path)) 
            if judge_value != '':
                return 0
            else:
                return -1
        except Exception, e:
            logger.error('Firefox judge :: judge action failed . error : %s ' % str(e))
            return -1


    def wait_func(self, wait_flag, wait_time):
        try:
            #wait_flag_string = 'WebDriverWait(self.__browser, wait_time).until(lambda br: %s)'
            #wait_flag = wait_flag_stirng % wait_flag
            #exec(wait_flag)
            print wait_flag, wait_time
            WebDriverWait(self.__browser, wait_time).until(lambda br: self.__browser.find_element_by_xpath('%s' % wait_flag))
        except Exception, e:
            logger.error(' Firefox wait_func :: wait action failed. error : ' + str(e))
            #return -1

        return 0

    def execute(self, step_name):
        try:
            js_script_temp = self.__config.get(step_name, 'script').strip()

            # 解析 execute 部分的配置文件
            try:
                value_string = self.__config.get(step_name, 'value').strip()
                value_list = value_string.split(' ')
            except Exception, e:
                print str(e)
                value_list = []

            # 判断需要执行的 js 代码是否需要利用传入的参数重新拼接
            if value_list == []:
                js_script = js_script_temp
            else:
                for each_value_key in value_list:
                    each_value = self.__params[each_value_key]
                    js_script_temp = js_script_temp.replace('miaoji_params@[%s]' % each_value_key, \
                        '%s' % each_value)
                js_script = js_script_temp
            self.__browser.execute_script('%s' % js_script)
        except Exception, e:
            logger.info('Firefox crawler :: execute js script failed. error : ' + str(e))    
            return -1

        return 0 


    def get(self, step_name):
        try:
            url = self.__url
            wait_flag = self.__config.get(step_name, 'flag').strip()
            try:
                wait_time = self.__config.get(step_name, 'time').strip()
                wait_time = int(wait_time)
            except:
                wait_time = 30
            
            logger.info('Firefox get :: crawling %s . ' % url)
            self.__browser.get(url)
            #self.wait_func(wait_flag, wait_time)
            content = self.__browser.page_source
            ''' 
            fout = open('get' + str(int(float(time.time()) * 1000)) + '.html','w')
            fout.write(content)
            fout.close()
            '''
            logger.info('Firefox get :: the page length of %s is %s' % (url, str(len(content))))
            if len(content) < 1000:
                #return -2
                return 0
        except Exception, e:
            logger.info('Firefox get :: get %s failed. error : %s' % (url, str(e)))
            return 0

        return 0



    def crawl(self):
        try:
            if self.__step_list == []:
                self.__browser.quit()
                return self.__result

            for each_step in self.__step_list:
                step_action_name = self.__config.get(each_step, 'action')
                if step_action_name == 'click':
                    temp_value = self.click(each_step)
                elif step_action_name == 'send':
                    temp_value = self.send(each_step)
                elif step_action_name == 'find':
                    temp_value = self.find(each_step)
                elif step_action_name == 'wait':
                    temp_value = self.wait(each_step)
                elif step_action_name == 'wait2':
                    temp_value = self.wait2(each_step)
                elif step_action_name == 'execute':
                    temp_value = self.execute(each_step)
                elif step_action_name == 'get':
                    temp_value = self.get(each_step)
                elif step_action_name == 'judge':
                    temp_value = self.judge(each_step)
                elif step_action_name == 'refresh':
                    temp_value = self.refresh(each_step)

                if temp_value == -1:# and step_action_name != 'wait2':
                    #self.__browser.quit()
                    logger.error('Firefox crawler :: crawl failed at %s step.' % each_step)
                    self.__result['error'] = UNKNOWN_TYPE 
                    return self.__result

                if temp_value == -1 and step_action_name == 'judge':
                    logger.error('Firefox crawler :: get middle vriable failed.')
                    self.__result['error'] = UNKNOWN_TYPE
                    return self.__result
                
                if temp_value == -2 and step_action_name == 'get':
                    logger.error('Firefox crawler :: crawl failed. error : proxy invalid')
                    self.__result['error'] = PROXY_INVALID
                    return self.__result

                if step_action_name[:4].lower() == 'wait' or step_action_name.lower() == 'refresh':
                    each_content = self.__browser.page_source.encode('utf-8')
                    open('ctrip.html','w').write(each_content)
                    self.__content = each_content
                    tmp_result, next_page_flag, error_code = self.parse()
                    self.__result['para'] += tmp_result
                    self.__result['error'] = error_code

        except Exception, e:
            logger.error('Firefox crawler :: crawl failed with error ' + str(e))
            #self.__browser.quit()
        finally:
            self.__browser.quit()

        return self.__result 


if __name__ == '__main__':
    firefox = FirefoxCrawler()

