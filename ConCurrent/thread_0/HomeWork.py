from threading import Thread,Lock
from multiprocessing import Process
import time,os
# 计算密集型函数
def count(x,y):
    c = 0
    while c < 2000000:
        c += 1
        x += 1
        y += 1

# io密集型函数
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(12222):
        f.write("csy\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()



time1 = time.time()
job = []
for i in range(10):
    # t1 = Thread(target=count, args=(1, 1))
    t1 = Thread(target=io)
    job.append(t1)
    t1.start()
for item in job:
    item.join()


time2 = time.time()
print("多线程执行一次,运行时间:",time2-time1)


time3 = time.time()
for i in range(10):
    # count(1,1)
    io()
time4 = time.time()
print("单线程执行十次,运行时间:",time4-time3)

##############

time5 = time.time()
job1 = []
for i in range(10):
    # t1 = Thread(target=count, args=(1, 1))
    t2 = Process(target=io)
    job1.append(t2)
    t2.start()
for item in job1:
    item.join()


time6 = time.time()
print("多进程执行一次,运行时间:",time6-time5)

#
# time7 = time.time()
# for i in range(10):
#     # count(1,1)
#     io()
# time8 = time.time()
# print("单进程执行十次,运行时间:",time4-time3)