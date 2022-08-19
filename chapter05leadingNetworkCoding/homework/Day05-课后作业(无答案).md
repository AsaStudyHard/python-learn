[TOC]

## Python进阶-day05

### 基础概念题

#### 1. 什么是IP地址？如何查看IP地址？

**参考答案:**

```bash
# 你的答案
IP: 地址就是计算机在互联网中的标识, 类似于现实生活中的门牌号

查看IP:
windows: ipconfig
linux: ifconfig
```

#### 2. 什么是端口？什么是端口号？知名端口号和动态端口号的范围是什么？

**参考答案:**

```bash
# 你的答案
端口: 就是数据进行交流通道的一种抽象, 因为不同的应用程序都需要同时进行通信, 如果放在同一个端口就会出现数据紊乱, 因此用端口来区分
端口号: 就是对计算机提供的端口的一种编号, 共有六万多个
知名端口: 0-1023
动态端口:除知名端口外的端口都是
```

#### 3. TCP 协议是什么？有什么特点？

**参考答案:**

```bash
# 你的答案
TCP: 就是互联网中数据传输的的一种协议, 大家只有遵循这种协议发送数据, 才会让数据被接收
特点: 面向连接的, 可靠的, 三次握手四次挥手
```

#### 4. 什么是socket？

**参考答案:**

```bash
# 你的答案
计算机底层给我们提供的一种封装工具, 使得我们在进行网络编程时不需要自己去写TCP的那些协议, 以及其他的一些协议, 简化了我们的开发
```

### 代码练习题

#### 1. 完成课上的代码【1-3遍】

#### 2. 编写一个TCP网络程序，功能如下：

1）客户端：每隔1秒中，将客户端的时间发送给服务器

```python
from datetime import datetime
# 获取代码执行时间的当前时间
now_time = datetime.now()
# 将时间格式化成字符串
time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
```

2）服务端：每次接收到客户端发送的时间，进行打印显示

**参考答案**：

1）客户端程序

```python
# 你的答案
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

```

2）服务端程序

```python
# 你的答案
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
```
