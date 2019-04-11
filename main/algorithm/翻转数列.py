"""
@author Lucas
@date 2019/4/3 14:07
"""


def reverseArray():
    NandM = str(input())
    n = int(NandM.split(" ")[0])
    m = int(NandM.split(" ")[1])

    # array = []
    # for i in range(1, n+1):
    #     array.append(i)
    #
    # for i in range(len(array)):
    #     if i % (2*m) == 0:
    #         for j in range(m):
    #             array[i+j] = -array[i+j]
    # print(array)
    #
    # sum = 0
    # for i in array:
    #     sum += i
    # print(sum)

    print(m*n/2)


if __name__ == '__main__':
    reverseArray()
