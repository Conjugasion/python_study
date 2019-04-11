"""
@author Lucas
@date 2019/3/29 20:05
"""


def groupAnagrams(myList):
    list1 = []
    for i in myList:
        strList = []
        for j in i:
            strList.append(j)
        list1.append(strList)
    print(list1)

    list2 = []
    for i in list1:
        list2.append(tuple(sorted(i)))
    print(list2)

    set1 = set(list2)
    print(set1)

    results = []
    for i in set1:
        index = []
        for j in range(len(list2)):
            if i == list2[j]:
                index.append(j)
        result = []
        for k in index:
            str1 = ""
            for l in list1[k]:
                str1 += l
            result.append(str1)
        results.append(result)
    print(results)


if __name__ == '__main__':
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

