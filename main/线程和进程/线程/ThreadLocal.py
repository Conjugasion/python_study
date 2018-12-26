"""
@author Lucas
@date 2018/12/18 22:35

"""
import threading

num = 10
# 创建全局的ThreadLocal对象
local = threading.local()


def run(param1, param2):
    param1 = param1 + param2
    param1 = param1 - param2


def func(n):
    # local.x 线程的局部变量
    local.x = num
    for i in range(100000):
        run(local.x, n)
    print("%s--%d" % (threading.current_thread().name, local.x))


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(5,))
    t2 = threading.Thread(target=func, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num=", num)
