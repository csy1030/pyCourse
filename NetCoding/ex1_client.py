from socket import *
from struct import *

#
st = Struct('i32sif')
ADDR = ('0.0.0.0',8888)
s = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("id:"))
    name = input("name:").encode()
    age = int(input("age:"))
    score = float(input("score:"))

    if not id:
        break
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR)
    print('sent')
    # msg,addr = s.recvfrom(1024)
    # print(msg.decode())

s.close()

