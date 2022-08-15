"""
file name:    Demo01ClassAttributeStart.py
date:         2022/8/15 9:33
author        ZhuJunfei
"""


class Dog(object):
    __count = 0

    @classmethod
    def show_dog_count(cls):
        print('current dog count = ', cls.__count)

    def __init__(self):
        self.__name = 'dog'
        Dog.__count += 1
        print('dog initialize')




if __name__ == "__main__":
    dog1 = Dog()
    Dog.show_dog_count()
    dog2 = Dog()
    Dog.show_dog_count()

