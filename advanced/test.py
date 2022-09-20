
from ast import arg


def print(*args):
    print(*args)


def wapp(func):
    def wappp(name):
        print("wappp::",func.__name__)
        func(name)
    return wappp



print(dir(print))