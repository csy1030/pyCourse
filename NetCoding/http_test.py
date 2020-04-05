from socket import *

s = socket()
s.bind(('0.0.0.0',8891))
s.listen(3)

connfd,addr = s.accept()
print("Connect from",addr)
data = connfd.recv(4096)
print(data.decode())
f = open('index.html','rb')
while True:
    line = f.readline()
    f.flush()
    connfd.send(line)


# data = """ HTTP/1.1 200 ok
# Content-Type:text/html
#
# <h1>hello world</h1>
# """

connfd.close()
s.close()

