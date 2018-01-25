# -*- coding:utf-8-*-

na = {}

bz = True

print("hi！您好，我们需要您来填写一个调查问卷")

while bz == True:
	name = raw_input("您的名字是：")
	wt = raw_input("您最想去的地方是：")

	na[name] = wt

	print("ok!")

	bz_1 = raw_input("请问您还有别人要继续填写词问卷吗？(有/没有)：")

	if bz_1 == "没有":
		bz = False
		print("您已结束调查")

print("调查结果如下：")
for k, v in na.items():
	print("姓名：" + k + "  想去的地方： " + v)




