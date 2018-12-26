try:
    print(int(3 / 1))
except ZeroDivisionError as e:
    print("除数不能为0")
except NameError as e:
    print("没有该变量")
else:
    print("代码正确")

print("**********")

try:
    print(int(4 / 0))
except:
    print("代码出错了")
else:
    print("代码正确")
finally:
    print("finally 一定执行")


