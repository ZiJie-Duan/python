
def func1(v1):
    #此处 v1在func1被定义时作为
    # func2不可修改的全局变量
    # 但对于全局依旧是局部变量
    def func2(v2):
        #func2 进行一些内部运算
        print(v1*v2)
    return func2 #函数将func2返回

f1 = func1(3)
f1(2)
f1(6)

def func3(v1):
    def func4(v2):
        return v1*v2
        #返回结果仅是形式不同
    return func4

f2 = func3(2)
print(f2(3))