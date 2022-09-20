import time
from types import TracebackType

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

    def print(self,message,type,source):
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

    def __init__(self,func):
        self.func = func
        self.mp = MessagePrinter()
    
    def __call__(self, *args, **kwds):
        self.
        

