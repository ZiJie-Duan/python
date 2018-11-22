year = 2018

for x in range(50):
	year += 1
	if year % 4 == 0:
		if year % 10 != 0:
			print(year)