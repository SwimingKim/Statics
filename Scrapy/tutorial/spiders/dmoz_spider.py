import scrapy
from tutorial.items import DmozItem

class DmozScrapy(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response) :
        """
        HTML파일 긁어오기
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)
        """
        for sel in response.xpath('//ul/li'):
            items = DmozItem()
            items['title'] = sel.xpath('a/text()').extract()
            items['link'] = sel.xpath('a/@href').extract()
            items['desc'] = sel.xpath('text()').extract()
            # print (title, link, desc)
            yield items
