def wapp(func):
    def wappp(name):
        print("wappp::",func.__name__)
        func(name)
    return wappp

def cl_wap(clas):
    pass

class SayGood:
    
    def __init__(self,name) -> None:
        self.name = name

    def say_good(self):
        print("you are good",self.name)
    
    def say_bey(self):
        print("see you next week",self.name)
        


SayGood.say_bey = wapp(SayGood.say_bey)

sg = SayGood("peter")
sg.say_bey()