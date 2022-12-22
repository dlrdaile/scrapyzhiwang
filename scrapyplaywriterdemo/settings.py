# Scrapy settings for scrapyplaywriterdemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyplaywriterdemo'

SPIDER_MODULES = ['scrapyplaywriterdemo.spiders']
NEWSPIDER_MODULE = 'scrapyplaywriterdemo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapyplaywriterdemo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10
RETRY_HTTP_CODES = [401, 403, 500, 502, 503, 504]
RETRY_TIMES = 10
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Ecp_ClientId=c221102210202888974; Ecp_loginuserbk=K10083; knsLeftGroupSelectItem=1%3B2%3B; Ecp_ClientIp=211.68.5.48; _pk_ref=%5B%22%22%2C%22%22%2C1671680232%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; _pk_id=88a63a3d-6c2c-4db1-9725-18b14e969710.1667394169.3.1671680232.1671680232.; _pk_ses=*; Ecp_IpLoginFail=221222113.12.27.135; SID_kns_new=kns25128007; ASP.NET_SessionId=ug2l3ix3bzfd4ygfftsj4y4f; SID_kns8=123148; dblang=ch; CurrSortField=%e7%9b%b8%e5%85%b3%e5%ba%a6%2frelevant%2c(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27time%27)+desc; CurrSortFieldType=desc',
    'Origin': 'https://kns.cnki.net',
    'Referer': 'https://kns.cnki.net/kns8/defaultresult/index',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapyplaywriterdemo.middlewares.ScrapyplaywriterdemoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    # 'gerapy_playwright.downloadermiddlewares.PlaywrightMiddleware': 543,
    # 'scrapyplaywriterdemo.middlewares.AddCookieDownloaderMiddleware': 500,
    # 'scrapyplaywriterdemo.middlewares.ProxyDownloaderMiddleware': 501,
}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy.pipelines.files.FileDownloadPipeline': 1,
    # 'scrapyplaywriterdemo.pipelines.FileDownloadPipeline': 300,
}
# FILES_STORE = './files'
# MEDIA_ALLOW_REDIRECTS = True
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# LOG_LEVEL = "INFO"
# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

# playwright config
# playwright timeout
GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT = 30
GERAPY_PLAYWRIGHT_HEADLESS = False

# Proxy
# GERAPY_PLAYWRIGHT_PROXY = 'http://127.0.0.1:1089'
# GERAPY_PLAYWRIGHT_PROXY_CREDENTIAL = {
#     'username': 'xxx',
#     'password': 'xxxx'
# }
# Window Size
# GERAPY_PLAYWRIGHT_WINDOW_WIDTH = 1400
# GERAPY_PLAYWRIGHT_WINDOW_HEIGHT = 700
# Screenshot
# pretend
GERAPY_PLAYWRIGHT_PRETEND = True
GERAPY_CHECK_PLAYWRIGHT_INSTALLED = True
RETRY_ENABLED = True
