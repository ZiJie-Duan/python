lb_a = []
import random
for x in range(100):
	jgz = random.randint(0,100)
	lb_a.append(jgz)
print(lb_a)

sc = 0

for x in lb_a:
	sc = sc + x

print(sc)