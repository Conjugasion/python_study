"""
@author Lucas
@date 2018/12/13 22:29

"""
from multiprocessing import Pool
import os, time, random


def run(name):
    print("子进程%d启动 --- pid = %s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print("子进程%d结束 --- pid = %s --- 耗时%.2f" % (name, os.getpid(), end-start))


if __name__ == '__main__':
    print("父进程启动")

    # 进程池
    pp = Pool(4)
    for i in range(6):
        # 创建进程，放入进程池管理
        pp.apply_async(run, args=(i, ))

    # 不能再向进程池添加进程
    pp.close()
    # 进程池对象调用join，会在进程池所有的子进程结束后再去执行父进程
    pp.join()
    print("父进程结束")
