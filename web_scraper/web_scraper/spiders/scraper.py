import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"

    def __init__(self, file=None, *args, **kwargs):
        super(ScraperSpider, self).__init__(*args, **kwargs)
        if file:
            with open(file, 'r') as f:
                self.start_urls = [line.strip() for line in f.readlines()]

    def parse(self, response):
        # Extract text from body, excluding script and style tags
        all_text = response.xpath('//body//text()[not(ancestor::script) and not(ancestor::style)]').getall()
        content = ' '.join(text.strip() for text in all_text if text.strip())

        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'meta_description': response.css('meta[name="description"]::attr(content)').get(),
            'h1': response.css('h1::text').getall(),
            'h2': response.css('h2::text').getall(),
            'content': content,
        }

        for a_tag in response.css('a::attr(href)'):
            yield response.follow(a_tag, self.parse)
