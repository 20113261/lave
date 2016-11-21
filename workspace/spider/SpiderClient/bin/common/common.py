#!/usr/bin/env python
#coding=UTF-8
'''
    Created on 2014-03-22
    @author: devin
    @desc:
        
'''
import jsonlib
import time
from util import http_client

proxy_client = http_client.HttpClientPool("10.136.8.94:8086")
#proxy_client2 = http_client.HttpClientPool("10.136.11.134:8087")
proxy_client2 = http_client.HttpClientPool("10.10.239.46:8087")

def getLocalIp(ifname = 'eth0'):
    import socket, fcntl, struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))

    ret = socket.inet_ntoa(inet[20:24])
    return ret

def set_proxy_client(client):
    global proxy_client2
    proxy_client2 = client

def get_proxy(source = None, allow_ports = [], forbid_ports = [], allow_regions = [], forbid_regions = [], user = 'realtime', passwd = 'realtime', proxy_info = {}):
    special_ip = '10.10.156.56|10.10.184.17|10.10.184.214|10.10.170.233|10.10.176.6|10.10.48.27|10.10.38.160|10.10.29.204|10.10.106.179|10.10.228.4|10.10.218.199'
    try:
	ip = getLocalIp() 
    	if ip in special_ip:
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
        allow = '_'.join( [str(i) for i in allow_ports] ) 
    if len(forbid_ports) != 0:
        forbid = '_'.join( [str(i) for i in forbid_ports] )

    if len(allow_regions) != 0:
        allow_regions_str = '_'.join( [i for i in allow_regions] )
    if len(forbid_regions) != 0:
        forbid_regions_str = '_'.join( [i for i in forbid_regions] )
    
    try:
        p = proxy_client2.get("/proxy?source=%s&user=crawler&passwd=spidermiaoji2014" % source)
        #p = proxy_client2.get("/proxy?source=%s&user=parser&passwd=parser" % source)
    except:
        p = ''

    return p

def invalid_proxy(proxy,source):
    return
    #if proxy != None:
    #    proxy_client.get("/update_proxy?status=Invalid&p=%s&source=%s"%(proxy,source))


def update_proxy(source_name, proxy, start_time, error_code):
    speed = time.time() - start_time
    if proxy != None or proxy != 'NULL':
        proxy_client2.get('/update_proxy?source=%s&proxy=%s&error=%s&speed=%s' % (source_name, proxy, \
                str(error_code), str(speed)))

    return None


if __name__ == '__main__':
    p = get_proxy(forbid_regions=['CN'])
    print p
