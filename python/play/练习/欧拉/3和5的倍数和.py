hi = []
for x in range(1,1000):

	if x % 3 == 0 or x % 5 == 0:
		hi.append(x)

a = 0
for x in hi:
	a += x

print(a)