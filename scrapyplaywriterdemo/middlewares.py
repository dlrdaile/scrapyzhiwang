# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import Request
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import requests
import json
import logging
from aiohttp.client import ClientSession


class AddCookieDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    accountpool_url = 'http://localhost:6789/bit_vpn/random'
    logger = logging.getLogger('middlewares.authorization')

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # res = requests.get('http://127.0.0.1:6789/bit_vpn/random')
        # data = res.json()
        # if data['status_code'] == 200:
        #     cls.cookie = json.loads(data['data'])
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    async def process_request(self, request: Request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        async with ClientSession() as client:
            response = await client.get(self.accountpool_url)
            if response.status != 200:
                logging.info('can not get a valid account')
                return
            data = await response.text()
            request.cookies = json.loads(json.loads(data)['data'])
        # if hasattr(self, 'cookie'):
        #     request.cookies = self.cookie
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # proxypool_url = 'http://localhost:5555/random'
    proxypool_url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=1&pack=285296&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
    logger = logging.getLogger('middlewares.proxy')

    async def process_request(self, request, spider):
        if request.meta.get('file_type', None):
            try:
                async with ClientSession() as client:
                    response = await client.get(self.proxypool_url)
                    if not response.status == 200:
                        logging.info('can not get a valid proxy')
                        return
                    data = await response.text()
                    ip = json.loads(data)['data'][0]['ip']
                    port = json.loads(data)['data'][0]['port']
                    proxy = f"{ip}:{port}"
                    self.logger.debug(f'set proxy {proxy}')
                    request.meta['proxy'] = f'http://{proxy}'
            except IndexError as e:
                pass

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
