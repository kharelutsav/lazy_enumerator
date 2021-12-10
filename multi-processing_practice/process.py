from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)


def g():
    info('function g')
    print("Fuck off")

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    q = Process(target=g)
    q.start()
    p.start()
    p.join()
    q.join()
    info('main line')