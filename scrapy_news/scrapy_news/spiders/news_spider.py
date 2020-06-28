import scrapy
import re
from scrapy_news.items import ScrapyNewsItem


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    start_urls = ['https://www.douban.com/gallery/',    # 豆瓣
                  'https://s.weibo.com/top/summary',    # 微博
                  'http://tieba.baidu.com/hottopic/browse/topicList?res_type=1&red_tag=h1923737578',  # 百度贴吧
                  'https://bbs.hupu.com/all-gambia',    # 虎扑
                  'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513',  # 百度今日热点
                  ]

    def parse(self, response):
        if response.url == self.start_urls[0]:    # 豆瓣
            yield from self.crawl_douban(response)
        if response.url == self.start_urls[1]:  # 微博
            yield from self.crawl_weibo(response)
        if response.url == self.start_urls[2]:  # 百度贴吧
            yield from self.crawl_tieba(response)
        if response.url == self.start_urls[3]:  # 虎扑
            yield from self.crawl_hupu(response)
        if response.url == self.start_urls[4]:  # 百度今日热点
            yield from self.crawl_topbaidu(response)

    def crawl_douban(self, response):
        trends = response.css('ul.trend > li > a')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'douban_spider'
            item['title'] = trend.css('a::text').extract_first()
            item['url'] = trend.css('a').attrib['href']
            item['remark'] = ''
            yield item

    def crawl_weibo(self, response):
        trends = response.css('td.td-02 > a')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'weibo_spider'
            item['title'] = trend.css('a::text').extract_first()
            href = self.get_weibo_href(trend)
            item['url'] = "https://s.weibo.com" + href
            item['remark'] = ''
            yield item

    def crawl_tieba(self, response):
        trends = response.css('div.main > ul > li  a')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'tieba_spider'
            item['title'] = trend.css('a::text').extract_first()
            item['url'] = trend.css('a').attrib['href']
            item['remark'] = ''
            yield item

    def crawl_hupu(self, response):
        trends = response.css('div.list> ul > li >span:nth-child(1) >a')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'hupu_spider'
            item['title'] = trend.css('a').attrib['title']
            item['url'] = "https://bbs.hupu.com" + trend.css('a').attrib['href']
            item['remark'] = ''
            yield item

    def crawl_github(self, response):
        trends = response.css('div> article.Box-row ')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'github_spider'
            title = "".join(trend.css('p::text').extract())
            re.sub(r'[\\*|“<>:/()（）0123456789]', '', title)
            title.replace('\n', '').replace('  ', '')
            item['title'] = title
            item['url'] = "https://github.com" + trend.css('h1>a').attrib['href']
            item['remark'] = ''
            yield item

    def crawl_topbaidu(self, response):
        trends = response.css('td.keyword >a:nth-child(1) ')
        for trend in trends:
            item = ScrapyNewsItem()
            item['source'] = 'topbaidu_spider'
            item['title'] = trend.css('a::text').extract_first()
            item['url'] = trend.css('a').attrib['href']
            item['remark'] = ''
            yield item

    def get_weibo_href(self, trend):
        href = trend.css('a').attrib['href']
        if href.startswith('javascript'):  ##javascript:void(0)
            href = trend.css('a').attrib['href_to']
        return href
