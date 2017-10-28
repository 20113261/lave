# encoding: utf-8
from common.check_book import mysql_ext
from datetime import datetime as dt
from common.check_book.check_book_config import check_book_ratio_development
from common.check_book.check_book_config import check_book_ratio_online
from common.check_book.check_book_config import check_book_ratio_test
import time
from mioji.common import parser_except
from mioji.common.logger import logger
__auth__ = 'fan bowen'


# 本文件是为了满足查定比的需求


class CheckBookRatio(object):
    # 此类为了查询sql用的
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        type_info = self.kwargs.get("type_info", "NULL")
        sid_info = self.kwargs.get("unionKey", "NULL")
        if type_info == "Development":
            self._mysql = mysql_ext.MySQLExt(**check_book_ratio_development)
        elif type_info == "online":
            self._mysql = mysql_ext.MySQLExt(**check_book_ratio_online)
        elif type_info == "test":
            self._mysql = mysql_ext.MySQLExt(**check_book_ratio_test)
        else:
            raise parser_except.ParserException(parser_except.TASK_ERROR,
                                                "{0}::任务类型不正确".format(sid_info))
        self.ptid = kwargs.get('ptid', '')  # 企业id
        self.unionKey = kwargs.get('unionKey', '')  # 源id
        self.today = dt.today().strftime("%Y%m")
        self.acc = kwargs.get('acc', '')  # 账号模式
        self.table = 'checkbook_statistic_partner_source'
        self.record_table = 'checkbook_partner_source'
        self.method = kwargs.get('method', '')  # 这个参数是说明更新哪个字段的

        self.api_name = kwargs.get('api_name')  # 更新以qid为单条记录
        self.qid = kwargs.get('qid')
        self.record_tuple = kwargs.get('record_tuple')  # 此处tuple形如为(1, 2, 3) 为此qid 使用了一次查询数 两笔订单数 三次退单数
        self.citme = int(time.time())

    def insert(self):
        # 此处为插入操作
        try:
            sql = "INSERT INTO {table} VALUES ('{ptid}', '{unionKey}', '{date}', {acc}, {check}, {book}, {refund})".format(
                table=self.table, ptid=self.ptid, unionKey=self.unionKey, date=self.today, acc=self.acc,
                check=1 if self.method == 'check' else 0,
                book=1 if self.method == 'book' else 0,
                refund=1 if self.method == 'refund' else 0
            )
            self._mysql.exec_sql(sql)
        except Exception as why:
            print why
        finally:
            self._mysql.close()

    def update(self):
        # 此处为更新调用次数加1
        try:
            sql = "UPDATE {table} SET `{method}` = `{method}` + 1 " \
                  "WHERE ptid='{ptid}' AND unionKey='{unionKey}' AND date='{date}' AND acc={acc}".format(
                      table=self.table, method=self.method, ptid=self.ptid, unionKey=self.unionKey,
                      date=self.today, acc=self.acc
            )
            self._mysql.exec_sql(sql)
        except Exception as why:
            print why
        finally:
            self._mysql.close()

    def insert_record_qid(self):
        try:
            sql = "INSERT INTO checkbook_partner_source values('{ptid}', '{unionKey}', {ctime}, {acc}, '{api}', {qid}, {check}, " \
                    "{book}, {refund})".format(ptid=self.ptid, unionKey=self.unionKey, ctime=self.citme, acc=self.acc,
                                               qid=self.qid,
                                               api=self.api_name, check=self.record_tuple[0],
                                               book=self.record_tuple[1], refund=self.record_tuple[2])
            self._mysql.exec_sql(sql)
        except Exception as why:
            print why
        finally:
            self._mysql

    def record(self):
        # 此处为看调用insert还是record 如果库中没有就插入， 有的话更新数值+1
        sql = 'select * from {0} where ptid="{1}" AND unionKey="{2}" AND date="{3}" AND acc={4}'.format(
            self.table, self.ptid, self.unionKey, self.today, self.acc
        )
        in_table = self._mysql.exec_sql(sql)
        if not in_table:
            self.insert()
        else:
            self.update()


def use_check(**kwargs):
    _check = CheckBookRatio(**kwargs)
    _check.method = 'check'
    _check.record()


def use_book(**kwargs):
    _book = CheckBookRatio(**kwargs)
    _book.method = 'book'
    _book.record()


def use_cancel(**kwargs):
    _cancel = CheckBookRatio(**kwargs)
    _cancel.method = 'refund'
    _cancel.record()


def use_record_qid(**kwargs):
    _record = CheckBookRatio(**kwargs)
    _record.insert_record_qid()

if __name__ == "__main__":
    use_check(ptid='A66691', unionKey='s119', acc=1, type_info="test")
    # use_book(ptid='A66691', unionKey='s119', acc=1)
    # use_cancel(ptid='A66691', unionKey='s119', acc=1)
    use_record_qid(ptid='A66691', unionKey='s119', acc=1, api_name="JAC", qid="15802436213", record_tuple=[3, 1, 0], type_info="test")



