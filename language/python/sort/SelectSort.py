def select_sort(nums: list) -> list:
    '''选择排序 利用最小元素下标优化，实现每轮只交换一次'''
    n = len(nums)
    # 比较轮数
    # 当前要找的最小位置

    for j in range(n - 1):
        min_index = j
        for i in range(j+1, n):
            if nums[min_index] > nums[i]:
                min_index = i
        nums[j], nums[min_index] = nums[min_index], nums[j]
    return nums


if __name__ == "__main__":
    nums = [64, 34, 1, 4, 7, 2, 45, 1, 32, 12]
    print('Before sort:{}'.format(nums))
    print('After sort:{}'.format(select_sort(nums)))
