from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)
server_addr = ('192.168.237.132',8888)
sockfd.connect(server_addr)
f = open('test_read','rb')

while True:
    data = f.readline()
    if not data:
        break
    sockfd.send(data.encode())
sockfd.close()
f.close()