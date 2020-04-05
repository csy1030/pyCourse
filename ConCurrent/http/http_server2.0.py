"""
    httpserver 2.0
    io 并发处理  select 多路复用
    基本的request解析
    使用类封装
"""
from socket import *
from select import select


# 将具体的http server功能封装
class HTTPServer:
    def __init__(self, server_address, static_dir):
        self.server_address = server_address
        self.static_dir = static_dir
        self.create_socket()
        self.bind()
        self.rlist = self.wlist = self.xlist = []

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    # 反复接收消息 io多路复用
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        self.rlist .append(self.sockfd)

        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    # 处理浏览器请求
                    self.handle(r)

    # 处理客户端请求
    def handle(self,connfd):
        request = connfd.recv(4096)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername,':',info)

        # info 分为访问网页和其他
        if info == '/' or info[-5] == '.html':
            self.get_html(connfd,info)
        else:
            pass

    # 处理网页
    def get_html(self,connfd,info):
        if info == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + info
        try:
            fd = open(filename)
        except Exception:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += '\r\n'
            responseBody = "<h1> Sorry, the page NOT FOUND </h1>"
        else:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = fd.read()
        # 无论那种情况都返回
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())



# 如何使用HTTPServer 类
if __name__ == "__main__":
    # 用户自己决定: 地址,内容
    server_addr = ('0.0.0.0', 8000)  # 服务器地址
    static_dir = "./static"  # 网页存放位置

    httpd = HTTPServer(server_addr, static_dir)  # 生成实例对象
    httpd.serve_forever()  # 启动服务
