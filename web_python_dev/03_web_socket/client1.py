import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
print("已经连接到服务器")
info = ''
while info != 'byebye':
    send_data = input("请输入要发送的数据：")
    s.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = s.recv(1024).decode()
    print("收到服务器的数据：", info)
s.close()