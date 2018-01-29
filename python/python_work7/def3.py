# -- coding:utf-8--

def make_shirt(cm = "xxl" , zy = "i love python"):
	print("您需要的尺码是：" + cm)
	print("您要打印的字样是：\n\t" + zy)

make_shirt("xl","hello! world!")

make_shirt()

def city(cs , gj):
	print(cs + '属于' + gj)

city('北京','中国')
city('华盛顿','美国')
city('东京','日本')