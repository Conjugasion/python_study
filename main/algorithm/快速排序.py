"""
@author Lucas
@date 2019/4/1 15:12
"""


# 快速排序
# 默认取第一个元素作为轴枢
def fastSort(a, left, right):

    if left >= right:
        return
    pivot = left
    i = left
    j = right

    while i < j:
        if a[j] >= a[pivot]:
            j -= 1
        else:
            if a[i] <= a[pivot]:
                i += 1
            else:
                a[i], a[j] = a[j], a[i]
    a[j], a[pivot] = a[pivot], a[j]
    fastSort(a, left, j-1)
    fastSort(a, j+1, right)


if __name__ == '__main__':
    a = [2, 8, 11, 7, 3, 3, 1, 4, 6, 10]
    fastSort(a, 0, 9)
    print(a)
