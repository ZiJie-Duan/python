# -- coding:utf-8--
import json

lj = 'user.json'

try:
	with open(lj) as name:
		names = json.load(name)
except:
	namename = input('请输入您的名字')
	with open(lj,'w') as name:
		json.dump(namename,name)
	print('欢迎！' + namename)
else:
	print("请问您是" + names + "吗？")
	z = input('yes/no')
	if z == 'yes':
		print("欢迎回来！" + names)
	else:
		namename = input('请输入您的名字')
		with open(lj,'w') as name:
			json.dump(namename,name)
			print('欢迎！' + namename)
