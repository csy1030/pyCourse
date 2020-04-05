"""
    广播发送
    1.
"""
from socket import *
from time import sleep

# 广播地址
dest = ('192.168.237.255',9999)
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = """
@@@@@@@@@@@@@@>..>@@@@@@@@@@@@@@@@@
@90232312312331231
FM103.9
"""
while True:
    sleep(2)
    s.sendto(data.encode(),dest)
s.close()