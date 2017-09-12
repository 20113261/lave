#!/bin/env 


import requests
import urllib2
import sys

def read_file(file_name):

    fr = open(file_name)
    file_str = fr.read()

    return file_str

def send(title,mail_info,mail_list):

    try:
        request_url = '''http://10.10.150.16:9000/sendmail?mailto=%s&content='%s'&eventip=10.10.150.16&title=%s''' % (urllib2.quote(mail_list),mail_info,title)
        req_obj = requests.post(request_url)
        print req_obj.text
        return_map = req_obj.json()
    except Exception,e:
        sys.stderr.write('Error code:%s\n' % e.message)
        return False

    if return_map['error_id'] == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print  'Usag:python x.py title err_info list'
    title = sys.argv[1]
    #err_file = sys.argv[2]
    err_info = sys.argv[2]
    mail_list = sys.argv[3]

    #mail_info_str = read_file(err_file)

    send(title,err_info,mail_list)

    
    #request_url = '''http://10.10.150.16:9000/sendmail?mailto='%s'&content=%s&eventip=10.10.150.16&title=%s''' % (mail_list,mail_info_str,title)
    #request_url = '''http://10.10.150.16:9000/sendmail?mailto=%s&content=%s&eventip=10.10.150.16&title=%s''' % (urllib2.quote(mail_list),mail_info,title)
    #requests.post(request_url)
