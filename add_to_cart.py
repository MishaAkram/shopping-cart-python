
from data import cart, get_username

# Define a function named add_to_cart that takes in a cart dictionary and a username as parameters

def add_to_cart():
    user_name= get_username()
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
            if user_name not in cart:
                # Add an empty list as the value for the username key in the cart dictionary
                cart[user_name] = []            
            # Append a dictionary representing the chosen item to the list associated with the username key in the cart dictionary
            cart[user_name].append({
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

# Define a function named remove_from_cart that takes in a cart dictionary and a username as parameters   
def remove_from_cart(cart, username):
    try:
        if username not in cart or not cart[username]:
            print("Cart is empty or username not found.")
            return

        # Display the current cart for the user
        print(f"Current Cart for {username}:")
        for index, item in enumerate(cart[username], start=1):
            print(f"{index}. {item['name']} - Price: ${item['price']}, Quantity: {item['quantity']}")

        # Prompt the user to enter the index of the item to remove
        index_to_remove = int(input("Enter the index of the item to remove:"))

        # Check if the index is within a valid range
        if 1 <= index_to_remove <= len(cart[username]):
            removed_item = cart[username].pop(index_to_remove - 1)
            print(f"Removed item: {removed_item}")

            # Update the product data file with the added quantity
            with open("products.txt", 'r') as file:
                content = file.read()
                items = content.split("\n")

                # Find the corresponding item in the product data
                name, price, available_quantity = removed_item['name'], removed_item['price'], removed_item['quantity']
                updated_quantity = int(available_quantity) + int(items[index_to_remove - 1].split(",")[2])

                # Update the product data with the added quantity
                updated_product = f"{name},{price},{updated_quantity}"
                content = content.replace(items[index_to_remove - 1], updated_product)

            # Write the updated content back to the product data file
            with open("products.txt", 'w') as fileW:
                fileW.write(content)

        else:
            print("Invalid index. Please enter a valid index.")
    
    # Handle exceptions
    except (ValueError, IndexError, TypeError, KeyError) as err:
        print("Invalid input. Please enter a valid value.")
        print(err)
    except Exception as err:
        print("Something went wrong. Please try again.")
        print(err)

