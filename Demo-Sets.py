product_categories=['fruits','coffee','vegetables','candy','coffee','candy']
print(product_categories)

category = set(product_categories)
print(type(category))

print(category)

coffee = {'Latte','Cappuccino', 'Espresso'}
print(coffee)

empty_set = set()
print(type(empty_set))

categories = {'fruits','coffee','vegetables','candy','coffee'}
#Removing elements
categories.discard('candy')
print(categories)

print('candy' in categories)
# categories.remove('candy')

# Adding elements
categories.add('seafood')
print(categories)

new_categories = {'electronics','clothing'}
categories.update(new_categories)
print(categories)
#pop() method
categories.pop()
print(categories)

