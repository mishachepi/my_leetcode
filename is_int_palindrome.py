"""
Is it palindrome int?
"""

def is_int_palindrome(dig: int) -> bool:
    list_dig = list(str(int))
    len_dig = len(list_dig)
    for i in range(len_dig):
        if list_dig[i] != list_dig[len_dig - i - 1]:
            return False
    return True
