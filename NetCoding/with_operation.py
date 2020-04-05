# with open('test') as f:
#     data = f.read()
#     print(data)

f_name = input("input name:")
with open(f_name) as f:
    while True:
        data = f.read(1024)
        f_new = open('new_file','w')
        f_new.write(data)
