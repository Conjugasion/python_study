"""
@author Lucas
@date 2018/12/12 20:12
UDP不需要建立连接，只需要知道对方的IP地址和端口号，数据传输不可靠，速度快
主要用于 网络广播
"""
import socket


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect("10.17.7.228", 8080)
while True:
    udp.send("hello world".encode("utf-8"))