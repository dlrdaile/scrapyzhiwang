# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PaperInfoItem(scrapy.Item):
    search_keyWord = Field()
    paper_id = Field()
    paper_name = Field()
    paper_detail_url = Field()
    source_journal = Field()
    source_database = Field()
    main_author_info = Field()
    other_author_info = Field()
    abstract = Field()
    key_words = Field()
    publish_date = Field()
    download_count = Field()
    quote_info = Field()


class AuthorInfoItem(scrapy.Item):
    author_name = Field()
    author_detail_url = Field()
    organization = Field()
    organization_detail_url = Field()


class DownloadFileItem(scrapy.Item):
    response_url = Field()
    search_keyWord = Field()
    paper_id = Field()
    paper_name = Field()
    pdf_download_url = Field()
    caj_download_url = Field()
    pass
