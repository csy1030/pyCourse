from socket import *

s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
