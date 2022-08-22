"""
Description:  进程的注意事项
Date:         2022/8/22 20:42
Author:       ZhuJunfei

Notice:
    进程之间的数据是不共享的
    进程之间的运行时相互独立的
    主进程会等待所有的子进程执行结束再结束
"""

import multiprocessing
import time

g_list = list()


def append_ele_g():
    """像g_list中添加元素"""
    for i in range(10):
        g_list.append(i)

    print(f'In child process g_list content = {g_list}')  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def start_process():
    prc1 = multiprocessing.Process(target=append_ele_g)
    prc1.start()


if __name__ == "__main__":
    start_process()
    time.sleep(1)
    print('main process finished')
    print(f'In main process g_list content = {g_list}')  # []


