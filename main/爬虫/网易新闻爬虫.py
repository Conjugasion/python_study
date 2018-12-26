"""
@author Lucas
@date 2018/12/5 10:41

"""
import re
import urllib.request
import ssl


url = "https://www.163.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/68.0.3440.75 Safari/537.36 "
}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

HTML = response.read().decode("gbk")

pattern = r'"province": \[.*?"url":"http://bj.news.163.com/".*?},'
re_province = re.compile(pattern, re.S)
provinceList = re_province.findall(HTML)
print(provinceList)


# HTML1 = HTML.replace(" ", "").replace("\n", "")
# HTML2 = HTML1.replace(" ", "")
# with open(r"D:\Tang\python_exercise\python_study\main\file\netEase.txt", "w") as f1:
#     f1.write(HTML2)

# with open(r"D:\Tang\python_exercise\python_study\main\file\netEase.txt", "r") as f2:
#     HTML2 = f2.read()


