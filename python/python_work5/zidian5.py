# -- coding:utf-8--

names = ["ljx","zz","gyj","dzj","wwb","why","yxd","zjc"]

ok_names = {
	"ljx":"啥都喜欢吃",
	"gyj":"方便面",
	"dzj":"各种肉",
	"wwb":"屎",
}

for name in names :
	if name in ok_names.keys() :
		print("谢谢你参与这次最喜欢食物调查" + name)
	else :
		print(name + "请问你最喜欢吃的食物是什么？")

