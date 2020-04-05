"""
    套接字非阻塞示例
"""

from socket import *
from time import sleep,ctime

# 创建tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8000))
sockfd.listen(3)

f = open('log.txt','a+')
# 设置套接字为非阻塞
# sockfd.setblocking(False)
sockfd.settimeout(2)
while True:
    print("waiting for connection")
    try:
        connfd,addr = sockfd.accept()
    except Exception as e:
        sleep(2)
        f.write("%s: %s\n" %(ctime(),e))
        f.flush()


