products = []
while True:
	name = input('type your products name ')
	if name == 'q':
		break
	price = input ('type the price ')
	products.append([name,price])


for small in products:
	print('price of ',small[0],'is',small[1])

with open('appleshopping.csv','w') as p:
	for small in products:
		p.write(small[0] +','+ small[1] + '/n')
