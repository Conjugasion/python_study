"""
@author Lucas
@date 2019/4/1 9:10
[80,30,60,20,  10,60,50,70,40]
"""
import math


def merge(a, start, mid, end):
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        if a[i] >= a[j]:
            temp.append(a[j])
            j += 1

    if i <= mid:
        for x in a[i:mid+1]:
            temp.append(x)
    if j <= end:
        for x in a[j: end+1]:
            temp.append(x)

    for x in range(len(temp)):
        a[start + x] = temp[x]


def merge_sort(a, start, end):

    if start < end:
        mid = int((start + end)/2)
        merge_sort(a, mid + 1, end)
        merge_sort(a, start, mid)

        merge(a, start, mid, end)


if __name__ == '__main__':
    a = [10, 20, 30, 40, 50, 1,  15, 25, 30, 45, 55, 60, 5, 0]
    # merge(a, 0, 4, 10)
    # print(a)
    merge_sort(a, 0, 13)
    print(a)

