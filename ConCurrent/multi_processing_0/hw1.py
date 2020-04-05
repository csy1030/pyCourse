"""
    multiprocessing创建两个进程，
    同时复制一个文件的上下两半部分，
    各自复制到一个新的文件里。
"""
from multiprocessing import Process
import os
file_name = 'test_file'

f = open(file_name,'r')
lines = f.readlines()
# 获取文本中字符数
count = len(lines)

def first(lines,count):
    new_file = open("first", 'w')
    for i in range(count//2):
        new_file.write(lines[i])
        new_file.flush()
    new_file.close()

def second(lines,count):
    new_file = open('second', 'w')
    for item in lines[count // 2 + 1:]:
        new_file.write(item)
        new_file.flush()
    new_file.close()

def top():
    fw = open("first", 'w')
    fw.write(f.read(count//2))
    fw.close()

def bottom():
    fw = open("second", 'w')
    f.seek(count//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()



p1 = Process(target= top)
p2 = Process(target= bottom)

p1.start()
print("first pid:",os.getpid())
p2.start()

print("second pid:",os.getpid())
p1.join()
p2.join()
print("finish writing")