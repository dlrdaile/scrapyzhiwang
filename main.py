from scrapy import cmdline
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapyplaywriterdemo.spiders.zhiwang import BitZhiwangSpider
if __name__ == '__main__':
    # settings = get_project_settings()
    # configure_logging(settings)
    # runner = CrawlerRunner(settings)
    #
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(BitZhiwangSpider)
    #     # yield runner.crawl(MySpider2)
    #     reactor.stop()
    #
    # crawl()
    # reactor.run() # the script will block here until the last crawl call is finished
    spider_name = 'zhiwang'
    cmdline.execute(f'scrapy crawl {spider_name}'.split())