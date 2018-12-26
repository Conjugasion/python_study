"""
@author Lucas
@date 2018/12/17 21:43

"""
from main.线程和进程.进程.封装进程对象 import lucasProcess

if __name__ == '__main__':
    print("父进程启动")
    p1 = lucasProcess("test1")
    p2 = lucasProcess("test2")
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("父进程结束")