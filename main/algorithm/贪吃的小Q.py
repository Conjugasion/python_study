"""
@author Lucas
@date 2019/4/3 14:55
"""


def eat():
    n, m = map(int, input().split(" "))

    # c = 2 - pow(0.5, n-1)
    # result = int(m/c)
    # print(result)
    count = 1
    while True:
        m = 0.5*m
        if m >= 1:
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    eat()
