def display_shopping_cart(cart_items):
    total_cost = 0
    print("\nShopping Cart:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))
    print("="*50)
    
    for item, details in cart_items.items():
        item_price = details['price']
        item_quantity = details['quantity']
        item_total = item_price * item_quantity
        total_cost += item_total
        
        print("{:<20} ${:<10.2f} {:<10} ${:<10.2f}".format(item, item_price, item_quantity, item_total))
    
    print("-"*50)
    print("{:<40} ${:<10.2f}".format("Total Cost:", total_cost))


# Example Usage
if __name__ == "__main__":
    shopping_cart = {
        "Vanilla Ice Cream": {"price": 5.50, "quantity": 2},
        "Chocolate Bar": {"price": 2.00, "quantity": 3},
        "Coffee Beans": {"price": 8.50, "quantity": 1}
    }

    display_shopping_cart(shopping_cart)
