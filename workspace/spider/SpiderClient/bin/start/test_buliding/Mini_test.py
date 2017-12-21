#!/usr/bin/python
# -*- coding: UTF-8 -*-
import gevent.monkey
gevent.monkey.patch_all()
import sys
sys.path.insert(0, '/home/SpiderClient/lib/crawler/controller/')
sys.path.insert(0, '/home/SpiderClient/lib/')
import csv
import codecs
import datetime
import pymysql
pymysql.install_as_MySQLdb()
import get_log_case
import logging
import gevent.pool

from mioji.spider_factory import factory
import requests
import json
from mioji.common.utils import simple_get_socks_proxy

get_source = {"host": "10.10.69.170", "user": "reader", "passwd": "miaoji1109", "db": "base_data"}
get_content = {"host": "10.10.155.146", "user": "reader", "passwd": "mioji1109", "db": "hjldb"}
get_hotel_content = {"host": "10.10.230.206", "user": "mioji_admin", "passwd": "mioji1109", "db": "verify_info"}
type_dict = {'flight': 'Flight', 'roundflight': 'RoundFlight', 'multiflight': 'MultiFlight', 'hotel': 'Hotel',
             'car': 'Car'}
type_dict2 = {'flight': 'flight_one_way', 'roundflight': 'flight_return', 'multiflight': 'flight_multi',
              'hotel': 'hotel', 'car': 'car'}
count_num = {'flight': 10, 'roundflight': 10, 'multiflight': 5, 'hotel': 10, 'car': 5}


def get_socks_proxy(source='', task='', ip_type='', ip_num='', verify_info=''):
    proxy = requests.get(
        "http://10.10.189.85:48200/?type=px001&qid=0&query={%22req%22:%20[{%22source%22:%20%22ctripFlight%22,%20%22num%22:%201,%20%22type%22:%20%22platform%22,%20%22ip_type%22:%20%22test%22}]}&ptid=test&tid=tid&ccy=spider_test").content
    proxy = json.loads(proxy)['resp'][0]['ips'][0]['inner_ip']
    return [proxy,
            '{"resp": [{"ips": [{"external_ip": "123.246.111.209", "inner_ip": "10.10.222.74:32238"}], "type": "platform", "source": "ctripFlight"}]}']


class MiniFactory:
    def __init__(self, task):
        self._mysql_source = pymysql.connect(**get_source)
        self._mysql_hotel_content = pymysql.connect(**get_hotel_content)
        self.source = task.get('source', '')
        self.type = task.get('type', '')
        self.con_type = task.get('con_type', 'ota')
        content_dict = {'1': 'ctrip', '2': 'expedia', '3': self.source}
        self.content_source = content_dict[str(task.get('test_num', 1))]
        self.check = {'Bool': False, 'auth': None, 'test_type': None}
        self.result_dict = []
        self.count = 0

        logging.info('已收到任务,测试source:{0},type:{1}'.format(self.source, self.type))

    def update_source(self):
        sql = "select * from source where status_test = 'Open' or verify_status_test = 'mioji'"
        cursor = self._mysql_source.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def use_list(self):
        source_list = self.update_source()
        api_list = []
        ota_list = []
        for i in source_list:
            if i[7] == '"NULL"':
                source_dict = {i[1]: {i[1]: i[2]}}
                ota_list.append(source_dict)
            else:
                source_dict = {i[1]: {i[1]: i[2], 'test': i[28], 'online': i[29]}}
                api_list.append(source_dict)
        return api_list, ota_list

    def get_content(self, co_num):
        content = []
        self.count += 1
        time = (datetime.datetime.now() - datetime.timedelta(self.count)).strftime('%Y%m%d')
        case_info = {'source': self.content_source, 'source_type': self.type, 'log_time': time}
        get_log = get_log_case.mk_case_log(case_info, co_num, verify=True)
        content_list = get_log.great_function()
        content = content + content_list
        return content

    def get_spider_run(self):
        content = []
        if self.con_type == 'api' and self.type == 'hotel':
            sql = "select * from workload_hotel_validation where source like '%{0}%' group by id limit 0,10".format(
                self.source)
            cursor = self._mysql_hotel_content.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            import random
            for i in data:
                content.append(
                    i[2] + '1&' + (datetime.datetime.now() + datetime.timedelta(days=random.randint(45, 90))).strftime(
                        '%Y%m%d'))
        else:
            co_num = count_num[self.type]
            while True:
                content_list = self.get_content(co_num)
                content += content_list
                if len(content) >= co_num:
                    break
                if self.count >= 8:
                    break
        ticket_info = {}
        logging.info('获取case完成,任务列表{0}'.format(content))
        from mioji.common.task_info import Task
        task = Task()
        from mioji.common import spider
        spider.slave_get_proxy = simple_get_socks_proxy
        if 'flight' in self.type:
            ticket_info = {'v_seat_type': 'E', 'env_name': 'test'}
        elif 'hotel' in self.type:
            ticket_info = {'occ': 2, 'num': 1, 'room_count': 1, 'env_name': 'test'}
        pool = gevent.pool.Pool(20)
        for cont in content[:10]:
            pool.add(gevent.spawn(self.spider_run, ticket_info, cont, task))
        pool.join()

        logging.info('测试运行完成，正在生成csv文件')

    def spider_run(self, ticket_info, cont, task):
        if self.con_type == 'api':
            ticket_info['auth'] = self.check['auth']
            task.other_info = {}
            task.redis_key = '1'
        else:
            pass
        task.source = self.source + type_dict[self.type]
        task.content = cont
        task.ticket_info = ticket_info
        logging.info('task:%s' % task)
        spider = factory.get_spider_by_old_task(task)
        code = spider.crawl()
        res = spider.result
        import time
        time.sleep(10)
        self.result_dict.append({'code': code, 'content': cont})

    def dinner(self):
        api, ota = self.use_list()
        logging.info('更新source表')
        if self.con_type == 'api':
            for i in api:
                if self.source == i.keys()[0] and type_dict2[self.type] == i[i.keys()[0]][i.keys()[0]]:
                    self.check['Bool'] = True
                    self.check['auth'] = i[i.keys()[0]]['test']
                    self.check['test_type'] = self.type
                    logging.info('API爬虫需要在ip白名单机器运行')
        else:
            for i in ota:
                if self.source == i.keys()[0] and type_dict2[self.type] == i[i.keys()[0]][i.keys()[0]]:
                    self.check['Bool'] = True
                    self.check['test_type'] = self.type
        if not self.check['Bool']:
            logging.info('此source没有在source表列表中找到')
            raise ('此source没有在source表打开列表中找到')
        self.get_spider_run()
        log_case_name = self.source + self.type + '测试结果.csv'
        self.csvfile = file(log_case_name, 'wb')
        self.csvfile.write(codecs.BOM_UTF8)
        self.writer = csv.writer(self.csvfile)
        self.writer.writerow(["源名称", "code", "content", "测试时间"])
        for i in self.result_dict:
            self.writer.writerow(
                [self.source + self.type, i["code"], i["content"], datetime.datetime.now().strftime('%Y%m%d')])
        print 'end'


if __name__ == '__main__':
    # 更新本地source表
    # test_num 1 城市三字码  2 机场三字码  3 使用自己源的case
    # type 飞机单程 flight 飞机往返 roundflight 飞机联程 multiflight 酒店 hotel
    task = {'source': '', 'type': '', 'con_type': '', 'test_num': 1}
    logging.info('输入源名称,类似于ctrip,yinlingApi:')
    task['source'] = raw_input()
    logging.info('task:%s' % task)
    logging.info('源类型,类似于flight,roundflight,multiflight,hotel:')
    task['type'] = raw_input()
    logging.info('task:%s' % task)
    logging.info('源属性,类似于api,ota:')
    task['con_type'] = raw_input()
    logging.info('task:%s' % task)
    logging.info('使用任务类型:')
    task['test_num'] = raw_input()
    logging.info('task:%s' % task)
    mini = MiniFactory(task=task)
    mini.dinner()
