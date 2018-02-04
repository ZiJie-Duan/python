# -- coding:utf-8--

class DL(object):
	def __init__(self):
		self.dlcs = 0

	def q(self):
		self.dlcs = self.dlcs + 1
		print(str(self.dlcs))

	def a(self):
		self.dlcs = 0
		print(str(self.dlcs))

hi = DL()
hi.q()
hi.q()
hi.q()
hi.q()
hi.q()

hi.a()