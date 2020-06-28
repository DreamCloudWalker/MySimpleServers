## MySimpleServers
My simple servers based on python, include news, weather and so on

什么是收费API？从来白嫖的我是不可能知道的

## 新闻（暂未部署）：
##### 请求url如下：
http://0.0.0.0:8080/news
##### 返回结果如下：
```
{
    "reason": "success",
    "result": {
        "stat": "1",
        "data": [
            {
                "article_id": 51,
                "source": "weibo_spider",
                "title": "公众需坚持6大重点防控措施",
                "url": "https://s.weibo.com/weibo?q=%23%E5%85%AC%E4%BC%97%E9%9C%80%E5%9D%9A%E6%8C%816%E5%A4%A7%E9%87%8D%E7%82%B9%E9%98%B2%E6%8E%A7%E6%8E%AA%E6%96%BD%23&Refer=new_time",
                "status": "0",
                "remark": "",
                "date": "2020-06-28 00:00:00",
                "create_time": "2020-06-28 20:35:18",
                "category": null,
                "author_name": null,
                "thumbnail_pic_s": null,
                "thumbnail_pic_s02": null,
                "thumbnail_pic_s03": null
            },
            {
                "article_id": 146,
                "source": "hupu_spider",
                "title": "日本首位忍者专业硕士生毕业，已开始进修博士课程",
                "url": "https://bbs.hupu.com/36238680.html",
                "status": "0",
                "remark": "",
                "date": "2020-06-28 00:00:00",
                "create_time": "2020-06-28 20:35:19",
                "category": null,
                "author_name": null,
                "thumbnail_pic_s": null,
                "thumbnail_pic_s02": null,
                "thumbnail_pic_s03": null
            }]
    }
}
```

## 天气（已部署）：
##### 请求url如下：
http://120.77.249.106/weather?city=101280601
##### 请求结果如下：
```
{
    "sevenDayWeather": [
        {
            "windpower": "3-4级转<3级",
            "temp_low": "27℃",
            "weather": "雷阵雨转多云",
            "temp_high": "32",
            "day": "21日（今天）",
            "wind": "南风"
        },
        {
            "windpower": "3-4级转<3级",
            "temp_low": "27℃",
            "weather": "雷阵雨转多云",
            "temp_high": "32",
            "day": "22日（明天）",
            "wind": "西南风"
        },
        {
            "windpower": "3-4级转<3级",
            "temp_low": "27℃",
            "weather": "雷阵雨",
            "temp_high": "31",
            "day": "23日（后天）",
            "wind": "西南风"
        },
        {
            "windpower": "3-4级",
            "temp_low": "26℃",
            "weather": "雷阵雨",
            "temp_high": "32",
            "day": "24日（周三）",
            "wind": "西南风"
        },
        {
            "windpower": "3-4级",
            "temp_low": "27℃",
            "weather": "雷阵雨转阵雨",
            "temp_high": "32",
            "day": "25日（周四）",
            "wind": "西南风"
        },
        {
            "windpower": "3-4级转<3级",
            "temp_low": "27℃",
            "weather": "阵雨转雷阵雨",
            "temp_high": "32",
            "day": "26日（周五）",
            "wind": "西南风"
        },
        {
            "windpower": "3-4级",
            "temp_low": "28℃",
            "weather": "阴",
            "temp_high": "31",
            "day": "27日（周六）",
            "wind": "西南风"
        }],
    "err": "success",
    "ret": "0"
}
```