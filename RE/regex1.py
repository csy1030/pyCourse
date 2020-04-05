import re

s = "2020年 年龄23岁"
pattern = r'\d+'

#返回包含匹配结果的迭代器
it = re.finditer(pattern,s)

for i in it:
    # 迭代得到的i是match 对象
    print(i.group())

# 完全匹配
m = re.fullmatch(r'\w+','hello-1997')
# 因为不是完全匹配所以 返回值为None

m = re.fullmatch(r'[0-9a-zA-Z-]+','hello-1997')

print(m.group())

