"""
def warpper_maker(func):
    def warpper():
        a = 666
        func()
    return warpper

@warpper_maker
def func1():
    print(a)


func1()
"""
import dis


def warp_maker(func):
    def warp():
        print(dir(func.__code__))
        func()
    return warp

def func1():
    print(a)

func1 = warp_maker(func1)
func1()
input()