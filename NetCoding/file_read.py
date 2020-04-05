"""
    文件读操作 演示
"""
fd = open('test','r')

# 读操作
import time
# while True:
    # time.sleep(1)
    # data = fd.read(12)
    # if not data:
    #     break
    # print("读取到的内容",data)
# data = fd.readline()
# print(data)

for line in fd:
    print(line)



fd.close()
