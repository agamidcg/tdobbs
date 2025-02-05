# my_list = [1,2,"apple",4.5,'tomato',75]
# my_list2 =["bread","milk"]
# print(my_list[2]) # prints apple
# print(my_list[0:3]) # prints 1, 2, apple
# print(my_list[2:5])
# print(my_list[:3]) # prints 1, 2, apple
# print(my_list[2:])
# print(my_list[0:5:2])
# print(my_list[-3:])
# print(my_list[::-1])
# print(my_list[0:5:3])
# my_list.append("banana") # this adds banana to the list
# print(my_list)
# my_list.remove(1)
# my_list.remove(2)
# my_list.remove(4.5)
# my_list.remove(75)
# print(my_list)
# my_list.insert(3, "oil") # this adds oil to index 3 moving 4.5 and other Elements up one index each
# print(my_list)
# my_list.extend(["eggs", "bacon"])
# print(my_list)
# my_list.extend(my_list2) # this adds list2 to list 
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# my_dict ={"name": "milk", "cost": 2.50, "store": "save-on", "amount": 2}
# print(my_dict["name"])
# my_dict["buy"] = True
# print(my_dict)

# set_1 = {"cheese", "bread", "deli meat"}
# set_2 = {"milk", "eggs", "bread"}
# union_set = set_1.union(set_2)
# print(union_set)
# union_set = set_2.intersection(set_1)
# print(union_set)
# diff_set = set_1.difference(set_2)
# print((diff_set))
# diff_set2 = set_2.difference(set_1)
# print(diff_set2)

# Day 3 Exercises
# created 3 tuples
#apple_tuple = ("apple", 0.50, 5)
#peach_tuple = ("peach", 0.75, 10)
#pear_tuple = ("pear", 0.65, 8)

#grocery_list =[]
# this adds all 3 tuples to the grocery list
#grocery_list = apple_tuple+peach_tuple+pear_tuple

#print each item seperate by indexing
# print(grocery_list [0])
# print(grocery_list [1])
# print(grocery_list [2])
# print(grocery_list [3])
# print(grocery_list [4])
# print(grocery_list [5]) 
# print(grocery_list [6])
# print(grocery_list [7])
# print(grocery_list [8])

# total_cost = grocery_list[1] * grocery_list[2]
# print(f"Total cost of apples ${total_cost:.2f}")# formatted to 2 decimals

# day 4 Excercises

# Conditional Statements

#tomato_dict = {"name": "tomato","cost": 2.25,"amount": 25,"backup": "canned tomatoes","available":False}
# conditional statements with single answer

# if not tomato_dict["available"]:
#     select_item = tomato_dict["backup"]
# else:
#     select_item = tomato_dict["name"]
# print(select_item)        


# conditional statements with mutiple answers

# if tomato_dict["amount"] < 5 and not tomato_dict["available"]:
#     select_item = "cherry_tomatoes"
#     select_amount = 1
# elif tomato_dict["amount"] >= 5 and not tomato_dict["available"]:
#     select_item = tomato_dict["backup"]
#     select_amount = 1

#     if tomato_dict["amount"] > 5:
#         select_amount = tomato_dict["amount"] / 5

# else:
#     select_item = tomato_dict["name"]
#     select_amount = tomato_dict["amount"]  

# print(f"Let's buy {select_amount} {select_item}")    

# For and While Loops

# create Dictionary as a Grocery_list 
# grocery_list = [
#     {
#         "name": "milk", "amount": 2, "cost": 2.5, "store": "Walmart",
#     },
#     {
#         "name": "bread", "amount": 1, "cost": 1.5, "store": "Kroger"
#     },
#     {
#         "name": "eggs", "amount": 12, "cost": 3, "store": "costco,"
#     },    
# ]

# For loop to print each item in list
#for item in grocery_list:
    #print(f"{item["name"]} - {item["amount"]} units - ${item["cost"]} - from {item["store"]}")

# while loop allows entering new items until user types done then the loop breaks
# while True:
#     command = input("Type a command add or done: ")
#     if command == "done":
#         break

#     name = input("Enter item name: ")
#     amount = int(input("enter amount: "))
#     cost = float(input("Enter cost: "))
#     store = input("Enter store: ")

#     new_item_dict = {"name": name, "amount": amount, "cost":  cost, "store": store}
   #grocery_list.append(new_item_dict) # this line adds new item to Grocery list
    # prints the name of item added to Grocery list
    #print(f"{name} was added to grocery list!")
    #prints the grocery list after each item is entered very ineffcient
    # for item in grocery_list:
    #     print(item)
 # prints the grocery list in easy to read format after user is finished adding items far more efficient
# for item in grocery_list:
#     print(item)

# loop through each item and calculate total cost with dollar sign
# for item in grocery_list: 
#     total_cost = item ["amount"] * item ["cost"]
#     item["total_cost"] = f"${total_cost:.2f}"# format with dollar sign and two decimal places

# print the item name and total cost
# for item in grocery_list:
#     print(item["name"], item["total_cost"])

# Loop Control

# grocery_list = ["milk", "bread", "eggs", "cheese", "apples", "bananas"]

# item_to_find = "cheese"

# for item in grocery_list:
#     if item == item_to_find:
#         print(f"found {item_to_find}!")
#         break

# else:
#     print(f"{item_to_find} not found in grocery list")    

# fruits = ["apples", "bananas"]

# for item in grocery_list:
#     if item in fruits:
#         pass
#     else:
#         print(f"non-fruit item: {item}")

# error messages and debugging

# pizza_price = 32.57
# people = 0

# try and except catches errors and creates an error message for the users
# try:
#     # calculates cost per person
#    cost_per_person = pizza_price / people
#    # prints the cost per person .2f rounds the answer to 2 decimals
#    print(f"Each person needs to pay: ${cost_per_person:.2f}")
#    # creates an error message for ZeroDivisionerrors
# except ZeroDivisionError:
#     print("ERROR: You must have at least one person to calculate the pizza cost")
