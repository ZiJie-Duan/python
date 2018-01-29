# -- coding:utf-8--

def hi(name,age,sex = "无性别的"):
	print("hello!" + name)
	print("你今年" + age + "岁了")
	print("你是个" + sex + "孩子")

hi("宫逸君","15","女")

hi(age = "150" , name = '汪文博', sex = "狼")#先列出没有预设的

hi("汪文博","233333")

