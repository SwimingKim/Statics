import scrapy
from crawltest.items import DmozItem

class QuotesSpider(scrapy.Spider) :
    name = 'quotes'
"""
""" 첫번째 """
    def start_requests(self) :
        urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2',
        ]
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response) :
        page = response.url.split('/')[-2]
        filename = 'quotes-%s' % page
        with open(filename, 'wb') as f :
            f.write(response.body)
        self.log('saved file %s' % filename)
""" 두번째 """
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        'http://quotes.toscrape.com/page/2',
    ]

    def parse(self, response) :
        page = response.url.split('/')[-2]
        filename = 'quotes-%s' % page
        with open(filename, 'wb') as f :
            f.write(response.body)
        self.log('saved file %s' % filename)
""" 세번째 """
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        'http://quotes.toscrape.com/page/2',
    ]

    def parse(self, response) :
        for quote in response.css('div.quote') :
            yield {
                'text' : quote.css('span.text::text').extract_first()
                'author' : quote.css('small.author::text').extract_first()
                'tags' : quote.css('div.tags a.tag::text').extract()
            }
"""


""" 네번째 """
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        'http://quotes.toscrape.com/page/2',
    ]

    def parse(self, response) :
        for quoto in response.css('div.quote') :
            myitem = DmozItem()
            myitem['text'] = quoto.css('span.text::text').extract_first(),
            myitem['author'] = quoto.css('small.author::text').extract_first(),
            myitem['tags'] = quoto.css('div.tags a.tag::text').extract(),
            yield myitem
