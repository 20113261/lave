#!/usr/bin/env python
#coding:utf-8

from db import QueryBySQL

def delete_duplicate_data(Type):
    
    if Type = 'bus':
        sql_bus = 'INSERT INTO bus_station SELECT * FROM extractBus group by city, station, source'
        ExecuteSQL(sql_bus)
    elif Type = 'train':
        sql_train = 'INSERT INTO train_station SELECT * FROM extractTrain group by city, station, source'
        ExecuteSQL(sql_train)


if __name__ == '__main__':

    import sys
    Type = sys.argv[1]
    delete_duplicate_data(Type)

