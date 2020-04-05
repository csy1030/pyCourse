import re

s = """
Hello world
你好 Sam
"""

# re.A 只能匹配ASCII码
regex = re.compile(r'[a-z]+',flags = re.I)
# 使  .  可以匹配到换行符
regex = re.compile(r'.+',flags = re.S)
# 匹配每行开头结尾
regex = re.compile(r'^你好',flags = re.M)
# 正则添加注释
pattern = r"""
\W+ # 第一部分
\s+ # 第二部分
\w+ # 第三部分
"""
regex = re.compile(pattern,flags = re.X)
l = regex.findall(s)
print(l)