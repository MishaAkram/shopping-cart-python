def display_shopping_cart(cart_items):
    total_cost = 0
    print("\nShopping Cart:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))
    print("="*50)
    
    for details in cart_items:
        item_name = details['name']
        item_price = details['price']
        item_quantity = details['quantity']
        item_total = float(item_price) * float(item_quantity)
        total_cost += item_total
        
        print("{:<20} ${:<10} {:<10} ${:<10.2f}".format(item_name, item_price, item_quantity, item_total))
    
    print("-"*50)
    print("{:<40} ${:<10.2f}".format("Total Cost:", total_cost))

