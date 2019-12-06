# -*- coding: utf-8 -*-
import os
from multiprocessing import Process

from pudb.remote import set_trace


def info(title):
    print(title)
    set_trace()
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
