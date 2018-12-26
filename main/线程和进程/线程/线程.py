"""
@author Lucas
@date 2018/12/18 21:37

"""
# 底层模块
import _thread

# 高级模块 封装了_thread模块
import threading
import time

a = 10


def say(num):
    print("子线程%s开始 num=%s" % (threading.current_thread().name, num))
    time.sleep(2)
    print(a)
    print("子线程%s结束 num=%s" % (threading.current_thread().name, num))


if __name__ == '__main__':
    print("主线程%s启动" % threading.current_thread().name)

    # 创建线程
    t1 = threading.Thread(target=say, name="say", args=(1, ))
    t1.start()

    # 等待子线程结束
    t1.join()

    print(a)
    print("主线程%s结束" % threading.current_thread().name)


