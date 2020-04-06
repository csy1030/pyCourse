from socket import *

HOST = '192.168.237.150'
PORT = 8000
name = ''

# def input_msg():
#     global name
#     while True:
#         name = input('Username:')
#         if not name:
#             print('Username cannot be blank')
#             continue
#         pwd = input('Password:')
#         if not pwd:
#             print('Password cannot be blank')
#             continue
#         return name,pwd

def to_register(s):
    global name
    while True:
        name = input('Username:')
        if not name:
            print('Username cannot be blank')
            continue
        pwd = input('Password:')
        if not pwd:
            print('Password cannot be blank')
            continue
        msg = 'R '+ name + ' ' + pwd
        s.send(msg.encode())
        msg_back = s.recv(1024).decode()
        if msg_back == 'exist':
            print('Username exist')

        else:
            print(msg_back)
            return True


def to_login(s):
    global name
    name = input('Username:')
    pwd = input("Password:")
    msg = 'L ' + name + ' ' + pwd
    s.send(msg.encode())
    msg_back = s.recv(1024).decode()
    if msg_back == 'OK':
        print("Welcome %s!" % name)

        return True
    elif msg_back == 'wrong':
        print("用户名或密码错误..")
        return False





def search_word(s):
    print("===========Dictionary=============")
    print("======q->quit====h->history=======")
    while True:
        word = input("word: ")
        if word == 'q':
            break
        elif word == 'h':
            get_history(s)
            continue
        word = 'S ' + word
        s.send(word.encode())
        trans = s.recv(1024).decode()
        print('trans:',trans)

def get_history(s):
    msg = 'H ' + name
    s.send(msg.encode())
    print('History')
    print("++++++++++")

    lines = s.recv(2048).decode()
    if lines == 'OK':
        print("++++++++++")
        return
    else:
        print(lines)

def main():
    s = socket()
    s.connect((HOST, PORT))
    while True:
        print("============================")
        print("===Welcome to eDictionary===")
        print("===Register==Login==Quit====")
        print("============================")
        cmd = input("cmd:")
        if cmd == 'r':
            is_success = to_register(s)
            if not is_success:
                print(is_success)
            else:
                search_word(s)
                break

        elif cmd == 'l':
            while True:
                is_success = to_login(s)
                if is_success:
                    break
            search_word(s)

        elif cmd == 'q':
            exit('Bye')


if __name__ == "__main__":
    main()