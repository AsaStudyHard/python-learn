"""
Description:  parent and child process
Date:         2022/8/22 10:32
Author:       ZhuJunfei

Notice:
    子父进程: 对于父进程而言他可以有n个子进程,在默认的状态下, 父进程会等子进程执行结束然后自己才会结束
    可以通过os.getpid()获取当前进程的 id, os.getppit() 获取该进程的父进程id

    但似乎没啥用啊, 也不是, 在我们目前学习的技术栈中, 没有使用到这个东西的概念
"""
import os
import time
import multiprocessing


# 跳舞函数
def dance(amount: int) -> None:
    print("dance: ", os.getpid(), os.getppid())
    for i in range(amount):
        print('跳舞中...')
        time.sleep(1)


# 唱歌函数
def sing(amount: int) -> None:
    print("sing: ", os.getpid(), os.getppid())
    for i in range(amount):
        print('唱歌中...')
        time.sleep(1)


def func():
    """开启多进程"""
    amount = 3
    d_process = multiprocessing.Process(target=dance, args=(amount, ))
    s_process = multiprocessing.Process(target=sing, kwargs={'amount': amount})

    # start
    d_process.start()
    s_process.start()


if __name__ == "__main__":
    print("main: ", os.getpid(), os.getppid())
    func()
