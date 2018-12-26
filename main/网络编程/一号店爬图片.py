"""
@author Lucas
@date 2018/12/6 19:37

"""
import os
import random
import re
import urllib.request


def imageCrawler(url, toPath):
    agentsList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 "
                  "QQBrowser/6.9.11079.201"]

    agentStr = random.choice(agentsList)
    req = urllib.request.Request(url, headers={"User-Agent": agentStr})
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
    # with open(r"D:\Tang\python_exercise\python_study\main\file\yhd\yhd.html", "wb") as f:
    #     f.write(HtmlStr)

    pattern = r'(//img\d{2}.*)/{1}(.*?)\.jpg'
    re_image = re.compile(pattern)
    imagesList = re_image.findall(HtmlStr)
    # print(imagesList)
    # print(len(imagesList))
    for imageUrl in imagesList:
        path = os.path.join(toPath, imageUrl[1] + ".jpg")
        urllib.request.urlretrieve("http:" + imageUrl[0] + "/" + imageUrl[1] + ".jpg", filename=path)


url = r"http://search.yhd.com/c0-0/k%25E6%25B5%25B7%25E5%25B0%2594%25E7%25A9%25BA%25E8%25B0%2583/"
toPath = r"D:\Tang\python_exercise\python_study\main\file\yhd"
imageCrawler(url, toPath)
