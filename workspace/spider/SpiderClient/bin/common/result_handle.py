#! /usr/bin/env python
#coding=utf-8

import sys
import json
from logger import logger


reload(sys)
sys.setdefaultencoding('utf-8')


def load_desc2json(room_list):
    '''
    本函数的功能是把 room_desc 为 json dump 成 String 的数据重新 load 成json
    '''

    if room_list == []:
        return room_list

    elif room_list[0][13] == -10:
        return room_list

    else:
        new_room_list = []
        for each_room in room_list:
            try:
                each_room_list = list(each_room)
                try:
                    each_room_desc = json.loads(each_room_list[26])
                    each_room_list[26] = each_room_desc
                except Exception, e:
                    pass
                new_room_list.append(tuple(each_room_list))
            except Exception, e:
                logger.info('%s' % str(e))
                continue

        return new_room_list






