"""
@author Lucas
@date 2018/12/3 9:57

"""
import itertools


passwd = ("".join(x) for x in itertools.product("0123456789", repeat=3))
print(next(passwd))
print(next(passwd))
print(next(passwd))
