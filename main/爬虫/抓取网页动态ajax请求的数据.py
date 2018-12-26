"""
@author Lucas
@date 2018/12/5 10:22

"""
import json
import urllib.request
import ssl


# 豆瓣
def ajaxCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) "
                      "Chrome/68.0.3440.75 Mobile Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    # 使用ssl创建未验证的上下文,为了爬取https
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData


