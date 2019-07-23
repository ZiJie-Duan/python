js = 2
while True:
	z = 20 * js
	zt = True
	for x in range(1,20):
		if z % x != 0:
			zt = False
			break
	if zt == True:
		print(z)
		break
	print(z)
	js += 1

