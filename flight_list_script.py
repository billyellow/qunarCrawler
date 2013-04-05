# -*- coding:utf8 -*-

import xml.etree.ElementTree as etree
import urllib

city_list = [
'北京',
'上海',
'广州',
'深圳',
'成都',
'杭州',
'武汉',
'西安',
'重庆',
'青岛',
'长沙',
'南京',
'厦门',
'昆明',
'大连',
'天津',
'郑州',
'三亚',
'济南',
'福州'
]

flight_list = []

for a in city_list:
    for b in city_list:
        context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=' + a + '-' + b)
        tree = etree.parse(context)
        root = tree.getroot()
        node = root[0][1]
        if (node.attrib['go_start'] != ''):
            print "('" + a + "', '" + b + "'),"
