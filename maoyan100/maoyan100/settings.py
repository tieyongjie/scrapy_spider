# Scrapy settings for maoyan100 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan100'

SPIDER_MODULES = ['maoyan100.spiders']
NEWSPIDER_MODULE = 'maoyan100.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maoyan100 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie': '__mta=216366633.1598757231221.1599140099298.1599140535496.7; uuid_n_v=v1; uuid=D33B1C30EA6E11EAABD8ED85325F9646E95690FF53FE4611A8EFBAD668944BED; _lxsdk_cuid=1743d5b57f657-00d1dd8169100d-3e3e5e0e-1fa400-1743d5b57f7c8; _lxsdk=D33B1C30EA6E11EAABD8ED85325F9646E95690FF53FE4611A8EFBAD668944BED; mojo-uuid=ffa230a17d4aba84d1ea4cf949d86284; _csrf=d316a480565cc00d2fd0bddf876afdd27d828d65e00210f3377bce0e8547e2b0; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598757231,1598758726,1599140099; mojo-session-id={"id":"754f4c4cf15a7cca469d2712b57ffde9","time":1599140099232}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1599140535; _lxsdk_s=174542d74b2-34b-a1c-671%7C%7C3',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan100.middlewares.Maoyan100SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan100.middlewares.Maoyan100DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'maoyan100.pipelines.Maoyan100Pipeline': 300,
   # 'maoyan100.pipelines.MonGoDBPipeline': 301,
   # 'maoyan100.pipelines.RedisPipeline': 302,
   # 'maoyan100.pipelines.ExcelPipeline': 303,
   'maoyan100.pipelines.MySQLPipeline': 304
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
