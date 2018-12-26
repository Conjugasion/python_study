from functools import reduce


def charTranInt(char):
    def run():
        print("run")

    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char]


# Map
list1 = ["1", "2", "3"]
tuple1 = ("1", "2", "3")
result = map(charTranInt, list1)
print(list(result))

# list2 = [1, 2, 3]
# list3 = str(list2)
# list4 = "[1, 2, 3]"
# print(type(list2[1]))
# print(type(list3))
#
# list5 = map(str, [1, 2, 3, 4])
# print(list(list5))
# print("*************")

# Reduce
list6 = [1, 2, 3, 4, 5]


def Sum(x, y):
    return x + y


r = reduce(Sum, map(charTranInt, list1))
print("r = %d" % r)
print(type(r))

# print(list("12345"))

print(3/2)
