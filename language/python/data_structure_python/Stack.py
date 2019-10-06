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


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.size())
    stack.pop()
    stack.push(4)
    print(stack)
    print(stack.is_empty())