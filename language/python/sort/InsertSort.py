def insert_sort(nums: list) -> list:
    '''插入排序'''
    n = len(nums)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums


if __name__ == "__main__":
    nums = [64, 34, 1, 4, 7, 2, 45, 1, 32, 12]
    print('Before sort:{}'.format(nums))
    print('After sort:{}'.format(insert_sort(nums)))
