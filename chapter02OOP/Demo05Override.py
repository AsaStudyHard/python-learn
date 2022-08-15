"""
file name:    Demo05Override.py
date:         2022/8/13 14:33
author        ZhuJunfei
"""


class Animal(object):
    def __init__(self):
        print("This is animal init")

    def show_info(self):
        print("This is animal show info method")


class Dog(Animal):
    def __init__(self):
        print("This is dog init")


if __name__ == "__main__":
    dog = Dog()
    dog.show_info()
