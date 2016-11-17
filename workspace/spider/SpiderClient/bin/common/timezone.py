#! /usr/bin/env python
#coding=utf-8

import sys
import time
import datetime
from city_common import City
from airport_common import Airport

reload(sys)
sys.setdefaultencoding('utf-8')


TimeZone = {
	'荷兰': {'country':'荷兰', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'挪威': {'country':'挪威', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'瑞士': {'country':'瑞士', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'奥地利': {'country':'奥地利', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'捷克': {'country':'捷克', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'波兰': {'country':'波兰', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'瑞典': {'country':'瑞典', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'意大利': {'country':'意大利', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'斯洛文尼亚': {'country':'斯洛文尼亚', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'法国': {'country':'法国', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'比利时': {'country':'比利时', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'西班牙': {'country':'西班牙', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'葡萄牙': {'country':'葡萄牙', 'standard':'0', 'summer':'1', \
		'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'}, 
	'卢森堡': {'country':'卢森堡', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'匈牙利': {'country':'匈牙利', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'丹麦': {'country':'丹麦', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'俄罗斯': {'country':'俄罗斯', 'standard':'3', 'summer':'3', \
		'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'}, 
	'德国': {'country':'德国', 'standard':'1', 'summer':'2', \
		'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}, 
	'芬兰': {'country':'芬兰', 'standard':'2', 'summer':'3', \
		'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'}, 
	'英国': {'country':'英国', 'standard':'0', 'summer':'1', \
		'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
	'中国': {'country':'中国', 'standard':'8', 'summer':'8', \
		'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'}
		}


Station = {
	'stt100001' : '德国', 
	'stt100002' : '英国', 
	'stt100003' : '德国', 
	'stt100004' : '意大利', 
	'stt100005' : '瑞士', 
	'stt100006' : '瑞士', 
	'stt100007' : '法国', 
	'stt100008' : '德国', 
	'stt100009' : '德国', 
	'stt100010' : '德国', 
	'stt100011' : '荷兰', 
	'stt100012' : '法国', 
	'stt100013' : '捷克', 
	'stt100014' : '意大利', 
	'stt100015' : '德国', 
	'stt100016' : '德国', 
	'stt100017' : '英国', 
	'stt100018' : '荷兰', 
	'stt100019' : '英国', 
	'stt100020' : '英国', 
	'stt100021' : '法国', 
	'stt100022' : '法国', 
	'stt100023' : '法国', 
	'stt100024' : '德国', 
	'stt100025' : '西班牙', 
	'stt100026' : '丹麦', 
	'stt100027' : '德国', 
	'stt100028' : '德国', 
	'stt100029' : '德国', 
	'stt100030' : '奥地利', 
	'stt100031' : '德国', 
	'stt100032' : '意大利', 
	'stt100033' : '西班牙', 
	'stt100034' : '英国', 
	'stt100035' : '意大利', 
	'stt100036' : '瑞士', 
	'stt100037' : '英国', 
	'stt100038' : '英国', 
	'stt100039' : '西班牙', 
	'stt100040' : '瑞典', 
	'stt100041' : '瑞士', 
	'stt100042' : '比利时', 
	'stt100043' : '法国', 
	'stt100044' : '奥地利', 
	'stt100045' : '瑞士', 
	'stt100046' : '西班牙', 
	'stt100047' : '英国', 
	'stt100048' : '德国', 
	'stt100049' : '意大利', 
	'stt100050' : '德国', 
	'stt100051' : '法国', 
	'stt100052' : '意大利', 
	'stt100053' : '法国', 
	'stt100054' : '捷克', 
	'stt100055' : '意大利', 
	'stt100056' : '法国', 
	'stt100057' : '英国', 
	'stt100058' : '比利时', 
	'stt100059' : '英国', 
	'stt100060' : '英国', 
	'stt100061' : '德国', 
	'stt100062' : '德国', 
	'stt100063' : '瑞典', 
	'stt100064' : '德国', 
	'stt100065' : '意大利', 
	'stt100066' : '匈牙利', 
	'stt100067' : '意大利', 
	'stt100068' : '英国', 
	'stt100069' : '德国', 
	'stt100070' : '意大利', 
	'stt100071' : '意大利', 
	'stt100072' : '德国', 
	'stt100073' : '瑞士', 
	'stt100074' : '荷兰', 
	'stt100075' : '奥地利', 
	'stt100076' : '德国', 
	'stt100077' : '西班牙', 
	'stt100078' : '意大利', 
	'stt100079' : '法国', 
	'stt100080' : '德国', 
	'stt100081' : '德国', 
	'stt100082' : '德国', 
	'stt100083' : '意大利', 
	'stt100084' : '德国', 
	'stt100085' : '奥地利', 
	'stt100086' : '比利时', 
	'stt100087' : '意大利', 
	'stt100088' : '意大利', 
	'stt100089' : '法国', 
	'stt100090' : '意大利', 
	'stt100091' : '意大利', 
	'stt100092' : '德国', 
	'stt100093' : '匈牙利', 
	'stt100094' : '法国', 
	'stt100095' : '法国', 
	'stt100096' : '西班牙', 
	'stt100097' : '意大利', 
	'stt100098' : '意大利', 
	'stt100099' : '法国', 
	'stt100100' : '德国', 
	'stt100101' : '意大利', 
	'stt100102' : '德国', 
	'stt100103' : '德国', 
	'stt100104' : '意大利', 
	'stt100105' : '荷兰', 
	'stt100106' : '法国', 
	'stt100107' : '英国', 
	'stt100108' : '瑞士', 
	'stt100109' : '西班牙', 
	'stt100110' : '英国', 
	'stt100111' : '德国', 
	'stt100112' : '瑞士', 
	'stt100113' : '比利时', 
	'stt100114' : '英国', 
	'stt100115' : '法国', 
	'stt100116' : '法国', 
	'stt100117' : '奥地利', 
	'stt100118' : '英国', 
	'stt100119' : '英国', 
	'stt100120' : '法国', 
	'stt100121' : '德国', 
	'stt100122' : '意大利', 
	'stt100123' : '比利时', 
	'stt100124' : '英国', 
	'stt100125' : '瑞士', 
	'stt100126' : '法国', 
	'stt100127' : '瑞士', 
	'stt100128' : '奥地利', 
	'stt100129' : '德国', 
	'stt100130' : '西班牙', 
	'stt100131' : '法国', 
	'stt100132' : '法国', 
	'stt100133' : '法国', 
	'stt100134' : '英国', 
	'stt100135' : '英国', 
	'stt100136' : '法国', 
	'stt100137' : '捷克', 
	'stt100138' : '法国', 
	'stt100139' : '德国', 
	'stt100140' : '波兰', 
	'stt100141' : '英国', 
	'stt100142' : '意大利', 
	'stt100143' : '英国', 
	'stt100144' : '意大利', 
	'stt100145' : '捷克', 
	'stt100146' : '法国', 
	'stt100147' : '意大利', 
	'stt100148' : '法国', 
	'stt100149' : '德国', 
	'stt100150' : '法国', 
	'stt100151' : '德国', 
	'stt100152' : '英国', 
	'stt100153' : '英国', 
	'stt100154' : '英国', 
	'stt100155' : '比利时', 
	'stt100156' : '意大利', 
	'stt100157' : '意大利', 
	'stt100158' : '奥地利', 
	'stt100159' : '英国', 
	'stt100160' : '德国', 
	'stt100161' : '意大利', 
	'stt100162' : '德国', 
	'stt100163' : '法国', 
	'stt100164' : '葡萄牙', 
	'stt100165' : '德国', 
	'stt100166' : '英国', 
	'stt100167' : '意大利', 
	'stt100168' : '法国', 
	'stt100169' : '意大利', 
	'stt100170' : '捷克', 
	'stt100171' : '比利时', 
	'stt100172' : '法国', 
	'stt100173' : '英国', 
	'stt100174' : '瑞士', 
	'stt100175' : '德国', 
	'stt100176' : '英国', 
	'stt100177' : '俄罗斯', 
	'stt100178' : '瑞士', 
	'stt100179' : '法国', 
	'stt100180' : '瑞士', 
	'stt100181' : '法国', 
	'stt100182' : '德国', 
	'stt100183' : '英国', 
	'stt100184' : '德国', 
	'stt100185' : '德国', 
	'stt100186' : '德国', 
	'stt100187' : '西班牙', 
	'stt100188' : '西班牙', 
	'stt100189' : '西班牙', 
	'stt100190' : '意大利', 
	'stt100191' : '瑞士', 
	'stt100192' : '英国', 
	'stt100193' : '奥地利', 
	'stt100194' : '英国', 
	'stt100195' : '德国', 
	'stt100196' : '法国', 
	'stt100197' : '瑞士', 
	'stt100198' : '德国', 
	'stt100199' : '德国', 
	'stt100200' : '德国', 
	'stt100201' : '德国', 
	'stt100202' : '英国', 
	'stt100203' : '法国', 
	'stt100204' : '瑞典', 
	'stt100205' : '法国', 
	'stt100206' : '德国', 
	'stt100207' : '德国', 
	'stt100208' : '瑞士', 
	'stt100209' : '英国', 
	'stt100210' : '英国', 
	'stt100211' : '瑞士', 
	'stt100212' : '英国', 
	'stt100213' : '挪威', 
	'stt100214' : '葡萄牙', 
	'stt100215' : '英国', 
	'stt100216' : '德国', 
	'stt100217' : '英国', 
	'stt100218' : '英国', 
	'stt100219' : '法国', 
	'stt100220' : '西班牙', 
	'stt100221' : '意大利', 
	'stt100222' : '葡萄牙', 
	'stt100223' : '英国', 
	'stt100224' : '英国', 
	'stt100225' : '英国', 
	'stt100226' : '荷兰', 
	'stt100227' : '德国', 
	'stt100228' : '德国', 
	'stt100229' : '西班牙', 
	'stt100230' : '法国', 
	'stt100231' : '西班牙', 
	'stt100232' : '卢森堡', 
	'stt100233' : '法国', 
	'stt100234' : '捷克', 
	'stt100235' : '荷兰', 
	'stt100236' : '荷兰', 
	'stt100237' : '英国', 
	'stt100238' : '瑞士', 
	'stt100239' : '捷克', 
	'stt100240' : '波兰', 
	'stt100241' : '瑞士', 
	'stt100242' : '英国', 
	'stt100243' : '奥地利', 
	'stt100244' : '德国', 
	'stt100245' : '瑞士', 
	'stt100246' : '奥地利', 
	'stt100247' : '英国', 
	'stt100248' : '法国', 
	'stt100249' : '意大利', 
	'stt100250' : '德国', 
	'stt100251' : '波兰', 
	'stt100252' : '西班牙', 
	'stt100253' : '英国', 
	'stt100254' : '德国', 
	'stt100255' : '荷兰', 
	'stt100256' : '英国', 
	'stt100257' : '意大利', 
	'stt100258' : '挪威', 
	'stt100259' : '德国', 
	'stt100260' : '法国', 
	'stt100261' : '瑞士', 
	'stt100262' : '法国', 
	'stt100263' : '德国', 
	'stt100264' : '捷克', 
	'stt100265' : '瑞士', 
	'stt100266' : '法国', 
	'stt100267' : '法国', 
	'stt100268' : '奥地利', 
	'stt100269' : '法国', 
	'stt100270' : '瑞士', 
	'stt100271' : '荷兰', 
	'stt100272' : '英国', 
	'stt100273' : '奥地利', 
	'stt100274' : '瑞士', 
	'stt100275' : '葡萄牙', 
	'stt100276' : '德国', 
	'stt100277' : '奥地利', 
	'stt100278' : '英国', 
	'stt100279' : '德国', 
	'stt100280' : '英国', 
	'stt100281' : '德国', 
	'stt100282' : '法国', 
	'stt100283' : '德国', 
	'stt100284' : '英国', 
	'stt100285' : '德国', 
	'stt100286' : '法国', 
	'stt100287' : '法国', 
	'stt100288' : '芬兰', 
	'stt100289' : '西班牙', 
	'stt100290' : '西班牙', 
	'stt100291' : '奥地利', 
	'stt100292' : '俄罗斯', 
	'stt100293' : '德国', 
	'stt100294' : '德国', 
	'stt100295' : '德国', 
	'stt100296' : '英国', 
	'stt100297' : '英国', 
	'stt100298' : '英国', 
	'stt100299' : '英国', 
	'stt100300' : '英国', 
	'stt100301' : '捷克', 
	'stt100302' : '瑞士', 
	'stt100303' : '德国', 
	'stt100304' : '德国', 
	'stt100305' : '比利时', 
	'stt100306' : '英国', 
	'stt100307' : '法国', 
	'stt100308' : '法国', 
	'stt100309' : '德国', 
	'stt100310' : '德国', 
	'stt100311' : '德国', 
	'stt100312' : '英国', 
	'stt100313' : '瑞士', 
	'stt100314' : '德国', 
	'stt100315' : '英国', 
	'stt100316' : '瑞士', 
	'stt100317' : '法国', 
	'stt100318' : '法国', 
	'stt100319' : '英国', 
	'stt100320' : '德国', 
	'stt100321' : '英国', 
	'stt100322' : '法国', 
	'stt100323' : '德国', 
	'stt100324' : '德国', 
	'stt100325' : '德国', 
	'stt100326' : '英国', 
	'stt100327' : '法国'
	}


def get_time_zone(para_type, params, current_time):
	para_list = ['airport', 'city', 'station']

	failed_tag = -100

	para_type = para_type.lower()

	if para_type not in para_list:
		print para_type
		print 'Wrong para type (airport, city or station)'
		return failed_tag

	if para_type == 'airport':
		try:
			country_name = Airport[params]['country'].encode('utf-8')
		except Exception, e:
			print 'Wrong airport :' + params + str(e)

	elif para_type == 'city':
		try:
			country_name = City[params]['country'].encode('utf-8')
		except Exception, e:
			print 'Wrong city name: ' + params + str(e)

	elif para_type == 'station':
		try:
			country_name = Station[params].encode('utf-8')
			current_time = current_time.replace(' ','T')
		except Exception, e:
			print 'Wrong station id : ' + params + str(e)


	try:
		country_info = TimeZone[country_name]
	except Exception, e:
		print 'Get country_name failed!'
		return failed_tag
	try:
		year_start_sec = int(time.mktime(time.strptime('2014-1-1T0:00:00','%Y-%m-%dT%H:%M:%S')))
		year_end_sec = int(time.mktime(time.strptime('2014-12-31T23:59:59','%Y-%m-%dT%H:%M:%S')))

		summer_start = country_info['summer_start']
		summer_end = country_info['summer_end']
		summer_start_sec = int(time.mktime(time.strptime(summer_start,'%Y-%m-%dT%H:%M:%S')))
		summer_end_sec = int(time.mktime(time.strptime(summer_end,'%Y-%m-%dT%H:%M:%S')))

		current_time_sec = int(time.mktime(time.strptime(current_time,'%Y-%m-%dT%H:%M:%S')))
		
		if (current_time_sec > summer_start_sec) and (current_time_sec < summer_end_sec) :
			timezone = int(country_info['summer'])
		elif (current_time_sec > year_start_sec and current_time_sec < summer_start_sec) or (current_time_sec > summer_end_sec and current_time_sec < year_end_sec):
			timezone = int(country_info['standard'])
		elif (current_time_sec > year_end_sec):
			timezone = int(country_info['standard'])
		else:
			timezone = failed_tag
		return timezone
	except Exception, e:
		print 'Wrong Time Format: ' + current_time
		print str(e)
		return failed_tag


def get_timezone(city_id, current_time):
	failed_tag = -100
	try:
		country_name = City[city_id]['country']
		city_info = TimeZone[country_name]
	except:
		print 'Wrong City ID: ' + city_id
		return failed_tag

	try:
		year_start_sec = int(time.mktime(time.strptime('2014-1-1T0:00:00','%Y-%m-%dT%H:%M:%S')))
		year_end_sec = int(time.mktime(time.strptime('2014-12-31T23:59:59','%Y-%m-%dT%H:%M:%S')))

		summer_start = city_info['summer_start']
		summer_end = city_info['summer_end']
		summer_start_sec = int(time.mktime(time.strptime(summer_start,'%Y-%m-%dT%H:%M:%S')))
		summer_end_sec = int(time.mktime(time.strptime(summer_end,'%Y-%m-%dT%H:%M:%S')))

		current_time_sec = int(time.mktime(time.strptime(current_time,'%Y-%m-%dT%H:%M:%S')))

		if current_time_sec > summer_start_sec and current_time_sec < summer_end_sec:
			timezone = int(city_info['summer'])
		elif (current_time_sec > year_start_sec and current_time_sec < summer_start_sec) or \
			(current_time_sec > summer_end_sec and current_time_sec < year_end_sec):
			timezone = int(city_info['standard'])
		elif (current_time_sec > year_end_sec):
			timezone = int(country_info['standard'])
		else:
			timezone = failed_tag
		return timezone
	except Exception, e:
		print 'Wrong Time Format: ' + current_time
		print str(e)
		return failed_tag


if __name__ == '__main__':
	print get_time_zone('station', 'stt100325', '2014-09-14T08:19:00')
	print get_time_zone('city', 'PAR', '2014-09-14T08:19:00')
	print get_time_zone('airport', 'CDG', '2014-09-14T08:19:00')
	print get_timezone('LON', '2014-09-14T08:19:00')
