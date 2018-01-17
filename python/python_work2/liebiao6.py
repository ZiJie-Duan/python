# -*- coding:utf-8-*-

name = ["dzj","zz","ljx"]

name_1 = name.pop()

print(name)

print(name_1)

name_1 = name.pop(0)

print(name)

print(name_1)


name.append("zke")

name.insert(0,"gyj")

print(name)

print("以上内容毫无意义，不必观看")
print("--------------------分界线----------------------")

print("以下是我的女性朋友名单：")
print(name)

name_3 = "gyj"

name.remove(name_3)

print("这个是我的新的女性朋友名单")
print(name)

print("因为某些原因，‘gyj’不再是我的朋友，所以我调用remove函数删除‘gyj的名字’")
print(" name_3 = 'gyj'\n name.remove(name_3)")

#不得不说上面的制表换行好强大