# -- coding:utf-8--
import time
import datetime
import json
import uuid
import os

#工作路径
gzlj = os.getcwd()
lj = os.path.join(gzlj, "users.json")

def p_h():
	#打印需要用到的函数
	print("du --------- 删除用户")
	print("au --------- 添加用户")
	print("lu --------- 列出所有用户")
	print("gu --------- 列出过期用户")



def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx


def wl_time(z):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime



def read_json():

	try:
		with open(lj) as zx:
			user = json.load(zx)
		return user
	except:
		return "f"


def w_json(users):

	with open(lj,'w') as ojbk:
		json.dump(users,ojbk)



def main():

	global users

	ui_in = input(": ")

	if ui_in == "du":
		keyy = ""
		#用于删除用户的判断
		print("\n删除用户模块\n")
		user_id = input("id: ")

		for key, value in users.items():
			a = value[4]
			if a == user_id:
				keyy = key
		del users[keyy]
		print("删除完成")


	if ui_in == "au":
		print("\n添加用户模块\n")
		user_name = input("用户名称： ")
		user_an = input("用户其他信息： ")
		user_time = input("用户时间： ")
		nowtime = now_time()
		time_s = int(user_time)
		wltime = wl_time(time_s)
		uid = str(uuid.uuid4())
		users[user_name] = [user_time,nowtime,wltime,user_an,uid]
		print("\n添加完成！\n")


	if ui_in == "lu":

		for key, value in users.items():
			print("\n 用户名称：" + key)
			print("用户激活的时长： " + value[0])
			print("激活时间： " + value[1])
			print("激活到： " + value[2])
			print("用户的其他信息： " + value[3])
			print("用户uuid： " + value[4])


	if ui_in == "gu":
		for key, value in users.items():
			time = value[2]
			print(time)
			nowtime = now_time()
			if time < nowtime:
				print("用户名称： " + key)
				print("用户激活的时长： " + value[0])
				print("激活时间： " + value[1])
				print("激活到： " + value[2])
				print("用户的其他信息： " + value[3])
				print("用户uuid： " + value[4])

	if ui_in == "h":
		p_h()


	if ui_in == "w":
		w_json(users)


import multiprocessing
#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	users = read_json()

	if users == "f":
		print("没有找到用户文件")
		users = {}
	else:
		print("发现用户文件")

	while True:
		main()

	






'''
with open(filename,'w') as ojbk:       //打开文件，存入ojbk中
    json.dump(numbers,ojbk)            //使用函数json.dump 让变量numbers存入ojbk

with open(filename) as zx:        //打开文件，存入变量zx中
    number = json.load(zx)   

'''