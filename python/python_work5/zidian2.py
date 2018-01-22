# -- coding:utf-8--

word = {}

word["title()"] = "title() 将字串符全部转换为首字母大写"
word["upper()"] = "upper() 将字串符全部转换为大写"
word["lower()"] = "lower() 将字串符全部转换为小写"

#以下是字典4部分内容的输入

word["keys()"] = "keys() 只选定字典中的键"
word["sorted()"] = "sorted() 按照顺序打印字典"
word["valuse()"] = "valuse() 只选定字典中的值"
word["set"] = "set() 只打印不相同的值"
word["items()"] = "items() 打印值和键"


for k, v in word.items():
	print("\n函数名称：" + k)
	print("函数用法：" + v)

