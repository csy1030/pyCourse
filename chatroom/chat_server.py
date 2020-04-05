"""
    功能: 类似qq群功能
    1. 有人进入聊天室需要输入姓名,姓名不能重复
    2. 有人进入聊天室时,其他人会收到通知:xxx进入了聊天室
    3. 一个发消息,其他人会受到:xxx:xxxx
    4. 有人退出聊天室,则其他人也会收到通知:xxx退出了聊天室
    5. 扩展功能:服务器可以向所有用户发送公告:
"""
from socket import *
import os,sys

ADDR = ('0.0.0.0',8888)
user = {}

# 接收客户端请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        # print(data.decode())
        msg = data.decode().split(' ')
        if msg[0] == 'L':
            do_login(s,msg[1],addr)
        elif msg[0] == 'C':
            do_chat(s,msg[1],' '.join(msg[2:]))
        elif msg[0] == 'Q':
            do_quit(s,msg[1])

# 进入聊天室
def do_login(s,name,addr):
    if name in user or "管理员" in user:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)
    # 通知其他人
    msg = "欢迎%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(),user[i])

    # 将用户加入user
    user[name] = addr

# 聊天
def do_chat(s,name,text):
    msg = "%s:%s" % (name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

# 退出程序
def do_quit(s,name):
    for item in user:
        if item != name:
            s.sendto("%s退出了...".encode() % name,user[item])
        else:
            s.sendto(b'EXIT',user[item])
    del user[name]
# 创建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    print("waiting for connection...")
    pid = os.fork()
    if pid < 0:
        print("Error")
        return
    # 子进程发送管理员消息
    elif pid == 0:
        while True:
            msg = input("管理员消息")
            msg = "C 管理员消息: " + msg
            s.sendto(msg.encode(),ADDR)
    # 请求处理
    else:
        do_request(s)  # 处理客户端请求

if __name__ == "__main__":
    main()