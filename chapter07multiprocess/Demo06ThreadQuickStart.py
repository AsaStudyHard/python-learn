"""
Description:  线程的快速入门
Date:         2022/8/22 21:05
Author:       ZhuJunfei

Notice:
    1. 线程是cpu执行的最小单元
    2. 线程会共享进程的数据
    3. 线程切换的开销远远小于进程

    使用threading.Thread()创建线程
    .start()启动线程
    同时我们可以给线程传递参数
"""

import time
import threading


def sing(counter: int) -> None:
    for i in range(counter):
        print('sing~')
        time.sleep(0.4)


def dance(counter: int) -> None:
    for i in range(counter):
        print('dance~')
        time.sleep(0.4)


def start_thread():
    counter = 10

    sing_thread = threading.Thread(target=sing, args=(counter,))
    dance_thread = threading.Thread(target=dance, kwargs={'counter': counter})

    sing_thread.start()
    dance_thread.start()


if __name__ == "__main__":
    start_thread()
