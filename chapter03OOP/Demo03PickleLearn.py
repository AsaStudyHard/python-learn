"""
file name:    Demo03PickleLearn.py
date:         2022/8/15 16:03
author        ZhuJunfei
"""

import pickle


def pickle_learn():
    s1 = 'hello'
    dumps = pickle.dumps(s1)
    print(dumps)


if __name__ == "__main__":
    pickle_learn()
