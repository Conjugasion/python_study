"""
@author Lucas
@date 2018/11/23 9:09

"""


def func(num):
    if num % 2 == 0:
        return True
    return False


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter1 = filter(func, list1)
print(list(filter1))
