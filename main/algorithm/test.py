"""
@author Lucas
@date 2019/4/2 8:53
"""
set1 = {1, 2, 3}
set2 = {2, 4}
print(set1-set2)
list1 = [1, 2, 3, 4]
for i in list1:
    if i == 2:
        list1.insert(2, 6)
print(list1)
