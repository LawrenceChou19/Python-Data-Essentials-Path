#Constructing a dictionary
supply = {'apple' : 4,'mango' : 6,'orange' : 8}
print(supply)
print(type(supply))

#Selecting a value
print(supply['mango'])

#Changing a value
supply['orange'] = 2
print(supply['orange'])

print(supply)

#Constructing a new dictionary
basket = dict(orange=1.2)
print(basket)

basket['lemon'] =0.9
print(basket)

#Creating a nested dictionary
inventory = {'orange': {'price': 1.2, 'stock': 10},'lemon' : {'price': 0.9,'stock': 20}}

print(inventory)
print(len(inventory))

#Retriving a value
inventory['orange']['price']
print(inventory)

#Converting lists into dictionaries
products = ['orange','lemon']
prices = [1.2,0.9]
cart = zip(products,prices)
print(cart)
cart = dict(zip(products,prices))
print(cart)

inventory =  {'apple' : 50,'lemon' : 10,'orange' : 40}
print(inventory)
#total stock quantity
print(inventory.values())
print(inventory.keys())
print(sorted(inventory.keys(), reverse = True))
print(sum(inventory.values()))
print(inventory.items())

#Memebershop testing 
print('orange' in inventory)

#Retrieve values
print(inventory.get('lemon'))
print(inventory.get('laptop','This key does not exist.'))

inventory = {'apple' : 30,'kiwi' : 20, 'orange' : 10}
print(inventory)

#Add a new element
inventory.update({'mango':5})
print(inventory)

inventory.update({'orange':100})
print(inventory)

#Add multiple elements
inventory.update({'pear':25,'lemon':15})
print(inventory)

#Remove elements
inventory.pop('orange')
print(inventory)
print(inventory.pop('orange','The product is not available'))

del inventory['kiwi']
print(inventory)

#Remove all the last added element
inventory.popitem()
print(inventory)

#Remove all elements
inventory.clear()
print(inventory)

inventory = {'mango': 30,'kiwi': 20, 'orange': 10}
print(inventory)

inventory_copy = inventory

print(inventory_copy)

inventory_copy.update({'lemon': 5 })
print(inventory)
print(inventory_copy)
#copy() method
supply= inventory.copy()
print(supply)
supply.update({'apple':10})
print(inventory)
print(supply)