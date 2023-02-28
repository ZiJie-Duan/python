import json
from types import FunctionType

"""
from memo import *

@MEMO()
"""

memory_var = None

def memory_global():
    global memory_var
    if memory_var:
        pass
    else:
        memory_var = MEMORY()
    return memory_var


class MEMORY:

    def __init__(self) -> None:
        self.memo = {}
        self.memo_path = "memo.json"
        self.memo_load()
    
    def __call__(self, key):
        return self.memo[key]
    
    def memo_load(self):
        try:
            with open(self.memo_path,"r") as f:
                self.memo = json.load(f)
        except:
            self.memo = {}

    def memo_write(self):
        with open(self.memo_path,"w") as f:
            json.dump(self.memo,f)
        
    def memo_add(self,key,value):
        self.memo[key] = value
        self.memo_write()
    
    def memo_del(self,key):
        del self.memo[key]
        self.memo_write()


class MEMO:
    """
    MEMO is a wrapper
    if used to record the value of attributes of each class

    it can be used on functions or classes.
    in functions, it will save the data in a file when the function start.
    in classes, it will record all the attributes when the init-function finished.
    now the MEMO only can record some base data class
    it can't record the calss which have abstract function or incloud other classes
    """

    def __init__(self, memory_mode = "normal"):
        self.memory_mode = memory_mode
        self.memory = memory_global()
    
    def __call__(self, mclass):
        
        if isinstance(mclass,FunctionType):
            # mclass is a function
            mfunction = mclass
            func = self.writer(mfunction)
            return func
        else:
            # mclass is a class
            mclass.__init__ = self.initer(mclass.__init__)

            return mclass
        
    def writer(self,mfunction):
        def wrapper(*args, **kwds):
            result = mfunction(*args, **kwds)
            self.save()
            return result
        return wrapper
    
    def initer(self,mclass):
        # this function used to init a class or record a class
        def wrapper(*args, **kwds):
            mclass(*args, **kwds)
            if args[0].__class__.__name__ in self.memory.memo:
                # if the data already in the memory structure
                for key, value in self.memory.memo[args[0].__class__.__name__].items():
                    args[0].__dict__[key] = value
            # if the data not in the memory structure
            # the function will record it
            self.memory.memo[args[0].__class__.__name__] = args[0].__dict__
        return wrapper

    def save(self):
        self.memory.memo_write()


# class MM:

#     def __init__(self):
#         self.data = {}

#     def __call__(self, key, value = None):
#         if value != None:
#             self.data[key] = value
#             return 0
#         return self.data[key]


# # @MEMO()
# class say_hello:

#     def __init__(self) -> None:
#         self.name = None
#         self.name2 = None

#     @MEMO()
#     def say_hello(self):
#         print("hello {}".format(self.name))
    
#     def say2_hello(self):
#         print("hello {} and {}".format(self.name,self.name2))


# sh = say_hello()
# sh.name = "peter"
# sh.name = "jason"
# sh.say_hello()
# sh.say2_hello()
# print()
