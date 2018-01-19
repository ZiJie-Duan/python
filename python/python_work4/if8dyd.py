# -- coding:utf-8--

names = []
if names:
    for name in names:
	    if name == "admin":
		    print("hi，欢迎回来管理员，接下来做些什么？")
	    else:
		    print("您好，欢迎登陆！")
else:
	print("请输入用户名")


print("---------------------------------------------------------------")


users = ["gyj","dzj","wwb","zz","ljx"]

users_1 = ["yxd","Gyj","lJx","zke","zyx"]

users_2 = []

for u_2 in users_1:
		u_3 = u_2.lower()
		users_2.append(u_3)

print(users_2)

for u_1 in users:
	if u_1 in users_2:
		print("抱歉，" + u_1 + "这个用户名已被注册！")
	else:
		print(u_1 + "这个用户名可以使用！")
		
		
print("---------------------------------------------------------------")


z = list(range(1,11))

for z_1 in z:
	if z_1 == 1 :
		print(str(z_1) + "st")
	elif z_1 == 2 :
		print(str(z_1) + "nd")
	elif z_1 == 3 :
		print(str(z_1) + "rd")
	else:
		print(str(z_1) + "nd")
		
