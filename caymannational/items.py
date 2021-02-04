import scrapy


class CaymannationalItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
