"""
Description:  多任务简介
Date:         2022/8/22 9:27
Author:       ZhuJunfei

Notice:
进程是操作系统分配资源的最小单位, 注意和线程做区分, 线程是cpu执行的基本单位

对于多进程而言, 我们使用python提供的multiprocess模块进行创建
multiprocess.Process(target=[], args=()),
    target 需要的是我们该进程要执行的代码
    args 是我们target 的函数需要的参数

进程的特性: 每一个进程之间的数据是不共享的
          python 进程可以使用多核,但是线程只能用单核 因为GIL(global interpreter lock)的存在
"""

import time
import multiprocessing


# 跳舞函数
def dance():
    for i in range(5):
        print('跳舞中...')
        time.sleep(1)


# 唱歌函数
def sing():
    for i in range(5):
        print('唱歌中...')
        time.sleep(1)


def func():
    """create multiprocess"""
    d_process = multiprocessing.Process(target=dance)
    s_process = multiprocessing.Process(target=sing)

    # start process
    d_process.start()
    s_process.start()


if __name__ == "__main__":
    func()
