# -- coding:utf-8--
print("您好！欢迎来到我们的2333餐厅")
nomber = raw_input("请问你们有多少人？")

z = int(nomber)

if z > 8:
	print("十分抱歉，没有空位了")
else:
    print("还有空位子，请您往里走")


#raw_input("请问你们有多少人？")

nomber = raw_input("请输入10的倍数")


z = int(nomber) % 10
if z == 0:
	print("ok")