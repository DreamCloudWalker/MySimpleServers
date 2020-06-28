# 字段和聚合API保持一致，方便做备份API
# https://www.juhe.cn/docs/api/id/235
import scrapy


class ScrapyNewsItem(scrapy.Item):
    # 内容来源网站
    source = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    # 文章时间有（可能没有）
    date = scrapy.Field()
    remark = scrapy.Field()
    category = scrapy.Field()
    author_name = scrapy.Field()
    thumbnail_pic_s = scrapy.Field()
    thumbnail_pic_s02 = scrapy.Field()
    thumbnail_pic_s03 = scrapy.Field()
