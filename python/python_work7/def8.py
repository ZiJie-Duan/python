# -- coding:utf-8--

def sandwich(*toppings):
	print('已添加的配料：')
	for zs in toppings:
		print('- ' + zs)

sandwich('蛋黄酱','三文鱼','玉米粒')