import json
from scrapy import Selector
import scrapy
from scrapy.http import FormRequest, HtmlResponse, Request, JsonRequest
from copy import deepcopy
from scrapyplaywriterdemo.items import PaperInfoItem, AuthorInfoItem, DownloadFileItem
import time
from gerapy_playwright import PlaywrightRequest
from urllib.parse import parse_qs
from playwright.async_api import Page


class BitZhiwangSpider(scrapy.Spider):
    name = 'zhiwang'
    allowed_domains = ['www.cnki.net']
    # base_url = 'https://webvpn.bit.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8'
    index_url = 'https://kns.cnki.net/kns8/Brief/GetGridTableHtml'
    searchKeyWords = ['ai', '脑机接口']
    post_data = {
        'IsSearch': 'false',
        # 'QueryJson': '{"Platform":"","DBCode":"CFLS","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"ai","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
        # 'SearchSql': '0645419CC2F0B23BC604FFC82ADF67C6E920108EDAD48468E8156BA693E89F481391D6F5096D7FFF3585B29E8209A884EFDF8EF1B43B4C7232E120D4832CCC896D30C069E762ACAB990E5EBAAD03C09721B4573440249365A4157D3C93DC874963F6078A465F9A4E6BEED14E5FD119B250F0488206491CF1C7F670020480B48EE2FF3341B3B9C8A0A38F9913EF596174EDD44BBA8277DA2BE793C92DF83782297DE55F70BBF92D5397159D64D1D3DAC96FAD28213BD3E1912A5B4A4AD58E5965CBDBA01069691140F14FD0298FBD1F452C7779EFF17124633292E356C88367122976245AA928FA07D061C0E091BB1136031750CD76D7D64E9D75B7FBAB11CAA5B80183AC60BB0885D2C0A0938C7D1F849656014326473DCB797D5D273C845DAF7FCE49D21478E9B06B77ADE6253ACD4FE1D87EE31B4B2C94E071EE733B3A64EA6EE9CD5F222FCD3DA1D83D9133EF8C9BED9ED3E55DA15F3B4A37C85463B60D2F0BEA46FC7135898D7D93F63AF8B2246716E32B699238901588EE5D1DEF30A01DCE9957CF6934E8B11E273747F9A9BB8ADF535E5E76F6A9386CFBE605748C132DA05E2D31832199B0A4ECF170ACA47154423CF6BBD9607FC505765E95637F93DC865AA738F5EE92B26DB9AF56509A5FC96FF9C3A1720633EBDDC62EC2162E7D5349CAC851ED0AD4E36DCF6FE25EBEAB42BF931DBE3CF4ED1A7BB8FD887C3C33D86B768B0BA7267C4E0E7DEE53D0931F71F07AE13BAFC46034A444EC24C7EA8F0086FAD197A8D2F18C6CBC5DF48050AF8D4C84DE03B9A6F1DF928D63286B1C924B7EC3BA8C2591D60491F95D271F0E7F02AA2AA93C3888B8CCEBB0414BD7145AD15A3166DB4860F85BC476B1B193C219EAE52E33E6BBC9B3AAAD97196977B7DABA36C04093ED723AD874EC6480477C6412B0F589DE6CC7D959855E41265213DCBB4D91238716DF38BF78C951259572F8E5968FAC5C5CDC006DBE919EEB5E5518F51162FCE7CDE520F60093D333FBE121D3164C6D2451F6431FB7973C659E6A9D287B545EC044DE2CBE170F3627719F8418D44E17987CEC7A89B52CB5525AF795DA892475ABF871C3A5A5FCBC5B03EB9BEC8598C8ADD7A68984BBBEF1244DD90386C05756687AB9D87A0B521319C093C3EC0D5EBEFDAB5459E29F1DA03D4C25DE740BF9FA2BC07DD510386E3BBE89F10D45513E29C8CF904763E723CE4BF2928D4DC2A731DD53595E9AACED90679FCDDACED022ECD59D72600A736D555A8B76BFE4CCD861E6A7F5A219EBE9A228BD008928299DB999D18F9CDD2E57E8C03EDF236E62EDB17A1FE5B023CF6E5A11892A5FA17EE5CFE348CA290DC691987A535223133D8CA101E8ABF13EFCAD929635E090B3C6BB6838E33B7C78C1DBA274101A6584300EF8D38C983AD544264217F6793562D19715CD711295C5410C72E88A64BD23D9049E5DF15EA6B3EB4473C1DDEBB416459322FEF0CC61D894476DCD62569527BE23FB7F66DF3F5182ABF2472FB60039CA77218F356D7F82E4EBAAA4C6875B5BD4729C81A29BDF55ED223AA0DAB04E1B248524FC504711360C330186327A780D6487BA831ABE55AAE38E69A0FBEF89D560E7AA26B991966E4B644338863E80AD9D1ACAD459EA933644C5A0D2EA44AD17205AED3BE66AEC01F48BA032EEBD620E2713082FE8D31E4A05A34F18BD389587FA4D3A9DFBB8C16AEE9C5FA9E667BA12A07B757D82F7BB41AC8867D9947CCBA3BB26381EC6D0D3966338DB6FA3D1A61F99A978C3B5ED2B31B7C14D54A4F688C4925C8AF99CB3EE3C2C06C7D35AD891BF0CFC820529FD990F2FF319BE195B1AD23C1667031C072EB1964F8512BB779125E46773C01714FCF0E339AEB0C44FB91B896A7A95AF4F81EB49006B570BC03ECA7D8DA45679F3B46A7AE3B46ED8D319CED49A3A5881A37CD3770703BDF026ACEF7D8662F85AFDBDD36C540FD419E18F30EA0483D24350B7C34C43F3D0065F339EAC15749DF8849F3880378FEA4AD7CCBAA827C828A5CAF7D56E97A87A3FAEEAE136B35FB37E8CE0233D9AF8DEABD47BD5B36A1B42B995D4F96FE744A2E25E9B6107801CACCA0DDC2B7ED5BFD39F68AB2E2BB66AB8286061049F3B5FFE871FFA520A7C0EEE3DEDF417D078DF9013B5F525C84BE257C0E19D7818928D36ACF368B21B36FDA0541F68BEC55F16C4300222A4186510D6D60CC27081D6315297C056CA5E950694B13A35535329912B1947961CA16DAED1708E77040DCD6C57D2A5290760352E880AC682E33F6BC1FB4DC98DE0590C5F64054DDA83A03DEC4CF13327CE8486BE653E88364331E034C6C090AA3F73CC5B1BC018775DF40043E5DE1B6E96CE7054F6EE308127DAB0229252F58284A55B9C7AFA5F0A4717CC4F3D5F826381FBE4FA4F77AC75FFA6A98BA51989F485B0812B143ADFF7F2D5AF39C5379AF16D797C7255CBD0D2FC3612A80F6D9A33DDB106C4C85843B9ECD514ECD4AB760C4E007843660CD1813E3E7ECFC6D5141EDA6394CEFE74FF821A529CBF431CE81AF039A991B413927B68B3E0B22924C377D38BD301B559E31C4350920462839F217DE6DEE37B74A974EA231F9F966EB300BFE09B99FD9C6D6E9BA9B493C017D0ADCD18A7CDE3265511DE7BF7848A13AA9C464A8077A0F4F717C6CE96D66559649C348BD09D7E0AAEFB7FC6698660A7D80D82C0AF2101DEA7AE5FA3B7E15AA3F352E2E65136E01DEC871E46A15D1BF77C8703ABCF2A2AE3892BE9EB8125B56D254C30DBA828172B77ACAFD26427132E9CBF8B3F4BAC3D176F3BA73F0A858924D26D180CB7EFF29515B42681DA2FE053B9BE1124D186DDC96E9F48CF82999C0F9D02E169AAD6C68B67F13D69EECBF864A446C5DA559521D2E0F22C0BFCCA0E9F06EB617DD2BA2F2A5987B4507D9056F4BDA4749D1126CD52AC0FD5584A5A30844599A7DFF73033C20CFC50CB96B39BD3E528FA296F398973C53EE1',
        'PageName': 'defaultresult',
        # 'HandlerId': '35',
        'DBCode': 'CFLS',
        'KuaKuCodes': 'CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD',
        # 'CurPage': '1',
        'RecordsCntPerPage': '50',
        'CurDisplayMode': 'custommode',
        'CurrSortField': 'CITY',
        'CurrSortFieldType': 'desc',
        'IsSortSearch': 'true',
        'IsSentenceSearch': 'false',
        'Subject': '',
    }
    QueryJson = {"Platform": "", "DBCode": "CFLS",
                 "KuaKuCode": "CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD",
                 "QNode": {
                     "QGroup": [{"Key": "Subject", "Title": "", "Logic": 1,
                                 "Items": [{"Title": "主题", "Name": "SU", "Value": "", "Operate": "%=",
                                            "BlurType": ""}],
                                 "ChildItems": []}]}}
    sortField = ['DOWNLOAD', 'CITY', 'ALL', 'PT', 'RELEVANT']
    post_data_dict = {}
    isDown = False

    def get_post_data(self, searchKeyWord, CurPage):
        QueryJson = deepcopy(self.QueryJson)
        post_data = deepcopy(self.post_data)
        QueryJson['QNode']['QGroup'][0]['Items'][0]['Value'] = searchKeyWord
        post_data['QueryJson'] = json.dumps(QueryJson)
        post_data['CurPage'] = str(CurPage)
        return post_data

    def start_requests(self):
        for searchKeyWord in self.searchKeyWords:
            self.post_data_dict[searchKeyWord] = self.get_post_data(searchKeyWord, 1)
            yield FormRequest(self.index_url, dont_filter=True,
                              callback=self.parse_index,
                              formdata=self.post_data_dict[searchKeyWord],
                              # headers=self.headers,
                              meta={'keyWord': searchKeyWord}
                              )

    def parse_index(self, response: HtmlResponse, **kwargs):
        page_num = response.xpath('//*[@id="countPageDiv"]/span[2]/text()').extract_first().split('/')[1]
        print(response.meta['keyWord'], page_num)
        self.post_data_dict[response.meta['keyWord']]['IsSortSearch'] = 'false'
        self.post_data_dict[response.meta['keyWord']]['SearchSql'] = response.xpath(
            '//*[@id="sqlVal"]/@value').extract_first()
        for page_id in range(2, 1 + min(2, int(page_num))):
            self.post_data_dict[response.meta['keyWord']]['CurPage'] = str(page_id)
            yield FormRequest(self.index_url, dont_filter=True,
                              callback=self.parse_detail,
                              formdata=self.post_data_dict[response.meta['keyWord']],
                              meta=response.meta
                              )
        yield from self.parse_detail(response, **kwargs)

    @staticmethod
    def strip_str(s:str):
        return s.strip()

    def parse_detail(self, response: HtmlResponse, **kwargs):
        dds: list[Selector] = response.xpath('//*[@id="gridTable"]/dl/dd')
        # meta: dict = deepcopy(response.meta)
        for dd in dds:
            item = PaperInfoItem()
            middle = dd.css('.middle')
            item['paper_id'] = dd.xpath('./div[@class="seq"]/input/@value').extract_first()
            item['paper_name'] = ''.join(map(self.strip_str,middle.xpath('.//h6/a//text()').extract()))
            item['paper_detail_url'] = middle.xpath('.//h6/a/@href').extract_first()
            # meta.update({'paper_id': item['paper_id'],
            #              'paper_name': item['paper_name']})
            # yield Request(self.base_url + item['paper_detail_url'], callback=self.parse_download, meta=meta)

            item['source_database'] = []

            for database_info in middle.xpath('.//h6/b'):
                item['source_database'].append({
                    'breif_name': database_info.xpath('./text()').extract_first(),
                    'complete_name': database_info.xpath('./@title').extract_first()
                })

            base_info = middle.css('.baseinfo')
            item['source_journal'] = {
                'name': base_info.xpath('./span[1]/a/text()').extract_first(),
                'url': base_info.xpath('./span[1]/a/@href').extract_first(),
            }
            item['publish_date'] = base_info.xpath('./span[@class="date"]/text()').extract_first()
            item['download_count'] = base_info.xpath('.//a[@class="downloadCnt"]/em/text()').extract_first()
            item['quote_info'] = {
                'quote_count': base_info.xpath('.//a[@class="KnowledgeNetLink"]/em/text()').extract_first(),
                'quote_paper_info_url': base_info.xpath('.//a[@class="KnowledgeNetLink"]/@href').extract_first(),
            }
            # main_author = middle.xpath('.//div[@class="authorinfo"]/p')
            # main_author_item = AuthorInfoItem()
            # main_author_item['author_name'] = middle.css('.authorinfo p').xpath('./a/text()').extract_first(),
            # main_author_item['author_detail_url'] = middle.xpath(
            #     './/div[@class="authorinfo"]/p/a/@href').extract_first(),
            # main_author_item['organization'] = middle.xpath('.//div[@class="authorinfo"]/p/span/a/text()').extract(),
            # main_author_item['organization_detail_url'] = middle.xpath(
            #     './/div[@class="authorinfo"]/p/span/a/@href').extract(),
            # item['main_author_info'] = dict(main_author_item)
            item['main_author_info'] = {
                'author_name': middle.css('.authorinfo p').xpath('./a/text()').extract_first(),
                'author_detail_url': middle.xpath('.//div[@class="authorinfo"]/p/a/@href').extract_first(),
                'organization': middle.xpath('.//div[@class="authorinfo"]/p/span/a/text()').extract(),
                'organization_detail_url': middle.xpath('.//div[@class="authorinfo"]/p/span/a/@href').extract(),
            }
            other_autho_info = middle.css('.otherAuthorinfos')

            item['other_author_info'] = []
            for other_author in other_autho_info.xpath('./p'):
                # other_author_item = AuthorInfoItem()
                # other_author_item['author_name'] = other_author.xpath('./a/text()').extract_first(),
                # other_author_item['author_detail_url'] = other_author.xpath('./a/@href').extract_first(),
                # other_author_item['organization'] = other_author.xpath('./span/a/text()').extract(),
                # other_author_item['organization_detail_url'] = other_author.xpath('./span/a/@href').extract(),
                # item['other_author_info'].append(dict(other_author_item))
                item['other_author_info'].append({
                    'author_name': other_author.xpath('./a/text()').extract_first(),
                    'author_detail_url': other_author.xpath('./a/@href').extract_first(),
                    'organization': other_author.xpath('./span/a/text()').extract(),
                    'organization_detail_url': other_author.xpath('./span/a/@href').extract(),
                })
            item['abstract'] = ''.join(middle.css('.abstract').xpath('./text() | ./font/text()').extract()).strip()
            item['key_words'] = middle.css('.keywords').xpath('./a/text()').extract()
            item['search_keyWord'] = response.meta['keyWord']
            yield item

    # def parse_download(self, response: HtmlResponse, **kwargs):
    #     downloadItem = DownloadFileItem()
    #     downloadItem['response_url'] = response.url
    #     downloadItem['paper_id'] = response.meta['paper_id']
    #     downloadItem['paper_name'] = response.meta['paper_name']
    #     downloadItem['pdf_download_url'] = response.urljoin(response.css('#pdfDown::attr(href)').extract_first())
    #     downloadItem['caj_download_url'] = response.urljoin(response.css('#cajDown::attr(href)').extract_first())
    #     downloadItem['search_keyWord'] = response.meta['keyWord']
    #     yield downloadItem

        # yield PlaywrightRequest(response.url, callback=self.parse_active, wait_until='networkidle',
        #                         dont_filter=True, priority=1, meta=response.meta, actions=self.img_action)

    # async def img_action(self, page: Page,**kwargs):
    #     if page.url.find('code') != -1:
    #         print(1)
    #         pass
    #     pass
    #
    # def parse_active(self, response: HtmlResponse, **kwargs):
    #     downloadItem = DownloadFileItem()
    #     downloadItem['response_url'] = response.url
    #     downloadItem['paper_id'] = response.meta['paper_id']
    #     downloadItem['paper_name'] = response.meta['paper_name']
    #     downloadItem['pdf_download_url'] = response.urljoin(response.css('#pdfDown::attr(href)').extract_first())
    #     downloadItem['caj_download_url'] = response.urljoin(response.css('#cajDown::attr(href)').extract_first())
    #     downloadItem['search_keyWord'] = response.meta['keyWord']
    #     yield downloadItem
