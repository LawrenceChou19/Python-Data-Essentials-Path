products = ('lemon','mango','orange')
print(products)
products_information= ('mango',1.4,[15,20])
print(len(products_information))

#Convert the tuple into a list
products_information=list(products_information)
print(products_information)
products_information[1] = 1.8
print(products_information)
products_information=tuple(products_information)
print(products_information)
products_information[2][1] = 10
products_information[2][0] = 33
print(products_information)

#Create a tuple with a single element
fruit = ('mango')
print(type(fruit))

mango_information = ('fruits',1.4,[10,15])
lemon_information = ('fruits',0.9,[5,8])
print(dir(mango_information))

products_information = mango_information+lemon_information
print(products_information)
print(products_information.count('fruits'))
print(products_information.index(0.9))
print(products_information[1])
print(products_information[-5])
print(products_information[:])
print(products_information[2:5])
print(products_information[3:])
print(products_information[:3])
print(products_information[5][1])

#packing tuples
quantity = (10,20,30)
print(quantity)
#unpacking tuples-1
(apple, orange,lime) = (10,20,30)
print(apple)
print(orange)
print(lime)
#unpacking tuples-2
(apple, orange,*lime) = (10,20,30,40,50,60)
print(apple)
print(orange)
print(lime)