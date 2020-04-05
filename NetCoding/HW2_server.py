"""
    1.使用tcp服务和客户端编程,将一个文件从客户端发送到服务端,
    文件类型为图片或普通文本
"""
from socket import *
file_name = 'test'
f = open(file_name,'ab+')

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
while True:
    try:
        print("Waiting for connection...")
        connfd,addr = sockfd.accept()
        print("Connected from:",addr)
    except KeyboardInterrupt:
        print("Stop server")
        break
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        f.write(data.decode())
        f.flush()
    print("Writing Finished")
    connfd.close()
f.close()
sockfd.close()



