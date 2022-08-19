"""
Description:  网络编程客户端代码实现
Date:         2022/8/19 19:52
Author:       ZhuJunfei
"""
import socket


def client():
    """
    客户端代码实现

    step:
        1. 创建socket对象, 设置使用的ip和网络传输协议
        2. 与服务端创建连接, 绑定端口和目标主机ip
        3. 发送信息, 接收信息
        4. 关闭socket
    """
    # 1. 创建socket对象, 设置使用的ip和网络传输协议
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 与服务端创建连接, 绑定端口和目标主机ip
    client_socket.connect(('127.0.0.1', 44111))

    # 3. 发送信息, 接收信息
    send_info = input('请输入要发送的数据: ')
    client_socket.send(send_info.encode())

    # 接受服务端的数据
    recv_content_b = client_socket.recv(1024)
    print('服务端返回的数据为: ', recv_content_b.decode())

    # 4. 关闭socket
    client_socket.close()


if __name__ == "__main__":
    client()
