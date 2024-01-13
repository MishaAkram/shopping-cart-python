def display_ice_cream_flavors(flavors):
    print("+--------------------------------------------------------------------+")
    print("|                   WELCOME TO ICE CREAM SHOP                        |")
    print("+--------------------------------------------------------------------+")
    print("| S.No | {:<20} | {:<10} | {:<25} |".format("Flavor", "Price", "Quantity Available"))
    print("+---------------------+------------+-------------------------+")
    i=1
    for flavor in flavors:
        name = flavor[0]
        price = f"${flavor[1]}"
        quantity = flavor[2]
        index = str(i)+"."
        print("| {:<4} | {:<20} | {:<10} | {:<25} |".format(index,name, price, quantity))
        i+=1

    print("+---------------------+------------+---------------------------------+")


