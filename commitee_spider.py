import scrapy

urls = []

for url in open('url.csv').readlines():
    urls.append(url.strip())


class CommiteeSpider(scrapy.Spider):
    name = 'commitee_spider'

    start_urls = urls

    def parse(self, response):
        for tr in response.css('.resultados tbody tr'):
            yield {
                'url': response.url,
                'nome': tr.css('td::text').getall()[0],
                'categoria': tr.css('td::text').getall()[1]
            }
