path = r"D:\Tang\python_exercise\python_study\main\file\file1.txt"
f = open(path, "r", encoding="utf-8", errors="ignore")

str1 = f.read()
print(str1)

# str2 = f. read(10)
# print(str2)
# str3 = f. read(10)
# print(str3)

# str4 = f.readline()
# print(str4)
# str5 = f.readline()
# print(str5)
#
# str6 = f.readlines()
# print(str6)

print("******")
f.seek(10)
str7 = f.read()
print(str7)
