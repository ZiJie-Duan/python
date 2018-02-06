# -- coding:utf-8--

lj = 'gyj.txt'

with open(lj) as ls_0:
	ls_1 = ls_0.readlines()

ls_2 = ''
for ls_3 in ls_1:
	ls_2 += ls_3.strip()

print(ls_2)

hii = '早上好！宫逸君！'
hi = hii.replace('宫逸君','朱紫')
print('\n' + hi)

hei = ls_2.replace('1','0')
print(hei)