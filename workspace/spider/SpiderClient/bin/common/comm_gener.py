#coding:utf-8
import MySQLdb
import sys
import json

def station_common(Type,host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select station,alias,station_id,city_id from " + Type + ";"
    cursor.execute(sql)
    datas = cursor.fetchall()


    temp_map = {}
    for data in datas:
        station = data[0].encode('utf-8').upper()
        try:
            alias = data[1].encode('utf-8').upper().split('&&')
        except:
            alias = []
        station_id = data[2].encode('utf-8')
        nu = 0
        try:
            if data[3].encode('utf-8') == "":
                nu = 1
        except:
            nu = 1

        if station in temp_map and nu == 1:
            continue
        temp_map[station] = station_id
        if len(alias) > 0:
            for a in alias:
                if a in temp_map:
                    continue
                temp_map[a] = station_id

    temp_vec = []
    for s in temp_map:
        temp_vec.append("\"" + s + "\":'" + temp_map[s] + "',")

    temp_vec.sort()
    if len(temp_vec) > 0:
        temp_vec[-1] = temp_vec[-1][:-1]

    f = open(Type + '_common.py','w')
    if Type == 'station':
        f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nStation = {\n")
    elif Type == 'bus':
        f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nBus_Dict = {\n")
    for v in temp_vec:
        f.write(v + '\n')
    f.write("}")
    f.close()
    cursor.close()
    conn.close()

def tax_common(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select city_cn_name,tax_rate from hotel_tax;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    check = set()
    temp_vec = []
    for data in datas:
        name = data[0].encode('utf-8')
        rate = float(data[1])
        if name not in check:
            check.add(name)
            temp_vec.append("\"" + name + "\":" + str(rate) + ",")

    temp_vec.sort()
    if len(temp_vec) > 0:
        temp_vec[-1] = temp_vec[-1][:-1]

    f = open('tax_common.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\ntax_dict = {\n")
    for v in temp_vec:
        f.write(v + '\n')
    f.write("}")
    f.close()
    cursor.close()
    conn.close()

def currency_common(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select currency_code,coin_sign from exchange;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    temp_vec = []
    for data in datas:
        code = data[0].encode('utf-8')
        if data[1] == None or data[1] == 'NULL':
            continue
        sign = data[1].encode('utf-8')
        temp_vec.append("\"" + sign + "\":'" + code + "',")

    temp_vec.sort()
    if len(temp_vec) > 0:
        temp_vec[-1] = temp_vec[-1][:-1]

    f = open('currency_common.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nCurrency_Dict = {\n")

    Currency_Dict={'$':'USD','¥':'CNY','£':'GBP','€':'EUR','HK$':'HKD','S$':'SGD','JP¥':'JPY','₡':'CRC','BS$':'BSD','AU$':'AUD','S$':'SGD','Tk':'BDT'}
    f.write(json.dumps(Currency_Dict,indent=4,ensure_ascii=False) + '\n')

    #for v in temp_vec:
    #    f.write(v + '\n')
    #f.write("}")

    f.close()
    cursor.close()
    conn.close()

def airline_code(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select code,name_en from airlines;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    temp_airline = []
    temp_vec = []
    for data in datas:
        code = data[0].encode('utf-8')
        try:
            en = data[1].encode('utf-8')
        except:
            continue
        temp_airline.append({'flight_en_name':en,'flight_id':code})
        temp_vec.append("\"" + en.strip() + "\":'" + code.strip() + "',")

    temp_vec.sort()
    if len(temp_vec) > 0:
        temp_vec[-1] = temp_vec[-1][:-1]

    f = open('airline_code.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nAirline_2_Code = {\n")
    for v in temp_vec:
        f.write(v + '\n')
    f.write("}")
    f.write("\n\ntemp_airline = \n")
    f.write(json.dumps(temp_airline,indent = 4,ensure_ascii=False))
    f.close()
    cursor.close()
    conn.close()

def airport_common(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select airport.iata_code,city.tri_code,city.name,airport.country,country.continent_code,country.continent,\
        city.py,country.country_code,city.name_en,city.time_zone from airport,city,country \
        where airport.city_id!='NULL' and airport.country!='NULL' and airport.city_id=city.id and \
        city.time_zone!=-100 and city.tri_code!='NULL' and airport.country=country.name;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    Airport = {}
    default_class = 2
    for data in datas:
        key = data[0].encode('utf-8')
        if key not in Airport:
            Airport[key] = {}
        else:
            continue
        city = data[1].encode('utf-8')
        city_cn_name = data[2].encode('utf-8')
        country = data[3].encode('utf-8')
        iatacode = key
        continent_code = data[4].encode('utf-8')
        continent = data[5].encode('utf-8')
        city_pinyin = data[6].encode('utf-8')
        country_code = data[7].encode('utf-8')
        city_en_name = data[8].encode('utf-8')
        timezone = int(data[9])
        try:
            airport_name = data[10].encode('utf-8')
        except:
            airport_name = 'NULL'
        n_class = default_class

        Airport[key]['city'] = city
        Airport[key]['city_cn_name'] = city_cn_name
        Airport[key]['country'] = country
        Airport[key]['iatacode'] = iatacode
        Airport[key]['continent_code'] = continent_code
        Airport[key]['continent'] = continent
        Airport[key]['city_pinyin'] = city_pinyin
        Airport[key]['country_code'] = country_code
        Airport[key]['city_en_name'] = city_en_name
        Airport[key]['timezone'] = timezone
        Airport[key]['class'] = n_class

        if airport_name != 'NULL':
            airport_cn[airport_name] = key
    f = open('airport_common.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nAirport = \n")
    f.write(json.dumps(Airport,indent = 4,ensure_ascii=False))
    f.close()

    sql = "select iata_code,name from airport;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    airport_cn = {}
    for data in datas:
        code = data[0].encode('utf-8')
        name = data[1].encode('utf-8').strip()
        if name != 'NULL' and len(name) > 0:
            airport_cn[name] = code
    f = open('airport_cn.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\nAirport_cn_Dict = \n")
    f.write(json.dumps(airport_cn,indent = 4,ensure_ascii=False))
    f.close()
    cursor.close()
    conn.close()

def area_common(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select area_id,source,sid from car_area_unid;"
    cursor.execute(sql)
    datas = cursor.fetchall()

    temp_map = {}
    for data in datas:
        area_id = data[0].encode('utf-8')
        source = data[1].encode('utf-8')
        sid = data[2].encode('utf-8')
        temp_map[sid + '_' + source] = area_id

    f = open('area_common.py','w')
    f.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\narea_dict = \n")
    f.write(json.dumps(temp_map,indent = 4,ensure_ascii=False))
    f.close()
    cursor.close()
    conn.close()

def city_common(host_str,user_str,passwd_str,db_str):
    conn = MySQLdb.connect(host=host_str,user=user_str,charset='utf8',passwd=passwd_str,db=db_str)
    cursor = conn.cursor()
    sql = "select name,name_en,py,country,time_zone,tri_code,id,summer_zone,ctrip_id,summer_start,summer_end from city where tri_code != 'NULL'"
    cursor.execute(sql)
    datas = cursor.fetchall()

    city = {}
    city_dict = {}
    city_name_dict = {}
    for cand_data in datas:
        word_list = []
        for cand_word in cand_data:
            if None == cand_word:
                word_list.append('NULL')
            elif isinstance(cand_word,float):
                word_list.append(cand_word)
            else:
                word_list.append(cand_word.encode('utf-8'))

        city_name_zh = word_list[0]
        city_name_en = word_list[1]
        city_name_py = word_list[2]
        country = word_list[3]
        time_zone = float(word_list[4])
        city_code = word_list[5]
        city_id = word_list[6]
        summer_zone = word_list[7]
        ctrip_id = word_list[8]
        summer_start = word_list[9]
        summer_end = word_list[10]

        city[city_code] = {'city_name_en':city_name_en,'country':country,'time_zone':time_zone,\
            'city_code':city_code,'city_name_py':city_name_py,'city_name_zh':city_name_zh}
        city_dict[city_code] = {'city_name_en':city_name_en,'city_id':city_id,'summer_zone':summer_zone,\
            'city_name_zh':city_name_zh,'country':country,'ctrip_id':ctrip_id,'time_zone':time_zone,\
            'summer_end':summer_end,'city_name_py':city_name_py,'city_code':city_code}
        city_name_dict[city_name_zh] = city_code

    out_file = file('city_common.py','w')
    out_file.write("#coding:utf-8\nimport os\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\n\n")
    out_file.write('City = ' + json.dumps(city,indent = 4,ensure_ascii=False) + '\n\n')
    out_file.write('city_dict = ' + json.dumps(city_dict,indent = 4,ensure_ascii=False) + '\n\n')
    out_file.write('city_name_dict = ' + json.dumps(city_name_dict,indent = 4,ensure_ascii=False) + '\n')
    out_file.close()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        user = 'reader'
        passwd = 'miaoji1109'
        host = '10.10.87.87'
        db = 'devdb'

        station_common("station",host,user,passwd,db)
        station_common("bus",host,user,passwd,db)
        tax_common(host,user,passwd,'onlinedb')
        currency_common(host,user,passwd,db)
        airline_code(host,user,passwd,db)
        airport_common(host,user,passwd,db)
        area_common(host,user,passwd,db)
        city_common(host,user,passwd,db)
        exit(1)

    Type = sys.argv[1]
    Cond = sys.argv[2]

    user = 'reader'
    passwd = 'miaoji1109'
    host = '10.10.87.87'

    if Type == "station" or Type == "bus":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        station_common(Type,host,user,passwd,db)

    elif Type == "hotel_tax":
        db = 'onlinedb'
        tax_common(host,user,passwd,db)

    elif Type == "exchange":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        currency_common(host,user,passwd,db)

    elif Type == "airlines":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        airline_code(host,user,passwd,db)

    elif Type == "airport":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        airport_common(host,user,passwd,db)

    elif Type == "car_area_unid":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        area_common(host,user,passwd,db)

    elif Type == "city":
        if Cond == "test":
            db = 'devdb'
        elif Cond == "online":
            db = 'onlinedb'
        else:
            print "env = test or online"
            exit(1)
        city_common(host,user,passwd,db)

    else:
        print "No need to update common file"
        exit(1)
