"""
    wait处理僵尸进程
"""

import os
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID",os.getpid())
    os._exit(2)

else:
    pid,status = os.wait()
    print("Child PID",pid)
    print("status",status)
    while True:
        pass