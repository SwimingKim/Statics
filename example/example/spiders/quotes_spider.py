import scrapy
from example.items import QuotesItem

class QuotesSpider(scrapy.Spider) :
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response) :
        for quote in response.css('div.quote') :
            myitem = QuotesItem()
            myitem['title'] = quote.css('span.text::text').extract_first()
            myitem['author'] = quote.css('small.text::text').extract_first()
            myitem['tags'] = quote.css('div.tags a.tag::text').extract()

            yield myitem
