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
        self.source = None

    def print(self,message,type):
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
            ms += "({})".format(self.source)
        ms += ":"+message
        print(ms)

class MessageBox:

    def __init__(self,cla):
        self.cla = cla
    
    def __call__(self):
        all_functions = dir(self.cla)
        function_list = []
        for function in all_functions:
            if "__" == function[:2] and "__" == function[-2:]:
                pass
            else:
                function_list.append(function)

        for function in function_list:
            exec("self.cla.{} = self.wrapper_maker(self.cla.{})".\
                format(function,function))
        return self.cla


    def wrapper_maker(self,func):
        def wrapper(*args, **kwds):
            mp = MessagePrinter()
            mp.source = func.__name__
            mp.print("function is running","IS-info")
            exec("self.cla.{}_mp = mp".format(mp.source))
            func(self.cla, *args, **kwds)
        return wrapper

def printm(cla,message,type="INFO"):
    funcName = sys._getframe().f_back.f_code.co_name
    exec("""cla.{}_mp.print("{}","{}")""".format(funcName,message,type))

@MessageBox
class GoodBoy:

    def __init__(self):
        self.name = ""
    
    def say_hello(self):
        printm(self,"hello: "+self.name)
    
    def say_bey(self):

        printm(self,"bey~~ "+self.name)
    
    def __unhappy(self):
        printm(self,"OHNO!! "+self.name)

    def say_it_does_not_matter(self):
        self.__unhappy()
        printm(self,"It doesn't matter " + self.name)


gb = GoodBoy()
gb.name = "Peter"
gb.say_hello()
gb.say_it_does_not_matter()
gb.say_bey()
input()