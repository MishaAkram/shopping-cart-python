from data import cart, username

# Define a function to display the shopping cart items
def display_shopping_cart(cart_items):
    total_cost = 0  # Initialize the total cost variable to 0
    print("\nShopping Cart:")  # Print a heading for the shopping cart
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))  # Print the column headers
    print("="*50)  # Print a line of equal signs for separation
    
    # Iterate through each item in the cart_items list
    try:
        for details in cart_items:
            item_name = details['name']  # Get the name of the item
            item_price = details['price']  # Get the price of the item
            item_quantity = details['quantity']  # Get the quantity of the item
            item_total = float(item_price) * float(item_quantity)  # Calculate the total cost for the item
            total_cost += item_total  # Add the item total to the total cost
            
            # Print the item details in a formatted manner
            print("{:<20} ${:<10} {:<10} ${:<10.2f}".format(item_name, item_price, item_quantity, item_total))
        print("-"*50)  # Print a line of dashes for separation
        print("{:<40} ${:<10.2f}".format("Total Cost:", total_cost))  # Print the total cost of the shopping cart
    except TypeError as err:
        print("Your cart is empty")
