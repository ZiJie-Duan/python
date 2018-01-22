
# -- coding:utf-8--

food = {
	"烤串":"东北",
	"烧麦":"内蒙古",
	"涮羊肉":"内蒙古",
	"烤鸭":"北京",
	"生煎":"上海",
	"火锅":"四川",
	"臭豆腐":"长沙",
	"寿司":"日本",
	"生鱼片":"日本",
	"饭团":"日本",
}

for k, v in food.items():
	kz = k
	vz = v
	print("想要吃" + kz + "就去" + v)


print("\n我想要吃的食物")

for k in food.keys():
	kz = k
	print(k)


print("\n好吃的食物的所在位置")

for v in set(food.values()):
	vz = v
	print(vz)

