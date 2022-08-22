"""
Description:  带有参数的进程的调用
Date:         2022/8/22 20:38
Author:       ZhuJunfei
"""

import multiprocessing


def customer_loop(counter: int) -> None:
    for i in range(counter):
        print(f'i = {i + 1}')


def start_process():
    counter = 10
    args_process1 = multiprocessing.Process(target=customer_loop, args=(counter,))
    args_process2 = multiprocessing.Process(target=customer_loop, kwargs={'counter': counter})

    # start processes
    args_process1.start()
    args_process2.start()


if __name__ == "__main__":
    start_process()
