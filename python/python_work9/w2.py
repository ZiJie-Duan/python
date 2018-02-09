import os
dqlj = os.getcwd()
print(dqlj)
lj = os.path.join(dqlj,'name.txt')
print(lj)

bz = True
while bz == True:
	name = raw_input('name: ')
	if name == 'q':
		break
	with open(lj,'a') as hi:
		hi.write('name: ' + name + '\n')

