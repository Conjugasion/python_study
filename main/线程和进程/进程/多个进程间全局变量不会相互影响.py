"""
@author Lucas
@date 2018/12/13 20:15
一个任务就是一个进程
"""
from multiprocessing import Process
from time import sleep

num = 100


def run():
    print("子进程开始")
    global num
    num += 1
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开始")

    p = Process(target=run)
    p.start()
    p.join()

    print("父进程结束 -- %d" % num)
