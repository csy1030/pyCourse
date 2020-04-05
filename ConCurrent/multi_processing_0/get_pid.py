import os
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID",os.getpid())
    print("Get parent PID",os.getppid())
else:
    print("Parent PID",os.getpid())
    print("Child PID",pid)
