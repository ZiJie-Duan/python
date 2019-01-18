
zd = {}
zd_2 = {}
zd_3 = {}

for x in range(0,12):
	for y in range(0,10):
		zd[str(x)+" "+str(y)] = "0"


zd["4 5"] = 2
zd["5 5"] = 1
zd["6 5"] = 2
zd["7 5"] = 1
zd["4 4"] = 1
zd["5 4"] = 2
zd["6 4"] = 1
zd["7 4"] = 2

z = []
for x in range(1,11):
	for y in range(1,9):
		a = str(x) + " " + str(y)
		z.append(a)

def change_zdz(zb,z,zz):
	zz[zb] = z


def derta(zb):
	zdz_2 = []
	zdz = []
	zb_lb = zb.split(' ')
	x = zb_lb[0]
	y = zb_lb[1]
	zb_1 = [int(x)+1,int(y)]
	zb_2 = [int(x)-1,int(y)]
	zb_3 = [int(x),int(y)+1]
	zb_4 = [int(x),int(y)-1]
	a = [zb_1,zb_2,zb_3,zb_4]
	for nb in a:
		x = nb[0]
		y = nb[1]
		zfc = str(x) + " " + str(y)
		zdz_zc = zd[zfc]
		zdz.append(zdz_zc)
	for x in zdz:
		b = int(x)
		zdz_2.append(b)

	e = max(zdz_2)
	return e


def qqq(zb):
	a = derta(zb) - 1.5
	b = a / abs(a)
	c = b+1
	return c


def j(zb):
	a = zd[zb]
	b = int(a)
	c = b - 0.5
	d = c / abs(c)
	return d


def dsd(zb):
	a = zd[zb]
	b = int(a)
	c = 1 + j(zb)
	d = c / 2
	e = 1 - j(zb)
	f = e / 2
	g = f * qqq(zb)
	h = b - d + g
	return h


def main():
	import copy

	global zd_2
	#for y in range(3):
	for x in z:
		rez = dsd(x)
		
		zd_2 = copy.deepcopy(zd)
		change_zdz(x,rez,zd_2)
	gshsc()
	


def gshsc():
	nbnb = []
	for x in range(1,11):
		for y in range(1,9):
			a = str(x) + " " + str(y)
			nbnb.append(a)
	
	z_lb = []
	for x in nbnb:
		b = zd[x]
		z_lb.append(b)

	asd_1 = z_lb[0:10]
	asd_2 = z_lb[10:20]
	asd_3 = z_lb[20:30]
	asd_4 = z_lb[30:40]
	asd_5 = z_lb[40:50]
	asd_6 = z_lb[50:60]
	asd_7 = z_lb[60:70]
	asd_8 = z_lb[70:80]

	z = [asd_8,asd_7,asd_6,asd_5,asd_4,asd_3,asd_2,asd_1]

	for x in z:
		for y in x:
			print(y,end=" ")
		print("")
	print("s")



main()