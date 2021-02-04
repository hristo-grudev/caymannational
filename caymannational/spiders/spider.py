import scrapy

from scrapy.loader import ItemLoader
from ..items import CaymannationalItem
from itemloaders.processors import TakeFirst


class CaymannationalSpider(scrapy.Spider):
	name = 'caymannational'
	start_urls = ['https://www.caymannational.im/news']

	def parse(self, response):
		post_links = response.xpath('//div[@class="col-sm-9 col-md-8"]/ul/li/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//ul[@class="pagination"]/li[@class="page-item next"]/a/@href')
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-sm-7 col-md-8"]/p//text()|//div[@class="col-sm-7 col-md-8"]/ul/li//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=CaymannationalItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
