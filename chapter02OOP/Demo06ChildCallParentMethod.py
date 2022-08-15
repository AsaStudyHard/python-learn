"""
file name:    Demo06ChildCallParentMethod.py
date:         2022/8/13 15:02
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

    def show_info(self):
        """子类中的info"""
        print("This is Dog class show info")
        # 方法1 父类名.同名方法(self, 形参1, ....) 父类名改了, 子类代码需要修改, 不够灵活
        Animal.show_info(self)
        # 方法2 灵活, 但是代码多
        super(Dog, self).show_info()
        # 方法3 推荐的写法
        super().show_info()


if __name__ == "__main__":
    dog = Dog()
    dog.show_info()


