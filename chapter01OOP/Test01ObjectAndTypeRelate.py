"""
description:  test object and tupe relate
date:         2022/8/12 12:47
author        ZhuJunfei
"""

if __name__ == "__main__":
    object_parent = object.__bases__
    # print(f'object parent type = {object}')
    print(f'Object object type is {object.__class__}')
    print(f'list type is {list.__class__}')
    print(f'list parent type is {list.__bases__}')
