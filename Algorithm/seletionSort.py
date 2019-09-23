def selsectionSort(arr):
    """
    选择排序
    roseau
    20190923
    时间复杂度：n^2
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def findSmallest(arr):
    """
    找到数组中最小的数，并返回其索引
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

if __name__ == "__main__":
    print( selsectionSort([5,3,1,2,6,7,8]))
