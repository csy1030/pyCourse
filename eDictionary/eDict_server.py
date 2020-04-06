"""
    电子词典 服务端
"""
from socket import *
import os,sys
from login_sys import LoginSys
from seach_word import SearchWord
HOST = '0.0.0.0'
PORT = 8009
user_name =''




def do_request(connfd):
    while True:

        data = connfd.recv(1024)

        msg = data.decode().split(' ')
        if msg[0]=='R':
            do_register(connfd,msg[1],msg[2])
        elif msg[0] == 'L':
            do_login(connfd,msg[1],msg[2])
        elif msg[0] == 'S':
            do_search(connfd,msg[1])
        elif msg[0] == 'H':
            do_history(connfd,msg[1])
        elif msg[0] == 'Q':
            do_quit(connfd,msg[1])


def do_register(connfd,name,pwd):
    global user_name
    user_name= name
    ls = LoginSys('user_db',name,pwd)
    if not ls.is_avail():
        connfd.send(b'exist')
    else:
        is_success = ls.register()
        if is_success is True:
            connfd.send(b'Register Successfully!')
        else:
            connfd.send(is_success.encode())


def do_login(connfd,name,pwd):
    global user_name
    user_name= name
    ls = LoginSys('user_db', name, pwd)
    connfd.send(b'OK') if ls.login() else connfd.send(b'wrong')

    # print("登录成功!") if ls.login() else print("用户名或密码错误..")

def do_search(connfd,word):
    search = SearchWord(word)
    trans = search.search()
    if trans == 'No':
        connfd.send(b'Not Found')
    else:
        search.record(user_name, word, trans[0])
        # print(sql)
        connfd.send(trans[0].encode())

def do_history(connfd,name):
    search = SearchWord()
    data = search.get_history(name)
    print(data)


def do_quit(connfd,msg):
    pass




def main():
    s = socket(AF_INET,SOCK_STREAM)
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen(3)
    print('Waiting for connection...')

    while True:
        try:
            connfd, addr = s.accept()
            print("connected from",addr)
        except KeyboardInterrupt:
            sys.exit("Server quit.")
        except Exception as e:
            print(e)
            continue

        pid = os.fork()
        if pid <0:
            print('error')
        elif pid == 0:
            do_request(connfd)
        else:
            pass

if __name__ == '__main__':
    main()