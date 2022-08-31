import scrapy
from scrapy import Request

from aQuanLiang.items import AquanliangItem


class AquanliangSpider(scrapy.Spider):
    name = 'aquanliang'
    # allowed_domains = ['www.aquanliang.com']
    start_urls = ['https://www.aquanliang.com/blog']
    baseUrl = 'https://www.aquanliang.com/blog/page/%d'
    offset = 1

    def parse(self, response):
        spanList = response.xpath('//div[@class="_1ySUUwWwmubujD8B44ZDzy"]/span')
        # print(len(spanList))
        for span in spanList:
            item = AquanliangItem()
            item['title'] = span.xpath('./div/div/a/div/text()').extract_first()
            item['publishTime'] = span.xpath('./div/div/div[2]/div[2]/text()').extract_first()
            item['readCounts'] = span.xpath('./div/div/div[2]/div[3]/text()').extract_first()
            item['cover'] = span.xpath('./div/a//img/@src').extract_first()
            yield item
        flag = response.xpath('//*[@id="__next"]/div/div[2]/section/main/section/div[2]/div[2]/ul/li[9]/a/@style').extract_first()
        if flag is None:
            self.offset += 1
            nextUrl = self.baseUrl % self.offset
            print(nextUrl)
            yield Request(nextUrl, callback=self.parse)
