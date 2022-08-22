"""
Description:  终止子线程
Date:         2022/8/22 21:13
Author:       ZhuJunfei

Notice:
    将子线程设置为daemon线程, 则在主线程执行完毕后, 子线程也会慢慢的死亡
"""

import time
import threading


def print_num():
    for i in range(10):
        print('i = ', i)
        time.sleep(0.3)
    print('child thread execution finished')


def start_threading():
    th1 = threading.Thread(target=print_num)
    th1.daemon = True
    th1.start()


if __name__ == "__main__":
    start_threading()
    time.sleep(0.5)
    print('main thread execution finished')
