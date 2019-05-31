"""
@author Lucas
@date 2019/4/1 14:37
"""


# 选择排序
def selectSort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    print(a)


if __name__ == '__main__':
    a = [2, 5, 9, 7, 3, 3, 1, 4, 6]
    selectSort(a)
