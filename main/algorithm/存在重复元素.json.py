"""
@author Lucas
@date 2019/3/29 17:22
"""


class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


s = Solution()
print(s.containsDuplicate([1, 2, 1, 3]))

print(list(x * x for x in range(10)))

hashmap = {0: 0, 2: 3}
print(type(hashmap))

tuple1 = (1, 2)
tuple2 = (2, 1)
print(tuple1 == tuple2)   # false

set1 = {1, 2}
set2 = {2, 1}
print(set1 == set2)    # true

list1 = [1, 2]
list2 = [2, 1]
print(list1 == list2)   # false

list3 = ["a", "b", "c"]

if "i" in "sin":
    print("i in sin")

for i in "asd":
    print(i)

print(len("asd"))
