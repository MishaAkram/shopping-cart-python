
from datetime import datetime
from data import get_username, cart, get_cart

# Get the current date and time
current_datetime = datetime.now()

def checkout():
    """
    Perform the checkout process by taking user input for the amount to be paid,
    retrieving the username and cart data, and saving the transaction history.
    """
    # Prompt the user to enter the amount to be paid
    amount = float(input("Enter the amount to be paid: "))
    # Initialize an empty string to store the cart items
    cart_string = ""
    user_cart = get_cart()

    # Iterate over each item in the cart
    for item in user_cart:
        print("item")
        print(item)
        # Concatenate the item name, price, and quantity to the cart string
        cart_string += cart_string + item["name"] + "," + str(item["price"]) + "," + str(item["quantity"]) + ":"

    # Remove the trailing "|" character from the cart string
    cart_string = cart_string[:-1]
    cart.pop(get_username())

    # Print the username and current datetime

    # Create the transaction history string
    history = "{}|[{}]|{}".format(get_username(), cart_string, current_datetime)
    history += "\n"

    # Append the transaction history to the "history.txt" file
    with open("history.txt", "a") as file:
        file.write(history)

