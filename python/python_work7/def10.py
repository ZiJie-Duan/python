# -- coding:utf-8--

def computer(name,size,**qt):
	computerx = {}
	computerx['name'] = name
	computerx['size'] = size
	for k, v in qt.items():  #注意！！！不要忘记加入items()
		computerx[k] = v
	return computerx   #注意！！不要忘记返回值

hi = computer('lucycore','12.9',cpu = 'Core i7') #注意！！要使用变量储存返回值

print(hi)