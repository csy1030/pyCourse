from multiprocessing import Array
from multiprocessing import Process
import time, random

# 创建共享内存
# 共享内存开辟5个整形列表空间
# shm = Array('i',5)
shm = Array('c','H')

def fun():
    # 共享内存可迭代
    for i in shm:
        print(i)
    # 修改共享内存
    shm[1] = 1000

p = Process(target = fun)
p.start()
p.join()

