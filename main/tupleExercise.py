tuple1 = (1, 2, 3, "good", True)
print(type(tuple1))
tuple1[3].replace("g", "f")
print(tuple1)
# tuple1[0]=2
# a = input("str:")

tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)
tuple4 = tuple2 + tuple3
print(max(tuple4))

list1 = [(1, 2, 3), {1:"a", 2: 'b'}]
print(tuple(list1))