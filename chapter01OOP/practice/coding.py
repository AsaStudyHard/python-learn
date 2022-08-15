# description:
# date:         2022/8/12 19:14
# author        ZhuJunfei

class Car(object):

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def move(self):
        print('汽车在移动')

    def __str__(self):
        return f'我的颜色是 {self.color}，型号是 {self.model}'


class Animal(object):

    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def run(self):
        print(f'{self.name} 正在 奔跑')

    def get_age(self):
        print(f'{self.name} 今年 {self.age} 岁了')

    def eat(self):
        print(f'{self.name} 正在吃 {self.food}')

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, color = {self.color}, food = {self.food}'


if __name__ == "__main__":
    BMW_X9 = Car('red', 'x9')
    AUDI_A9 = Car('black', 'A9')

    print(f'BMW_X9 = {BMW_X9}')
    print(f"AUDI_A9 = {AUDI_A9}")

    car = Animal('car', 3, 'white', 'mouse')
    car.eat()
    durg_dog = Animal('durg_dog', 5, 'black', 'bad man')
    durg_dog.run()
