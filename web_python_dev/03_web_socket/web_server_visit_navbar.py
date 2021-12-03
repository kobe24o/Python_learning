import socket
import re
from multiprocessing import Process  # 多线程

HTML_ROOT_DIR = './'  # 设置静态页面的根目录


class HTTPServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.listen(128)  # 最大连接数128
        print("服务器等待客户端连接...")
        while True:
            client_socket, client_addr = self.server_socket.accept()  # 建立客户端连接
            print("[%s, %s]用户连接上了" % client_addr)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            # 实例化线程，第一个参数调用函数 ，第二个参数 传递给前者的参数，元组形式
            handle_client_process.start()  # 开启线程
            client_socket.close()  # 关闭客户端socket

    def handle_client(self, client_socket):
        # 处理客户端请求
        request_data = client_socket.recv(1024)  # 接收客户端请求
        print("request data:", request_data)
        request_lines = request_data.splitlines()  # 按行分割
        for line in request_lines:
            print(line)  # 输出信息
        request_start_line = request_lines[0]  # 获取请求报文
        print("*" * 10)
        print(request_start_line.decode("utf-8"))
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        # 使用正则表达式，提取请求的文件名，group(1) 列出第一个括号匹配部分
        if file_name == "/":
            file_name = "/simple_navbar.html"
        try:
            # 尝试打开文件
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            # 读取文件失败，返回404
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: Michael server\r\n"
            response_body = "The file %s is not found! please check again!" % (HTML_ROOT_DIR + file_name)
        else:
            file_data = file.read()
            file.close()
            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: Michael server\r\n"
            response_body = file_data.decode("utf-8")
        # 拼接返回数据
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)
        client_socket.send(bytes(response, "utf-8"))  # 向客户端发送响应数据
        client_socket.close()  # 关闭客户端连接

    def bind(self, port):
        self.server_socket.bind(("127.0.0.1", port))


def main():
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == "__main__":
    main()
