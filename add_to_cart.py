
def add_to_cart(cart ,username):
    with open("products.txt", 'r') as file:
        items = file.readlines()
        replaced_content = ""
        for index, item in enumerate(items):
            print(f"{index + 1}. {item.strip()}")        
        choice = int(input("Enter the number of the item you want to add to the cart: "))
        quantity = int(input("Enter the quantity of the item you want to add to the cart: "))
        if choice >= 1 and choice <= len(items):
            name,price,quantity_ =  chosen_item = items[choice - 1].strip().split(",")
            if username not in cart:
                cart[username] = []
            
            cart[username].append({
                "name": name,
                "price": price,
                "quantity": quantity
            })
            update_product = ""
            name, price, quantity_ = chosen_item = items[choice - 1].strip().split(",")
            update_product = f"{name},{price},{int(quantity_) - quantity}"
            new_line = item.replace(item, update_product)
            replaced_content = replaced_content + new_line + "\n"
            print(f"Chosen item: {chosen_item}")
            print(f"Cart: {cart}")
        else:
            print("Invalid choice. Please try again.")
    with open("products.txt", 'w') as file:
        file.write(replaced_content)

def update_quantity_products_List(choice, quantity, file, items):
    update_product = ""
    name, price, quantity_ = chosen_item = items[choice - 1].strip().split(",")
    update_product = f"{name},{price},{int(quantity_) - quantity}"
    file.write(f"{chosen_item},{update_product}\n")
            
   