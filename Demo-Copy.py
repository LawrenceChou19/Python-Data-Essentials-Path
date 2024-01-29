
#Aliasing
quantity= [2,4,6]
print(quantity)
quantity_copy = quantity

print(quantity is quantity_copy)

quantity_copy.append(10)
print(quantity_copy)
print(quantity)

#Cloning
quantity_clone = list(quantity)
#quantity_clone = quantity[:]
quantity_clone.append(20)
print(quantity_clone)
print(quantity)

products = ['banana','lemon','orange','mango','tv','laptop']
products.sort()
print(products)
# print(help(products))
products.sort(reverse=True)
print(products)
products.sort(reverse=False)
print(products)
 
fruits = ['pear','orange','apple','pineapple']
fruits.reverse()
print(fruits)

#Concatenating lists
basket = products + fruits
print(basket)

print(basket.count('orange'))
text = 'Welcome to our store'
print(text.split())

