s = input("请用写下一段字符串：")
zt = False

def hw(st):
	global zt
	a = list(s)
	b = 1
	for x in range(len(a)//2):
		if a[b-1] == a[-b]:
			b += 1
		else:
			zt = True

	if zt == True:
		print("这并不是回文")
	else:
		print("这是个回文")

hw(s)
input("")