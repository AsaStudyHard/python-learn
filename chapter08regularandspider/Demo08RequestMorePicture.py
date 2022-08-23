"""
Description:  get more pictures
Date:         2022/8/23 17:14
Author:       ZhuJunfei
"""

import re
import requests


def get_more_pics() -> None:
    # 模拟客户端发送请求
    url = 'http://127.0.0.1:8080'
    response_data = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'})
    print(response_data.content.decode())

    # 从网页中获取img的请求路径, 然后进行批量下载
    regular = r'<img src=".+?/(.*?)"'
    # ['images/0.jpg', ...] 匹配出这样的数据
    image_paths = re.findall(regular, response_data.content.decode())
    print(image_paths)

    # 开始grab
    for i in image_paths:
        image_data = requests.get(url + '/' + i, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'})

        # 下载
        down_path = 'spider_data/' + i.split('/')[1]
        with open(down_path, 'wb') as f:
            f.write(image_data.content)


if __name__ == "__main__":
    get_more_pics()
