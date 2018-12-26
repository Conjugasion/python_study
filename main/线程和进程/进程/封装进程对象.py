"""
@author Lucas
@date 2018/12/12 21:28
自定义进程
"""
import os
import time
from multiprocessing import Process


class lucasProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s-%s)启动" % (self.name, os.getpid()))
        time.sleep(3)
        print("子进程(%s-%s)结束" % (self.name, os.getpid()))
