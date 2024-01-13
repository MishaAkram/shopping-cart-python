
def display_shopping_list(shopping_list):
    print("Here is your shopping list:")
    for item in shopping_list:
        print(item)

def get_shopping_items_list_from_file():
    shopping_list = []
    with open("products.txt", "r") as file:
        i=1
        for line in file:
            product, price, quantity = line.strip().split(",")
            display_item = f"{i}. {product} - ${price} - {quantity}"
            shopping_list.append(display_item)
            i+=1
    return shopping_list
   
   