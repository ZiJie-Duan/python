# -*- coding:utf-8-*-

sandwich = ["金枪鱼三明治","蛋黄酱三明治","大虾三明治"]

my_sandwich = []

while sandwich :
	ls = sandwich.pop()
	print("加入列表")
	print(ls)

	my_sandwich.append(ls)

print("我喜欢的三明治")

print(my_sandwich)