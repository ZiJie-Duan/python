import dis
from re import S

#不传参的修饰器
def wrapper(func):
    #定义一个修饰器的构造器
    def message_box(name):
        #定义一个修饰器, name 为func的参数
        func_name = func.__name__
        print("[{}] 调用函数".format(func_name))
        func(name)
        print("[{}] 运行结束".format(func_name))
    return message_box
        #使用闭包方法将 包裹着函数的修饰器返回

@wrapper # 等价于 say_hello = wrapper(say_hello)
def say_hello(name):
    print("hello! {}".format(name))

say_hello("Ethan")
input()

def message_box(type): #带有参数修饰器
    #type 参数用于传入关于修饰器的调整参数
    if type == "easy":
        def wrapper(func):
            #第二层函数 用于传入function
            #第二层并不会被表现出来
            def mgb(*args):
                func_name = func.__name__
                print("[{}] 调用函数".format(func_name))
                func(*args)
            return mgb
        return wrapper
    else:
        def wrapper(func):
            def mgb(*args):
                func_name = func.__name__
                print("[{}] 调用函数".format(func_name))
                func(*args)
                print("FINISH")
            return mgb
        return wrapper

@message_box("a")
def say_hello3(name):
    print("hello! {}".format(name))

say_hello3("Ethan")
input()


class MessageBox:
    # 使用类进行修饰器的实现
    def __init__(self,func) -> None:
        self.func = func
        #此处，在类初始化的时候将function传入
        #将function作为类的内部属性
    
    def __call__(self, *args) -> None:
        #__call__是python的高级语法，魔法函数
        #call 可以将实例化的类作为可执行对象来调用
        #call 等价于 () 
        print("[{}] 调用函数".format(self.func_name))
        self.func(*args)
        print("[{}] 运行结束".format(self.func_name))
    
    #所以，本质上就是 将一个函数传入类中
    #将整个类包裹函数，并使用call将整个类变为可调用对象

@MessageBox
def say_hello2(name):
    print("hello! {}".format(name))

say_hello("Peter")
input()


class MessageBox2:
    #带参数的类修饰器
    def __init__(self,cargs) -> None:
        self.cargs = cargs
        #初始化用于初始化 类的导出参数
    
    def __call__(self, func):
        #call 函数用于传入function
        def mg(*args):
            #此处是被包裹起来的函数
            print("args = " + args[0])
            func(*args)
        return mg


@MessageBox2("None")
def say_hello4(name):
    print("hello! {}".format(name))

say_hello4("Peter")
input()