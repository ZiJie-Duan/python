# -- coding:utf-8--

color = "green"

if "green" == color:
	print("+5")
	

if "green" == color:
	print("+5")
else:
	print("+10")


if "green" == color:
	print("+5")
if "green" != color:
	print("+10")
	
print("--------------------------------------------------------------")

color_1 = "red"

if "green" == color_1:
	a = "+5"
elif "red" == color_1:
	a = "+10"
elif "yellow" == color_1:
	a = "+15"
	
print("玩家分数" + a)


print("--------------------------------------------------------------")


age = 38

if (age > 0) and (age < 2):
	print("hi，你好！，你是一名婴儿！")
elif age < 4:
	print("hi，你正在蹒跚学步！")
elif age < 13:
	print("hi,你是一名儿童。")
elif age < 20:
	print("hello!,你可是一个青少年哦！")
elif age < 65:
	print("呦！你现在是个成年人，趁着现在赶紧去啪啪啪吧！")
elif (age < 120) and (age > 64):
	print("啊偶，您现在是老年人了。")
else:
	print("OK！ 你现在可以去买口棺材了！！！")

print("--------------------------------------------------------------")

sg = ["apple","bananas"]

if "apple" in sg:
	print("哦！原来你也喜欢苹果！")
if "bananas" in sg:
	print("哦！原来你也喜欢香蕉！")
if "sb" in sg:
	print("哦！原来你也喜欢sb！")










