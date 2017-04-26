#!/bin/env
# coding=utf-8
import requests
import urllib2
import sys


def read_file(file_name):
    fr = open(file_name)
    file_str = fr.read()

    return file_str


def send(title, mail_info, mail_list):
    try:
        request_url = '''http://10.10.150.16:9000/sendmail?mailto=%s&content='%s'&eventip=10.10.150.16&title=%s''' % (
            urllib2.quote(mail_list), mail_info, title)
        req_obj = requests.post(request_url)
        print req_obj.text
        return True
    except Exception, e:
        sys.stderr.write('Error code:%s\n' % e.message)
        return False


if __name__ == '__main__':
    # send('slave 进程被kill', 'content',
    #      'dujun@mioji.com;changjing@mioji.com;hourong@mioji.com;shengweisong@mioji.com')

    print send('Test', 'test', 'hourong@mioji.com')
