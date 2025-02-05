# Exercise 1: Grocery Item Categorization Using Conditional Statements

# food_items = ["apple", "bread", "milk"]
# non_food_items = ["soap", "detergent", "paper"]

# item = input("please enter grocery item: ")

# if item in food_items:
#     print(f"{item} is a food item")

# elif item in non_food_items:
#     print(f"{item} is a non-food item")

# else:
#     print("unknown item")

# Exercise 2: Making a Burger with a While Loop


# # creates a list of items needed for the meal
# item_list = [

#     {"name": "fries", "cost": 6.25, "amount": 1},
#     {"name":"burger patties", "cost": 13.50, "amount": 1},
#     {"name": "burger buns", "cost": 3.50, "amount": 2},
#     {"name": "tomato", "cost": 1.5, "amount": 2},
#     {"name": "lettuce", "cost": 5.00, "amount": 1},
#     {"name": "ketchup", "cost": 3.47, "amount": 1},
#     {"name": "pickles", "cost": 4.25, "amount": 1},
# ]

# # creates an empty shopping_list
# shopping_list = []

# # creates a variable called budget 
# budget = 27.50

# # creates a variable total_cost with a value of zero
# total_cost = 0.00

# # creates a variable index starting at zero
# index = 0

# # creates a welcome message
# print("Welcome to the Burger Builder!")

# # Create a message telling you your budget
# print(f"Your budget is: ${budget:.2f}")

# # creates a while loop that that runs as long as the total cost is under the budget
# while total_cost <= budget and index < len(item_list):

    
#         # prompt the user for the index of item to add
#         index = int(input("Enter the index of item to add: "))

#         # gets item at current index from item_list
#         item = item_list[index]

#         # adds the item name to  the shopping list
#         shopping_list.append(item["name"])

#         # adds the item cost to the total cost by calculating the cost multiplied by the amount
#         total_cost += item["cost"] * item["amount"]
        
#         # moves to the next index
#         index += 1
        
     

            
#  # prints the shopping list 
# print(shopping_list)

# Exercise 3: Extending Logic With Nesting

# creates a list of items needed for the meal
# item_list = [

#     {"name": "fries", "cost": 6.25, "amount": 1},
#     {"name":"burger patties", "cost": 13.50, "amount": 1},
#     {"name": "burger buns", "cost": 3.50, "amount": 2},
#     {"name": "tomato", "cost": 1.5, "amount": 2},
#     {"name": "lettuce", "cost": 5.00, "amount": 1},
#     {"name": "ketchup", "cost": 3.47, "amount": 1},
#     {"name": "pickles", "cost": 4.25, "amount": 1},
# ]

# # creates an empty shopping_list
# shopping_list = []

# # creates a variable called budget 
# budget = 27.50

# # creates a variable total_cost with a value of zero
# total_cost = 0.00

# # creates a variable index starting at zero
# index = 0

# # creates a welcome message
# print("Welcome to the Burger Builder!")

# # Create a message telling you your budget
# print(f"Your budget is: ${budget:.2f}")

# # creates a while loop that that runs as long as the total cost is under the budget
# while total_cost <= budget and index < len(item_list):

    
#         # prompt the user for the index of item to add
#         index = int(input("Enter the index of item to add: "))

#         # gets item at current index from item_list
#         item = item_list[index]

#         # adds the item name to  the shopping list
#         shopping_list.append(item["name"])

#         # adds the item cost to the total cost by calculating the cost multiplied by the amount
#         total_cost += item["cost"] * item["amount"]
        
#         # moves to the next index
#         index += 1
        
     
#         # skip a line before the for loop prints
#         print()

#         # a for loop that prints each item in the shopping list
#         for item in shopping_list:
#             print(item)

#         # print ten dashes after each for loop
#         print("----------")

            
#  # prints the shopping list 
# print(shopping_list)

# Exerscise 4: Breaking the loop

# creates a list of items needed for the meal
# item_list = [

#     {"name": "fries", "cost": 6.25, "amount": 1},
#     {"name":"burger patties", "cost": 13.50, "amount": 1},
#     {"name": "burger buns", "cost": 3.50, "amount": 2},
#     {"name": "tomato", "cost": 1.5, "amount": 2},
#     {"name": "lettuce", "cost": 5.00, "amount": 1},
#     {"name": "ketchup", "cost": 3.47, "amount": 1},
#     {"name": "pickles", "cost": 4.25, "amount": 1},
# ]

# # creates an empty shopping_list
# shopping_list = []

# # creates a variable called budget 
# budget = 27.50

# # creates a variable total_cost with a value of zero
# total_cost = 0.00

# # creates a variable index starting at zero
# index = 0

# # creates a welcome message
# print("Welcome to the Burger Builder!")

# # Create a message telling you your budget
# print(f"Your budget is: ${budget:.2f}")

# # creates a while loop that that runs as long as the total cost is under the budget
# while total_cost <= budget and index < len(item_list):

    
#         # prompt the user for the index of item to add
#         index = int(input("Enter the index of item to add: "))

#         # gets item at current index from item_list
#         item = item_list[index]

#         # adds the item name to  the shopping list
#         shopping_list.append(item["name"])

#         # adds the item cost to the total cost by calculating the cost multiplied by the amount
#         total_cost += item["cost"] * item["amount"]
        
#         # moves to the next index
#         index += 1
        
     
#         # skip a line before the for loop prints
#         print()

#         # a for loop that prints each item in the shopping list
#         for item in shopping_list:
#             print(item)

#         # print ten dashes after each for loop
#         print("----------")

#         # check if fries, burger patties, and burger buns are in shopping list
#         if "fries" in shopping_list and "burger patties" in shopping_list and "burger buns" in shopping_list:
#             print(f"We can make burgers and fries for ${total_cost:.2f}")
#             break
#         else:
#             print("Adding this item would exceed your budget")
   
    
        
#  # prints the shopping list 
# print(shopping_list)

# Exercise 5: Error Handling with Try-Except

# creates a list of items needed for the meal
# item_list = [

#     {"name": "fries", "cost": 6.25, "amount": 1},
#     {"name":"burger patties", "cost": 13.50, "amount": 1},
#     {"name": "burger buns", "cost": 3.50, "amount": 2},
#     {"name": "tomato", "cost": 1.5, "amount": 2},
#     {"name": "lettuce", "cost": 5.00, "amount": 1},
#     {"name": "ketchup", "cost": 3.47, "amount": 1},
#     {"name": "pickles", "cost": 4.25, "amount": 1},
# ]

# # creates an empty shopping_list
# shopping_list = []

# # creates a variable called budget 
# budget = 27.50

# # creates a variable total_cost with a value of zero
# total_cost = 0.00

# # creates a variable index starting at zero
# index = 0

# # creates a welcome message
# print("Welcome to the Burger Builder!")

# # Create a message telling you your budget
# print(f"Your budget is: ${budget:.2f}")

# # creates a while loop that that runs as long as the total cost is under the budget
# while total_cost <= budget and index < len(item_list):

#     try:
#         # prompt the user for the index of item to add
#         index = int(input("Enter the index of item to add: "))

#         # gets item at current index from item_list
#         item = item_list[index]

#         # adds the item name to  the shopping list
#         shopping_list.append(item["name"])

#         # adds the item cost to the total cost by calculating the cost multiplied by the amount
#         total_cost += item["cost"] * item["amount"]
        
#         # moves to the next index
#         index += 1
        
     
#         # skip a line before the for loop prints
#         print()

#         # a for loop that prints each item in the shopping list
#         for item in shopping_list:
#             print(item)

#         # print ten dashes after each for loop
#         print("----------")

#         # check if fries, burger patties, and burger buns are in shopping list
#         if "fries" in shopping_list and "burger patties" in shopping_list and "burger buns" in shopping_list:
#             print(f"We can make burgers and fries for ${total_cost:.2f}")
#             break
#         else:
#             print("Adding this item would exceed your budget")
   
#     except ValueError:
#         # if the input is not an integer, handle the error
#        print("Error: the index must be an integer")
        
#  # prints the shopping list 
# print(shopping_list)

# Exercise 6: Customize Your Script

# creates a list of items needed for the meal
item_list = [

    {"name": "eggs", "cost": 6.25, "amount": 1},
    {"name":"biscuits", "cost": 5.42, "amount": 1},
    {"name": "bacon", "cost": 5.50, "amount": 1},
    {"name": "milk", "cost": 2.50, "amount": 1},
    {"name": "butter", "cost": 5.00, "amount": 1},
    {"name": "fruit", "cost": 4.25, "amount": 1},
]

# creates an empty shopping_list
shopping_list = []

# creates a variable called budget 
budget = 19.70

# creates a variable total_cost with a value of zero
total_cost = 0.00

# creates a variable index starting at zero
index = 0

# creates a welcome message
print("Welcome to the Breakfast Builder!")

# Create a message telling you your budget
print(f"Your budget is: ${budget:.2f}")

# creates a while loop that that runs as long as the total cost is under the budget
while total_cost <= budget and index < len(item_list):

    try:
        # prompt the user for the index of item to add
        index = int(input("Enter the index of item to add: "))

        # gets item at current index from item_list
        item = item_list[index]

        # adds the item name to  the shopping list
        shopping_list.append(item["name"])

        # adds the item cost to the total cost by calculating the cost multiplied by the amount
        total_cost += item["cost"] * item["amount"]
        
        # moves to the next index
        index += 1
        
        # skip a line before the for loop prints
        print()

        # a for loop that prints each item in the shopping list
        for item in shopping_list:
            print(item)

        # print ten dashes after each for loop
        print("----------")

        # check if eggs, bacon, and bicuits are in shopping list
        if "eggs" in shopping_list and "bacon" in shopping_list and "biscuits" in shopping_list:
            print(f"We can make burgers and fries for ${total_cost:.2f}")
            break
        
    except ValueError:
        # if the input is not an integer, handle the error
       print("Error: the index must be an integer")
        
 # prints the shopping list 
print(shopping_list)



