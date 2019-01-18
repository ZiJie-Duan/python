
def sum(x):
	if x < 3:
		return x
	else:
		return sum(x-1) + sum(x-2)


def add():
	b = []
	for x in range(1,99999):
		s = sum(x)
		if s < 4000000:
			b.append(s)
		else:
			return b
			break


lb = add()
a = 0
for x in lb:
	if x % 2 == 0:
		a += x
		print(a)

print(a)