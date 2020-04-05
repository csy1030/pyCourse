from multiprocessing import Semaphore, Process
from time import sleep
import os

# 创建信号量
# 服务程序最多允许3个进程同时执行事件
sem = Semaphore(3)

def handle():
    print("%d  想执行时间" % os.getpid())
    # 将信号量减一
    sem.acquire()
    print("%d  开始执行操作" % os.getpid())
    sleep(3)
    print("%d  完成操作" % os.getpid())
    # 将信号量加一
    sem.release()

jobs = []

# 10个进程请求执行事件
for i in range(5):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()


