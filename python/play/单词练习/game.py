# -- coding:utf-8--
import random

def read_word():
	#用于读取word的函数
	#返回一个二维数组
	en_word = []
	ch_word = []
	word = []

	#读取中文单词 存入列表
	with open("wc.txt") as x:
		for xx in x:
			#去除换行符
			xxx = xx.strip('\n')
			ch_word.append(xxx)

	#读取英文单词 存入列表
	with open("we.txt") as x:
		for xx in x:
			#去除换行符
			xxx = xx.strip('\n')
			en_word.append(xxx)

	#求出列表含有多少个单词
	number_word = len(en_word)
	for x in range(number_word):
		#组合为一个单词二维列表
		add_word = [ch_word[x],en_word[x]]
		word.append(add_word)

	return word


def random_word(english,chinese):
	#拼写函数
	print("please type the English word of this meaning: " + chinese)
	
	while True:	
		word = input(": ")
		if word == english:
			print("yes!")
			break
		else:
			print("Wrong, please try again.")


def mc_word_ch(english,chinese,chinese2,chinese3,chinese4):

	#用于进行中文选择题的函数
	print("Please choose the correct Chinese ")
	print("word: " + english)
	lb = [chinese,chinese2,chinese3,chinese4]

	#将列表随机化
	lb_sj = random.sample(lb, 4)

	#数字列表
	number_lb = ["1","2","3","4"]

	for x in range(1,5):
		#格式化输出
		print(str(x) + ", " + lb_sj[x-1])

	print("")

	while True:	
		mc = input("Please enter the correct serial number： ")
		#获取用户选择答案
		mcc = lb_sj[int(mc)-1]
		if mcc == chinese:
			print("yes!")
			break
		else:
			print("Wrong, please try again.")


def mc_word_en(english,chinese,english2,english3,english4):

	#用于进行英文选择题的函数
	print("Please choose the correct English ")
	print("word: " + chinese)
	lb = [english,english2,english3,english4]

	#将列表随机化
	lb_sj = random.sample(lb, 4)

	#数字列表
	number_lb = ["1","2","3","4"]

	for x in range(1,5):
		#格式化输出
		print(str(x) + ", " + lb_sj[x-1])

	print("")

	while True:	
		mc = input("Please enter the correct serial number： ")
		#获取用户选择答案
		mcc = lb_sj[int(mc)-1]
		if mcc == english:
			print("yes!")
			break
		else:
			print("Wrong, please try again.")


def random_list(list):
	#随机列表生成函数
	number_lb = len(list)
	list_sj = random.sample(list, number_lb)
	return list_sj


def read_lb_z(list):
	#返回列表值
	a = list[0]#ch
	b = list[1]#en
	return a, b 


def random_ch(word_list):
	#用于获取干扰信息的函数
	number_lb = len(word_list)
	list_sj = random.sample(word_list, number_lb)
	sj_sx = random.sample(list_sj, 3)
	ch_2 = sj_sx[0][0]
	ch_3 = sj_sx[1][0]
	ch_4 = sj_sx[2][0]
	return ch_2,ch_3,ch_4
	


def random_en(word_list):
	#用于获取干扰信息的函数
	number_lb = len(word_list)
	list_sj = random.sample(word_list, number_lb)
	sj_sx = random.sample(list_sj, 3)
	en_2 = sj_sx[0][1]
	en_3 = sj_sx[1][1]
	en_4 = sj_sx[2][1]
	return en_2,en_3,en_4



def main():
	print("单词游戏 请选择您需要的模式：")
	print("1,检查拼写")
	print("2,英文单选")
	print("3,中文单选")

	mod = input("请选择(输入序号即可)：")
	cqmod = input("单词是否随机抽取？(y/n)：")

	if cqmod == "y":
		if mod == "1":
			#获取单词
			word_list = read_word()
			#获取随机顺序单词列表
			word_list_sj = random_list(word_list)
			for word_l in word_list_sj:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				random_word(en,ch)

		if mod == "2":
			word_list = read_word()
			word_list_sj = random_list(word_list)
			for word_l in word_list_sj:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				en2,en3,en4 = random_en(word_list_sj)
				mc_word_en(en,ch,en2,en3,en4)


		if mod == "3":
			word_list = read_word()
			word_list_sj = random_list(word_list)
			for word_l in word_list_sj:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				ch2,ch3,ch4 = random_ch(word_list_sj)
				mc_word_ch(en,ch,ch2,ch3,ch4)


	if cqmod == "n":
		if mod == "1":

			#获取单词
			word_list = read_word()
			for word_l in word_list:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				random_word(en,ch)

		if mod == "2":

			word_list = read_word()
			for word_l in word_list:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				en2,en3,en4 = random_en(word_list)
				mc_word_en(en,ch,en2,en3,en4)

		if mod == "3":
			word_list = read_word()
			for word_l in word_list:
				#获取中文与英文
				ch, en = read_lb_z(word_l)
				ch2,ch3,ch4 = random_ch(word_list)
				mc_word_ch(en,ch,ch2,ch3,ch4)


main()