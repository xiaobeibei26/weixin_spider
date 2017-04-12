# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# from scrapy.conf import settings

class WeixinPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client['sougou']
        self.collection = self.db['sougou_weixin']

    def process_item(self, item, spider):

        self.collection.insert(dict(item))
        return item
