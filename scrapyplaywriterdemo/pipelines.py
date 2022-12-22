# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.media import MediaPipeline
import hashlib
from scrapy.http import Request, JsonRequest, HtmlResponse
from os.path import splitext
from scrapyplaywriterdemo.items import DownloadFileItem
# from scrapy.utils.log import log
import logging
from urllib.parse import parse_qs


class FileDownloadPipeline(FilesPipeline):
    @classmethod
    def from_crawler(cls, crawler):
        cls.logger = logging.getLogger(__name__)
        cls.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'show_vpn=0; show_faq=0; wengine_vpn_ticketwebvpn_bit_edu_cn=071bf5666d6d0add; refresh=0',
            'Referer': 'https://webvpn.bit.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFD2011&filename=GWDZ201124021&uniplatform=NZKPT&v=Rz9srhnqvbS4Yibak0tuT9keINrEQ6yJBgRVwno5_0tDHDQkoirFfCNOEBBp8P54',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        try:
            pipe = cls.from_settings(crawler.settings)
        except AttributeError:
            pipe = cls()
        pipe.crawler = crawler
        pipe._fingerprinter = crawler.request_fingerprinter
        return pipe

    def file_path(self, request: Request, response=None, info=None, *, item=None):
        extention = request.meta['file_type']
        keyWord = item['search_keyWord']
        paper_name = item['paper_name']
        paper_id = item['paper_id']
        file_name = f'{keyWord}/{paper_name}_{paper_id}.{extention}'
        return file_name

    # def file_downloaded(self, response, request, info, *, item=None):

    def item_completed(self, results, item, info):
        files_paths = [x['path'] for ok, x in results if ok]
        if not files_paths:
            raise DropItem('Files Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        if isinstance(item, DownloadFileItem):
            self.header['Referer'] = item['response_url']
            if item['pdf_download_url']:
                yield Request(item['pdf_download_url'],
                              headers=self.header,
                              meta={
                                  'file_type': 'pdf',
                              })
            if item['caj_download_url']:
                yield Request(item['caj_download_url'],
                              headers=self.header,
                              meta={
                                  'file_type': 'caj',
                              })
