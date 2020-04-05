"""
    IO多路复用select实现多客户端通信
    重点代码
"""

from socket import *
from select import select

# 设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(3)

# 设置关注的IO
rlist = [s]
wlist = []
xlist = []

while True:
    # 监控IO的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历三个返回值列表,判断那个IO发生了
    for r in rs:
        # 如果套接字就绪则处理链接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)  # 加入新的关注IO
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b'ok')
            # 希望我们主动处理这个IO
            wlist.append(r)
    for w in ws:
        w.send(b"roger")
        wlist.remove(w)

        pass


