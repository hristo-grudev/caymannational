BOT_NAME = 'caymannational'

SPIDER_MODULES = ['caymannational.spiders']
NEWSPIDER_MODULE = 'caymannational.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'caymannational.pipelines.CaymannationalPipeline': 100,

}