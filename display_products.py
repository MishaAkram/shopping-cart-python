 
# Define a function to display ice cream flavors
def display_ice_cream_flavors(flavors):
    # Print a header for the ice cream shop
    print("+--------------------------------------------------------------------+")
    print("|                   WELCOME TO ICE CREAM SHOP                        |")
    print("+--------------------------------------------------------------------+")
    # Print a table header for the flavors
    print("| S.No | {:<20} | {:<10} | {:<25} |".format("Flavor", "Price", "Quantity Available"))
    print("+---------------------+------------+-------------------------+")
    # Initialize a counter variable
    i=1
    # Iterate over each flavor in the list of flavors
    for flavor in flavors:
        # Extract the name, price, and quantity of the flavor
        name = flavor[0]
        price = f"${flavor[1]}"
        quantity = flavor[2]
        # Generate an index for the flavor
        index = str(i)+"."
        # Print a row in the table for the flavor
        print("| {:<4} | {:<20} | {:<10} | {:<25} |".format(index,name, price, quantity))
        # Increment the counter
        i+=1

    # Print a footer for the table
    print("+---------------------+------------+---------------------------------+")


