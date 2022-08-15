"""
description:  烤地瓜案例
date:         2022/8/12 14:43
author        ZhuJunfei
"""


class SweetPotato(object):
    def __init__(self):
        self.state = '生的'
        self.cooked_time = 0
        self.condiments = list()

    def cooked(self, time):
        """
        烧烤地瓜方法
        :param time: 烧烤时间
        :return: not return
        """
        if (time > 0):
            self.cooked_time += time
            if 3 <= self.cooked_time < 6:
                self.state = '夹生'
            if 6 <= self.cooked_time < 8:
                self.state = '熟了~'
            if self.cooked_time >= 8:
                self.state = '糊了糊了~'
            print('烤完了')
        else:
            print("请输入正常的烧烤时间")

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        if len(self.condiments) == 0:
            return f'sweet potato current state {self.state}, cooked_time = {self.cooked_time}'
        else:
            return f'sweet potato current state {self.state}, cooked_time = {self.cooked_time}, condiments = {self.condiments}'


def testSwitch():
    state = 3
    print(f'state = {"生" if state == 0 else "夹生" if state == 1 else "熟了" if state == 2 else "糊了"}')


if __name__ == "__main__":
    sp1 = SweetPotato()
    print(sp1)
    sp1.cooked(3)
    sp1.add_condiments('盐')
    sp1.cooked(3)
    sp1.add_condiments('孜然')
    print(sp1)
    testSwitch()