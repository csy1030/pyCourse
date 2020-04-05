from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "Csy")


t.setName("YFF")
# 线程名称
print("Thread name:",t.getName())

# 线程生命周期
print("is alive?",t.is_alive())
