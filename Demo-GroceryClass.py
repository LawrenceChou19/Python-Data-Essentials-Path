class GroceryClass:
    def __init__(self,name):
        self.name = name
        self.groceries_dict = {}
        
    def input_groceries(self):
        while True:
            item_name_input = input("Input an item(type 'end to finish): ")
            if item_name_input == "end":
                break
            item_price_input = input("Input an item's price: ")
            self.groceries_dict[item_name_input] = float(item_price_input)
            
    def info(self):
        print(f"Here is your {self.name} grocery list: ")
        for name, price in self.groceries_dict.items():
            print(f"{name}: {price}")
        print(f"Total amount: {self.total_cost()}")
        
    def find_in_dict(self,*item_names):
        for item_name in item_names:
            for item in self.groceries_dict.keys():
                if item == item_name:
                    print(f"{item_name} is on the list!") 
                    break
            else:
                print(f"{item_name} is not on the list.")
    
    def total_cost(self):
        total_cost = 0
        for item_price in self.groceries_dict.values():
            total_cost += item_price
        return total_cost
def separate_section():
    print("-" * 80)
    
monday_groceries = GroceryClass("Monday") # Assign class to monday_groceries
monday_groceries.input_groceries()
separate_section()
monday_groceries.find_in_dict("potatoes","eggs","bread")
separate_section()
monday_groceries.info()
