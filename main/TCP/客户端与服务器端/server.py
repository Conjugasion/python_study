"""
@author Lucas
@date 2018/12/12 19:24

"""
import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip端口
server.bind(("10.17.7.228", 8081))

# 监听 可以有五个客户端连接我
server.listen(5)
print("服务器启动成功......")

# 等待连接
clientSocket, clientAddress = server.accept()
print("%s -- %s 连接成功" % (str(clientSocket), clientAddress))

while True:
    # 每次接受1K数据
    data = clientSocket.recv(1024)
    revData = data.decode("utf-8")
    print("客户端发送：" + revData)
    # 回复客户端
    sendData = input("输入返回给客户端的数据：")
    clientSocket.send(sendData.encode("utf-8"))

