lb_a = []
import random
for x in range(3):
	jgz = random.randint(0,5)
	lb_a.append(jgz)
print(lb_a)


z = 0
for x in lb_a:
	z += x
print(z)



z = 0

cs = 0
while cs < len(lb_a):
	z += lb_a[cs]
	cs += 1

print(z)



z = 0
x = 0
def sum(lb_a):
	global z
	global x
	if x < len(lb_a):
		z = lb_a[x]
		x += 1
		sun(lb_a)  

print(z)