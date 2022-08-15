"""
file name:    Demo04MoreIngeritance.py
date:         2022/8/13 15:25
author        ZhuJunfei
"""


class SmallDog(object):
    def eat(self):
        print('小口吃东西')

    def sleep(self):
        print('小憩一会')


class BigDog(object):
    def drink(self):
        print('大口喝水')

    def sleep(self):
        print('呼呼大睡')


# SuperDog 类定义时同时继承了 SmallDog 和 BigDog
class SuperDog(SmallDog, BigDog):
    def sleep(self):
        # 通过super(class, first argument).method_name(arguments)
        super(SmallDog, self).sleep()


if __name__ == "__main__":
    # 获取SuperDog继承关系
    superDog = SuperDog()
    superDog.sleep()