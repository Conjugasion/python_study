"""
@author Lucas
@date 2018/11/27 22:50

"""

import itertools

# 排列(不可重复)
mylist1 = list(itertools.permutations([1, 2, 3, 4], 3))
print(mylist1)
print(len(mylist1))

# 组合(不可重复)
mylist2 = list(itertools.combinations([1, 2, 3, 4], 3))
print(mylist2)
print(len(mylist2))

# 排列(可重复)
mylist3 = list(itertools.product([1, 2, 3, 4, 5], repeat=4))
print(mylist3)
print(len(mylist3))
