x= 2 
def add_two(num):
    num +=2 
    return num
# add_two(x)
x = add_two(x)
print(x)

def add_to_list(some_list,item):
    some_list.append(item)

lst = [1,2,3]
add_to_list(lst,4)

print(lst)