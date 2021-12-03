import socket

host = "127.0.0.1"  # IP
port = 8080  # 端口
web = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web.bind((host, port))  # 绑定端口
web.listen(5)  # 监听,最多5个连接
print("服务器启动成功, 等待客户端连接...")
while True:
    conn, addr = web.accept()  # 建立客户端连接
    print("客户端连接成功, 地址:", addr)
    data = conn.recv(1024)  # 获取客户端发送的数据
    print("接收到客户端发送的数据:", data.decode())
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World, Michael!')  # 发送数据给客户端
    conn.close()  # 关闭连接
    print("客户端连接关闭")
