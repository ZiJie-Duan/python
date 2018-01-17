my_friends = ["zz","ljx","zke","yxd","gyj","wwb"]

txt = "hello!"

for a in my_friends[:3]:
	print(txt + " " + a)
	
print("------------------------")
for a in my_friends[1:4]:
	print(txt + " " + a)
	
print("------------------------")
for a in my_friends[-3:]:
	print(txt + " " + a)
	
print("------------------------")

my_pizzas = ["fruit_pizza","shrimp_pizza"]
#fruit=水果 shrimp=虾
friend_pizzas = my_pizzas[:]

my_pizzas.append("steak_pizza")
#steak=牛排

friend_pizzas.append("caramel_pizza")
#caramel=焦糖

for b in my_pizzas[:]:
	print(b)
	
print("------------------------")

for c in friend_pizzas[:]:
	print(c)

