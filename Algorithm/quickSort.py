def quickSort(array):
    """
    快速排序
    利用分而治之的思想
    使用递归解决
    时间复杂度：nlogn
    """
    if len(array) <= 1:
        # base case
        return array
    else:
        # recursive case
        pivot = array[0]  # 基准值

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == "__main__":
    mylist = [1, 3, 2, 89, 34, 67, 33, 45, 68]
    print(quickSort(mylist))
