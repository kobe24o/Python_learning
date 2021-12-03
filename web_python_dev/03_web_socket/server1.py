import socket

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print('建立连接：', addr)
info = sock.recv(1024).decode()
while info != "byebye":
    if info:
        print("收到信息：", info)
    send_data = input("请输入发送的信息：")
    sock.send(send_data.encode())
    if send_data == "byebye":
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()