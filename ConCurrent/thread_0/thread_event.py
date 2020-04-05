from threading import Thread,Event
from time import sleep

s = None
e = Event()
# 模拟暗号对接
def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 共享资源操作完毕

t = Thread(target = 杨子荣)
t.start()
print("答对口令就是自己人")

e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
else:
    print("错误")

t.join()
