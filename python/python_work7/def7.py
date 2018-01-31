# -- coding:utf-8--

names = ['dzj','ljx','wwb','gyj','zke']

new_names = []

ls_names = names[:]

#while hi 意思是使用pop()函数删除列表中的值
#并且判断hi列表中是否有剩余的值

def name(hi):
	while hi:   
		new_name = 'wow ' + hi.pop()  
		print(new_name)
		new_names.append(new_name)

name(ls_names)

print(new_names)

print(names)