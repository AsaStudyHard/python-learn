"""
Description:  主进程结束的同时结束子进程的方式
Date:         2022/8/22 11:20
Author:       ZhuJunfei

Notice:
    可以使用2种方式:
    1. 设置子进程为守护进程, 这样主进程执行结束, 子进程也会逐渐的结束
    2. 在主进程中直接 打断 子进程
"""
import multiprocessing
import time


def func():
    for i in range(3):
        print('child process execution')
        time.sleep(1)


if __name__ == "__main__":
    child_process = multiprocessing.Process(target=func)
    # child_process.daemon = True  # set daemon

    child_process.start()
    time.sleep(1)
    print('main process finished')
    child_process.terminate()  # Direct interrupt process
