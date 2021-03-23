#因式解析器
number = input("a>>")
number = int(number)
#number2 = input("b>>")
#number2 = int(number2)


for x in range(number):
	for y in range(number):
		value = x*y 
		if value == number:
			print("匹配结果：" + str(x) + "---"+ str(y))