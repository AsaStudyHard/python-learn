"""
Description:  FastAPI hello learn
Date:         2022/8/20 16:51
Author:       ZhuJunfei

question:
1. 什么是HTTP协议？
HTTP: 超文本传输协议, 一种应用层的协议, 规定了请求和响应的数据格式, 也就是按什么规则发送我们的数据.
需要和TCP做区分, TCP是作用在传输层的协议, 用于数据在网络之间的传递, 而不在乎数据的格式是否正确

2. web服务器有什么用？
web服务器, 一般就是一台机器, 专门接收我们客户端的请求, 然后调用该请求对应的web框架中的方法, 返回响应

3. 画图：浏览器请求百度过程的

"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/index')
def hello_world():
    return 'hello, world'


if __name__ == "__main__":
    print(hello_world())
    # uvicorn 是web服务器, fastAPI是一个web框架
    uvicorn.run(app, host='127.0.0.1', port=8080)
