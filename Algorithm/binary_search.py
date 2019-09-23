def binary_search(list,item):
    """
    binary_search
    receive a sorted array and the key item, ouput the index of that item
    roseau
    2019/9/23
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)  # int() to Round down
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return 'Not fonud'


if __name__ == '__main__':
    mylist = list(range(1,20,2))
    print("input string is:" , mylist)
    print('19 is ' , binary_search(mylist,19))
    print('9 is ' , binary_search(mylist,9))
    print('200 is ' , binary_search(mylist,200))


