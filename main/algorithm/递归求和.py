"""
@author Lucas
@date 2019/4/10 19:55
"""


def sum(list1):
    if not list1:
        return 0
    else:
        result = list1[0]
        list1.pop(0)
        return result + sum(list1)


if __name__ == '__main__':
    list1 = [1, 2, 3, 6]
    print(sum(list1))

