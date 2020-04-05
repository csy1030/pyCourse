import re
pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)

# 获取match对象
obj = regex.search("abcdefghi")

# 属性变量
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
print("=================")

print(obj.start())
print(obj.end())
print(obj.span())
print(obj.groupdict()) # 获取捕获组字典
print(obj.groups())  # 子组对应内容




