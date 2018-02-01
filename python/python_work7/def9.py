# -- coding:utf-8--

def users(name, age, **qt):
	userss = {}
	userss['name'] = name
	userss['age'] = age
	for k, z in qt.items():
		userss[k] = z
	return userss

hi = users('ljx', '14', haha= 'jajajaja',has3= 'nigediaomao')

print(hi)