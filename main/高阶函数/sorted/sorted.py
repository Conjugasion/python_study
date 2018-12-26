"""
@author Lucas
@date 2018/11/23 9:26

"""

def func():
    pass


list1 = [2, 3, 5, 1, 4]
tuple1 = (2, 3, 5, 1, 4)
dict1 = {3: "a", 1: "b"}
list2 = sorted(list1)
tuple2 = sorted(tuple1)
dict2 = sorted(dict1)
print(list2)
print(tuple2)
print(dict2)

list3 = [-2, 3, 5, -1, 4]
list4 = sorted(list3, key = abs)
print(list4)

