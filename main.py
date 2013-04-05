# -*- coding: utf-8 -*-
import web
import model

urls = (
    '/', 'index',
    '/crawl', 'crawl',
    '/log', 'log'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        i = web.input()
        if (i):
            res = model.select_flight(i.from_place, i.to_place, i.date, i.search_type)
        else:
            i = None
            res = None
        return render.index(res, i) 

class crawl:
    def GET(self):
        import crawler
        list = crawler.autocrawl()
        return "success"

class log:
    def GET(self):
        logs = model.get_log()
        return render.log(logs)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app = app.cgirun()

