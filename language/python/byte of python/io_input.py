def reverse(text):
    return text[::-1]


def is_palindrome(text):
    """判断是否为回文"""
    return text == reverse(text)


something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a parlindrome")
else:
    print("No, it is not a palindrome")
