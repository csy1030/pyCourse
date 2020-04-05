# 管道通信
import multiprocessing as mp
import os,time

# 创建管道
fd1,fd2 = mp.Pipe(False)

def fun(name):
    time.sleep(3)
    # 向管道写入内容
    fd2.send({name:os.getpid()})

jobs = []
for i in range(6):
    p = mp.Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

# 读取管道
for i in range(6):
    data = fd1.recv()
    print(data)

# 回收进程
for i in jobs:
    i.join()