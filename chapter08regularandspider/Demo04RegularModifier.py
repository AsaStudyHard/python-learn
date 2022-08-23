"""
Description:  正则修饰符的学习
Date:         2022/8/23 11:16
Author:       ZhuJunfei
"""

import re


def three_modifier():
    """三种matching learn"""
    # I: 忽略大小写
    my_str = 'aB'
    match = re.match('ab', my_str)
    print(match)  # None
    match = re.match('ab', my_str, flags=re.I)
    print(match)  # aB

    # M: 可以多行匹配
    my_str = 'aabb\nbbcc'
    m_match = re.match(r'^\w{4}$', my_str)
    print(m_match)  # None
    m_match = re.match(r'^\w{4}$', my_str, flags=re.M)
    print(m_match)  # aabb

    # S使得 . 可以matching \n
    my_str = '\nabc'
    s_match = re.match(r'.', my_str)
    print(s_match)  # None
    s_match = re.match(r'.', my_str, flags=re.S)
    print(s_match)  # \n


if __name__ == "__main__":
    three_modifier()
