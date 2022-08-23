"""
Description:  贪婪模式和非贪婪模式的学习
Date:         2022/8/23 11:30
Author:       ZhuJunfei
"""

import re


def greedy_model():
    my_str = '<div>test1</div><div>test2</div>'
    # resist your greedy

    # 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
    greedy_data = re.match('<div>.*</div>', my_str)
    print(greedy_data)
    print(greedy_data.group())  # 获取整个正则表达式匹配的内容

    # non greedy model, 在量词后面加一个 ?, 就匹配一个
    greedy_data = re.match('<div>.*?</div>', my_str)
    print(greedy_data)
    print(greedy_data.group())  # 只获取一个

    my_str = 'abvc'
    data = re.findall('.*', my_str)
    print(data)


if __name__ == "__main__":
    greedy_model()
