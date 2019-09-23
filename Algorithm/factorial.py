def fact(x):
    """
    利用递归计算阶乘
    roseau
    20190923
    """
    if x == 1:
        # base case
        return 1
    else:
        # recursive case
        return x * fact(x - 1)


if __name__ == "__main__":
    print(fact(5))
