"""
file name:    Demo03PickleLearn.py
date:         2022/8/15 16:03
author        ZhuJunfei
"""

import pickle


def my_dumps(file_path, date):
    with open(file_path, 'wb') as f:
        content = pickle.dumps(date)
        f.write(content)


def my_loads(file_path):
    with open(file_path, 'rb') as f:
        content = pickle.load(f)
        print(type(content))
        print(*content)


def pickle_learn():
    file_path = 'test.pickle'
    date = ['你好啊', 123, {'name': 'zs'}]
    # dumps进行序列化
    my_dumps(file_path, date)

    # loads进行反序列化
    my_loads(file_path)


if __name__ == "__main__":
    pickle_learn()
