"""
file name:    Demo03SingleInheritance.py
date:         2022/8/13 11:09
author        ZhuJunfei
"""


class Parent(object):
    def __init__(self):
        self.money = 10000000

    def show_money(self):
        print(f'money = {self.money}')


class Child(Parent):
    pass


if __name__ == "__main__":
    ch1 = Child()
    ch1.show_money()
    # 查看类的继承关系
    print(Child.__mro__)