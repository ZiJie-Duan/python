# -*- coding:utf-8-*-

stop = ""

print("欢迎来到贝拉贝拉电影院")

while stop != "stop":
	stop = raw_input("请问您的年龄是？")

	if stop != "stop":
		if int(stop) < 3:
			z = 3
		elif int(stop) < 13:
			z = 10
		elif int(stop) < 100:
			z = 15
		print("您的年龄所对应的票价是： " + str(z))
	else:
		print("您已退出票价查询")
   
