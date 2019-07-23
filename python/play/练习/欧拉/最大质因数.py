
def kaigen():
	z = 600851475143

	list2f = []
	for x in range(2,888888):
		list2f.append(x)

	while True:

		if len(list2f) == 1:
			break
		wz = len(list2f) + 1
		wz = wz //2
		wz = wz -1
		yz = list2f[wz]
		yz = yz * yz

		if yz > z:
		
			del list2f[wz:len(list2f)]
		else:

			del list2f[0:wz+1]

	return list2f[0]

def get_max_zs(z):


	for x in range(3,z+1):
		zt = 1
		for y in range(2,x):
			if x % y == 0:
				zt = 0
				break
		if zt == 1:
			print(x)


a = kaigen()
print(a)
get_max_zs(a)






