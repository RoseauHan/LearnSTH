class Queue(object):
    '''利用list实现一个队列'''

    def __init__(self):
        '''队列的初始化'''
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        self.__list.pop(0)

    def is_empty(self):
        '''判断队列是否为空'''
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)

    def __str__(self):
        return '{}'.format(self.__list)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()

