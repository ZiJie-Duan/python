
a = 100

for aa in range(2,a):
	x = 2
	for x in range(2,aa):
		if aa % x == 0:
			break
	else:
		print(aa)
			

