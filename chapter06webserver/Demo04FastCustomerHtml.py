"""
Description:  基于fastapi框架动态发挥html页面
Date:         2022/8/20 20:55
Author:       ZhuJunfei
"""
import os.path

from fastapi import FastAPI
import uvicorn
from fastapi import Response

api = FastAPI()


@api.get('/')
@api.get('/index')
@api.get('/index.html')
def index():
    """返回index.html页面"""
    with open('./sources/html/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    return Response(html_content, media_type='text\html')


@api.get('/images/{image_name}')
def get_images(image_name):  # 获取请求资源路径
    """返回images下的图片"""
    # 判断文件是否存在
    request_path = f'./sources/images/{image_name}'
    # 返回数据
    if os.path.isfile(request_path):
        with open(request_path, 'rb') as f:
            image_data = f.read()
        # 返回的数据类型是image, so media_type = ...
        return Response(image_data, media_type='image/jpg')


@api.get('/render')
@api.get('/render.html')
def render():
    with open('./sources/html/render.html', 'r', encoding='utf8') as f:
        html_data = f.read()
    print('hello world')
    return Response(html_data, media_type='text\html')

@api.get('/favicon.ico')
def get_favicon():
    """返回ico"""
    with open('./sources/html/favicon.ico', 'rb') as f:
        ico_data = f.read()

    return Response(ico_data, media_type='image\ico')


if __name__ == '__main__':
    # 热更新我们这里就不演示了
    uvicorn.run("Demo04FastCustomerHtml:api", host='127.0.0.1', port=8080, reload=True)
