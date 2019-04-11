"""
@author Lucas
@date 2019/3/25 22:16
找出两个字符串的最大公共子串
12332  56523327
"""


def find():
    s1 = str(input())
    s2 = str(input())
    list1 = []
    list2 = []
    for i in range(len(s1)):
        list1.append(s1[i:i + 1])
    for i in range(len(s2)):
        list2.append(s2[i:i + 1])

    finalResult = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            continue
        else:
            index = []
            for j in range(len(list2)):
                if list2[j] == list1[i]:
                    index.append(j)

            for k in index:
                result = []
                for (x, y) in zip(list1[i:], list2[k:]):
                    if x != y:
                        break
                    else:
                        result.append(x)
                    if len(result) > len(finalResult):
                        finalResult = result
    print(finalResult)


if __name__ == '__main__':
    find()
    # 其中一方到头了，双方都停止循环
    # set1 = {1, 2, 3}
    # set2 = {4, 5}
    # for (x, y) in zip(set1, set2):
    #     print(x)
    #     print(y)
    #     print("*********")
