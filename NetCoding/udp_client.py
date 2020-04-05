"""
    udp客户端
    重点代码
"""

from socket import *

# 服务器地址
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

sockfd.close()