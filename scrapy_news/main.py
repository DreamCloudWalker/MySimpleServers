# coding: utf-8
import web
from handle import Handle
from scrapy.cmdline import execute
import sys
import os

urls = (    # urls是一个元组变量，成员必须成对出现，奇数元素表示url，其后的元素表示对应的处理类
    '/news', 'Handle',
)

# 线上部署，web.py提供了WSGI支持，可以将其架设在apache等web服务器之上
# app = web.application(urls, globals())
# application = app.wsgifunc()

# 本地调试, http://127.0.0.1:8080/news
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# 本地调试直接运行scrapy_news
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'news_spider'])   # 方法1

# if __name__ == '__main__':
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    # app.run()

