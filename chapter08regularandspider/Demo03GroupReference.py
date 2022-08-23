"""
Description:  分组引用
Date:         2022/8/23 10:44
Author:       ZhuJunfei
"""

import re


def group_reference():
    my_str = '123   123    123'
    regular = r'(?P<num>\d+)\s*(?P=num)\s*(?P=num)'
    search = re.search(regular, my_str)
    print(search)
    print('search.group(1) = ', search.group())
    # print('search.group(2) = ', search.group(2))
    # print('search.group(3) = ', search.group(3))


if __name__ == "__main__":
    group_reference()
