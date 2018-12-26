"""
@author Lucas
@date 2018/12/4 17:23

"""
import urllib.request

# 向指定url地址发起请求，并返回服务器相应的数据
response = urllib.request.urlopen("http://www.baidu.com")

# data = response.read()

# print(type(data))

# 将爬取到的网页写入文件
# with open(r"D:\Tang\python_exercise\python_study\main\file\baidu.html", "wb") as f:
#     f.write(data)

# data1 = response.readlines()
# print(data1)
# print(type(data1))


# 当前环境的有关信息
print(response.info())

# 返回状态码
print(response.getcode())

# 返回当前正在爬去的url地址
print(response.geturl())

url = r"https://www.baidu.com/s?wd=%E8%A7%A3%E7%A0%81%E8%A7%A3%E7%A0%81%E8%A7%A3%E7%A0%81&rsv_spt=1&rsv_iqid" \
      r"=0xdbf7449f0001d5ff&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=%25E8" \
      r"%25A7%25A3%25E7%25A0%2581%25E8%25A7%25A3%25E7%25A0%2581%25E8%25A7%25A3%25E7%25A0%2581&rsv_t" \
      r"=5ed0EqswK6mSNeSx0fMeaI8ZLKXWM6hgfYEAbqkJoM06cq4hVOAod6biDlX%2B84QX1DEM&rsv_pq=f6c559bc0001ec43&prefixsug" \
      r"=%25E8%25A7%25A3%25E7%25A0%2581%25E8%25A7%25A3%25E7%25A0%2581%25E8%25A7%25A3%25E7%25A0%2581&rsp=0 "

# 解码
newUrl1 = urllib.request.unquote(url)
print(newUrl1)

# 编码
newUrl2 = urllib.request.quote(url)
print(newUrl2)
