"""
@author Lucas
@date 2018/12/12 19:24

"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.17.7.228", 8081))

while True:
    data = input("请输入发送给服务器的数据：")
    client.send(data.encode("utf-8"))
    # 每次接受1K数据
    info = client.recv(1024)
    print("服务器回复：", info.decode("utf-8"))