"""
    线程示例
"""
from time import sleep
import threading
import os
# 线程函数
def music():
    for i in range(5):
        sleep(2)
        print(os.getpid(),"play music")
# 创建线程对象
t = threading.Thread(target = music)
t.start()

# 主线程任务
for i in range(3):
    sleep(3)
    print(os.getpid(),"播放音乐")

t.join()
