# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GanjiPipeline(object):

    def __init__(self):
        self.db = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            db = "test",
            user = "root",
            passwd = "password",
            charset = "utf8",
            use_unicode = True
        )

    # def open_spider(self, spider):
    #     self.db = pymysql.connect(
    #         server = "127.0.0.1:3306",
    #         database = "test",
    #         charset = "utf8"
    #     )
    #
    # def close_spider(self, spider):
    #     self.db.close()

    def process_item(self, item, spider):
        print self.db
        cursor = self.db.cursor()
        sql = "insert into shanghai_zufang (title, price) values (%s,%s)"
        print item['title'], item['price']
        cursor.execute(sql, (item['title'].encode("utf8"), item['price'].encode("utf8")))
        self.db.commit()
        return item

