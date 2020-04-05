"""
    poll 多路服用
    次重点
"""

from socket import *
from select import *

# 设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

# 创建poll
p = poll()

# 建立查找字典  {fileno:io_obj}
fdmap = {s.fileno():s}

# 设置关注IO
p.register(s,POLLIN|POLLERR)

# 循环监控IO事件发生
while True:
    events = p.poll()  #  阻塞等待IO发生
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c
            # 为什么把pollhup写上面 因为

            # 断开事件发生时,POLLIN也会就绪
        elif event & POLLHUP:  #客户端退出
            print("客户端退出")
            p.unregister(fd)  #取消关注
            fdmap[fd].close()  # 关闭套接字
            del fdmap[fd]   # 从字典删除
        elif event & POLLIN: # 客户端发消息
            data = fdmap[fd].recv(1024)
            if not data:
                continue
            print(data.decode())
            fdmap[fd].send(b'OK')
