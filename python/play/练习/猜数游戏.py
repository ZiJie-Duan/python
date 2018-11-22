a = input("您想生成多大数字以内的随机数：")
print("我已随机生成一个" + a + "以内的数字")

import random
jgz = random.randint(0,int(a))

js = 0
while True:
	cc = input("您猜一个数：")
	if jgz == int(cc):
		js += 1
		break
	if jgz > int(cc):
		print("小了！")
		js += 1
	if jgz < int(cc):
		print("大了！")
		js += 1


print("恭喜您，猜到了！")
print("您一共猜测了" + str(js) + "次")
input()