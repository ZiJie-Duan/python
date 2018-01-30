# -- coding:utf-8--

def music(name,zj):
	music_0 = {name : zj}
	return music_0

bz = '0'
lucycore = {}

while bz == '0':
	name_1 = raw_input("歌手名称：")
	zj_1 = raw_input("专辑名称：")
	music_2 = music(name_1,zj_1)
	for k, y in music_2.items():
		print(k + ':' + y)
	bz_1 = raw_input("是否还要继续存储：y/n ")
	if bz_1 != 'y':
		bz = '1'

	for k, y in music_2.items():
		lucycore[k] = y

for k, y in lucycore.items():
	print('作者：' + k + '  ' + '专辑：' + y)
