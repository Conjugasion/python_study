"""
@author Lucas
@date 2018/12/5 9:08

"""
import random
import urllib.request

url = "http://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) "
                         "Chrome/68.0.3440.75 Mobile Safari/537.36"}

# 设置请求体
# req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(req)
# data = response.read().decode("utf-8")
# print(data)

agentsList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0", "Mozilla/5.0 (Windows NT "
                                                                                        "6.1; WOW64) "
                                                                                        "AppleWebKit/534.50 (KHTML, "
                                                                                        "like Gecko) Version/5.1 "
                                                                                        "Safari/534.50",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 "
              "QQBrowser/6.9.11079.201"]

agentStr = random.choice(agentsList)
req = urllib.request.Request(url, headers={"User-Agent": agentStr})
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
