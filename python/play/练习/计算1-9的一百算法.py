
def change_ten_to_t(x):
	z_list = []
	xx = x
	while True:
		if xx == 0:
			break
		else:
			z = divmod(xx,3)
			st = str(z[1])
			z_list.append(st)
			xx = z[0]

	z_list = z_list[::-1] #反转列表的语法
	
	nb = len(z_list)
	for x in range(8 - nb):
		z_list.append("0")

	return z_list


def make_t_list():
	re_list = []

	for x in range(1,6561):
		re_list.append(change_ten_to_t(x))
	return re_list


def c(main_list):
	main_c_list = []
	for x in main_list:
		son_str = "1"
		js = 2
		for y in x:
			if y == "0":
				son_str = son_str + str(js)
				js += 1
			if y == "1":
				son_str = son_str + " + " + str(js)
				js += 1
			if y == "2":
				son_str = son_str + " - " + str(js)
				js += 1

		main_c_list.append(son_str)
	return main_c_list

def c_v(e):
	for x in e:
		v = eval(x)
		if v == 100:
			print(x)
			print(v)



l = make_t_list()
e = c(l)
c_v(e)

