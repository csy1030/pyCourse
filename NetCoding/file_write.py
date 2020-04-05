fd = open('test','rb')
data = fd.read() # 得到字节串
print(data)
fd.close()