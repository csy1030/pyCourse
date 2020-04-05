"""
    select 函数讲解
"""

from socket import socket
from select import select

# 做几个IO用作监控
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

fd = open('log.txt','a+')
print("开始提交监控的列表")
rs,ws,xs = select([fd],[fd],[])

# 被动去做的事情
print("rs:",rs)
# 主动去做的事情
print("ws:",ws)
print("xs:",xs)
