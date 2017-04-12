import random
from .useragents import agents
from .ip_pool import mogo_queue#导入数据库代理池
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
class UserAgentmiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent

class ProxyMiddleware1(object):
    def __init__(self):
        # super(ProxyMiddleware1, self).__init__(settings)继承这里的坑以后再填吧
        #HttpProxyMiddleware.__init__(self, settings)
        '''类的重载这里我暂时调不好，老是报错，所以只好继承object了'''
        # self.ip_pools = [
        #     {'ip': '110.73.15.11:8123'},
        #     {'ip': '124.88.67.14:80'},
        #     {'ip': '42.81.58.198:80'},
        #     ]
        self.ip_lists = mogo_queue('ip_database', 'proxy_collection')#链接到数据库
        self.ip_pools = self.ip_lists.find_proxy()#获得数据库所有代理
    def process_request(self, request, spider):
        ip = random.choice(self.ip_pools)
        print('当前使用的ip：',ip)
        #request.meta['proxy'] = 'http://{}'.format(ip['ip'])
        request.meta['proxy'] = 'http://{}'.format(ip)









