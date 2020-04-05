import re
import sys

port = sys.argv[1]

f = open('1.txt')

# 找到port段落
while True:
    data = ''
    for line in f:
        if line != '\n':
            data += line
        else:
            break
    print(">>>>",data)
    if not data:
        break

    key_word = re.match(r'\S+',data).group()
    if port == key_word:
        try:
            address = re.search(pattern,data).group()
            print(address)
        except:
            print("No address")
        break

