class Node(object):
    '''链表节点定义'''

    def __init__(self, item):
        '''必要初始化'''
        self.elem = item
        self.next = None


class SingleLinkList(object):
    '''单链表的实现'''

    def __init__(self, node=None):
        '''单链表的初始化'''
        self.__head = node

    def is_empty(self) -> bool:
        '''判断是否为空'''
        return self.__head is None

    def length(self) -> int:
        '''链表长度'''
        # 若链表为空
        if self.is_empty():
            return 0
        # 若链表非空，需要计数
        count = 0
        # 定义遍历游标（指针）
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        '''链表头部添加元素'''
        # 新建节点
        node = Node(item)
        # 将node的next指向旧的头节点
        node.next = self.__head
        # 将头节点标志指向新节点
        self.__head = node

    def travel(self):
        '''链表的遍历'''
        if self.is_empty():
            return
        cur = self.__head
        while cur:
            print(cur.elem)
            cur = cur.next

    def append(self, item):
        '''链表尾部添加元素'''
        # 若链表为空，尾部插入即为头部插入
        if self.is_empty():
            self.add(item)
        else:
            # 新建节点
            node = Node(item)
            # 找尾节点
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos: int, item: int):
        '''指定位置插入元素'''
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 1
            while count < pos:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''链表的删除'''
        # 若链表为空
        if self.is_empty():
            return
        pre = None  # 保存前驱节点
        cur = self.__head  # 遍历指针
        while cur:
            # 链表中是否存在给定的item值的节点
            if cur.item == item:
                if cur == self.__head:
                    # 若删的是头节点
                    self.__head = cur.next
                else:
                    # 若删除非头节点
                    pre.next = cur.next
                break
            # 遍历指针后移
            pre = cur
            cur = cur.next

    def search(self, item) -> bool:
        '''查找节点是否存在'''
        # 链表是否为空
        if self.is_empty():
            return False
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            # 遍历指针后移
            cur = cur.next
        # 当循环结束时，链表遍历完成
        return False

    def get_head(self):
        return self.__head


if __name__ == "__main__":
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.add(1)
    print(sll.is_empty())
    print(sll.length())
    sll.add(2)
    sll.add(3)
    sll.travel()
    sll.append(4)
    sll.travel()
    print(sll.search(3))
