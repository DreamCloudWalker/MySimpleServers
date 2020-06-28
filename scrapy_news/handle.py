import json
import sys
import os
import pymysql
import datetime

pymysql.install_as_MySQLdb()


def crawl_news():
    results = []
    db = pymysql.connect(host='localhost', user='root', password='hanhun@001',
                         db='news_spider', port=3306, charset='utf8')
    cursor = db.cursor()
    try:
        num = cursor.execute('select * from article_info')
        if num <= 0:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            # execute(['scrapy', 'crawl', 'news_spider'])   # 方法1
            os.system('scrapy crawl news_spider')  # 方法2
            # subprocess.Popen('scrapy crawl news_spider')  # 方法3
            cursor.execute('select * from article_info')
            db.commit()
        # cursor.scroll(0, mode='absolute')
        # results = cursor.fetchall()
        desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        results = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来
        # print(results)
    except:
        print("Unexpected error:", sys.exc_info())
    finally:
        db.commit()
        cursor.close()
        db.close()
    return results


def format_data(crawl_results):
    result = {"reason": "success"}
    news_result = {"stat": "1"}
    news_result["data"] = crawl_results
    result["result"] = news_result
    return json.dumps(result, default=convert_time)


def convert_time(time):
    if isinstance(time, datetime.datetime):
        return time.__str__()


class Handle(object):
    def GET(self):
        crawl_results = crawl_news()
        ret = format_data(crawl_results)
        return ret

    def POST(self):  # TODO
        return 'post data'
