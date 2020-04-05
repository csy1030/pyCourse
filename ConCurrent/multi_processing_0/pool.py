"""
    进程池原理示例
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池时间
def worker(msg):
    sleep(2)
    print(msg)
# 创建进程池
pool = Pool(2)

# 向进程池添加事件
for i in range(20):
    msg = "Hello %d" % i
    pool.apply_async(func = worker,args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
