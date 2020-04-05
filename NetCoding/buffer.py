"""
    缓冲区示例
"""

# fd = open('test','w',0)  # no buffer (not allowed)

fd = open('test','w',1)  # line buffer (not allowed)

while True:
    s = input(">>")
    fd.write(s)
    fd.flush() # 立即刷新缓冲，磁盘交互

