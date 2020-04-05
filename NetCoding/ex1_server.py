from socket import *
from struct import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
st = Struct('i32sif')
f = open('student_info.txt','a')
while True:
    print("Waiting for input...")
    data, addr = s.recvfrom(1024)
    print("connected from",addr)
    data = st.unpack(data)
    sorted_data = "%d  %s  %d  %.2f\n" % (data[0],data[1].decode(),data[2],data[3])
    f.write(sorted_data)
    f.flush()
    s.sendto(b'written one',addr)
    print("Finished writing")
f.close()
s.close()
