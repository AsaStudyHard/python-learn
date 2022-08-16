"""
file name:    Demo01Closure.py
date:         2022/8/16 9:14
author        ZhuJunfei
"""


def outer():
    count = 0

    def inner(a, b):
        nonlocal count
        count += 1
        return a + b

    return inner


if __name__ == '__main__':
    add = outer()
    sum = add(1, 2)
    print(sum)
