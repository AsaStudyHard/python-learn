"""
Description:  
Date:         2022/8/22 16:04
Author:       ZhuJunfei
"""
import threading

# 定义全局变量
g_num = 0
# 创建锁对象
lock = threading.Lock()


def sum_num1():
    global g_num
    # 循环一次给全局变量加1
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        g_num += 1
        # 释放锁
        lock.release()


def sum_num2():
    global g_num
    # 循环一次给全局变量加1
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动两个线程
    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()
    print('g_num', g_num)
