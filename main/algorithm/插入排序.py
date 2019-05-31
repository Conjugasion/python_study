"""
@author Lucas
@date 2019/4/1 13:28
"""


# 插入排序
def insertSort(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    print(a)


if __name__ == '__main__':
    a = [2, 5, 9, 7, 3, 3, 1, 4]
    insertSort(a)
