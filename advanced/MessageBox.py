import time
import sys
from types import FunctionType

"""
How to use it
|

from MessageBox import*
mp,print = init_env()

@MessageBox(mp)

add these code befor function or class

"""


class MessagePrinter:

    def __init__(self) -> None:
        self.setting = {
            "date_and_time" : False,
            "time" : True,
            "source" : True,
            "type" : True,
        }
            #type有四种类型
            # IS-info, INFO, ERR, WARN
            # inside_info 不具有用户提示的属性
        self.original_print = print

    def print_core(self,message,type="INFO",source="None"):
        ms = ""
        if self.setting["date_and_time"]:
            t = time.time()
            timeArray = time.localtime(t)
            ms += time.strftime("%Y-%m-%d %H:%M:%S ", timeArray)
        if self.setting["time"]:
            t = time.time()
            timeArray = time.localtime(t)
            ms += time.strftime("%H:%M:%S ", timeArray)
        if self.setting["type"]:
            ms += "[{}]".format(type)
        if self.setting["source"]:
            ms += "({})".format(source)
        ms += ":"+str(message)
        self.original_print(ms)


class MessageBox:

    def __init__(self,mp,mode="easy"):
        #here input arguments
        self.mp = mp # message class
        self.mode = mode # mode choice 
    
    def __call__(self,cla):
        # find out all of the functions created by the programmer
        if isinstance(cla,FunctionType):
            # cla is a function
            func = self.wrapper_maker(cla)
            return func
        else:
            # cla is a class

            all_functions = dir(cla)
            function_list = []
            for function in all_functions:
                if "__" == function[:2] and "__" == function[-2:]:
                    pass
                else:
                    function_list.append(function)

            # cover the original code to add the wrapper
            for function in function_list:
                exec("cla.{} = self.wrapper_maker(cla.{})".\
                    format(function,function))
            return cla

    def wrapper_maker(self,func):
        if self.mode == "easy":
            def wrapper(*args, **kwds):
                self.mp.print_core("start running","IS-info",func.__name__)
                return func(*args, **kwds)
                # here must get the number of the arguments
                # then chooise use *args or not 
            return wrapper
        else:
            def wrapper(*args, **kwds):
                self.mp.print_core("start running","IS-info",func.__name__)
                result = func(*args, **kwds)
                self.mp.print_core("finish","IS-info",func.__name__)
                return result
            return wrapper

def init_env():
    mp = MessagePrinter()
    def print(message,type="INFO"):
        source = sys._getframe().f_back.f_code.co_name
        mp.print_core(message,type,source)
    return mp, print

