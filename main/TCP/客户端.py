"""
@author Lucas
@date 2018/12/11 21:47
TCP链接
"""
import socket

# 创建一个socket
# 参数1：指定协议AF_INET 或者 AF_INET6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 参数是一个元组
sk.connect(("www.baidu.com", 80))

sk.send(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")

# 等待接收数据
data = []
while True:
    # 每次接受1K数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b"".join(data)).decode("utf-8")

# 断开连接
sk.close()
# print(dataStr)

headers, HTML = dataStr.split('\r\n\r\n', 1)
# print(headers)
print(HTML)