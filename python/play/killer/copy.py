import random
import os
import shutil

while True:
	a = random.randint(0,999999999)

	i = 'C:\\Users\\lucycore\\Desktop\\bbbb\\a.exe'
	n = "C:\\Users\\lucycore\\Desktop\\bbbb\\" + str(a) + ".exe"
	shutil.copyfile(i,n)

	os.system(n)
