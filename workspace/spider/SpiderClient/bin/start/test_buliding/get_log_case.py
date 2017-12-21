#!/usr/bin/env python
# coding=UTF-8
import requests
import datetime
import pymysql

pymysql.install_as_MySQLdb()
import json
import csv
import codecs
import re

# hjldb sql 对照
dict1 = {'multiflight': 'interline', 'roundflight': 'flightround', 'flight': 'flight', 'hotel': 'hotel','car':'zuche'}
dict4 = {'flight': 'Flight', 'roundflight': 'RoundFlight', 'multiflight': 'MultiFlight', 'hotel': 'Hotel','car':'Car'}
dict5 = {'multiflight': 'flightmulti', 'roundflight': 'flightround', 'flight': 'flight', 'hotel': 'hotel','car':'Car'}
dict2 = {'MultiFlight': 'interline', 'RoundFlight': 'flightround', 'Flight': 'flight', 'Hotel': 'hotel','Car':'car'}
dict3 = {'MultiFlight': 'flightmulti', 'RoundFlight': 'flightround', 'Flight': 'oneway', 'Hotel': 'hotel','Car':'car'}

get_case_verification = {
    "host": "10.10.155.146",
    "user": "reader",
    "passwd": "mioji1109",
    "db": "hjldb",
}


class mk_case_log:
    def __init__(self, case_info, co_num, verify=True):
        if verify:
            self.verify = verify
            self.log_type = "YZ"
            self.source = case_info.get('source')
            self.source_type = case_info.get("source_type")
            self.error_code = str(0)
            self.log_time = case_info.get("log_time", "null")
            self._mysql = pymysql.connect(**get_case_verification)
            self.co_num = co_num
        else:
            self.verify = verify
            self.log_type = case_info.get("log_type", "YZ")
            self.source = case_info.get("source")
            self.source_type = case_info.get("source_type")
            self.error_code = str(case_info.get("error_code"))
            self.log_time = case_info.get("log_time", "null")
            self._mysql = pymysql.connect(**get_case_verification)
            self.co_num = 10

    def mk_log_cass(self):
        if self.verify:
            pass
        else:
            log_case_name = self.source + "_" + self.error_code + "_" + self.log_type + "_" + self.source_type + "_case.csv"
            print "log case name:", log_case_name
            self.csvfile = file(log_case_name, 'wb')
            self.csvfile.write(codecs.BOM_UTF8)
            self.writer = csv.writer(self.csvfile)
            self.writer.writerow(["源名称", "code", "qid", "content", "页面上传md5", "跟踪结果", "处理方法", "修复后运行此批content结果"])

    def select_case(self):
        "获取任务的qid"
        if self.log_time == "null":
            case_time = self.get_time()  # 获取前一天的时间
        else:
            case_time = self.log_time

        if self.verify:
            b = dict1[self.source_type]
            sql = "SELECT * FROM count_verify_failed_qid WHERE source='{0}' AND data_type='{1}' AND date='{2}' AND err_reason like '%success%'".format(
                self.source, b, case_time
            )
        else:
            if self.log_type == "YZ":
                sql = "SELECT * FROM count_verify_failed_qid WHERE source='{0}' AND data_type='{1}' AND date='{2}' AND err_reason like '%code:{3}%' group by qid limit 0,10;".format(
                    self.source, dict2[self.source_type], case_time, self.error_code
                )
            elif self.log_type == "Pre_YZ":
                a = {'MultiFlight': 'interline', 'RoundFlight': 'round', 'Flight': 'oneway'}
                b = a[self.source_type]
                sql = "SELECT * FROM err_message WHERE source='{0}' AND data_type='{1}' AND date='{2}' AND err_reason like '%{3}%' group by qid limit 0,10;".format(
                    self.source, b, case_time, self.error_code
                )
            else:
                raise ("检查一下输入内容")
        print sql
        cursor = self._mysql.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        print "data"
        print data
        self._mysql.close()
        return data, case_time

    def get_time(self):
        '''获取前一天的时间'''
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        n_days = now - delta
        log_time = n_days.strftime('%Y%m%d')
        return log_time

    def get_log(self, case_list, case_time):
        '''
        获取日志
        '''
        las = "sp001_" + self.source + dict4[self.source_type]
        content_list = []
        for case in case_list:
            if len(content_list) >= self.co_num:
                break
            qid = case[3]
            url_1 = "http://oa.mioji.com/opui/api/logQuery/detail?backend=1&env=online&tname=nginx_api_log_{0}&qid={1}".format(
                case_time, qid)
            log_resp1 = requests.get(url_1)
            case_typenum_dict = json.loads(log_resp1.content)
            case_typenum_infos = case_typenum_dict["data"]
            case_typenum = []
            for case_typenum_info in case_typenum_infos[0]:
                if las in case_typenum_info[1]:
                    case_typenum.append(case_typenum_info)
            md5_keys = []
            for i in case_typenum:
                url_2 = "http://oa.mioji.com/opui/api/logQuery/detail?tname=nginx_api_log_{0}&env=online&id={1}".format(
                    case_time, i[0])
                log_resp2 = requests.get(url_2)
                resp_2 = json.loads(log_resp2.content)

                resp_2_data = resp_2["data"]
                if json.loads(resp_2_data["response"])['error_code'] == int(self.error_code):
                    content = json.loads(resp_2["data"]['req_params'])
                    ac = {'MultiFlight': 'flightmulti', 'RoundFlight': 'flightround', 'Flight': 'flight'}
                    if self.log_type == 'YZ':
                        if len(content_list) >= self.co_num:
                            break
                        if self.verify:
                            a = dict5[self.source_type]
                        else:
                            a = dict3[self.source_type]
                        if a in content['redis_key']:
                            content = content['other_info']["content"] if content != '' else None
                            print content
                            if content not in content_list:
                                content_list.append(content)
                                resp_datas = json.loads(resp_2_data["response"])["data"]
                                resp_data = resp_datas[-1]
                                md5_key = resp_data["md5_key"]
                                if md5_key not in md5_keys:
                                    md5_keys.append(md5_key)
                                    if self.verify:
                                        pass
                                    else:
                                        self.writer.writerow([self.source, self.error_code, qid, content, md5_key, ])
                            else:
                                pass
                        else:
                            pass
                    else:
                        if ac[self.source_type] in content['redis_key']:
                            if len(content_list) > 10:
                                break
                            list_a = content['redis_key'].split('|')
                            if '&' in list_a[2]:
                                content = list_a[1] + '|' + list_a[2]
                            else:
                                content = list_a[1]
                            print content
                            if content not in content_list:
                                content_list.append(content)
                                resp_datas = json.loads(resp_2_data["response"])["data"]
                                resp_data = resp_datas[-1]
                                md5_key = resp_data["md5_key"]
                                if md5_key not in md5_keys:
                                    md5_keys.append(md5_key)
                                    if self.verify:
                                        pass
                                    else:
                                        self.writer.writerow([self.source, self.error_code, qid, content, md5_key, ])
        if self.verify:
            pass
        else:
            self.csvfile.close()
        return content_list

    def great_function(self):
        self.mk_log_cass()
        # 从进龙处获取错case的qid
        cases_tup, case_time = self.select_case()
        # 通过qid去运维处获取日志文件，获取md5等信息。
        list_content = self.get_log(cases_tup, case_time)
        return list_content


if __name__ == "__main__":
    case_info = {
        "log_type": "YZ",
        # 验证 YZ   预验证  Pre_YZ
        "source": "expedia",
        "source_type": "Flight",
        # 单程: Flight 往返: RoundFlight 联程: MultiFlight 酒店： hotel
        "error_code": 22,
        "log_time": "20171211"
        # 选填，默认查前一天的
    }
    get_log = mk_case_log(case_info,verify=False)
    list_c = get_log.great_function()
    print list_c
