#!/usr/bin/env python
#coding=UTF8
'''
    @author: devin
    @time: 2014-02-23
    @desc:

'''
import os
import redis
from crawler.controller.slave import Slave
from crawler.worker import Workers
from workload import ControllerWorkload
from common.task import Task
from common.logger import logger
from common.common import set_proxy_client
from common.common import frame_ip
from common.common import verify_cn_ip
from util import http_client
from DBUtils.PooledDB import PooledDB
from common.mtIpDict import mt_ip_dict
import MySQLdb
import time
import urllib
import jsonlib
import json
import threading
import traceback
import sys
import gc
import gevent
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue, Empty
SINGLE_REQUEST_TIMEOUT = 15
MULTI_REQUEST_TIMEOUT = 60
PARSER_ERROR = 11
SLAVE_ERROR = 41
WORK_ERROR = 97
reload(sys)
sys.setdefaultencoding('utf-8')

def getLocalIp(ifname = 'eth0'):
    import socket, fcntl, struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))

    ret = socket.inet_ntoa(inet[20:24])

    return ret

_uc_host = '123.59.70.19'
_uc_user = 'writer'
_uc_pswd = 'miaoji1109'
_uc_db = 'crawl'

_uc_redis_host = '120.132.95.246'
_uc_redis_port = 6379

try:
    cand_local_ip = getLocalIp()

    #verify server, use validation DB
    if cand_local_ip not in frame_ip:
        _uc_db = 'validation'

    #UC machine,use inner ip
    if cand_local_ip.startswith('10.10.'):
        _uc_host = '10.10.154.38'
        _uc_redis_host = '10.10.24.130'

except Exception,e:
    logger.error("update uc_db fail. err " + str(e))


uc_db_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=2, maxconnections=10,\
        host=_uc_host, port=3306, user=_uc_user, passwd=_uc_pswd,\
        db=_uc_db, charset='utf8', use_unicode=False)

uc_redis_pool = redis.ConnectionPool()

def UCRedisConnection(db=0, redis_host=_uc_redis_host, redis_port=_uc_redis_port):
    r = redis.Redis(host=redis_host, port=redis_port, db=db, connection_pool=uc_redis_pool)
    return r

def setRedisConf(host,port):
    global _uc_redis_host
    _uc_redis_host = host

    global _uc_redis_port
    _uc_redis_port = port

def UCConnection():
    conn = uc_db_pool.connection()
    return conn

def load_parsers(config):

    parsers = {}
    import os
    import sys

    sections = config.sections()
    sections.remove('slave')
    sections.remove('proxy')
    sections.remove('master')
    for ele in sections:
        parsers[ele] = dict(config.items(ele))

    return parsers

def getallSource(config):

    sections = config.sections()
    sections.remove('slave')
    sections.remove('proxy')
    sections.remove('master')

    return sections


def work(task):
    import time
    import os
    import new
    cur_time_str = str(time.time()).replace('.','')

    error = 0
    proxy_or_ticket = 'NULL'

    if task.source not in parsers:
        logger.error("no parser for the task: %s" % task.task_data)
        error = PARSER_ERROR
        workload.complete_workload(task, error, proxy_or_ticket)
        return error

    logger.info('get a new task from tasks.data = ' + task.task_data)
    info.process_task_num += 1
    task_data = task.task_data
    parser = parsers[task.source]
    try:
        abspath = os.path.abspath(os.getcwd())
        dirname = os.path.dirname(abspath)

        file_path = parsers[task.source]['file_path']
        class_name = parsers[task.source]['class_name']
        mode_name = parsers[task.source]['mode_name']

        source_dir = os.path.join(dirname, file_path)
        sys.path.insert(0, source_dir)
        stime = time.time()
        mod = __import__(mode_name)
        clazz= getattr(mod, class_name)
        parser = new.instance(clazz)
        etime = time.time()
        logger.info('creating instance cost\t [%s ms] \t [%s]' % (str(etime-stime),task.source))
    except Exception, e:
        error_info = str(traceback.format_exc().split('\n'))
        error = WORK_ERROR
        workload.complete_workload(task, error, proxy_or_ticket)
        logger.error("[create instance failed: task_data:%s] [traceback:%s]" %(task_data,error_info))
        return
    print task
    try:
        error_value = parser.parse(task, flag = is_recv_real_time_request)

        logger.info("verify_result: " + str(task) + '\t' + str(error_value))

        if type(error_value) is int:
            error = error_value
        else:
            error, proxy_or_ticket = error_value
    except Exception, e:
        error_info = str(traceback.format_exc().split('\n'))
        logger.error("[Parser Exception in slave: task_data:%s  error:%s][traceback:%s]" %(task_data, str(e),error_info))
        error = SLAVE_ERROR

    #gc.collect()

    if error:
        info.error_task_num += 1
    workload.complete_workload(task, error, proxy_or_ticket)
    return


def request(params):
    task = Task()
    task.source = 'source_100'
    result = {'result':'0','task':[]}
    try:
        task.error = '12'
        req_tasks = eval(urllib.unquote(params.get('req')))
        logger.info('Task :: '+str(req_tasks))
        task.req_qid = params.get('qid')
        task.req_uid = params.get('uid')
    except Exception,e:
        logger.error('get request params error: ' +str(task.source)+ str(e))
        result['err_code'] = 'Not enough arguments'
        return json.dumps(result)

    for req_task in req_tasks:

        try:
            task.source = req_task.get('source')
            task.content = req_task.get('content')
            #task.proxy_info = proxy_info
            #task.ticket_info = req_task.get('ticket_info')
            task.req_md5 = task.ticket_info.get('md5','default_md5')


            task.master_info = req_task.get('master_info','default_host')
            task.host = task.master_info.get('master_addr')

            task.redis_host = task.master_info.get('redis_addr').split(':')[0]
            task.redis_port = task.master_info.get('redis_addr').split(':')[-1]

            task.redis_db = task.master_info.get('redis_db')
            task.redis_passwd = task.master_info.get('redis_passwd')

            task.req_qid_md5 = task.req_qid + '_' + task.req_md5
            task.other_info = req_task.get('other_info','default_other_info')
            other_info =  task.other_info.get('redis_key')
            for each in  other_info:
                task.redis_key = each
                task.other_info['redis_key'] = each
                workload.add_workload(task)

        except Exception,e:
            result['task'].append({'err_code':'task error'})
            continue

        result['task'].append({'err_code':'0'})

    return json.dumps(result)

def getForbideSectionName():
    forbide_section_str = ''
    conn = MySQLdb.connect(host=_uc_host, user='reader', charset='utf8',passwd='miaoji1109', db='onlinedb')
    cursor = conn.cursor()

    sql = "select sectionName from parserSource2Module where forbide='1'"

    cursor.execute(sql)

    datas = cursor.fetchall()

    forbide_section = set()

    for cand_data in datas:
        try:
            forbide_section.add(cand_data[0].encode('utf-8'))
        except Exception,e:
            pass

    forbide_section_str = '_'.join(forbide_section)

    return forbide_section_str


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: %s config_file_path" % sys.argv[0]
        sys.exit()

    # 读取配置文件
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read(sys.argv[2])

    try:
        forbide_section_str = getForbideSectionName()
    except Exception,e:
        logger.error('get forbide source fail.err = ' + str(e))
        forbide_section_str = ''

    logger.info('foorbide sectionName : ' + forbide_section_str)
    # set proxy client
    proxy_client = http_client.HttpClientPool(config.get("proxy", "host"),maxsize = 20)
    set_proxy_client(proxy_client)


    redis_host = config.get("redis","host")
    redis_port = config.getint("redis","port")
#    redis_db = config.getint("redis","db")
#    redis_password = config.get("redis","password")
    setRedisConf(redis_host,redis_port)

    import os
    #host, port = config.get("slave", "host"), config.getint("slave", "port")
    cmd = 'mioji-host -a'
    #host = os.system(cmd)
    host =  os.popen(cmd).read().strip()

    if (None == host or '' == host.replace('.','')):
        try:
            host = getLocalIp()
        except Exception,e:
            logger.error('call getLocalIp fail. error = ' + str(e))
            sys.exit(1)

    if(None == host or '' == host.replace('.','')):
        logger.error('get localhost Ip fail')
        sys.exit(1)

    port = int(sys.argv[1])
    master_host = config.get("master", "host")

    sources = getallSource(config)

    is_recv_real_time_request = config.getint("slave","recv_real_time_request")

    workload = ControllerWorkload(master_host, sources, forbide_section_str, recv_real_time_request = is_recv_real_time_request )


    parsers = load_parsers(config)

    workers = Workers(workload, work, config.getint("slave", "thread_num"),recv_real_time_request = is_recv_real_time_request)

    if host in mt_ip_dict:
        host = mt_ip_dict[host]

    slave = Slave(host, port, master_host, workers,recv_real_time_request =  is_recv_real_time_request)

    slave.info.name = config.get("slave", "name")
    slave.register("/rtquery", request)

    info = slave.info
    slave.run()
