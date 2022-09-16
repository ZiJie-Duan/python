
def func(*k):
    #当*号写于函数参数定义前方时
    #作为收集器来使用，收集不限数量的参数
    #作为列表存入K
    for x in k:
        print(x)

func(1,2,3,4,5,6) #多参数示例 
func(*[1,2,3,4]) #当*号存在于列表之前时，将列表解开作为顺序变量传入

def func2(*k,**y):
    #**双星号 作为有名字的参数的传入标志
    #双星号 收集变量，并自动存入字典
    for i in k:
        print(i)
    for key, value in y.items():
        print("{} : {}".format(key,value))

func2(1,2,3,name="hello",name2="hiii")
