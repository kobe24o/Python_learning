import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP套接字
s.bind(('127.0.0.1', 1314))
print('绑定 UDP服务 到 1314 端口')
data, addr = s.recvfrom(1024) # 收到的数据是 byte 类型
data = float(data) * 1.8 + 32
send_data = "转换后的温度（华氏温度）：" + str(data)
print("从%s:%s收到请求数据" % addr)
s.sendto(send_data.encode('utf-8'), addr) # 发送数据给客户端
s.close()