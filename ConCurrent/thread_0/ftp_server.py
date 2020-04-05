"""
    ftp  文件服务器
    并发网络功能训练
"""

from socket import *
from threading import Thread
import os
from time import sleep
# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
d_FTP = "/home/samyoung/PycharmProjects/PythonCourseP2/FTP/"
u_FTP = '/home/samyoung/PycharmProjects/PythonCourseP2/FTP/MyFile/'
# 将客户端请求功能封装为类
class FtpServer:
    def __init__(self,connfd,d_FTP_PATH,u_FTP_PATH):
        self.connfd = connfd
        self.d_path = d_FTP_PATH
        self.u_path = u_FTP_PATH

    def do_list(self,d_u):
        # 获取文件列表
        if d_u == 'd':
            path = self.d_path
        elif d_u == 'u':
            path = self.u_path
        else:
            print("输入有误")

        file_list = os.listdir(path)
        if not file_list:
            self.connfd.send("该文件类别为空".encode())
            return
        else:
            self.connfd.send(b'OK')
        fs = ''
        for file in file_list:
            # 筛去隐藏文件和非普通文件
            if file[0] != '.' and \
                os.path.isfile(path + '/' + file):
                fs += file + '\n'
        self.connfd.send(fs.encode())

    def do_quit(self):
        return
    # 接收client发出的文件名
    # 打开读取该文件
    # 发送
    def do_download(self):
        file_name = self.connfd.recv(128).decode()
        file_name =  self.d_path + '/' +file_name
        print(file_name)
        try:
            f = open(file_name,'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
            self.connfd.send(data)
            f.close()

    def do_upload(self):
        print("文件上传中...")
        file_name = self.connfd.recv(128).decode()
        print("客户端要上传文件:",file_name)
        self.connfd.send(b"OK")
        sleep(0.1)
        file_name = self.d_path + '/' + file_name
        f = open(file_name, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()
        text = "上传成功!"
        self.connfd.send(text.encode())



# 客户端请求处理函数
def handle(connfd):

    type = connfd.recv(1024).decode()
    d_FTP_PATH = d_FTP + type
    u_FTP_PATH = u_FTP
    ftp = FtpServer(connfd,d_FTP_PATH,u_FTP_PATH)
    while True:
        data = connfd.recv(1024).decode()
        if not data or data[0] == "Q":
            ftp.do_quit()
        elif data[0] == "L":
            ftp.do_list('d')
        elif data == "D":
            ftp.do_list('d')
            ftp.do_download()
        elif data == "U":
            ftp.do_list('u')
            ftp.do_upload()



# 网络搭建
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port of 8000")
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            print("Quit.")
            return
        print("连接的客户端:",addr)
        # 创建的线程请求
        client = Thread(target=handle,args = (connfd,))
        client.daemon=True
        client.start()

if __name__ == "__main__":
    main()