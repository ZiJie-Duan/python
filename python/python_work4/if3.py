# -- coding:utf-8--

age_1 = 30
age_2 = 21

print("\n网吧进入规则")

if (age_1 < 18) and (age_2 < 18):
	print("很抱歉，你们未满18岁，不可进入此网吧")
else:
	print("欢迎光临")


print("\n-----------------------------------------------")

print("酒店入住规则")

if (age_1 > 20) or (age_2 > 20):
	print("欢迎光临")
else:
	print("十分抱歉！没有20岁以上的人无法入住！")

