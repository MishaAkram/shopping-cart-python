
# Define a function named add_to_cart that takes in a cart dictionary and a username as parameters
def add_to_cart(cart ,username):
    # Open the "products.txt" file in read mode
    with open("products.txt", 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into a list of items using newline as the delimiter
        items = content.split("\n")
        # Initialize an empty string to store the replaced content
        replaced_content = ""       
        # Prompt the user to enter the number of the item they want to add to the cart
        choice = int(input("Enter the number of the item you want to add to the cart: "))
        # Prompt the user to enter the quantity of the item they want to add to the cart
        quantity = int(input("Enter the quantity of the item you want to add to the cart: "))
        # Check if the choice is within the valid range of items
        if choice >= 1 and choice <= len(items):
            # Extract the name, price, and quantity of the chosen item from the items list
            name, price, quantity_ =  chosen_item = items[choice - 1].strip().split(",")
            # Check if the available quantity of the chosen item is less than the desired quantity
            if int(quantity_) < quantity:
                # Print an error message and return from the function
                print("Sorry, we don't have enough of that item.")
                return

            # Check if the username is not already in the cart dictionary
            if username not in cart:
                # Add an empty list as the value for the username key in the cart dictionary
                cart[username] = []            
            # Append a dictionary representing the chosen item to the list associated with the username key in the cart dictionary
            cart[username].append({
                "name": name,
                "price": price,
                "quantity": quantity
            })
            # Initialize an empty string to store the updated product information
            update_product = ""
            # Extract the name, price, and quantity of the chosen item from the items list
            name, price, quantity_ = chosen_item = items[choice - 1].strip().split(",")
            # Calculate the updated quantity of the chosen item
            update_product = f"{name},{price},{int(quantity_) - quantity}"
            # Replace the original item information with the updated product information in the content string
            content = content.replace(items[choice -1], update_product)
            # Open the "products.txt" file in write mode
            with open('products.txt', 'w') as fileW:
                # Write the updated content to the file
                fileW.write(content)
            # Print the chosen item
            print(f"Chosen item: {chosen_item}")
            # Print the updated cart
            print(f"Cart: {cart}")
        else:
            # Print an error message for an invalid choice
            print("Invalid choice. Please try again.")

# Define a function named update_quantity_products_List that takes in the choice, quantity, file, and items as parameters
def update_quantity_products_List(choice, quantity, file, items):
    # Initialize an empty string to store the updated product information
    update_product = ""
    # Extract the name, price, and quantity of the chosen item from the items list
    name, price, quantity_ = chosen_item = items[choice - 1].strip().split(",")
    # Calculate the updated quantity of the chosen item
    update_product = f"{name},{price},{int(quantity_) - quantity}"
    # Write the updated product information to the file
    file.write(f"{chosen_item},{update_product}\n")
            
   