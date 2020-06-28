# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import pymysql
import datetime
import sys


class ScrapyNewsPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='hanhun@001',
                                       db='news_spider', port=3306, charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        try:
            # last_id = self.cursor.lastrowid
            self.cursor.execute(
                'INSERT INTO news_spider.article_info(source, title, url, remark, date, create_time)'
                'VALUES("{}","{}","{}","{}","{}","{}")'.format(item['source'],
                                                               item['title'],
                                                               item['url'],
                                                               item['remark'],
                                                               datetime.datetime.now().strftime("%Y-%m-%d"),
                                                               datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
            self.connect.commit()
        except :
            print("Unexpected error:", sys.exc_info())
            # self.cursor.execute('rollback;')
            self.connect.rollback()
        return item
        # 关闭数据库

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
