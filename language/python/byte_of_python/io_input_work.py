def reverse(text):
    return text[::-1]


def is_palindrome(text):
    """排除空格标点大小的回文判断"""

    text = ''.join([i.lower() for i in text if str.isalpha(i)])
    return text == reverse(text)


something = input("Enter something:")

if is_palindrome(something):
    print("Yes ,It is palindrome")
else:
    print("No, It's not parlindrome")
