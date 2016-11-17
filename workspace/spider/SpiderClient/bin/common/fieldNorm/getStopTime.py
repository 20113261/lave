#!/usr/bin/env python
#coding:utf-8


import os
import re
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

month = {'JAN':'01', 'FEB':'02', 'MAR':'03', 'APR':'04', 'MAY':'05', 'JUN':'06',\
        'JUL':'07', 'AUG':'08', 'SEP':'09', 'OCT':'10', 'NOV':'11', 'DEC':'12' } 

def getDateTime(content):
    content_tmp = content.split('T')
    d = content_tmp[0].strip()
    t = content_tmp[1].strip()
    #t = content_tmp[0]
    result = ''
    '''
    将1:40p, 12:20AM, 20:30
    时间格式标准化：HH:MM:SS
    '''
    if len(t[:t.find(':')]) == 1:
        t = '0' + t
    if t[-1].lower() == 'a':
        t = t[:-1]
    elif t[-1].lower() == 'p' and t[:2] != '12':
        t = str(int(t[:2]) + 12) + t[2:-1]
    elif t[-1].lower() =='p' and t[:2] == '12':
        t = '00' + t[2:-1]
    result = t + ':00'
    '''
    日期格式标准化：YYYY-MM-DD
    '''

    pat_ch = re.compile(ur'[\u4e00-\u9fff]', re.M)      #将汉字替换
    d = pat_ch.sub('-', d.decode('utf-8'), 2)
    d = pat_ch.sub('', d.decode('utf-8'), 2)
    d = d.replace(' ', '-')                             #将空格，'/'替换。
    d = d.replace('/', '-')
    sp = d.split('-')          
    sp_len = len(sp)
    if sp_len == 3:     #对应各式:'2015-11-25' '2014/2/3' '2015年8月20日' 'Sep 4 2015'
        mon = d[:3].upper()
        if mon in month.keys():
            d_tmp = d.split('-')
            if len(d_tmp[1]) == 1:
                d_tmp[1] = '0' + d_tmp[1]
            d = d_tmp[2] + '-' + month[mon] + '-' + d_tmp[1]
        else:
            for i in range(3):
                if len(sp[i]) == 1:
                    sp[i] = '0' + sp[i]
            d = '-'.join(sp)
    else:
        if len(sp[0]) < 2:                  # 对应格式:"1 Sep"
            sp[0] = '0' + sp[0]
        if len(sp) == 2:
            mon = month[sp[1].upper()]
            today = str(datetime.date.today())
            year = today[:4]
            if int(mon) < int(today[5:7]):
                year = str(int(year) + 1)
            d = year + '-' + mon + '-' + sp[0]
            
    result = d + 'T' + result
        
    return result

def gStopTime(content_list):

    result = ''
    if model == '1':
        con_tmp_list = content_list.split('|')
        for each in con_tmp_list:
            each_list = each.split('_')
            for every in each_list:
                result += getDateTime(every) + '_'
            result = result[:-1] + '|'
    elif model == '2':
        pass
    else:
        pass

    return result[:-1]



if __name__ == '__main__':
    #print chmode('2015年11月25日T01:40p')
    print getStopTime('2015-06-25T00:30:00_2015-06-25T06:25:00|2015-06-26T02:10:00_2015-06-26T06:35:00|2015-06-26T19:25:00_2015-06-26T20:10:00')


