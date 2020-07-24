# encoding=utf-8
import ConfigParser

import MySQLdb


def generaterSubordinateConfig():
    for cfg_file_name in ['subordinate.spider.ini', 'subordinate.validation.ini', 'subordinate.startwithD.ini',
                          'newframeFlight.ini',  'test.online.ini']:

        config = ConfigParser.ConfigParser()
        config.add_section('data_type')
        config.set('data_type', '10.10.106.179', 'Flight')
        config.set('data_type', '10.10.29.204', 'Flight')
        config.set('data_type', '10.10.38.160', 'Flight')
        config.set('data_type', '10.10.153.6', 'Flight')
        config.set('data_type', '10.10.95.70', 'ListHotel')
        config.set('data_type', '10.10.84.225', 'ListHotel')
        config.set('data_type', '10.10.48.27', 'ListHotel')
        config.set('data_type', '10.10.100.30', 'ListHotel')
        config.set('data_type', '10.10.111.212', 'ListHotel')
        config.set('data_type', '10.10.99.125', 'ListHotel')
        config.set('data_type', '10.10.228.4', 'RoundFlight_MultiFlight')
        config.set('data_type', '10.10.218.199', 'RoundFlight_MultiFlight')
        config.set('data_type', '10.10.246.77', 'Rail_Bus')

        if cfg_file_name == 'subordinate.routine.ini':
            config.add_section('main')
            config.set('main', 'host', '10.10.110.74:48069')

            config.add_section('proxy')
            config.set('proxy', 'host', '10.10.239.46:8087')

            config.add_section('subordinate')
            config.set('subordinate', 'thread_num', 3)

            config.set('subordinate', 'name', 'un_used_name')
            config.set('subordinate', 'recv_real_time_request', 0)
            config.set('subordinate', 'env', 'routine')

            # uc
            config.add_section('mysql')
            config.set('mysql', 'host', '10.10.154.38')
            config.set('mysql', 'user', 'writer')
            config.set('mysql', 'pswd', 'miaoji1109')
            config.set('mysql', 'db', 'crawl')

            # spiderbase
            config.add_section('spiderbase')
            config.set('spiderbase', 'host', '10.19.118.147')
            config.set('spiderbase', 'user', 'reader')
            config.set('spiderbase', 'pswd', 'mioji1109')
            config.set('spiderbase', 'db', 'source_info')

            config.add_section('redis')
            config.set('redis', 'host', '10.10.24.130')
            config.set('redis', 'port', 6379)

        elif cfg_file_name == 'subordinate.online_c.ini':
            config.add_section('main')
            config.set('main', 'host', '10.10.244.26:48068')

            config.add_section('proxy')
            config.set('proxy', 'host', '10.10.239.46:8087')

            config.add_section('subordinate')
            config.set('subordinate', 'thread_num', 1)

            config.set('subordinate', 'name', 'un_used_name')
            config.set('subordinate', 'recv_real_time_request', 1)
            config.set('subordinate', 'env', 'OnlineC')

            # uc
            config.add_section('mysql')
            config.set('mysql', 'host', '10.10.154.38')
            config.set('mysql', 'user', 'writer')
            config.set('mysql', 'pswd', 'miaoji1109')
            config.set('mysql', 'db', 'validation')

            # spiderbase
            config.add_section('spiderbase')
            config.set('spiderbase', 'host', '10.19.118.147')
            config.set('spiderbase', 'user', 'reader')
            config.set('spiderbase', 'pswd', 'mioji1109')
            config.set('spiderbase', 'db', 'source_info')

            config.add_section('redis')
            config.set('redis', 'host', '10.10.24.130')
            config.set('redis', 'port', 6379)

        elif cfg_file_name == 'subordinate.online_d.ini':
            config.add_section('main')
            config.set('main', 'host', '10.19.102.211:48068')

            config.add_section('proxy')
            config.set('proxy', 'host', '10.19.191.121:8087')

            config.add_section('subordinate')
            config.set('subordinate', 'thread_num', 1)

            config.set('subordinate', 'name', 'un_used_name')
            config.set('subordinate', 'recv_real_time_request', 1)
            config.set('subordinate', 'env', 'OnlineD')

            config.add_section('mysql')
            config.set('mysql', 'host', '10.10.154.38')
            config.set('mysql', 'user', 'writer')
            config.set('mysql', 'pswd', 'miaoji1109')
            config.set('mysql', 'db', 'validation')

            # spiderbase
            config.add_section('spiderbase')
            config.set('spiderbase', 'host', '10.19.118.147')
            config.set('spiderbase', 'user', 'reader')
            config.set('spiderbase', 'pswd', 'mioji1109')
            config.set('spiderbase', 'db', 'source_info')

            config.add_section('redis')
            config.set('redis', 'host', '10.10.24.130')
            config.set('redis', 'port', 6379)
        elif cfg_file_name == 'subordinate.test.ini':
            config.add_section('main')
            config.set('main', 'host', '10.10.216.3:48068')

            config.add_section('proxy')
            config.set('proxy', 'host', '10.10.239.46:8087')

            config.add_section('subordinate')
            config.set('subordinate', 'thread_num', 1)

            config.set('subordinate', 'name', 'un_used_name')
            config.set('subordinate', 'recv_real_time_request', 1)
            config.set('subordinate', 'env', 'Test')

            # uc
            config.add_section('mysql')
            config.set('mysql', 'host', '10.10.154.38')
            config.set('mysql', 'user', 'writer')
            config.set('mysql', 'pswd', 'miaoji1109')
            config.set('mysql', 'db', 'validation')

            # spiderbase
            config.add_section('spiderbase')
            config.set('spiderbase', 'host', '10.19.118.147')
            config.set('spiderbase', 'user', 'reader')
            config.set('spiderbase', 'pswd', 'mioji1109')
            config.set('spiderbase', 'db', 'source_info')

            config.add_section('redis')
            config.set('redis', 'host', '10.10.24.130')
            config.set('redis', 'port', 6379)

        conn = MySQLdb.connect(host='10.10.238.148', user='mioji_admin',
                               charset='utf8', passwd='mioji1109', db='spider_config')
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

            if file_path == 'subordinate_UC_parser' or file_path == 'subordinate_UC_validation':
                continue

            config.add_section(section_name)
            config.set(section_name, 'class_name', class_name)
            config.set(section_name, 'file_path', file_path)
            config.set(section_name, 'mode_name', mode_name)

        cfgfile = open(cfg_file_name, 'w')
        config.write(cfgfile)
        cfgfile.close()


if __name__ == '__main__':
    generaterSubordinateConfig()