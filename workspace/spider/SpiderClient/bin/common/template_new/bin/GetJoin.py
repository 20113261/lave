#!/usr/bin/env python 
#coding:utf-8

from GetJsonContent import *

class GetJoin(GetJsonContent):

    def __init__(self):
        pass


    def GetUnder(self, eachDict, route):
        #获取字段格式为A_B_C的数据
        con_list = []
        under_res = ''
        if route.find('&') > -1:
            route_list = route.split('&')
            list_temp = self.GetJsonValues(eachDict, route_list[0])
            result = []
            res_type = type(list_temp)
            if res_type == list:
                con_list = list_temp
            else:
                con_list.append(list_temp)
            for every in con_list:
                res = self.GetJsonValues(every, route_list[1])
                if res == None:
                    continue
                result.append(res)

            under_res = '_'.join(result)
        else:
            try:
                under_res = self.GetJsonValues(eachDict, route)
            except Exception, e:
                under_res = 'NULL'

        return under_res


    def GetVertical(self, eachDict, route):
        #获取字段格式为A_B|B_C的数据（主要为stop_id, stop_time）
        vertical = ''
        con_list = []
        route_list = route.split('&')
        list_temp = self.GetJsonValues(eachDict, route_list[0])
        result = []
        res_type = type(list_temp)
        
        if res_type == list:
            con_list = list_temp
        else:
            con_list.append(list_temp)
        
        for every in con_list:

            dep = self.GetJsonValues(every, route_list[1])
            dest = self.GetJsonValues(every, route_list[2])

            str = dep + '_' + dest

            result.append(str)

        vertical = '|'.join(result)

        return vertical




if __name__ == '__main__':
    
    import sys
    sys.path.append('..')

    from PageTreeDict import *
    pt = PageTreeDict()
    
    import os

    with open('../test/ceair_json', 'r') as f:
        page = f.read()

    gj = GetJoin()
    dict0 = pt.PageTreeDict(page, 'json')
    list = gj.GetJsonValues(dict0, 'airResultDto|productUnits')
    i = 1
    for every in list:
        res = gj.GetUnder(every, 'oriDestOption@0|flights&stayTime')
        print res
         
