# -- coding:utf-8--

class User(object):
	'''The class used to store user information'''
	def __init__(self,last_name,first_name,sex,age,address):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.address = address

	def info(self):
		print('个人信息列表：')
		print('姓：' + self.last_name)
		print('名：' + self.first_name)
		print('性别：' + self.sex)
		print('年龄：' + self.age)
		print('住址：' + self.address)

	def hello(self):
		print(self.last_name + self.first_name + '你好啊！')

hi = User('汪','文博','男','15','北京市东城区太阳宫')

hi.info()
hi.hello()

hi = User('朱','紫','女','16','北京市东城区朝阳门南小街')

hi.info()

hi = User('李','嘉熙','男','15','内蒙古包头市昆都仑区凯旋豪庭')

hi.info()