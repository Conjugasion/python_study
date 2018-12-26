"""
@author Lucas
@date 2018/12/13 21:46

"""
import os
from multiprocessing import Process
from time import sleep


def run(str):
    print("子进程开始")
    for j in range(8):
        print("Son %s ---- pid = %s ---- ppid = %s" % (str, os.getpid(), os.getppid()))
        sleep(1.5)
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开始")
    # 创建子进程
    p = Process(target=run, args=("Tdf",))
    p.start()

    '''
    创建多个子进程
    '''

    for i in range(5):
        print("Father ---- pid = %s" % os.getpid())
        sleep(1)

    # 等待子进程结束后，父进程再结束
    p.join()
    print("父进程结束")
