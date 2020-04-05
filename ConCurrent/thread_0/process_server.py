"""
    多进程网络并发
    重点代码
"""
from socket import *
from multiprocessing import Process
import sys,signal

def handle(c):
    print("Connected from:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


# 创建监听套接字
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程
# 僵尸进程处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 循环等待客户端链接
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("Server quit.")
    except Exception as e:
        print(e)
        continue
    # 创建新的客户端请求
    p = Process(target=handle, args = (c,))
    # 主线程退出,分支线程也退出
    p.daemon = True
    p.start()