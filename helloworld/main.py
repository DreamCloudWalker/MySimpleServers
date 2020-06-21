# -*- coding: utf-8 -*-
# filename: main.py
# test by http://127.0.0.1:8080/helloworld
import web

urls = (    # urls是一个元组变量，成员必须成对出现，奇数元素表示url，其后的元素表示对应的处理类
    '/helloworld', 'HelloWorld',
)


class HelloWorld(object):
    def GET(self):
        return 'Hello World'


# 本地调试
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
