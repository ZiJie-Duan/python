import time

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
            func(self.cla, *args, **kwds)
        return wrapper



class GoodBoy:

    def __init__(self):
        self.name = ""
    
    def say_hello(self):
        print("hello",self.name)
    
    def say_bey(self):
        print("bey~~",self.name)
    
    def __unhappy(self):
        print("OHNO!!")

    def say_it_does_not_matter(self):
        self.__unhappy()
        print("It doesn't matter ",self.name)

gb = GoodBoy()
gb.name = "Peter"
gb.say_hello()
gb.say_it_does_not_matter()
gb.say_bey()
input()