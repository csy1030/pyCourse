
from socket import *
import sys
from threading import Thread
from config import *
import re,json

# 服务器地址
ADDR = (HOST,PORT)

# 和WebFrame通信
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
    # 将请求字典转换为json数据发送
    data = json.dumps(env)
    s.send(data.encode())
    # 接收webframe数据,接收json
    data = s.recv(4096 * 100).decode()
    return json.loads(data) # 返回数据字典

# 封装httpserver基本功能
class HTTPServer:
    def __init__(self,addr):
        self.addr = addr
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    def bind(self):
        self.sockfd.bind(self.addr)
        self.ip = self.addr[0]
        self.port = self.addr[1]

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen to the port %d"%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print('Connected from',addr)
            client = Thread(target=self.handle(connfd),args=((connfd,)))
            client.setDaemon(True)
            client.start()

    def handle(self,connfd):
        print("Request from:", connfd.getpeername())
        request = connfd.recv(4096).decode()  # 接收http请求
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"  # 匹配到   GET /
        try:
            env = re.match(pattern,request).groupdict()
            print(env)
        except:
            connfd.close()
            return

    def response(self,connfd,data):
        if data['status'] == '200':
            f = open('index.html')
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type: text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type: text/html\r\n"
            responseHeaders += '\r\n'
            responseBody += data['data']
        elif data['status'] == '500':
            pass


        connfd.send((responseHeaders + responseBody).encode())

if __name__ == "__main__":
    http = HTTPServer(('127.0.0.1',8000))
    http.serve_forever()
