"""
狄杰斯特拉算法的思想：
1、找到最便宜的节点，即可在最短时间内前往的节点
2、对于该节点的邻居，检查是否有前往它们的更短的路径，如果有，就更新其开销
3、重复这个过程，直到对图中的每个节点都这样做了
4、计算最终路径
要编码解决无环加权图的问题，需要三个散列表：graph、costs、parents
随着算法的进行，需要不断更新散列表costs和parents

roseau
20190923
"""

"""
用于表示加权图的散列表 graph
"""
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


"""
用于存储每个节点的开销的散列表 costs
"""
infinity = float("inf")  # 在python中表示无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

"""
用于存储父节点的散列表 parents
"""
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []  # 用于记录已经处理过的节点


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 若当前节点的开销更低且未被处理
            lowest_cost = cost  # 就将其视为开销最低的点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # 在未处理的节点中找到开销最小的节点
while node is not None:  # 在所有节点都被处理过后才结束
    cost = costs[node]   # 获取该节点的开销
    neighbors = graph[node]   # 获取该节点的邻居
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果当前节点前往该邻居更近
            costs[n] = new_cost  # 就更新其邻居的开销
            parents[n] = node  # 同时将该邻居的父节点设置为当前节点
    processed.append(node)  # 将该节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找到接下来要处理的节点，并循环
