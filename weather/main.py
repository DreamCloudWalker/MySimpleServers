# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/weather', 'Handle',
)
app = web.application(urls, globals())

application = app.wsgifunc()
#if __name__ == '__main__':
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    # app.run()