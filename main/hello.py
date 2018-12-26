print(5 & 7)  # 与 101 & 111 得到 101(5)
print(5 ^ 7)  # 异或 101 ^ 111 得到 010(2)
print(5 | 7)  # 或 101 | 111 得到 111(7)
print(~4)  # 取反 -5  计算机存储补码，4的补码是0100，按位取反得到1011(补码)，再得到反码1010，最后得到原码1101(-5)
# -5：原码1101 反码1010 补码1011，按位取反0100

print(-4 << 3)  # 左移得到100000
print(2 >> 1)  # 右移得到01(1)

str1 = "good man"
str2 = str1 * 3
f = 3.1415926
d = 10.00
print(str2)
print(str1[0])
print("\"str1\"= %s\nf=%.3f, d=%d" % (str1, f, d))
print("'str1' = " + str1 + ",f= " + str(f) + ",d= " + str(d))

# 截取
str3 = str1[0:6]  # good m 不包括6
str4 = str1[:]
print(str3)
print(str4)
print("good man" is str1)
print("o" not in str1)

'''
运算优先级
** 幂运算
~  +  -  取反 正负号
*  /  %  //
+  - 
>>  <<  移位
&
^  |
<=  <  >  >=
==  !=
'''

'''
and or not 
in  not in
is  not is
'''

print(r"\\\t\\")
print(-5 // 3)  # 向下取整
print("制表\t符")

num1 = eval("123")
print(num1)
len(str1)

print("\t")
for i in range(10):
    if i == 1:
        continue
    if i == 9:
        break
    print(i)

print(5 / 3)

# str2 = int(input())
# print(type(str2))

# print(2 < "3")

print(0o654)

汉字变量 = "汉字str"
print(汉字变量)

list1 = [1, 2, 3]

str5 = " as d \n asd"
print(str5.replace(" ", "").replace("\n", ""))
