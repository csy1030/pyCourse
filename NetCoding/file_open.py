"""
    文件操作示例
"""
try:
    fd = open("test",'w')
except FileNotFoundError as e:
    print(e)
else:
    print("文件打开成功")

# 读写操作

# 关闭文件
fd.close()