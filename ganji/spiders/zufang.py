import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GanjiItem


class ZufangSpider(CrawlSpider):
    name = "zufang"
    allow_domains = ["ganji.com"]
    start_urls = ["http://sh.ganji.com/fang1/"]
    rules = (Rule(LinkExtractor(allow=(r'http://sh.ganji.com/fang1/o\d+')),
                  callback='parse_content', follow=True),)

    def parse_content(self, response):
        ganj = GanjiItem()
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        price_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        time.sleep(10)
        for i, j in zip(title_list, price_list):
            ganj["title"] = i
            ganj["price"] = j
            yield ganj

