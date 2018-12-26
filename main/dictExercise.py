dict1 = {"Tom": 23, "Lucas": 24}
# print(dict1["Jack"])    # 报错
print(dict1.values())

for key, value in enumerate(dict1):
    print(key, value)

str1 = "Lucas is a good man Lucas is a good man Lucas is a good man Lucas is a good man"
print(str1.count("good"))
list1 = str1.split(" ")
dict2 = {}
print(list1)
for v in list1:
    c = dict2.get(v)
    if c is None:
        dict2[v] = 1
    else:
        dict2[v] += 1
print(dict2["good"])

