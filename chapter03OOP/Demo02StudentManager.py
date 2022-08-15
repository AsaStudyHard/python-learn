"""
file name:    Demo02StudentManager.py
date:         2022/8/15 11:32
author        ZhuJunfei
"""
import os
import pickle


class Student(object):
    def __init__(self, _name: str, _age: int, _tel: int):
        self.name = _name
        self.age = _age
        self.tel = _tel

    def to_dict(self) -> dict:
        return {'name': self.name, 'age':self.age, 'tel':self.tel}

    def __str__(self) -> str:
        return f'name = {self.name}, age = {self.age}, tel = {self.tel}'


class SysManager(object):
    @staticmethod
    def menu():
        """
        显示功能菜单
        """
        print('-' * 20)
        print('-> 1. 添加学生')
        print('-> 2. 查询所有学生')
        print('-> 3. 查询某个学生')
        print('-> 4. 修改某个学生')
        print('-> 5. 删除某个学生')
        print('-> 6. 保存信息')
        print('-> 7. 退出系统')
        print('-' * 20)

    def __init__(self):
        self.stus = list()

    def add_stu_info(self):
        print('add_stu_info')
        name = input('请输入学生姓名: ')
        stu: Student

        # 判断学生是否存在
        res = self.__judge_stu(name)
        if res is None:
            age = int(input('请输入学生年龄: '))
            tel = int(input('请输入学生电话: '))

            # 创建学生对象进行数据的保存
            stu = Student(name, age, tel)
            self.stus.append(stu)
            print(*self.stus)
        else:
            print('学生已经存在')
        self.clear_screen()

    def clear_screen(self):
        input('按任意键继续...')


    def show_all_stu(self):
        print('show_all_stu')
        for stu in self.stus:
            print(stu)
        self.clear_screen()

    def show_one_stu(self):
        print('show_one_stu')
        tar_name = input('请输入要查询的学生姓名: ')
        res = self.__judge_stu(tar_name)
        if res is None:
            print('该学生不存在')
            return
        print(res)
        self.clear_screen()

    def update_one_stu(self):
        print('update_one_sti')
        tar_name = input('请输入要修改的学生姓名: ')
        res = self.__judge_stu(tar_name)

        if res is None:
            print('该学生不存在')
            return

        res.name = input('请输入要修改的学生姓名: ')
        res.age = int(input('请输入学生年龄: '))
        res.tel = int(input('请输入学生电话: '))
        print(f'修改后的数据为: \n\t ---> {res}')

        self.clear_screen()

    def delete_one_stu(self):
        print('delete_one_stu')
        tar_name = input('请输入要删除的学生姓名: ')
        res = self.__judge_stu(tar_name)
        if res is None:
            print('该学生不存在')
            return
        self.stus.remove(res)

    def save_data(self):
        print('save_data')

        new_stus = list()
        for stu in self.stus:
            stu:Student
            new_stus.append(stu.to_dict())

        # 写入文件
        with open('stu.pickle', 'wb') as f:
            dumps = pickle.dumps(new_stus)
            f.write(dumps)

        print(*new_stus)

    def load_date(self):
        file_path = 'stu.pickle'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = pickle.load(f)
                print(content)

            # 把文件内容转为对象列表
            for stu in content:
                stu: dict
                self.stus.append(Student(stu.get('name'), stu.get('age'), stu.get('tel')))

        print(self.stus)


    def __judge_stu(self, tar_name: str) -> Student:
        for stu in self.stus:
            if tar_name == stu.name:
                return stu
        return None


def start():
    sm = SysManager()

    sm.load_date()

    # 初始化2个测试数据
    # stu1 = Student('zs', 23, 111)
    # stu2 = Student('ls', 22, 222)
    # sm.stus.append(stu1)
    # sm.stus.append(stu2)

    while True:
        # 显示功能菜单
        SysManager.menu()

        # 接收用户的输入
        cmd_num = input('请输入功能数字：')

        # 根据用户的输入，判断用户要进行操作
        if cmd_num == '1':
            sm.add_stu_info()
        elif cmd_num == '2':
            sm.show_all_stu()
        elif cmd_num == '3':
            sm.show_one_stu()
        elif cmd_num == '4':
            sm.update_one_stu()
        elif cmd_num == '5':
            sm.delete_one_stu()
        elif cmd_num == '6':
            sm.save_data()
        elif cmd_num == '7':
            print('退出系统！')
            sm.save_data()
            break
        else:
            print('输入有误！请重新输入！')


if __name__ == "__main__":
    start()
    # str1 = 'hello'
    # for i in range(len(str1)):
    #     print(str1.__getitem__(i))
