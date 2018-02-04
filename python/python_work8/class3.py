# -- coding:utf-8--

class users(object):
	def __init__(self,name,sex):
		self.name = name
		self.sex = sex
		self.age = 0

	def info(self):
		print('用户信息列表：')
		print('姓名：' + self.name)
		print('性别：' + self.sex)

	def infox(self):
		print('用户信息列表：')
		print('姓名：' + self.name)
		print('性别：' + self.sex)
		print('年龄：' + str(self.age))

	def sz(self,z):
		self.age = z

	def szj(self,zx):
		self.age += zx

user = users('dzj','man')

user.info()

#user.age = 16

user.sz(15)
user.szj(1)

user.infox()

