"""
@author Lucas
@date 2018/12/5 9:36

"""
'''
将数据拼接到请求路径的后面传递给服务器
'''
import urllib.request

url = ""
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
