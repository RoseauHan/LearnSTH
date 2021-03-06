# !/usr/bin/env python3  
# -*-coding:utf-8 -*-
def test_var_args():
    """
    *args 用来发送一个非键值对的可变数量的参数列表给一个函数
    """
    def test_var_args(f_arg, *argv):
        print("first normal arg:", f_arg)
        for arg in argv:
            print("another arg through *argv:", arg)

    test_var_args('han', 'rose', 'test', 'haha')


def greet_me():
    """
     **kwargs 允许将不定长度的键值对作为参数传递给一个函数
     """
    def greet_me(**kwargs):
        for key, value in kwargs.items():
            print("{0} == {1}".format(key, value))

    greet_me(name="roseauhan")


def test_args_kwargs():
    """
    使用*args，**kwargs调用一个函数
    """
    args = ("two", 3, 5)
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}

    def test_args_kwargs(arg1, arg2, arg3):
        print("arg1:", arg1)
        print("arg2:", arg2)
        print("arg3:", arg3)

    test_args_kwargs(*args)
    test_args_kwargs(**kwargs)


def generator_fibon():
    """
    Iterable: 可迭代对象 返回__iter__方法或定义了__getitem__方法
    Iterator: 迭代器     定义了__next__方法
    Generators 生成器 yield （暂时生成）一个值
    """
    def fibon(n):
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

    for x in fibon(100):
        print(x)


def test_generator_function():
    """ 
    next() 获取序列的下一个元素 注意越界会报错：StopIteration （for循环已经自动检查）
    """
    def generator_function():
        for i in range(3):
            yield i

    gen = generator_function()
    print(next(gen))
    print(next(gen))
    print(next(gen))


def test_iter():
    """
    iter() 可以根据一个可迭代对象返回一个迭代器
    """
    my_string = "roseauhan"
    iter_my_string = iter(my_string)
    print(next(iter_my_string))


def test_map():
    """
    map(要映射的函数，输入list)
    """
    items = [1, 2, 3, 4, 5, 6]
    squired = list(map(lambda x: x ** 2, items))
    print(squired)

    # 甚至可以用于一列表的函数
    def multiply(x):
        return x * x

    def add(x):
        return x + x

    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(list(value))


def test_filter():
    """
    Filter 过滤列表中的元素，符合要求：函数映射到该元素时返回值为True
    """
    number_list = range(-5, 5)
    less_than_zero = filter(lambda x: x < 0, number_list)
    print(list(less_than_zero))


def test_reduce():
    """
    reduce 计算一个整数列表的乘积
    """
    from functools import reduce
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print(product)


def test_count():
    """
    count 返回某一元素在列表、元组中的个数
    """
    a = (1, 2, 2, 3, 5, 2, 5, 32)
    print(a.count(2))
    b = [1, 3, 45, 2, 1, 1, 2]
    print(b.count(2))


def test_set():
    """
    set 不包括重复的值 可用于过滤重复，集合计算
    """
    some_list = ['a', 'b', 'c', 'd', 'a', 'b', 'd', 'm']
    dulicates = set([x for x in some_list if some_list.count(x) > 1])
    print(dulicates)

    valid = {'rose', 'han', 'test'}
    input_set = {'rose', 'yes'}
    print(input_set.intersection(valid))  # intersection 计算交集
    print(input_set.difference(valid))  # difference 计算差集

    a = {1, 2, 3}
    print(type(a))  # 可以使用{}直接创建set


def test_three_operation():
    """
    三元运算符 condition_is_true if conditon else condition_is_false
    """
    is_fat = True
    state = 'fat' if is_fat else "not fat"
    print(state)


def test_decorator():
    """
    装饰器 函数中可以定义函数，也可以返回函数， 函数可以作为参数传递
    """
    def a_new_decorator(a_func):
        def wrapTheFunction():
            print("doing things before a_func")
            a_func()
            print("doing things after a_func")

        return wrapTheFunction

    def a_function_requiring_decoration():
        print("I need decoration")

    a_function_requiring_decoration()
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration())
    a_function_requiring_decoration()


def test_defaultdict():
    """
    Collections 容器 包含多种数据类型 defaultdict 不需要检查是否存在key
    """
    from collections import defaultdict
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Yasoob', 'Red'),
        ('Ali', 'Black'),
    )

    favourate_colours = defaultdict(list)
    for name, colour in colours:
        favourate_colours[name].append(colour)
    print(favourate_colours)


def test_defaultdict_avoid_keyerror():
    """
    字典中对一个键进行嵌套赋值时，若该键不存在，会触发keyerror。本方法将解决该问题
    """
    import collections
    import json
    tree = lambda: collections.defaultdict(tree)
    some_dict = tree()
    some_dict['colours']['favourite'] = 'yellow'
    print(json.dumps(some_dict))


def test_counter():
    """
    Counter 是一个计数器，帮助我们针对某项数据进行计数
    """
    from collections import Counter
    colours = (
        ('a', '12'),
        ('b', '22'),
        ('c', '52'),
        ('a', '72'),
        ('c', '82'),
    )
    favs = Counter(name for name, colours in colours)
    print(favs)

    with open('./../cpp/README.md') as f:
        line_count = Counter(f)
        print(line_count)


def test_deque():
    """
    deque 提供一个双端队列，可以从头/尾两端添加或删除元素
    """
    from collections import deque
    d = deque()
    d.append('1')
    d.append('2')
    d.append('3')
    print(d)
    d.pop()
    print(d)
    d.popleft()
    d.appendleft('hah')
    print(d)


def test_nametuple():
    """
    nametuple 把元组变成一个针对简单任务的容器 让元组变得“自文档”了
    """
    from collections import namedtuple
    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    print(perry.age)


def test_enumerate():
    """
    Enumerate 枚举 是Python内置函数，允许我们遍历数据并且自动计数
    """
    some_list = ['h', 'z', 'y', 'h', 'y']
    for counter, value in enumerate(some_list):
        print(counter, value)


def test_dir():
    """
    introspection 对象自省: 运行时判断一个对象得类型的能力
    dir 返回一个列表，列出一个对象所拥有的属性和方法
    """
    my_list = [1, 1, 2, 3]
    print(dir(my_list))


def test_type():
    """
    type 返回一个对象的类型
    """
    print(type([]))
    print(type(''))
    print(type({}))
    print(type(dict))
    print(type(3))


def test_id():
    """
    id 返回任意不同种类对象的唯一ID
    """
    name = "hahah"
    print(id(name))
    print(id(None))
    print(id(''))


# inspect 获取对象的信息
# This module encapsulates the interface provided by the internal special
# attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
# It also provides some help for examining source code and class layout.
#
# Here are some of the useful functions provided by this module:
#
#     ismodule(), isclass(), ismethod(), isfunction(), isgeneratorfunction(),
#         isgenerator(), istraceback(), isframe(), iscode(), isbuiltin(),
#         isroutine() - check object types
def test_inspect():
    import inspect
    print(inspect.getmembers(str))


# Comprehension 推导式（解析式） 可以从一个数据序列构建另一个新的数据序列的结构体
# 包括 列表推导式、字典推导式、集合推导式

# 1 list Comprehension
# 规范 variable = [out_exp for out_exp in input_list if out_exp == 2]
# 对于快速生成列表很有用
def test_list_comprehension():
    multiples = [i for i in range(30) if i % 3 is 0]
    print(multiples)

    squared = [x ** 2 for x in range(10)]
    print(squared)


# dict Comperhension 字典推导式
def test_dict_comprehension():
    mcase = {'a': 10, 'b': 34, 'A': 7}
    mcase_frequency = {
        k.lower: mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
        for k in mcase.keys()
    }
    print(mcase_frequency)

    print({v: k for k, v in mcase.items()})


# set Comprehension 集合推导式
def test_set_comprehension():
    squared = {x ** 2 for x in [1, 1, 2]}
    print(squared)
    print(type(squared))


# 异常处理
def test_except():
    try:
        with open('test.txt', 'r') as f:
            read = f.read()
    except (IOError, EOFError) as e:
        print("如果try发生异常，将会执行这里的代码")
        print('An error occurred. {}'.format(e.args[-1]))
    else:
        print("这里的代码只会在try语句里没有触发异常才执行，但这里的异常不会被捕获")
    finally:
        print("无论是否异常，这里的代码都会执行")


def test_lambda():
    """lambda 表达式 (匿名函数) 若你不想在程序中使用这段代码两次，你也许可以使用lambda表达式，它和普通函数一样
    原型：lambda: 参数：操作（参数）
    """
    add = lambda x, y: x + y
    print(add(2, 3))

    # 列表排序时使用
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1], reverse=True)
    print(a)

    # 列表并行排序
    # data = zip(list1, list2)
    # data.sort()
    # list1, list2 = map(lambda t:list(t), zip(*data))
    # 有问题


# 一行式
def one_line_code():
    # https://wiki.python.org/moin/Powerful%20Python%20One-Liners
    # 简易的 Web server
    # python -m http.server

    # 漂亮的打印  ???
    from pprint import pprint
    my_dict = {'name': 'han', 'age': 21, 'personality': 'happy'}
    pprint(my_dict)

    # ...


def test_for_else():
    """
    for 也有else从句，在循环正常结束时执行
    """
    for n in range(2,10):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*',n/x)
                break
        else:
            print(n,'is a prime number')


# 使用Python操作C语言的三种方式


# open函数
def test_open():
    import io
    try:
        with open('photo.jpg', 'rb') as inf:
            jpgdata = inf.read()
        
        if jpgdata.startswith(b'\xff\xd8'):
            text = u'This is a JPEG file(%d bytes long)\n'
        else:
            text = u'This is a random file(%d bytes long)\n'
        
        with io.open('summary.txt','w', encoding='utf-8') as outf:
            outf.write(text % len(jpgdata))
    except Exception as e:
        print(e)
    finally:
        print("DONE!")

import sys
def test_argv():
    print('The command line arguments are:')
    for i in sys.argv:
        print(i)
    print('\n\nThe pythonPath is', sys.path, '\n')




if __name__ == '__main__':
    # test_var_args()
    # greet_me()
    # test_args_kwargs()
    # generator_fibon()
    # test_generator_function()
    # test_iter()
    # test_map()
    # test_filter()
    # test_reduce()
    # test_count()
    # test_set()
    # test_three_operation()
    # test_decorator()
    # test_defaultdict()
    # test_defaultdict_avoid_keyerror()
    # test_counter()
    # test_deque()
    # test_nametuple()
    # test_enumerate()
    # test_dir()
    # test_type()
    # test_id()
    # test_inspect()
    # test_list_comprehension()
    # test_dict_comprehension()
    # test_set_comprehension()
    # test_except()
    # test_lambda()
    # one_line_code()
    # test_for_else()
    #test_open()
    test_argv()
