#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser


config_file_path = os.environ["CONFIG_FILE"]


class ConfigHelper:

    def __init__(self, file_path=config_file_path):
        self.config = ConfigParser.ConfigParser()
        self.config.read(file_path)
        self.read_config()

    def read_config(self):
        self.proxy_host = self.config.get("proxy", "host")
        self.master_host = self.config.get("master", "host")
        self.redis_host = self.config.get("redis", "host")
        self.redis_port = self.config.getint("redis", "port")
        self.redis_db = self.config.getint('redis', 'db')

        self.mysql_host = self.config.get('mysql', 'host')
        self.mysql_user = self.config.get('mysql', 'user')
        self.mysql_passwd = self.config.get('mysql', 'pswd')
        self.mysql_db = self.config.get('mysql', 'db')

        self.is_recv_real_time_request = self.config.getint("slave", "recv_real_time_request")
        self.thread_num = self.config.getint("slave", "thread_num")

        self.data_type = dict(self.config.items('data_type'))

