"""
@author Lucas
@date 2018/12/3 23:25

"""
import re

'''
字符串切割
使用正则切割
'''

str1 = "Lucas is       a good man"
print(str1.split(" "))
print(re.split(r" +", str1))


'''
re.finditer函数
'''
str2 = "Lucas is a good man Lucas is a good man Lucas is a good man"
iter = re.finditer(r"(Lucas)", str2)
while True:
    try:
        i = next(iter)
        print(i)
    except StopIteration as e:
        break


'''
字符串的替换和修改
re.sub 
re.subn
'''

str3 = "Lucas is a good man Lucas is a good man Lucas is a good man"
print(re.sub(r"good", r"bad", str3, count=2))
print(re.subn(r"good", r"bad", str3, count=2))


'''
分组
'''
str4 = "0575-83185101"
m = re.match(r"(?P<first>\d{4})-(?P<last>\d{8})", str4)
print(m.group(0))

print(m.group(1))
print(m.group("first"))

print(m.group(2))
print(m.group("last"))

print(m.groups())


'''
用编译后的对象去匹配
'''
pat = r"\d{4}-\d{8}"
re_homePhone = re.compile(pat)
print(re_homePhone.match("0575-831585101"))




























