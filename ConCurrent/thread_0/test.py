# 计算密集型函数
def count(x,y):
    c = 0
    while c < 70000:
        c += 1
        x += 1
        y += 1

# io密集型函数
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(12222):
        f.write("csy\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()
