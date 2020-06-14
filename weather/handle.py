# -*- coding: utf-8 -*-
# filename: handle.py
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

import urllib
import hashlib
import web  # need: pip install web.py
import json
import chardet

def get_html(url):
    html = urllib.urlopen(url)
    return html.read()

def get_data(html_text):
    final = {"ret": "0", "err": "success"}
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find('div', {'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')  #BeautifulSoup库函数find_all，返回一个Python list数组
    arrayWeather = []

    for day in li:
        date = day.find('h1').string
        weather = {"day": date}
        inf = day.find_all('p')
        weather["weather"] = inf[0].string
        if inf[1].find('span') is None:
            #temperature_highest = None
            temperature_highest = inf[1].find('i').string
            temperature_highest = temperature_highest.replace('C', '')
        else:
            temperature_highest = inf[1].find('span').string
            temperature_highest = temperature_highest.replace('C', '')
        temperature_lowest = inf[1].find('i').string
        temperature_lowest = temperature_lowest.replace('C', '')
        weather["temp_low"] = temperature_lowest
        weather["temp_high"] = temperature_highest
        if (len(inf) > 2):
            # print len(inf)
            if len(inf[2].find_all("span")) > 1:
                wind = inf[2].find_all("span")[0]["title"]
                #if (len(inf[2].find_all("span")) > 1):
                   # wind += " -> "
                   # wind += inf[2].find_all("span")[1]["title"]
                weather["wind"] = wind
            windpower = inf[2].find("i").string
            weather["windpower"] = windpower
        arrayWeather.append(weather)

    final["sevenDayWeather"] = arrayWeather

    return final


class Handle(object):
    def GET(self):
        base_url = "http://www.weather.com.cn/weather/";
        param = web.input().city # "101280601" #request.values.get('city')
        suffix = ".shtml"
        html_doc = get_html(base_url + param + suffix)
        result = get_data(html_doc)
        return json.dumps(result)
    def POST(self):
        return 'post data'