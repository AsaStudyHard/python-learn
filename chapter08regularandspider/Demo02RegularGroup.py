"""
Description:  正则分组
Date:         2022/8/23 10:19
Author:       ZhuJunfei
"""

import re


def re_group():
    """正则分组的学习"""
    my_str = '<div><a href="https://www.itcast.cn" target="_blank">传智播客</a><p>Python</p></div>'
    regular = '<a.*>(.*)</a.*'
    content = re.search(regular, my_str)
    print('content = ', content.group(1))


if __name__ == "__main__":
    re_group()
