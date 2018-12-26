list1 = [1, [1, 2], 3, 4, 5]
print(list1.pop(3))
print(list1.remove([1, 2]))
print(list1.clear())

list2 = [1, 2, 3, 4, 5, 3, 4, 5, 6]
index1 = list2.index(3, 3, 8)
print(index1)

removeNum = 3
allCount = list2.count(removeNum)
i = 0
while i < allCount:
    list2.remove(removeNum)
    i += 1
print(list2)
