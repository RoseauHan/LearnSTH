from collections import deque  # 引入队列


def search(name):
    """
    广度优先搜索
    roseau
    """
    search_queue = deque()  # 创建一个队列
    search_queue += graph[name]  # 将邻居都加入到这个搜索队列中
    searched = []  # 用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 就取出其中的第一个人
        if person not in searched:  # 仅当这个人没检查过时才检查
            if person_is_seller(person):  # 检查这个人是不是芒果销售商
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商，将这个人的朋友都加入到搜索队列
                searched.append(person)  # 将这个人标记为检查过
    return False  # 如果执行到这里，就说明队列中没人是芒果销售商


if __name__ == "__main__":
    """
    利用散列表实现图的数据结构
    """
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    def person_is_seller(person):
        # 判断该人是否为芒果销售商
        if person[:-1] == 'l':
            return True

    print(search("you"))
