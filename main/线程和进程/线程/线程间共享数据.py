"""
@author Lucas
@date 2018/12/18 22:07

"""
import threading

num = 10


def run(n):
    global num
    for i in range(1000000):
        num = num + n
        num = num - n


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(10,))
    t2 = threading.Thread(target=run, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num=", num)