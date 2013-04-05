# -*- coding:utf8 -*-

from google.appengine.ext import db

class flight(db.Model):
    from_place = db.StringProperty()
    to_place = db.StringProperty()
    go_date = db.DateProperty()
    book_date = db.DateProperty()
    price = db.IntegerProperty()

class logs(db.Model):
    date = db.DateProperty()
    log = db.StringProperty()

def select_flight(from_place, to_place, date, search_type): 
    query = "SELECT * FROM flight " + "WHERE  from_place = '" + from_place + "' AND to_place =  '" + to_place 

    if (search_type == "book"):
        query = query + "' AND go_date = DATE('" + date + "') ORDER BY book_date ASC"
    elif (search_type == "go"):
        query = query + "' AND book_date = DATE('" + date + "') ORDER BY go_date ASC"

    q = db.GqlQuery(query) 
                    
    return q.fetch(44, 0)

def get_log():
    q = logs.all()
    q.order('-date')
    return q.fetch(30, 0)
