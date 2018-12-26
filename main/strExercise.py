str1 = "h*el*lo w*orld "
print(len(str1))
print(str1.split("*"))

str2 = '''food is delicious!
food is bad!
food is too much!
'''

print(str2.splitlines())
data1 = str2.encode("utf-8")
print(data1)
str3 = "1#$5A"
print(str3.isupper())
str4 = "Food Is Delicious!"
print(str4.istitle())
