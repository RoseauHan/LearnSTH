def bubble_sort(nums: list) -> list:
    '''in place sort'''
    n = len(nums)  # 计算长度
    # 外循环，控制比较的论数
    for j in range(1, n):
        # 内循环：通过比较相邻元素的值，找到每轮最大的值
        # i: 0~(n-1-j) 由于range左闭右开,故range(n-j)
        for i in range(n-j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


if __name__ == "__main__":
    nums = [64, 34, 1, 4, 7, 2, 45, 1, 32, 12]
    print('Before sort:{}'.format(nums))
    print('After sort:{}'.format(bubble_sort(nums)))
