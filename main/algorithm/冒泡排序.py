"""
@author Lucas
@date 2019/3/26 20:55
"""


def bubbleSort(a):
    for i in range(len(a) - 1):  # 一共要尝试冒几次泡
        for j in range(len(a) - i - 1):  # 每次要两两比较几次
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


if __name__ == '__main__':
    a = [2, 5, 9, 7, 3, 3, 1, 4, 9]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
    bubbleSort(a)
    bubbleSort(b)
