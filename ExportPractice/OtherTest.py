"""
file name:    OtherTest.py
date:         2022/8/14 11:58
author        ZhuJunfei
"""


def func1(*args, b='a', **kwargs):
    print(type(args))
    print(kwargs)


def func2(ls: list) -> list:
    """列表去重 (10分)"""
    # 第一眼, 使用set的特性, 去重, 然后进行排序, 转换为list
    s = set(ls)
    l = sorted(s)
    return l


def func3() -> None:
    """
    	1. 用代码新建一个文件 A.txt
    	2. 在里面写入 ==> 人生苦短，我用Python
    	3. 用代码实现将 A.txt 内容拷贝到 B.txt
    """
    f_p = open('A.txt', 'wb+')
    content = '人生苦短, 我用Python'.encode('utf-8')

    f_p.write(content)
    # 移动游标位置
    f_p.seek(0)
    # 读出
    read_content = f_p.read()

    f_w = open('B.txt', 'wb')
    f_w.write(read_content)
    f_w.close()


def func4() -> None:
    """已知列表中有一组学员的考试成绩，求每个学员的考试成绩总分和平均分"""
    scores_list = [{'name': '张三', 'math': 94, 'language': 87, 'english': 99},
                   {'name': '李四', 'math': 76, 'language': 64, 'english': 66},
                   {'name': '王五', 'math': 88, 'language': 85, 'english': 79},
                   {'name': '周六', 'math': 90, 'language': 89, 'english': 100}]

    for i in scores_list:
        total_score = 0
        avg_score = 0
        i: dict
        stu_info = i.values()
        stu_scores = list(stu_info)[1:]
        print(stu_scores)
        for single_score in stu_scores:
            total_score += single_score
        avg_score = round(total_score / len(stu_scores), 2)
        print(f'name = {i.get("name")}, total = {total_score}, avg = {avg_score}')


def func5() -> None:
    for first in range(1, 10):
        for second in range(1, first + 1):
            print(f'{first} * {second} = {first * second} \t', end='')
        print()


def func6() -> None:
    while (True):
        print("***************简易计算器***************")
        print("请输入你要进行的操作（+-*/）", end='')
        choice = input()
        print("请输入数字1：", end='')
        num1 = int(input())
        print("请输入数字2：", end='')
        num2 = int(input())
        if choice == '+':
            print(f'结果: {num1 + num2}')
        elif choice == '-':
            print(f'结果: {num1 - num2}')
        elif choice == '*':
            print(f'结果: {num1 * num2}')
        elif choice == '/':
            print(f'结果: {num1 / num2}')
        else:
            print('输入的操作符有误')
            return


class Employee(object):
    def __init__(self, _name: str):
        self.__name = _name

    def get_name(self) -> str:
        return self.__name

    def get_salary(self) -> int:
        return 0

    def set_name(self, _name: str) -> None:
        self.__name = _name

    def __str__(self) -> str:
        return f'Employee:\n\t name = {self.__name}'


class Manager(Employee):
    __FIX_SALARY = 15000

    def __init__(self, _name: str, _working_hour: int):
        super().__init__(_name)
        self.__working_hour = _working_hour

    def get_salary(self) -> int:
        return Manager.__FIX_SALARY

    def __str__(self):
        return f'Manager: \n\t name = {self.get_name()} \n\t salary = {self.get_salary()}'


class Programmer(Employee):
    __PRICE = 60

    def __init__(self, _name: str, _working_hour: int):
        super().__init__(_name)
        self.__working_hour = _working_hour

    def get_salary(self) -> int:
        return self.__working_hour * Programmer.__PRICE

    def __str__(self):
        return f'Programmer: \n\t name = {self.get_name()} \n\t salary = {self.get_salary()}'


NAME = '姓名'
JOG_TITLE = '职位'
JOG_TITLE_M = 'Manager'
JOG_TITLE_P = 'Programmer'
WORKING_TIME = '工作时间'


def func7() -> None:
    emps = [
        {'姓名': '刘备', '职位': 'Manager', '工作时间': 160},
        {'姓名': '张飞', '职位': 'Programmer', '工作时间': 200},
        {'姓名': '赵云', '职位': 'Programmer', '工作时间': 180}
    ]

    for emp in emps:
        job_title = emp.get(JOG_TITLE)
        if job_title == JOG_TITLE_M:
            manager = Manager(emp.get(NAME), emp.get(WORKING_TIME))
            print(manager)
        elif job_title == JOG_TITLE_P:
            programming = Programmer(emp.get(NAME), emp.get(WORKING_TIME))
            print(programming)
        else:
            continue


if __name__ == "__main__":
    # func1(1, 2, 3, b = 'c', a = 'd')
    # list1 = [1, 2, 3, 5, 2, 3, 5, 6, 7, 4, 8, 9]
    # new_ls = func2(list1)
    # print(*new_ls)
    # func3()
    # func4()
    # func5()
    # func6()
    func7()
