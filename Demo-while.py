# print("Grocery list program")
# grocery_list = []
# user_input = None

# while user_input !="end":
#     user_input = input("Input an item (type 'end' to finish): ")
#     if user_input != "end":
#         grocery_list.append(user_input)
# print("Here is your grocery list:")
# print(grocery_list)

lst = [23,45,67]
i=0

while i< len(lst):
    print(f"{i} element is {lst[i]}")
    i= i+1
print("Moving on!")

print("Grocery list program")
grocery_list = []
user_input = None

while user_input !="end":
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input != "end":
        grocery_list.append(user_input)
print("Here is your grocery list:")
i=0
while i < len(grocery_list):
    print(f"{grocery_list[i]}")
    i=i+1
    
#Access the indices while iterating over a list
lst= [23,33,22]
for index, value in enumerate(lst):
    print(f"{index}.{value}")

#Interating over dictionaries
bank_account={
    "name" : "Luna",
    "number": "021000012",
    "balance": 20000
}

#Iterate just over the keys
print("Keys")
for key in bank_account.keys():
    print(key)
    
#Iterate over keys and values
print("Keys and values")
for key , value in bank_account.items():
    print(f"{key}: {value}")
    

for lc in range(5):
    print(lc)
print("Moving on !")


#improve
grocery_list =[]
while True:
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input == "end":
        break
    
    grocery_list.append(user_input)
print("Here is your grocery list:")
for item in grocery_list:
    print(f"{item}")
    
bread_on_list = False
for item in grocery_list:
    if item == "bread":
        print("Bread is on the list!")
        bread_on_list = True
        break
if not bread_on_list:
    print("Bread is not on the list.")