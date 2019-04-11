"""
@author Lucas
@date 2019/4/8 14:00
"""


def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)


if __name__ == '__main__':
    a = factorial(5)
    print(a)

