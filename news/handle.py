import newspaper  # need pip install newspaper3k in python3.x env
import web  # need: pip install web.py
import json


def get_html(url):
    return newspaper.build(url, language='zh')


def get_data(newsAnalysis):
    result = {"reason": "success"}
    newsResult = {"stat": "1"}
    data = []

    for article in newsAnalysis.articles:
        news = {}
        try:
            article.download()
            article.parse()
            news["title"] = article.title
            news["url"] = article.url
            if len(article.authors) > 0:
                news["author_name"] = article.authors[0]
            else:
                news["author_name"] = "NULL"
            news["date"] = article.publish_date.strftime("%Y-%m-%d")
            news["thumbnail_pic_s"] = article.top_image
            data.append(news)
        except:
            news["title"] = "NULL"
            news["url"] = "NULL"
            continue

    # for category in news.category_urls():
    #     print(category)

    newsResult["data"] = data
    result["result"] = newsResult
    print(result)

    return result


class Handle(object):
    def GET(self):
        base_url = "https://www.sina.com.cn/"
        html_doc = get_html(base_url)
        result = get_data(html_doc)
        return json.dumps(result)

    def POST(self):  # TODO
        return 'post data'
