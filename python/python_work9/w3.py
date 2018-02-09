# -- coding:utf-8--
bz = True

while bz == True:
	print('加法计算器')
	aa = input('加数：')
	bb = input('加数：')
	input('按下回车继续')
	if aa == 'q':
		break
	try:
		a = int(aa)
		b = int(bb)
	except:
		print('请您输入数字')
		print('请重新启动程序')
	else:
		c = a + b
		print(c)
