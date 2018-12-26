"""
@author Lucas
@date 2018/12/12 20:36

"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入数据：")
    client.sendto(data.encode("utf-8"), ("10.17.7.228", 8900))
    info = client.recv(1024).decode("utf-8")
    print("服务器说：", info)