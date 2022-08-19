"""
Description:  代码题 第二题, 客户端：每隔1秒中，将客户端的时间发送给服务器
Date:         2022/8/19 20:12
Author:       ZhuJunfei
"""
import socket
import time
from datetime import datetime


def client():
    """
    client 代码实现
    Returns: not return

    step:
        1. 创建socket, 绑定ip协议(socket.AF_INET), 以及网络传输协议(socket.SOCKET_STREAM)
        2. 创建客户端与服务端的连接, 需要服务端的ip和port, 使用tuple作为参数
        3. 每隔一秒发送信息
        4. 关闭连接
    """

    # 1. 创建socket, 绑定ip协议(socket.AF_INET), 以及网络传输协议(socket.SOCKET_STREAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 创建客户端与服务端的连接, 需要服务端的ip和port, 使用tuple作为参数
    client_socket.connect(('192.168.0.164', 12345))

    # 3. 每隔一秒发送信息
    count = 0
    while True:
        # sleep unit is second
        # 10 second procedure ending
        time.sleep(1)
        count += 1
        # 设置发送内容
        content = f'第 {count} 次发送'
        # 获取代码执行时间的当前时间
        now_time = datetime.now()
        # 将时间格式化成字符串
        time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")

        client_socket.send(f'{content}, date = {time_str}'.encode())

        # 接收服务端信息
        service_content_b = client_socket.recv(1024)
        print(service_content_b.decode())

        if count == 5:
            break

    # 4. 关闭连接
    client_socket.close()


if __name__ == "__main__":
    client()
