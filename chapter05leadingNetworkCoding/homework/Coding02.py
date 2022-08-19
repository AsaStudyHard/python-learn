"""
Description:  服务端代码实现
Date:         2022/8/19 20:24
Author:       ZhuJunfei
"""
import socket


def service():
    """
    service coding

    Returns: not return
    step: total 7
    1. 创建服务端socket, 绑定ip(af_inet) 和 网络传输协议(socket_stream)
    2. 绑定主机ip和port
    3. 设置监听, 也就是最大连接数 listen
    4. 等待接收客户端的请求, 获取客户端socket, address info
    5. 获取客户端传递的信息,
    6. 返回对应的信息
    7. 关闭连接, 2个socket
    """
    # 1. 创建服务端socket, 绑定ip() 和 网络传输协议()
    service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定主机ip和port, 参数以元组的形式进行包裹
    service_socket.bind(('192.168.0.164', 12345))

    # 3. 设置监听, 也就是最大连接数 listen
    service_socket.listen(127)

    # 4. 等待接收客户端的请求, 获取客户端socket, address info, 相当于客户端执行connect
    client_socket, client_ads_info = service_socket.accept()

    # 源源不断接收信息
    try:
        while True:
            # 5. 获取客户端传递的信息
            client_content_b = client_socket.recv(1024)
            # print(client_socket)
            print(f'client info = {client_ads_info}, send data is {client_content_b.decode()}')

            # 6. 返回对应的信息
            client_socket.send('服务端已经接受到信息'.encode())
    except ConnectionAbortedError as e:
        print('连接中断')
        client_socket.close()
        service_socket.close()


if __name__ == "__main__":
    service()
