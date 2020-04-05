# 文件偏移量示例
fd = open("test",'r+')
print("当前文件偏移量位置：",fd.tell())



fd.seek(3,1)  # 1表示相对与当前位置--3表示向后偏移3个
print(fd.read(2))
print("当前文件偏移量位置：", fd.tell())
fd.close()