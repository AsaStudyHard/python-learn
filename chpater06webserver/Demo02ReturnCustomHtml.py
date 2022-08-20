"""
Description:  return customer html
Date:         2022/8/20 11:26
Author:       ZhuJunfei
TODO: 修改为多任务的服务器, 该如何做?

"""
import os
import socket


def service():
    """
    服务端具体代码实现
    Returns: not return
    """
    # 1. 创建服务端的socket, 使用哪一种ip协议, 以及使用哪一种网络传输协议 TCP,
    # socket.AF_INET代表ipv4,
    # socket.SOCK_STREAM代表TCP协议
    # 这2个变量不过是socket定义的宏常量而已
    service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 和服务端的端口进行绑定 bind(tuple(address, ip))
    service_socket.bind(('127.0.0.1', 8080))

    # 3. 设定我们能够接收的请求数 listen()
    service_socket.listen(127)

    while True:
        # 4. 等待接收客户端的请求, 然后获取于该客户端对应的socket
        client_socket, client_adr_info = service_socket.accept()

        # 5. 接收客户端的数据, 字节码形式, 一次接收1024个字节的数据, 如果内容超过我们限定的呢? 晚上测试一下
        client_content_b = client_socket.recv(1024)
        # 解码输出
        client_content = client_content_b.decode()
        print("client transfer info = ", client_content)

        # 6. 返回客户端响应
        # 设置响应报文
        response_line = b'HTTP/1.1 200 ok\r\n'
        response_header = b'Server: diao; \r\nContent-type: text/html;charset=utf-8\r\n'

        # 获取用户传递的资源路径
        client_content_list = client_content.split('\r\n')
        request_line = client_content_list[0]
        request_resource = request_line.split(' ')[1]

        html_file_path = './sources/html' + request_resource
        # 发送网页数据
        if request_resource == '/':
            html_file_path = './sources/html/gdp.html'

        if os.path.isfile(html_file_path):
            with open(html_file_path, 'rb') as f:
                response_body = f.read()
        else:
            html_file_path = './sources/html/notFound.html'
            with open(html_file_path, 'rb') as f:
                response_body = f.read()

        # 访问图片数据
        if '.jpg' in request_resource:
            # 表示请求图片资源
            html_file_path = './sources' + request_resource
            with open(html_file_path, 'rb') as f:
                response_body = f.read()

        print('---> ', html_file_path)
        send_info = response_line + response_header + b'\r\n' + response_body

        # 将字符串encode, 进行返回
        client_socket.send(send_info)

        # 7. 关闭socket连接
        client_socket.close()


if __name__ == "__main__":
    service()
