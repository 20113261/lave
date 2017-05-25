#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser


config_file_path = os.environ["CONFIG_FILE"]


class ConfigHelper:

    def __init__(self, file_path=config_file_path):
        self.config = ConfigParser.ConfigParser()
        self.config.read(file_path)

        self.proxy_host = '10.10.239.46:8087'
        self.master_host = '10.10.99.53:4141'
        self.redis_host = '10.10.24.130'
        self.redis_port = 6379
        #  self.redis_db = self.config.getint('redis', 'db')
        self.mysql_host = "10.10.154.38"
        self.mysql_user = "writer"
        self.mysql_passwd = "miaoji1109"
        self.mysql_db = 'crawl'
        self.spiderbase_host = '10.19.118.147'
        self.spiderbase_user = 'reader'
        self.spiderbase_passwd = 'mioji109'
        self.spiderbase_db = 'source_info'
        self.is_recv_real_time_request = 0
        self.thread_num = 1
        self.data_type = {}

        self.read_config()

    def read_config(self):
        self.proxy_host = self.config.get("proxy", "host")
        self.master_host = self.config.get("master", "host")
        self.redis_host = self.config.get("redis", "host")
        self.redis_port = self.config.getint("redis", "port")
        #  self.redis_db = self.config.getint('redis', 'db')

        self.mysql_host = self.config.get('mysql', 'host')
        self.mysql_user = self.config.get('mysql', 'user')
        self.mysql_passwd = self.config.get('mysql', 'pswd')
        self.mysql_db = self.config.get('mysql', 'db')
        self.spiderbase_host = self.config.get('spiderbase', 'host')
        self.spiderbase_user = self.config.get('spiderbase', 'user')
        self.spiderbase_passwd = self.config.get('spiderbase', 'pswd')
        self.spiderbase_db = self.config.get('spiderbase', 'db')

        self.is_recv_real_time_request = self.config.getint("slave", "recv_real_time_request")
        self.thread_num = self.config.getint("slave", "thread_num")

        self.data_type = dict(self.config.items('data_type'))

