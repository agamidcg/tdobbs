# Exercise 1: Working with List

# apples_tuple = ("apples", 0.50, 5)
# milk_tuple = ("milk", 2.50, 2)
# bread_tuple = ("bread", 2.00, 2)
# Blank grocery list
#grocery_list = []

# this block of code adds each of the tuples to the grocery list
# grocery_list.extend(apples_tuple)
# grocery_list.extend(milk_tuple)
# grocery_list.extend(bread_tuple)

# this block of code prints each element using indexing
# print(grocery_list [1]) 
# print(grocery_list [2])
# print(grocery_list [3])
# print(grocery_list [4])
# print(grocery_list [5])
# print(grocery_list [6])
# print(grocery_list [7])
# print(grocery_list [8])

#this block of code totals each item then prints each item with totals
# apples_total = grocery_list [1] * grocery_list [2]
# print(f"apples total: ${apples_total}")
# milk_total = grocery_list [4] * grocery_list [5]
# print(f"milk total: ${milk_total}")
# bread_total = grocery_list [7] * grocery_list [8]
# print(f"bread total: ${bread_total}")

# this block of code totals all 3 items and prints total cost
# total_cost = apples_total + milk_total + bread_total
# print(f"This is your total cost: ${total_cost}")

# Exercise 2: Working with Dictionaries

#this block creates 3 Dictionaries
# apple_dict = {"name": "apple", "price": 0.50, "quantity": 5}
# peach_dict = {"name": "peach", "price": 0.70, "quantity": 10}
# pear_dict = {"name": "pear", "price":  0.60, "quantity": 4}

# totals for apple_dict
# total_cost = apple_dict['price'] * apple_dict['quantity']
# apple_dict["total_cost"] =  2.5
# print(apple_dict)
# print(f"Total cost of apples: ${apple_dict["total_cost"]}")

# totals for peach_dict
# total_cost = peach_dict["price"] * peach_dict["quantity"]
# peach_dict["total_cost"] = 7.0
# print(peach_dict)
# print(f"Total cost of peaches: ${peach_dict["total_cost"]}")

# totals for pear_dict
# total_cost  = pear_dict["price"] * pear_dict["quantity"] 
# pear_dict["total_cost"] = 2.4
# print(pear_dict)
# print(f"Total cost of pears: ${pear_dict['total_cost']}")

# Exercise 3: Slicing and Sorting a List

# num_list =  [16, 47, 1, 3, 5, 9, 15, 2]
# print(num_list [1:])
# print(num_list  [0:3])
# print(num_list [-3])
# num_list.sort(reverse=True)
# print(num_list)
# length = len(num_list)
# print(length)

# Exercise 4: Sets Operations

# dairy_set = {"milk", "butter", "cream", "yogurt", "cheese"}
# desserts_set = {"jello", "chocolate", "candy", "cookies", "muffins"}
# dairy_set.add("ice_cream")
# desserts_set.add("ice_cream")
# print(dairy_set)
# print(desserts_set)
# dairy_set.remove("cream")
# desserts_set.remove("muffins")
# print(dairy_set)
# print(desserts_set)
# print(dairy_set.intersection(desserts_set))
