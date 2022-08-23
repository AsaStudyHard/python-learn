"""
Description:  
Date:         2022/8/23 15:14
Author:       ZhuJunfei
"""

import requests


def quick_start():
    url = 'https://www.4399.com'
    response = requests.get(url)

    print(response.content.decode('gbk'))


if __name__ == "__main__":
    quick_start()
