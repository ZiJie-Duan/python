import time
import sys

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
        ms += ":"+message
        print(ms)


class MessageBox:

    def __init__(self,mp,mode="easy"):
        #here input arguments
        self.mp = mp # message class
        self.mode = mode # mode choice 
    
    def __call__(self,cla):
        # find out all of the functions created by the programmer
        self.cla = cla

        all_functions = dir(self.cla)
        function_list = []
        for function in all_functions:
            if "__" == function[:2] and "__" == function[-2:]:
                pass
            else:
                function_list.append(function)

        # cover the original code to add the wrapper
        for function in function_list:
            exec("self.cla.{} = self.wrapper_maker(self.cla.{})".\
                format(function,function))
        return self.cla

    def wrapper_maker(self,func):
        if self.mode == "easy":
            def wrapper(*args, **kwds):
                self.mp.print_core("start running","IS-info",func.__name__)
                func(*args, **kwds)
            return wrapper
        else:
            def wrapper(*args, **kwds):
                self.mp.print_core("start running","IS-info",func.__name__)
                func(*args, **kwds)
                self.mp.print_core("finish","IS-info",func.__name__)
            return wrapper


def printm(message,type="INFO"):
    source = sys._getframe().f_back.f_code.co_name
    mp.print_core(message,type,source)

mp = MessagePrinter()

@MessageBox(mp=mp)
class GoodBoy:

    def __init__(self):
        self.name = ""
    
    def say_hello(self):
        printm("hello: "+self.name)
    
    def say_bey(self):

        printm("bey~~ "+self.name)
    
    def __unhappy(self):
        printm("OHNO!! "+self.name)

    def say_it_does_not_matter(self):
        self.__unhappy()
        printm("It doesn't matter " + self.name)


gb = GoodBoy()
gb.name = "Peter"
gb.say_hello()
gb.say_it_does_not_matter()
gb.say_bey()
input()