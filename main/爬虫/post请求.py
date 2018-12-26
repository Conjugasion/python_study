"""
@author Lucas
@date 2018/12/5 10:05

"""
'''
参数打包传输
速度慢，安全，修改数据建议采用post
'''
import urllib.request
import urllib.parse


url = "http://www.baidu.com"
data = {
    "username": "Lucas",
    "passwd": "666"
}
# 对要发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")
# 请求体
req = urllib.request.Request(url, data=postData)
# 获得response
response = urllib.request.urlopen(req)

print(response.read().decode("utf-8"))

















