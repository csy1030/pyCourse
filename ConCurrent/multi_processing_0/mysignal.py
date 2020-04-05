"""
    信号方法处理僵尸进程
"""

import os
import signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    pass
elif pid == 0:
    print("Child PID",os.getpid())
else:
    while True:
        pass