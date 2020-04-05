"""
    作业：
    1. 每隔1s 向文件test.txt 中写入一行数据
    1.2019-7-30  12:12:12
    2.2019-7-30 12:12:13
    3.2019-7-30
    程序无限循环 ctrl-c推出
    当重新写入时， 内容会继续向下写， 序号能够接上
"""
import time

f = open('test', 'a+')
f.seek(0)
count = 0
for lines in f:
    count += 1

while True:
    count += 1

    f.write("%d. %s\n" % (count, time.ctime()))
    f.flush()
    time.sleep(1)
