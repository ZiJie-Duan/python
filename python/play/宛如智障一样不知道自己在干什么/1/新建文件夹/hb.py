
y_7 = [[0,7,0],[1,7,0],[2,7,0],[3,7,0],[4,7,0],[5,7,0],[6,7,0],[7,7,0],[8,7,0],[9,7,0]]
y_6 = [[0,6,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0],[7,6,0],[8,6,0],[9,6,0]]
y_5 = [[0,5,0],[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],[6,5,0],[7,5,0],[8,5,0],[9,5,0]]
							  #sbsbsbsbbbsbsbsbsbbsssbsbsbsbsb
y_4 = [[0,4,0],[1,4,0],[2,4,0],[3,4,0],[4,4,0],[5,4,0],[6,4,0],[7,4,0],[8,4,0],[9,4,0]]
y_3 = [[0,3,0],[1,3,0],[2,3,0],[3,3,0],[4,3,2],[5,3,0],[6,3,0],[7,3,0],[8,3,0],[9,3,0]]
							  #sbsbsbsbbbsbsbsbsbbsssbsbsbsbsb
y_2 = [[0,2,0],[1,2,0],[2,2,0],[3,2,0],[4,2,0],[5,2,0],[6,2,0],[7,2,0],[8,2,0],[9,2,0]]
y_1 = [[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0],[8,1,0],[9,1,0]]
y_0 = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0],[9,0,0]]

wwb = [y_0,y_1,y_2,y_3,y_4,y_5,y_6,y_7]

#print(wwb)
def change_poin(x,y,mbz):
	wwb[y][x][2] = mbz

def zhdz(lb):
	x = lb[0]
	y = lb[1]
	return wwb[y][x][2]


def zt_is_one_or_two(lb):
	a = lb[2]
	return a

def change_four_poin(lb):
	x = lb[0]
	y = lb[1]

	poin_1_zb = [x-1,y]
	poin_2_zb = [x+1,y]
	poin_3_zb = [x,y+1]
	poin_4_zb = [x,y-1]

	if zhdz(poin_1_zb) == 0:
		x = poin_1_zb[0]
		y = poin_1_zb[1]
		change_poin(x,y,2)
	if zhdz(poin_2_zb) == 0:
		x = poin_2_zb[0]
		y = poin_2_zb[1]
		change_poin(x,y,2)
	if zhdz(poin_3_zb) == 0:
		x = poin_3_zb[0]
		y = poin_3_zb[1]
		change_poin(x,y,2)
	if zhdz(poin_4_zb) == 0:
		x = poin_4_zb[0]
		y = poin_4_zb[1]
		change_poin(x,y,2)


def main():
	for a in wwb:
		for b in a:
			if zt_is_one_or_two(b) == 2:
				change_four_poin(b)
			if zt_is_one_or_two(b) == 1:
				x = b[0]
				y = b[1]
				change_poin(x,y,mbz)

main()
wwb.reverse()
for x in wwb:
	print(x)