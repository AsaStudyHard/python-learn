"""
file name:    homework.py
date:         2022/8/13 18:14
author        ZhuJunfei
"""


# 1.定义一个人的基类,类中要有初始化方法,方法中初始化人的姓名,年龄两个属性.
class Person(object):
    def __init__(self, _name, _age):
        # 3.将类中的姓名和年龄属性私有化.
        self.__name = _name
        self.__age = _age

    # 2.提供\__str__方法，返回姓名和年龄信息.
    def __str__(self):
        return f'name = {self.name}, age = {self.age}'

    # 4.提供获取私有属性的方法.
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # 5.提供可以设置私有属性的方法.
    def set_name(self, _name: str):
        self.__name = _name

    def set_age(self, _age: int):
        # 6.设置年龄时限制范围(0-100).
        if 0 < _age < 100:
            self.__age = _age


'''
请写出一个Car作为基类,BMW类继承于Car类,基类中有`__init__`方法(包含name,color).
创建Car和BMW的实例对象, 并分别打印对象的2个属性值
'''


class Car(object):
    def __init__(self) -> None:
        self.name = 'car'
        self.color = 'orange'


class BMW(Car):
    def __init__(self) -> None:
        self.name = '宝马'
        self.color = 'white'


"""
1. 动物:吃,喝,跑,叫
2. 猫的叫声是"喵喵"
3. 狗的叫声是"旺旺"
4. 猫狗继承于动物,并且有猫、狗有自己的属性.
"""


class Animal(object):
    def running(self) -> None:
        print('animal is running')


class Dog(Animal):
    def __init__(self) -> None:
        self.__name = "京巴狗"

    def running(self) -> None:
        print(f'{self.__name} is running')

    def eating(self) -> None:
        print(f'{self.__name} is eating')


class Cat(Animal):
    def __init__(self) -> None:
        self.__name = "波斯猫"

    def running(self) -> None:
        super().running()
        print(f'{self.__name} is running')

    def eating(self) -> None:
        print(f'{self.__name} is eating')


def method_name():
    car = Car()
    bmw = BMW()
    print(f'car: \n \t{car.name}, {car.color}')
    print(f'bmw: \n \t{bmw.name}, {bmw.color}')


class Animal2(object):
    def running(self):
        print('animal is running')


class Kitty(Animal2):

    def running(self):
        Animal2.running(self)
        print('kitty is running')

    def eat(self):
        print('kitty is eating')


def method_name2():
    cat = Cat('小花猫')
    dog = Dog('小白狗')
    cat.cry()
    cat.drinking()
    dog.cry()


class CustomClass(object):
    def __init__(self, _name: str) -> None:
        self.__name = _name

    def set_name(self, _name: str) -> None:
        if 0 < len(_name) < 10:
            self.__name = _name

    def __str__(self) -> str:
        return f'name = {self.__name}'


class Man(object):
    def __init__(self, _name: str, _age: int) -> None:
        self.__name = _name
        self.__age = _age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, _age: int) -> None:
        if 0 < _age < 100:
            self.__age = _age
        else:
            print('输入的年龄错误')

    def set_name(self, _name: str) -> None:
        self.__name = _name

    def __str__(self) -> str:
        return f'{self.__name}:{self.__age}'


class Horse(object):
    def eat(self):
        print('马吃草')


class Donkey(object):
    def eat(self):
        print('驴吃草')


class Mule(Horse, Donkey):
    def eat(self):
        print('骡子先吃')
        super(Mule, self).eat()
        super(Horse, self).eat()


def method_name3():
    kitty = Kitty()
    kitty.running()
    kitty.eat()


def method_name4():
    customClass = CustomClass('你的背包')
    print(customClass)
    customClass.set_name('终有一天还是会破烂')
    print(customClass)


def method_name5():
    man1 = Man('张三', 20)
    print(man1)
    man1.set_age(30)
    print(man1)
    man2 = Man('李四', 30)
    print(man2)


def let_run(animal: Animal):
    # 多态的体现
    animal.running()


def method_name6():
    mule = Mule()
    mule.eat()


if __name__ == "__main__":
    # method_name()
    # method_name2()
    # method_name3()
    # method_name4()
    # method_name5()
    # method_name6()
    cat = Cat()
    dog = Dog()
    let_run(cat)
    cat.eating()
    let_run(dog)
    dog.eating()
