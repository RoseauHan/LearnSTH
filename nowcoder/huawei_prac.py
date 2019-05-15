'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
abc
输出
3
'''


def test_ascii_num():
    print(len(set([i for i in input() if ord(i) in range(128)])))


"""
输入一个整数，将这个整数以字符串的形式逆序输出

程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001


输入描述:
输入一个int整数

输出描述:
将这个整数以字符串的形式逆序输出

示例1
输入
1516000
输出
0006151
"""


def test_reverse_1():
    print(int(input()[::-1]))


def test_reverse_2():
    a = list(input())
    a.reverse()
    print(' '.join(a[i] for i in range(len(a))))


def test_input():
    a = input().split()
    for i in reversed(a):
        print(i, end='')


"""
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入
复制
9
cap
to
cat
card
two
too
up
boat
boot
输出
复制
boat
boot
cap
card
cat
to
too
two
up
"""


# 学习输入的处理！！
# a, res = int(input()), []
def test_dict_sort():
    while True:
        try:
            num = int(input())
            l = []
            for i in range(num):
                l.append(input())
            res = sorted(i)
            for i in res:
                print(i)
        except:
            break


"""
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。 
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
abc
123456789
输出
abc00000
12345678
90000000
"""


def test_str_8():
    while True:
        try:
            str = input()
            while True:
                if len(str) < 8:
                    print(str + (8 - len(str)) * '0')
                    break
                elif len(str) > 8:
                    print(str[0:8])
                    str = str[8:len(str)]
                else:
                    print(str)
                    break
        except:
            break


"""
题目描述
写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
0xA
输出
10
"""


def test_hex_to_dec():
    while True:
        try:
            string = input()
            print(int(string, 16))
        except:
            break


"""
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）

最后一个数后面也要有空格

详细描述：


函数接口说明：

public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：

String



输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5
"""


def test_zhishu_factor():
    while True:
        try:
            a = int(input())
            for i in range(2, a // 2 + 1):
                if a % i == 0:
                    for j in range(2, i // 2 + 1):
                        if i % j == 0:
                            break
                    else:
                        print(i, end=' ')
        except:
            break


"""
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
5.5
输出
6
"""
def test_quzhen():
    while True:
        try:
            a = float(input())
            b = str(a * 10)
            if (int(b[1]) >= 5):
                print(int(b[0]) + 1)
            else:
                print(int(b[0]) - 1)
        except:
            break

if __name__ == '__main__':
    # test_ascii_num()
    # test_reverse_2()
    # test_input()
    # test_dict_sort()
    # test_str_8()
    # test_hex_to_dec()
    # test_zhishu_factor()
    # test_quzhen()
    a = 19
    print(int(19,2))