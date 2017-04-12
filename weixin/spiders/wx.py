# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from weixin.items import WeixinItem

class WxSpider(scrapy.Spider):
    name = "wx"
    allowed_domains = ["sogou.com"]
    start_urls = ['http://sogou.com/']

    def parse(self, response,):

        key = 'python'
        # for i in range(1, 11):
        for i in range(3, 4):
            url = 'http://weixin.sogou.com/weixin?query=' + key + '&type=2&page=' + str(i)
            yield Request(url=url, callback=self.get_content)

    def get_content(self, response):
        print(response.text)
        lis = response.xpath('//div[@class="news-box"]//li')
        for li in lis:
            item = WeixinItem()
            s_title = ""
            box_title = li.xpath('.//div[@class="txt-box"]/h3/a//text()').extract()
            for tt in box_title:
                s_title = s_title + tt
            s_title = s_title.replace(' ', '').replace('\n', '')

            item['title'] = s_title
            box_url = li.xpath('.//div[@class="txt-box"]/h3/a/@href')[0].extract()

            item['link'] = box_url
            s_info = ""
            box_info = li.xpath('.//p[@class="txt-info"]//text()').extract()
            for ii in box_info:
                s_info = s_info + ii
            s_info = s_info.replace(' ', '').replace('\n', '')

            item['dec'] = s_info
            box_s_p = li.xpath('.//div[@class="txt-box"]/div[@class="s-p"]/a/text()')[0].extract()
            item['author'] = box_s_p
            print(item)
            yield item



