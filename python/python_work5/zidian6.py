# -- coding:utf-8--

user_0 = {"姓名":"朱紫","年龄":"16","性别":"女","居住城市":"北京"}

user_1 = {"姓名":"李嘉熙","年龄":"14","性别":"男","居住城市":"包头"}

user_2 = {"姓名":"汪文博","年龄":"16","性别":"男","居住城市":"北京"}

users = [user_0,user_1,user_2]

q = 0
for user in users:
	q = q + 1
	print("\n以下是用户" + str(q) + "的信息")
	for k, v in sorted(user.items()):
		print(k + ":" + v)

print("------------------------------------------------------------------")


cat = {"name":"老虎","age":"0.3","master":"段子杰"}

dog = {"name":"danfer","age":"4","master":"祖嘉豪"}

animals = [cat,dog]


for animal in animals:
	print("\n")
	for k, v in animal.items():
		print(k + ":" + v)
	
print("------------------------------------------------------------------")

favorite_places = {
    "朱紫":"日本",
    "段子杰":"日本",
    "汪文博":"粪堆",
}

for name, address in favorite_places.items():
	print(name + "想要去" + address)

