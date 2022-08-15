"""
description:  define class
date:         2022/8/12 9:40
author        ZhuJunfei
"""


class Dog(object):

    def eat(self):
        print("dog eating")

    def dark(self):
        print("dog is darking")


if __name__ == "__main__":
    wangcai = Dog()  # 创建对象
    wangcai.eat()  # 调用方法
    wangcai.dark()

    # add some attribute
    wangcai.name = '旺财'
    wangcai.age = 9
    print(f'dog name = {wangcai.name}, In the {wangcai.age}, it is died')



