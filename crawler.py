# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import datetime
import urllib
import model

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flight_list import flight_list_lite

def crawler(from_place, to_place):
    for i in range(5):
        context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=' + from_place + '-' + to_place)
        break
    except:
        time.sleep(4)
    tree = etree.parse(context)
    root = tree.getroot()

    for node in root[0][1:]:
        go_date = datetime.datetime.strptime(node.attrib['date'], "%Y-%m-%d").date()
        book_date = datetime.datetime.now().date()
        price = int(node[0].attrib['price'])
        e = model.flight(from_place = from_place, to_place = to_place, go_date = go_date, book_date = book_date, price = price)
        e.put()

    return True 
        
def autocrawl():
    date = datetime.datetime.now().date()
    log = ""

    for (from_place, to_place) in flight_list_lite:
        if (crawler(from_place, to_place)):
            log = log + '<li>'  +  from_place + '  ' + to_place + '  done</li>'
    
    e = model.logs(date = date, log = log)
    e.put()
    return True

if __name__ == '__main__':
    autocrawl()
