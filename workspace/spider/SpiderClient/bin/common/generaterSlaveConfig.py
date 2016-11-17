#encoding=utf-8
import sys
import MySQLdb
import ConfigParser


def generaterSlaveConfig():
    for cfg_file_name in ['slave.spider.ini','slave.validation.ini','slave.mt.ini']:

        config = ConfigParser.ConfigParser()
        if cfg_file_name == 'slave.spider.ini':
            config.add_section('master')
            config.set('master','host','10.10.99.53:10086')

            config.add_section('proxy')
            config.set('proxy','host','10.10.177.197:8087')

            config.add_section('slave')
            config.set('slave','thread_num',15)

            config.set('slave','name','slave_156_8089_total')
            config.set('slave','recv_real_time_request',1)

            #uc
            config.add_section('mysql')
            config.set('mysql','host','10.10.154.38')
            config.set('mysql','user','writer')
            config.set('mysql','pswd','miaoji1109')
            config.set('mysql','db','crawl')

            config.add_section('redis')
            config.set('redis','host','10.10.24.130')
            config.set('redis','port',6379)

        elif 'slave.validation.ini' == cfg_file_name:
            config.add_section('master')
            config.set('master','host','10.10.145.240:9999')

            config.add_section('proxy')
            config.set('proxy','host','10.10.177.197:8087')

            config.add_section('slave')
            config.set('slave','thread_num',15)

            config.set('slave','name','slave_156_8089_total')
            config.set('slave','recv_real_time_request',1)

            #uc
            config.add_section('mysql')
            config.set('mysql','host','10.10.154.38')
            config.set('mysql','user','writer')
            config.set('mysql','pswd','miaoji1109')
            config.set('mysql','db','validation')

            config.add_section('redis')
            config.set('redis','host','10.10.24.130')
            config.set('redis','port',6379)

        elif 'slave.mt.ini' == cfg_file_name:
            config.add_section('master')
            config.set('master','host','123.59.45.19:9999')

            config.add_section('proxy')
            config.set('proxy','host','120.132.92.44:8087')

            config.add_section('slave')
            config.set('slave','thread_num',15)

            config.set('slave','name','slave_156_8089_total')
            config.set('slave','recv_real_time_request',1)


            #mt
            config.add_section('mysql')
            config.set('mysql','host','123.59.70.19')
            config.set('mysql','user','writer')
            config.set('mysql','pswd','miaoji1109')
            config.set('mysql','db','validation')

            config.add_section('redis')
            config.set('redis','host','120.132.95.246')
            config.set('redis','port',6379)

        conn = MySQLdb.connect(host='10.10.154.38', user='reader', charset='utf8',passwd='miaoji1109', db='onlinedb')
        cursor = conn.cursor()

        sql = "select sectionName,className,filePath,modeName from parserSource2Module"

        cursor.execute(sql)

        datas = cursor.fetchall()

        cursor.close()
        conn.close()

        for data in datas:
            if None in data:
                continue
            section_name = data[0].encode('utf-8')
            class_name = data[1].encode('utf-8')
            file_path = data[2].encode('utf-8')
            mode_name = data[3].encode('utf-8')

            if file_path == 'slave_UC_parser' or 'slave_UC_validation' == file_path:
                continue

            config.add_section(section_name)
            config.set(section_name,'class_name',class_name)
            config.set(section_name,'file_path',file_path)
            config.set(section_name,'mode_name',mode_name)

        cfgfile = open(cfg_file_name,'w')
        config.write(cfgfile)
        cfgfile.close()

if __name__ == '__main__':
    generaterSlaveConfig()
