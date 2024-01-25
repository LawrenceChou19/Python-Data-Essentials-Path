products = ['apple','banana','orange','pineapple','mango','pear','grape','lemon']
print(products)
print(products[-1])

print(products.index('lemon'))
print(products[7])


print('mango' in products)

print('apple' not in products)
products[1] = 'lime'
print(products)

print(products[2:4])
print(products[2:])
print(products[:6])