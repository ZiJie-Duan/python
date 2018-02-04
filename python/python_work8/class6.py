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

class Admin(User):
	def __init__(self,last_name,first_name,sex,age,address):
		super(Admin,self).__init__(last_name,first_name,sex,age,address)
		self.privileges = []

	def add(self):
		ad = raw_input('add ')
		self.privileges.append(ad)
		print(ad)

	def output(self):
		print(self.privileges)

ces = Admin('d','zj','man','16','beijing')

ces.add()
ces.add()
ces.add()

ces.info()

ces.output()

