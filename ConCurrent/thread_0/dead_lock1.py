from threading import Thread,RLock
import time


lock = RLock()
num = 0  # 共享资源
class MyThread(Thread):
    def fun1(self):
        global num

        # ↓出现死锁原因↓
        with lock:
            num -= 1
    def fun2(self):
        global num
        if lock.acquire():
            num += 1
            if num > 5:
                self.fun1()
            print("num = ",num)
            lock.release()
    def run(self):
        while True:
            time.sleep(0.5)
            self.fun2()

t = MyThread()
t.start()
t.join()
