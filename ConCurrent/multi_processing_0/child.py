"""
    创建二级子进程防止僵尸进程
"""

import os
from time import *
def f1():
    for i in range(4):
        sleep(2)
        print("写代码...")
def f2():
    for i in range(6):
        sleep(1)
        print("测试")

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    p = os.fork() # 二级子进程
    if p == 0:
        f2()
    else:
        os._exit(0)
else:
    os.wait()
    f1()
