lj = 'name.txt'
bz = True

while bz == True:
	name = raw_input('name: ')
	if name == 'q':
		break
	with open(lj,'a') as hi:
		hi.write('name: ' + name + '\n')

        

