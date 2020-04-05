"""
    udp套接字服务端
    重点代码
"""

from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

# 收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    if not data:
        break
    print("收到的消息:",data.decode())
    sockfd.sendto(b"Thanks",addr)

# 关闭套接字
sockfd.close()
