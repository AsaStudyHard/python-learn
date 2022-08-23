"""
Description:  获取网页图片
Date:         2022/8/23 15:45
Author:       ZhuJunfei
"""

import requests


def get_image():
    url = 'https://cdnb.artstation.com/p/assets/images/images/050/362/115/4k/anton-fadeev-tm-explorationslibrary4-green-2000.jpg?1654675901&dl=1'
    # url = 'https://t7.baidu.com/it/u=1819248061,230866778&fm=193&f=GIF'

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'})
    with open ('image.jpg', 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    get_image()
