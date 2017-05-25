#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2014-03-22
    @author: devin
    @desc:

'''
import jsonlib
import time
from util import http_client
from logger import logger
from conf_manage import ConfigHelper

config_helper = ConfigHelper()

proxy_client = http_client.HttpClientPool("10.136.8.94:8086")
proxy_client2 = http_client.HttpClientPool(config_helper.proxy_host, maxsize=20)


def getLocalIp(ifname='eth0'):
    import socket, fcntl, struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))

    ret = socket.inet_ntoa(inet[20:24])
    return ret


def set_proxy_client(client):
    global proxy_client2
    proxy_client2 = client


frame_ip = '10.10.48.27|10.10.38.160|10.10.29.204|10.10.106.179|10.10.228.4|10.10.218.199|10.10.246.77|10.10.153.6|10.10.95.70|10.10.84.225|10.10.100.30|10.10.111.212|10.10.99.125|10.10.156.116|'
verify_cn_ip = '10.10.156.116|10.10.156.56|10.10.184.17|10.10.184.214|10.10.170.233|10.10.176.6|10.10.199.118|10.19.194.208|10.19.10.128|10.19.111.69|10.10.155.184'
special_ip = frame_ip + '|' + verify_cn_ip


def get_proxy(source=None, allow_ports=[], forbid_ports=[],
              allow_regions=[], forbid_regions=[], user='realtime', passwd='realtime', proxy_info={}):
    try:
        ip = getLocalIp()
        if ip not in special_ip:
            return 'REALTIME'
    except:
        return None

    if proxy_info == {}:
        pass
    else:
        # todo, 当前全部使用默认值
        if proxy_info.has_key("allow_ports"):
            allow_ports = proxy_info['allow_ports']
        if proxy_info.has_key("forbid_ports"):
            forbid_ports = proxy_info['forbid_ports']
        if proxy_info.has_key("allow_regions"):
            allow_regions = proxy_info['allow_regions']
        if proxy_info.has_key("forbid_regions"):
            forbid_regions = proxy_info['forbid_regions']

    allow = ""
    forbid = ""
    allow_regions_str = ""
    forbid_regions_str = ""

    if len(allow_ports) != 0:
        allow = '_'.join([str(i) for i in allow_ports])
    if len(forbid_ports) != 0:
        forbid = '_'.join([str(i) for i in forbid_ports])

    if len(allow_regions) != 0:
        allow_regions_str = '_'.join([i for i in allow_regions])
    if len(forbid_regions) != 0:
        forbid_regions_str = '_'.join([i for i in forbid_regions])

    try:
        p = proxy_client2.get("/proxy?source=%s&user=crawler&passwd=spidermiaoji2014" % source)
        # p = proxy_client2.get("/proxy?source=%s&user=parser&passwd=parser" % source)
    except:
        p = ''

    return p


def invalid_proxy(proxy, source):
    return
    # if proxy != None:
    #    proxy_client.get("/update_proxy?status=Invalid&p=%s&source=%s"%(proxy,source))


def update_proxy(source_name, proxy, start_time, error_code):
    special_ip = frame_ip + '|' + verify_cn_ip
    try:
        ip = getLocalIp()
        if ip not in special_ip:
            return None
    except:
        return None

    speed = time.time() - start_time
    if proxy != None or proxy != 'NULL':
        proxy_client2.get('/update_proxy?source=%s&proxy=%s&error=%s&speed=%s' % (source_name, proxy, \
                                                                                  str(error_code), str(speed)))

    return None


def getStrMd5(srcStr):
    import hashlib
    myMd5 = hashlib.md5()
    myMd5.update(srcStr)
    strMd5 = myMd5.hexdigest()

    return strMd5


def writerTupleDataToFile(rooms_list, out_file):
    try:
        import json
        for cand_room in rooms_list:
            out_file.write(json.dumps(cand_room) + '\n')
    except Exception, e:
        logger.error('writer data to tmp file fail ' + str(e))
        import sys
        sys.exit(1)
        pass


def getTupleDataFromFile(file_name):
    '''
    将酒店例行抓取的数据存储到临时文件中,避免内存的大量使用
    抓取完成后从文件中读取所有数据然后插入数据库
    '''
    data_list = []
    import json
    try:
        in_file = file(file_name)
        for line in in_file:
            line = line.strip()

            if '' == line:
                continue

            cand_data = json.loads(line)

            data_list.append(cand_data)
    except Exception, e:
        logger.error('get data from file fail.error = ' + str(e) + '\n')

    import os
    os.system('rm ' + file_name)
    return data_list


if __name__ == '__main__':
    # p = get_proxy(forbid_regions=['CN'])
    cand_str = 'test str'
    print getStrMd5(cand_str)
