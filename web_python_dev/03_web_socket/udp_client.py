import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("请输入要转换的摄氏温度：")
s.sendto(data.encode(), ("127.0.0.1", 1314))
print(s.recv(1024).decode())
s.close()