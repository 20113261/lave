#!/usr/bin/python
# -*- coding: UTF-8 -*-

import common.insert_db
from common.common import get_proxy
from mioji import spider_factory
from mioji.spider_factory import factory

# from mioji.common.task_info import Task

insert_db = common.insert_db
get_proxy = get_proxy
debug = False
spider_factory.config_spider(insert_db, get_proxy, debug)


def entry_test(task):
    spider = factory.get_spider_by_old_task(task)
    if spider is None:
        spider = factory.get_spider_by_old_source(task.source)
        if spider is None:
            return None
        spider.task = task
    return spider


def reload_and_config():
    # 重新load
    from common.common import get_proxy
    import common.insert_db
    insert_db = common.insert_db
    get_proxy = get_proxy
    debug = False
    spider_factory.config_spider(insert_db, get_proxy, debug)
