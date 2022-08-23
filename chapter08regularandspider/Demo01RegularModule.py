"""
Description:  正则模块的学习
Date:         2022/8/23 9:45
Author:       ZhuJunfei
"""

import re


def match_search_findall():
    my_str = 'abc_123_DFG_456'
    # match 从头开始匹配
    # match = re.match(r'\d{2}', my_str)
    match = re.match(r'bc', my_str)

    print(f'match = {match}')  # None

    # search 扫描整体, 选出第一个符合要求的子串
    # search = re.search(r'\d{3}', my_str)
    search = re.search(r'bc', my_str)
    print(f'search = {search.group()}')

    # findall 找到所有符合要求的子串
    findall = re.findall(r'\d{3}', my_str)
    print(f'findall = {findall}')


if __name__ == "__main__":
    match_search_findall()
