"""
@author Lucas
@date 2018/12/4 14:57

"""
import re


# QQ
re_QQ = re.compile(r"^[1-9]\d{5,10}$")
print(re_QQ.search("5160206080"))

# 邮箱
re_mail = re.compile(r"^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$")
print(re_mail.search("tdf516020608@163.com"))

