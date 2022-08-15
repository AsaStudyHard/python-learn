"""
file name:    Demo02PrivateLearn.py
date:         2022/8/13 10:41
author        ZhuJunfei
"""


class Dog(object):
    def __init__(self, _name, _age):
        self.name = _name
        self.__age = _age

    def get_age(self):
        """
        返回 private age
        Returns:
                age
        """
        return self.__age

    def set_age(self, _age):
        if (_age > 200):
            print('你家狗成精了')
            return
        elif (_age < 0):
            print('这狗越活越年轻')
            return
        else:
            self.__age = _age

    def __show_age(self):
        print("dog age = ", self.__age)


def custom_add(num1: int, num2: int) -> int:
    return num1 + num2

if __name__ == "__main__":
    dog = Dog('旺旺', 5)
    # print(dog.get_age())
    # dog.set_age(2000)
    # dog.set_age(15)
    # print(dog.get_age())
    # print("dog private age = ", dog._Dog__age)
    # 调用私有方法
    # dog._Dog__show_age()
    print()

