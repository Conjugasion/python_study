"""
@author Lucas
@date 2018/12/6 20:40

"""
import random
import urllib.request
import ssl
import re
import os
from collections import deque


def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(htmlBytes.decode("utf-8"))


def getHtmlBytes(url):
    agentsList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
                  "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
                  "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
                  "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
                  "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
                  "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
                  "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11"]

    agentStr = random.choice(agentsList)
    req = urllib.request.Request(url, headers={"User-Agent": agentStr})
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()


def QQCrawler(url, toPath):
    HtmlBytes = getHtmlBytes(url)
    # writeFileBytes(HtmlBytes, toPath)
    # HtmlStr = HtmlBytes.decode("utf-8")
    HtmlStr = str(HtmlBytes)

    pattern1 = r'<p class.*?(\d{6,11}).*?</p>'
    # pattern1 = r'[1-9]\d{7,10}'
    re_QQ = re.compile(pattern1)
    QQList = re_QQ.findall(HtmlStr)
    # 去重
    QQList = list(set(QQList))
    # print(QQList)
    # print(len(QQList))
    f = open(toPath, "a")
    for QQ in QQList:
        f.write(QQ + "\n")
    f.close()

    # 匹配网址
    pattern2 = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,' \
               r'3}))(:[0-9]{1,4})*(/[]a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pattern2)
    urlList = re_url.findall(HtmlStr)
    urlList = list(set(urlList))
    # print(urlList)
    # print(len(urlList))

    return urlList


def center(url, toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = QQCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)


url = r"https://www.douban.com/group/topic/17359302/"
toPath = r"D:\Tang\python_exercise\python_study\main\file\QQ\number.txt"
center(url, toPath)
