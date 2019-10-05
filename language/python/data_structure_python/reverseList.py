from SingleLinkList import Node, SingleLinkList

def reverseList(head: Node) -> SingleLinkList:
    '''翻转链表'''
    if not head:
        return SingleLinkList()
    # cur 是遍历指针
    cur = head.next
    # pre是cur的前驱节点
    pre = None
    head.next = None

    while cur:
        pre = cur
        cur = cur.next
        pre.next = head
        head = pre
    return SingleLinkList(head)
