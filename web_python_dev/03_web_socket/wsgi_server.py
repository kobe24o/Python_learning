# WSGI 服务器
from wsgiref.simple_server import make_server
from wsgi_app import app

# 创建一个服务器，IP地址为空，端口号为8000，处理函数是app
httpd = make_server('', 8000, app)
print('Serving HTTP on port 8000...')
httpd.serve_forever()  # 开始监听HTTP请求
