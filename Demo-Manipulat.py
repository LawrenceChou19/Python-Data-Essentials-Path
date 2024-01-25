#creating a list
products = ['orange','mango']

#calling the len function
print(len(products))

#calling the append metod
products.append('banana')
products.pop()
print(products)

products = ['apple','banana','orange','mango']
products.append('lemon')
products.pop()
print(products)

products.remove('apple')
print(products)

products.insert(2,'lemon')
print(products)


electronics = ['TV','laptop']
products.extend(electronics)
print(products)

electronics.clear()
print(electronics)

del electronics
print(electronics)