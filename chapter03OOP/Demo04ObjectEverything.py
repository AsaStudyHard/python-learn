"""
file name:    Demo04ObjectEverything.py
date:         2022/8/15 16:17
author        ZhuJunfei
"""


class Dog(object):
    pass


def func():
    print('object.__class__', object.__class__)
    print('object.__class__', type.__class__)
    print('object.__bases__', object.__bases__)
    print('type.__bases__', type.__bases__)

    dog = Dog()
    print('dog.__class__', dog.__class__)


def func2():
    print('list.__class__: \t', list.__class__)
    print('tuple.__class__: \t', tuple.__class__)
    print('dict.__class__: \t', dict.__class__)
    print('-' * 20)
    print('list.__bases__: \t', list.__bases__)
    print('tuple.__bases__: \t', tuple.__bases__)
    print('dict.__bases__: \t', dict.__bases__)
    print('-' * 20)
    mylist = list([1, 2, 3])
    print('mylist.__class__: \t', mylist.__class__)
    print('mylist.__bases__: \t', mylist.__bases__)

if __name__ == "__main__":
    # func()
    func2()