import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080
s.connect((host, port))
while True:
    send_data = input("请输入要发送的数据：")
    if send_data == "exit":
        break
    s.send(send_data.encode("utf-8"))
    recvData = s.recv(1024).decode("utf-8")  # 最大接收1024字节
    print("接收到的数据：", recvData)
s.close()