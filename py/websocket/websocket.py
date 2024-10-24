import asyncio  # 导入异步IO模块
import json  # 导入JSON处理模块
import websockets  # 导入WebSocket处理模块

# 存储所有连接的客户端
clients = set()  # 使用集合来存储客户端连接
messages = []  # 存储消息的列表

# 处理客户端消息
async def handle_client(websocket, path):  # 定义异步函数处理客户端连接
    clients.add(websocket)  # 将新客户端添加到连接客户端集合中
    try:
        async for message in websocket:  # 异步循环接收客户端消息
            data = json.loads(message)  # 将接收到的消息转换为JSON格式
            if data['type'] == 'message':  # 如果消息类型是普通消息
                # 确保消息包含所需的键
                if 'id' in data and 'username' in data and 'message' in data and 'timestamp' in data:
                    # 存储消息及其ID、用户名和时间戳
                    messages.append({'id': data['id'], 'username': data['username'], 'message': data['message'], 'userId': data['userId'], 'timestamp': data['timestamp']})
                    # 将消息广播给所有连接的客户端
                    await broadcast(json.dumps(data))
            elif data['type'] == 'revoke':  # 如果消息类型是撤回消息
                # 确保消息包含所需的键
                if 'id' in data and 'userId' in data:
                    # 根据ID查找消息
                    msg = next((msg for msg in messages if msg['id'] == data['id']), None)
                    if msg and msg['userId'] == data['userId']:
                        messages.remove(msg)  # 从消息列表中移除该消息
                        # 将撤回消息广播给所有连接的客户端
                        await broadcast(json.dumps(data))
    finally:
        clients.remove(websocket)  # 从连接客户端集合中移除客户端

async def broadcast(message):  # 定义异步函数广播消息
    if clients:  # 如果有连接的客户端
        await asyncio.wait([asyncio.create_task(client.send(message)) for client in clients])  # 异步发送消息给所有客户端

# 启动WebSocket服务器
async def start_server():  # 定义异步函数启动服务器
    async with websockets.serve(handle_client, "localhost", 6789):  # 启动WebSocket服务器，监听本地6789端口
        print("WebSocket server started")  # 打印服务器启动信息
        await asyncio.Future()  # 运行服务器直到手动停止

# 运行服务器
asyncio.run(start_server())  # 使用asyncio运行服务器