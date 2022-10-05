import dis
import sys

def printa():
    print(sys._getframe().f_back.f_code.co_name)

def warp_maker(func):
    def warp():
        print("OK")
        func()
    return warp
    
@warp_maker
def func1():
    print("OK2")
    printa()

func1()

input()

