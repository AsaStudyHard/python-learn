"""
Description:  深浅拷贝的学习
Date:         2022/8/16 15:47
Author:       ZhuJunfei
"""


def reference_review():
    lao_wang = [100, 100]
    wife = list.copy(lao_wang)
    print(id(lao_wang[0]), id(wife[0]))


if __name__ == "__main__":
    import copy

    # 简单元祖
    my_tuple1 = (2, 3, 5)

    # 浅拷贝
    my_tuple3 = copy.copy(my_tuple1)

    print('id(my_tuple1)：', id(my_tuple1))
    print('id(my_tuple3)：', id(my_tuple3))
