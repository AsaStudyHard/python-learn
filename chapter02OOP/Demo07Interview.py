"""
file name:    Demo07Interview.py
date:         2022/8/13 15:59
author        ZhuJunfei
"""


class A(object):
    def func(self):
        print("A")


class B(A):
    def func(self):
        super().func()
        print("B")


class C(A):
    def func(self):
        super().func()
        print('C')


class D(B, C):
    def func(self):
        super().func()
        print('D')


if __name__ == "__main__":
    d = D()
    d.func()
