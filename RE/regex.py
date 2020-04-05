import re
s = 'Sam:1997,Jenny:1998'
pattern = r'\w+:\d+'

# l = re.findall(pattern,s)

# compile 对象调用
regex = re.compile(pattern)
l = regex.findall(s,0,12)
print(l)

s = "hello world how are you doing sam"
l = re.split(r'[^\w]+',s)
print(l)


s = "时间: 2020/04/02"
ns = re.sub(r'/','-',s)
print(ns)
# 2020-04-02
