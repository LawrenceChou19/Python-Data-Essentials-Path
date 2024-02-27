def separate_section():
    print("-" * 80)

print("Grocery list program.")
grocery_list =[]

while True:
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input == "end":
        break
    grocery_list.append(user_input)
    
# print("-" * 20)
separate_section()

print("Here is your grocery list:")
for item in grocery_list:
    print(f"{item}")
    
# print("-" * 20)    
separate_section()
    
bread_on_list = False

def find_in_list(some_list,item_name):
    for item in some_list:
        if item == item_name:
            print(f"{item_name} is on the list!") 
            break
    else:
        print(f"{item_name} is not on the list!")
        
find_in_list(grocery_list,"carrots")
find_in_list(grocery_list,"bread")
find_in_list(grocery_list,"potatoes")

#or

def find_in_list(some_list,item_name="bread"):
    for item in some_list:
        if item == item_name:
            print(f"{item_name} is on the list!") 
            break
    else:
        print(f"{item_name} is not on the list!")       
        
find_in_list(item_name="carrots",some_list=grocery_list)
find_in_list(grocery_list,"bread")
find_in_list(grocery_list)
separate_section()
    

def print_params(x,*args):
    print("x:",x)
    print("args:",args)
    print("args[0]",args[0])
print_params("a","b","c","d")
separate_section()
    
def print_params(x,*args, **kwargs):
    print("x:",x)
    print("args:",args)
    print("args[0]",args[0])
    print("kwargs:",kwargs)
    print("kwargs['first']:",kwargs['first'])
print_params("a","b","c","d",first="e",second="f")
