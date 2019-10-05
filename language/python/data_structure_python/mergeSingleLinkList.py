from SingleLinkList import Node, SingleLinkList


def merge_list(l1: Node, l2: Node) -> SingleLinkList:
    '''合并两个递增有序的链表'''
    head = Node(0)
    first = head

    # 当两个链表都不为空
    while l1 and l2:
        # l1 和 l2 谁指向的节点值小，就挂载在结果链表中
        # 且挂载后，均需后移
        if l1.elem < l2.elem:
            head.next = l1  # 挂载节点
            l1 = l1.next  # 后移
        else:
            head.next = l2
            l2 = l2.next
        # 结果链表的头节点往后移，方便挂载下一个节点
        head = head.next
    # 当循环结束时，l1 l2至少有一个为空
    if l2:
        l1 = l2
    head.next = l1
    return SingleLinkList(first.next)


if __name__ == "__main__":
    l1 = SingleLinkList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l2 = SingleLinkList()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    l3 = merge_list(l1.get_head(), l2.get_head())
    l3.travel()