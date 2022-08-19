"""
Description:  str to bytes
Date:         2022/8/19 15:48
Author:       ZhuJunfei
"""


def func():
    str1 = "你好"
    str2 = "我不好"
    str3 = '啦啦啦啦'
    # default using utf8 encode
    encode1 = str1.encode()

    # using gbk encode
    encode2 = str2.encode('gbk')
    print(encode1)
    print(str2.encode())
    print(encode2)

    # decode
    str1_b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
    str2_b = b'\xce\xd2\xb2\xbb\xba\xc3'

    print(str1_b.decode('utf8'))
    print(str2_b.decode('gbk'))


def func2():
    with open('text.b', 'wb') as f:
        b = '你好'.encode('gbk')
        f.write(b)
        print(b)

    with open('text.b', 'rb') as f:
        read = f.read()
        content = read.decode('gbk')
        print(read)


if __name__ == "__main__":
    # func()
    func2()