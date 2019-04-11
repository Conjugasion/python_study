"""
@author Lucas
@date 2019/4/3 15:36
"""


def musicList():
    allLength = int(input())
    a, x, b, y = map(int, input().split(" "))

    count = min(allLength//a, x)
    result = 0
    for i in range(0, count+1):
        if (allLength - i*a) % b == 0:
            b_num = (allLength - i*a) // b
            if b_num <= y:
                a_num = i
                a_poss = factorial(x)//((factorial(a_num))*(factorial(x-a_num)))
                b_poss = factorial(y)//((factorial(b_num))*(factorial(y-b_num)))
                result += a_poss * b_poss

    print(result % 1000000007)


def factorial(c):
    if c == 0:
        return 1
    sum = 1
    for i in range(1, c+1):
        sum = sum*i
    return sum


if __name__ == '__main__':
    musicList()
    # print(factorial(10))








