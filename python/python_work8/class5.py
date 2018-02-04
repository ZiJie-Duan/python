# -- coding:utf-8--

class HI(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def hello(self):
		print('hello! ' + self.name)
	def godie(self):
		print('hhhh' + str(self.age))

class Hii(HI):
	def __init__(self,name,age,ce):
		super(Hii,self).__init__(name,age)
		self.ce = ce

	def a(self):
		print(self.ce)


hi = Hii('dzj',16,'lucycore')

hi.hello()

hi.a()
