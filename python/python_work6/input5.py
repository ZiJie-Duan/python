# -*- coding:utf-8-*-

stop = ""

print("欢迎来到贝拉贝拉电影院")

stop_1 = 0

stop_2 = ""

while stop_1 < 5:
	stop = raw_input("请问您的年龄是？")

	stop_1 = stop_1 + 1

	stop_2 = stop

	if stop_2 == "q!":
		break
	else:
		if int(stop) < 3:
			z = 3
		elif int(stop) < 13:
			z = 10
		elif int(stop) < 100:
		 	z = 15
		print("您的年龄所对应的票价是： " + str(z))


	    