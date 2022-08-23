"""
Description:  返回图片资源, 获取请求资源路径
Date:         2022/8/23 14:55
Author:       ZhuJunfei
"""
import os

from fastapi import FastAPI
import uvicorn
from fastapi import Response

app = FastAPI()

@app.get('/favicon.ico')
def get_favicon():
    """返回ico"""
    with open('./sources/html/favicon.ico', 'rb') as f:
        ico_data = f.read()

    return Response(ico_data, media_type='image\ico')

@app.get('/images/{image_path}')
def return_image(image_path):
    """返回images下的图片"""
    # 判断文件是否存在
    request_path = f'./sources/images/{image_path}'
    # 返回数据
    if os.path.isfile(request_path):
        with open(request_path, 'rb') as f:
            image_data = f.read()
        # 返回的数据类型是image, so media_type = ...
        return Response(image_data, media_type='image/jpg')

@app.get('/')
@app.get('/index')
@app.get('/index.html')
def index():
    """返回index.html页面"""
    with open('./sources/html/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    return Response(html_content, media_type='text\html')


if __name__ == "__main__":

    uvicorn.run(app, host='127.0.0.1', port=9090)
