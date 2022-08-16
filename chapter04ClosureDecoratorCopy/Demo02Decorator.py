"""
Description:  装饰器的学习
Date:         2022/8/16 10:03
Author:       ZhuJunfei
"""
import time


def func1():
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum


def func2():
    _res = 0
    for i in range(1000000):
        _res *= i
    return _res


def spend_time(func):
    def test_time():
        start_time = time.time_ns()
        func()
        end_time = time.time_ns()
        print(f'spent time: {((end_time - start_time) / 1000000.0):.3f} ms')
    return test_time


if __name__ == "__main__":
    # print(time.time_ns() / 1000000000.0)
    func1 = spend_time(func1)
    func1()
    func2 = spend_time(func2)
    func2()