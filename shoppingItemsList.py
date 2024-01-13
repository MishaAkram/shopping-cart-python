from display_products import display_ice_cream_flavors

def display_shopping_list(shopping_list):
    display_ice_cream_flavors(shopping_list)

def get_shopping_items_list_from_file():
    shopping_list = []
    with open("products.txt", "r") as file:
        i=1
        for line in file:
            shopping_list.append(line.strip().split(","))
            i+=1
    return shopping_list
   
   