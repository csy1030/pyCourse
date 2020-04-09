from socket import *
from settings import *
from select import *
from urls import * # urls 模块
import json

frame_address = (frame_ip,frame_port)

# 应用类,将功能封装在类中
class Application:
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind(frame_address)

    def start(self):
        self.sockfd.listen(5)
        print("Listen to the port %d" % frame_port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []

        # select IO 多路复用监听请求
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for r in rs:
                # 如果是套接字表示有客户端连接
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    rlist.append(connfd)
                # 如果不是客户端连接,说明有人发消息
                else:
                    self.handle(r)
                    rlist.remove(r)
    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)   # 解析请求字典
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass

        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + '/index.html'
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            f = open(STATIC_DIR + '/404.html')
            return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}

    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return{'status':'200','data':func()}
        return {'status':'404','data':'Sorry...'}

if __name__ == '__main__':
    app = Application()
    app.start()
