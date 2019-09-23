def countDown(num):
    """
    利用递归进行倒计时
    roseau
    20190923
    """
    print(num)
    if num <= 0:
        # base case
        return
    else:
        # recursive case
        countDown(num - 1)

if __name__ == "__main__":
    countDown(10)
