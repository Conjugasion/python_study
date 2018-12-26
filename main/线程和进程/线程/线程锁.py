"""
@author Lucas
@date 2018/12/18 22:22

"""
import threading

num = 10
lock = threading.Lock()


def run(n):
    global num
    # for i in range(1000000):
    #     获得锁
    #     lock.acquire()
    #     try:
    #         num = num + n
    #         num = num - n
    #     finally:
    #         必须释放锁
    #         lock.release()
    for i in range(1000000):
        with lock:
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
