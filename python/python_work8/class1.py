# -- coding:utf-8--

class Hi(object):
	'''问好'''

	def __init__(self,name,sex):
		'''初始化'''
		self.name = name
		self.sex = sex

	def hello(self):
		print('尊敬的' + self.name + self.sex + '士 您好！')

	def hihihi(self):
		print('hi!!!' + self.name + '最近怎么样啊？')


hii = Hi('朱紫','女')

hii.hello()
hii.hihihi()

hii = Hi('汪文博','男')

hii.hello()
hii.hihihi()

hii = Hi('宫逸君','女')

hii.hello()
hii.hihihi()