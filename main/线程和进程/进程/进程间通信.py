"""
@author Lucas
@date 2018/12/18 19:40

"""
import os
import time
from multiprocessing import Process, Queue


def write(q):
    print("启动写子进程%s" % os.getpid())
    for char in ["a", "b", "c", "d"]:
        q.put(char)
        time.sleep(1)
    print("结束写子进程%s" % os.getpid())


def read(q):
    print("启动读子进程%s" % os.getpid())
    while True:
        value = q.get(True)
        print("Value = " + value)


if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # pr进程死循环，只能强行结束
    pr.terminate()

    print("父进程结束")
