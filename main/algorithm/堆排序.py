"""
@author Lucas
@date 2019/4/2 9:51
"""


# 堆排序
# 建大顶堆
def heap(a):
    while True:
        flag = True
        for i in range(len(a)):
            if (2*i + 1) < len(a) and (2*i + 2) < len(a):
                if a[2*i + 1] > a[2*i + 2]:
                    max = 2*i + 1
                else:
                    max = 2*i + 2
                if a[max] > a[i]:
                    a[i], a[max] = a[max], a[i]
                    flag = False
            elif (2*i + 1) < len(a):
                if a[2*i + 1] > a[i]:
                    a[i], a[2*i + 1] = a[2*i + 1], a[i]
                    flag = False
        if flag:
            break
    return a


def heapSort(a):
    count = len(a)
    result = []
    for i in range(count):
        a = heap(a)
        result.append(a[0])
        a[0], a[-1] = a[-1], a[0]
        a = a[:-1]
    result.reverse()
    return result


if __name__ == '__main__':
    a = [4, 6, 8, 5, 9, 1, 3, 2]
    b = heap(a)
    print(b)
    result = heapSort(a)
    print(result)
