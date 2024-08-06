import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://google.com']

    def parse(self, response):
        # Step 4: Extract data
        title = response.xpath('//title/text()').get()
        yield {'title': title}

        # Example: Extracting all paragraphs
        paragraphs = response.xpath('//p/text()').getall()
        for paragraph in paragraphs:
            yield {'paragraph': paragraph}
