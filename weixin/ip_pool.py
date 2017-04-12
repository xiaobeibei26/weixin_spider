from _datetime import datetime,timedelta
from pymongo import MongoClient

class mogo_queue():
   
    def __init__(self,db,collection,timeout=60):
        self.client = MongoClient()
        self.database =self.client[db]#链接数据库
        self.db = self.database[collection]#链接数据库里面这个表
    def find_proxy(self):
        proxy_list = []  # 用来接收从数据库查找到的所有代理,返回包含代理的列表
        for i in self.db.find():
            proxy = i['proxy']
            proxy_list.append(proxy)
        return proxy_list