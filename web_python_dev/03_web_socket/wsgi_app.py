# wsgi 应用程序
def app(environ, start_response):
    # 响应信息
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ, start_response)
    file_name = environ['PATH_INFO'][1:] or 'simple_navbar.html'
    print(file_name)
    HTML_ROOT_DIR = './'
    try:
        # 打开文件
        file = open(HTML_ROOT_DIR + file_name, 'rb')
    except IOError:
        # 响应异常
        response_body = "{} not found".format(HTML_ROOT_DIR + file_name)
    else:
        # 读取文件
        file_data = file.read()
        file.close()
        # 构造响应数据
        response_body = file_data.decode('utf-8')
    return [response_body.encode('utf-8')]  # 返回数据