
import os
import sys
from db import QueryBySQL, ExecuteSQL

BUSDIR = '/search/Sextract/extractStationSQL/bus/'
TRAINDIR = '/search/Sextract/extractStationSQL/train/'


def extractB():

    file_l = os.listdir(BUSDIR)

    for subdir in file_l:
        sql_l = os.listdir(BUSDIR + subdir)
        for sql in sql_l:
            mysqlStr = 'mysql -uroot -pmiaoji@2014! jiangzongjin < ' + BUSDIR + subdir + '/' + sql
            print mysqlStr
            os.system(mysqlStr)
            insertStr = 'insert into jiangzongjin.extractBus select dest_city, dest_station,source from bus'
            res = ExecuteSQL(insertStr)
        

def extractT():

    file_l = os.listdir(TRAINDIR)

    for subdir in file_l:
        sql_l = os.listdir(TRAINDIR + subdir)
        for sql in sql_l:
            mysqlStr = 'mysql -uroot -pmiaoji@2014! jiangzongjin < ' + TRAINDIR + subdir + '/' + sql
            print mysqlStr
            os.system(mysqlStr)
            insertStr = 'insert into jiangzongjin.extractTrain select dept_city, dept_id,source from train_new'
            insertStr = 'insert into jiangzongjin.extractTrain select dest_city, dest_id,source from train_new'
            res = ExecuteSQL(insertStr)



if __name__ == '__main__':

    import sys
    Type = sys.argv[1]
    if Type.lower() == 'bus':
        extractB()
    elif Type.lower() == 'train':
        extractT()
    else:
        pass
