from collections import Iterable

print(isinstance([], Iterable))

l1 = (x for x in [1, 2, 3, 4, 5])
print(next(l1))
print(next(l1))

l2 = (x for x in {'dict1': "good", 'dict2': "bad"})
print(next(l2))
print(next(l2))

endstr = "end"
str = ""
for line in iter(input, endstr):
    str += line + "\n"
print(str)

