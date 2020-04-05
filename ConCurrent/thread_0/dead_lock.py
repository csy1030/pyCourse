import time
from threading import Lock,Thread

lock = Lock()
# 交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

def transfer(from_,to,amount):
    # 上锁成功返回True
    if from_.lock.acquire():
        from_.withdraw(amount)  # 自己账户金额减少
        # time.sleep(1)  # 将会产生死锁
        if to.lock.acquire(): # 对方账户上锁
            to.deposit(amount) # 对方账户金额增加
            to.lock.release()  # 对方账户解锁
        from_.lock.release()

    print("转账完成")
    print("Sam balance: %d, Jenny balance: %d" %(from_.balance,to.balance))
Sam = Account('Sam',5000,Lock())
Jenny = Account('Jenny',8000,Lock())

# 两个账户相互转钱
t1 = Thread(target = transfer,args=(Sam,Jenny,1000) )
t2 = Thread(target= transfer,args = (Jenny,Sam,500))

t1.start()
t2.start()
t1.join()
t2.join()