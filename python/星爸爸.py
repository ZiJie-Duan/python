# -- coding:utf-8--

class User(object):
	'''bbbbbb'''
	def __init__(self,name,age,sex,address):
		self.name = name
		self.age = age
		self.sex = sex
		self.address = address

	def ad(self):
		print('管理员列表：')
		print(self.name)
		print(self.age)
		print(self.sex)
		print(self.address)


class Coffee(object):
	def __init__(self):
	    self.coffee = ['拿铁','豆奶拿铁','香草拿铁','榛果风味拿铁','浓郁咖啡拿铁','焦糖玛奇朵','摩卡','卡布奇诺','美式咖啡']
	    self.tea = ['抹茶拿铁','红茶拿铁','冰摇桃桃绿茶','冰摇柚柚蜂蜜红茶','冰摇红莓黑加仑茶','冰摇芒果花草茶','冰摇柠檬茶','乌龙茶']
	    self.xbl = ['抹茶','抹茶可可碎片','浓缩咖啡','焦糖咖啡','摩卡可可碎片','榛果风味摩卡','香草风味','芒果西番莲果茶','芒果豆奶']
	    self.ps = ''
	    self.name = ''
	    self.size = ''

	def work_process(self):
		print('\n手工调制浓缩咖啡：')
		for ls_1 in self.coffee:
			print('\t' + ls_1)
		print('\n茶瓦纳：')
		for ls_2 in self.tea:
			print('\t' + ls_2)
		print('\n星冰乐_：')
		for ls_3 in self.xbl:
			print('\t' + ls_3 + '星冰乐')
		print('\n请问您需要些什么？')
		sham_name = raw_input('\t名称：')
		sham_size = raw_input('\t(小杯/大杯/超大杯)：')
		sham_ps = raw_input('\t备注：')
		self.name = sham_name
		self.ps = sham_ps
		self.size = sham_size

		print('\n您的订单：')
		print('\t名称：' + self.name)
		print('\t大小：' + self.size)
		print('\t备注：' + self.ps)



