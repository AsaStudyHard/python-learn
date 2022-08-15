"""
description:  搬家具案例
date:         2022/8/13 10:10
author        ZhuJunfei
"""


class Item(object):
    """
    家具类
        args:
            type: 名称
            area: 面积
    """
    def __init__(self, _type, _area):
        self.type = _type
        self.area = _area

    def __str__(self):
        return f'name = {self.type}, area = {self.area}'


class Home(object):
    def __init__(self, _area, _address):
        self.area = _area
        self.address = _address
        self.free_area = _area

    def __str__(self):
        return f'area = {self.area}, address = {self.address}, free area = {self.free_area}'

    def add_item(self, item):
        """
        添加家具
        Args:
            item: 家具类实例

        Returns: not return
        """
        if self.free_area >= item.area:
            print(f"{item.type}放置成功")
            self.free_area -= item.area
        else:
            print(f'房屋剩余面积为{self.free_area}, 你要放置的家具面积是{item.area}')


if __name__ == "__main__":
    pass
