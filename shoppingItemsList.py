 # Importing the function display_ice_cream_flavors from the module display_products
from display_products import display_ice_cream_flavors

# Defining a function named display_shopping_list that takes a parameter named shopping_list
def display_shopping_list(shopping_list):
    # Printing a message to indicate that the shopping list is being displayed
    print("Here is your shopping list:")
    # Iterating over each item in the shopping list
    for item in shopping_list:
        # Printing each item in the shopping list
        print(item)

# Defining a function named get_shopping_items_list_from_file
def get_shopping_items_list_from_file():
    # Creating an empty list named shopping_list
    shopping_list = []
    # Opening the file named "products.txt" in read mode
    with open("products.txt", "r") as file:
        # Initializing a variable named i with a value of 1
        i=1
        # Iterating over each line in the file
        for line in file:
            # Stripping the line of any leading or trailing whitespace and splitting it by comma
            # Appending the resulting list to the shopping_list
            shopping_list.append(line.strip().split(","))
            # Incrementing the value of i by 1
            i+=1
    # Returning the shopping_list
    return shopping_list

   
   