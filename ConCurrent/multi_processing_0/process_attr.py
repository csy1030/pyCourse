from multiprocessing import Process
from time import sleep

def tm():
    for i in range(3):
        sleep(5)
        print(ctime())
p = Process(target=tm,name= 'csy')
p.daemon = True
p.start()
print("Name:",p.name)
print("PID:",p.pid)
print("is Alive:",p.is_alive())
