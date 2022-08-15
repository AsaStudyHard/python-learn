"""
description:  self, and megic method
date:         2022/8/12 10:36
author        ZhuJunfei
"""


class Dog(object):

    def show_self(self):
        print(f"in class self id = {id(self)}")


class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def show_info(self):

        if self.gender == "male":
            print(f"the man name is {self.name}")
        if self.gender == 'female':
            print(f"the woman name is {self.name}")
        if self.gender not in ['male', 'female']:
            print(f"the human name is {self.name}")

    def __str__(self):
        return f'name = {self.name}, gender = {self.gender}'


class Person2(object):
    count = 0

    def __init__(self):
        print(f"input {Person2.count} name, please")
        self.name = input()
        Person2.count += 1

    def show_info(self):
        print(f'this is {Person2.count} dog, it name is {self.name}')


def test03():
    alice = Person('Alice', 'female')
    alice.show_info()
    bob = Person('Bob', 'male')
    bob.show_info()


def test04():
    lilei = Person("李雷", 21)
    hanmeimei = Person("韩梅梅", 22)

    print(f"lilei info = {lilei}")
    print(f"hanmeimei info = {hanmeimei}")


if __name__ == "__main__":
    """
    wangcai = Dog()
    print(f'outside class wangcai id = {id(wangcai)}')
    wangcai.show_self()

    dahei = Dog()
    print(f'dahei id = {id(dahei)}')
    dahei.show_self()
    """
    # test03()
    test04()
