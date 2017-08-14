#-*- coding:utf-8 -*-
# __author__ :'YQ'

import urllib2
import ssl
import json
from cons import cons

ssl._create_default_https_context = ssl._create_stdlib_context#跳过证书认证
station_dict = {}
for i in cons.split('@'):
    if i :
        tmp_list = i.split('|')
        station_dict[tmp_list[1]] = tmp_list[2]

#print station_dict['北京']
train_date = '2017-07-20'
from_station = station_dict['长沙']
to_station = station_dict['成都']

def getList():
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(train_date,from_station,to_station))

    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36')
    html = urllib2.urlopen(req).read()
    dict = json.loads(html)#将dict转换为标准的json
    return dict['data']['result']

cs = 0
# 软卧 = 23
# 车次 = 3
# 出发时间 = 8
# 到达时间 = 9
# 历时 = 10
# 硬卧 = 28
for i in getList():
    tmp_list = i.split('|')
    if tmp_list == u'无' or tmp_list == '--':
        continue
    if int(tmp_list[23])>0:
        print str(tmp_list[3]) + ' 软卧有票'
    break
    pass


