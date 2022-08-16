"""
Description:  装饰器的学习
Date:         2022/8/16 10:03
Author:       ZhuJunfei
"""
import time


def spend_time(func):
    def test_time(lalala):
        start_time = time.time_ns()
        func(lalala)
        end_time = time.time_ns()
        print(f'spent time: {((end_time - start_time) / 1000000.0):.3f} ms')

    return test_time


@spend_time  # func1 = spend_time(func1)
def func1(lalala):
    print('lalala = ', lalala)
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum


@spend_time  # func2 = spend_time(func2)
def func2():
    _res = 0
    for i in range(1000000):
        _res *= i
    return _res


def logger(filename:str):
    def outer_decorator(func):
        def decorator(*args, **kwargs):
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f'{func.__name__} 被调用了')
            return func()

        return decorator

    return outer_decorator


@logger('aaa.log')
# 等同于logger = logger('aaa.log') -> 此时的logger是outer_decorator, 然后python 解释器调用outer_decorator(login)将函数名传递进去
# 于是 login = logger(login)
def login():
    print('login is running')


@logger('bbb.log')
def register():
    print('register is running')


if __name__ == "__main__":
    # print(time.time_ns() / 1000000000.0)
    # func1('乌拉~')
    # func2()
    login()
    register()
