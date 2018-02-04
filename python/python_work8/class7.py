# -- coding:utf-8--

class AB(object):
	def __init__(self,a=6666):
		self.a = a

	def i(self):
		print(self.a)


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
		self.b = AB()


hiiiii = Admin('d','zj','man','16','lucyc')

hiiiii.b.i()

