import unittest

__author__ = "roseauhan"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "roseauhan"


class Stack(object):
    '''利用list来实现一个后进先出的栈'''

    def __init__(self):
        '''初始化'''
        self.__list = []

    def push(self, item):
        '''入栈'''
        self.__list.append(item)

    def pop(self):
        '''出栈'''
        return self.__list.pop()

    def peak(self):
        '''栈顶元素'''
        return self.__list[-1]

    def is_empty(self):
        '''是否为空'''
        return self.__list == []

    def size(self):
        '''栈元素的个数'''
        return len(self.__list)

    def __str__(self):
        '''实现打印操作'''
        return '{}'.format(self.__list)

    def __repr__(self):
        '''实现打印操作'''
        return '{}'.format(self.__list)

    def __eq__(self, value):
        """Override the default Equals behavior"""
        return self.__list == value


class TestStack(unittest.TestCase):
    '''Stack的单元测试'''

    def test_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.size()
        self.assertEqual(result, 2, "Should be 2")

    def test_push(self):
        '''test push operation'''
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack
        self.assertEqual(result, [1, 2], "should be [1,2]")

    def test_pop(self):
        '''test push operation'''
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        result = stack
        self.assertEqual(result, [1], "should be [1]")

    def test_empty(self):
        '''test push operation'''
        stack = Stack()
        result = stack.is_empty()
        self.assertTrue(result, "should be True")

    def test_peak(self):
        '''test push operation'''
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.peak()
        self.assertEqual(result, 2, "should be 2")


if __name__ == '__main__':
    unittest.main()
