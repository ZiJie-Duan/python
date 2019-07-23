
def make_time_list():
	re = []
	for x in range(100,1000):
		for y in range(100,1000):
			c = x * y
			c = str(c)
			re.append(c)

	return re

def yz_hw(z):

	zt = True

	list_z = list(z)

	if len(list_z)%2 == 0:
		for x in range(0,len(list_z)):
			y = len(list_z)-1-x
			if list_z[x] != list_z[y]:
				zt = False

	else:
		xhz = len(list_z) + 1
		xhz = xhz//2
		xhz = xhz - 1

		for x in range(0,xhz):
			y = len(list_z)-x-1
			if list_z[x] != list_z[y]:
				zt = False
	return zt


def get_max_hw(l):
	listx = []
	maxs = ""

	for x in l:

		if yz_hw(x):
			listx.append(x)

	maxs = int(listx[0])
	for x in listx:
		if maxs < int(x):
			maxs = int(x)


	return maxs


a = make_time_list()

print(get_max_hw(a))


















