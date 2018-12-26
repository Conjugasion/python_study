import time

# 时间戳
c1 = time.time()
print(int(c1))

# 元组
t1 = time.gmtime(c1)
print(t1)

t2 = time.localtime(c1)
print(t2)

c2 = time.mktime(t2)
print(c2)

# 字符串
s1 = time.asctime(t2)
print(s1)

s2 = time.ctime(c2)
print(s2)

q1 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
print(q1)

y1 = time.clock()
print(y1)
time.sleep(2)
y2 = time.clock()
print(y2)
time.sleep(2)
y3 = time.clock()
print(y3)