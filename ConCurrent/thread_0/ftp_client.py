from socket import *
from time import sleep
import sys
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b'L') # 发送列表请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024)
            print("文件列表:")
            print(data.decode())
        else:
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用,再见")

    # 功能:输入需要下载的文件名
    # 发送出去
    # 接收server返回的文件
    # 写入操作
    def do_download(self):
        self.sockfd.send(b'D')
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024)
            print("文件列表:")
            print(data.decode())
        else:
            print(data)
        file_name = input("输入要下载的文件名:")
        self.sockfd.send(file_name.encode())

        f = open('/home/samyoung/PycharmProjects/PythonCourseP2/FTP/MyFile/'+file_name,'wb')
        while True:
            data = self.sockfd.recv(4096)
            if data == b'##':
                break
            f.write(data)
        f.close()
        print("下载成功!")

    # 上传操作
    def do_upload(self):
        self.sockfd.send(b'U')
        data = self.sockfd.recv(128)
        if data == b'OK':
            data = self.sockfd.recv(1024)
            print("文件列表:")
            print(data.decode())
        else:
            print(data)
        file_name = input("请输入要上传的文件名:")
        self.sockfd.send(file_name.encode())
        cmd = self.sockfd.recv(128)
        if cmd == b"OK":
            f = open('/home/samyoung/PycharmProjects/PythonCourseP2/FTP/MyFile/' + file_name, 'rb')
            while True:
                data = f.read()
                if not data:
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
                sleep(0.1)
            f.close()


        text = self.sockfd.recv(20).decode()
        print(text)





def request(sockfd):
    ftp = FtpClient(sockfd)
    while True:
        print("\n=========命令选项============")
        print("************list --> ls*********")
        print("**********download --> d ********")
        print("***********upload --> u**********")
        print("************quit --> q***********")
        cmd = input("输入命令:")
        if cmd == "ls":
            ftp.do_list()
        elif cmd == "d":
            ftp.do_download()
        elif cmd == "u":
            ftp.do_upload()
        elif cmd == 'q':
            ftp.do_quit()

# 网络链接
def main():
    ADDR = ('192.168.237.143',8000)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败")
        return
    else:
        print("""**********************
                 data     file    image
                 **********************
        """)
        type = input("请输入文件种类:")
        if type not in ['data','file','image']:
            print("输入有误")
            return
        else:
            sockfd.send(type.encode())
            request(sockfd)  # 发送具体请求

if __name__ == "__main__":
    main()