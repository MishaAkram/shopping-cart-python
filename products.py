

# user input
def input_icecream():
    # Prompt the user to enter the name of the ice cream flavor
    icecream_flavour = input("Please enter the name of the ice cream flavor you wish to add: ")
    # Prompt the user to enter the price of the ice cream flavor
    icecream_price = float(input("Please enter the price of the ice cream flavor you wish to add: "))
    # Prompt the user to enter the quantity of the ice cream flavor
    icecream_quantity = int(input("Please enter the quantity of the ice cream flavor you wish to add: "))
    # Concatenate the ice cream flavor, price, and quantity into a string
    icecream = icecream_flavour + ": " + str(icecream_price) + ", " + str(icecream_quantity)
    # Return the ice cream details
    return icecream

# write to file
def add_new_icecream(icecream):
    # Open the file in append mode
    with open("icecream.txt", "a") as file:
        # Write the ice cream details to the file
        file.write(icecream + "\n")

# update ice cream price
def update_icecream_price():
    # Prompt the user to enter the name of the ice cream flavor to update
    icecream_flavour = input("Please enter the name of the ice cream flavor you wish to update: ")
    # Prompt the user to enter the new price of the ice cream flavor
    icecream_price = float(input("Please enter the new price of the ice cream flavor you wish to update: "))
    # Open the file in read mode
    with open("icecream.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line by ":" to get the stored flavor
            stored_flavour, _ = line.strip().split(":")
            # Check if the entered flavor matches the stored flavor
            if icecream_flavour == stored_flavour:
                # Open the file in write mode
                with open("icecream.txt", "w") as file:
                    # Write the new price to the file
                    file.write(str(icecream_price) + "\n")
                # Return True to indicate successful update
                return True
    # Return False if the flavor was not found
    return False

def restock_icecream_flavour():
    # Prompt the user to enter the name of the ice cream flavor to restock
    icecream_flavour = input("Please enter the name of the ice cream flavor you wish to restock: ")
    # Prompt the user to enter the quantity of the ice cream flavor to restock
    icecream_quantity = int(input("Please enter the quantity of the ice cream flavor you wish to restock: "))
    # Open the file in read mode
    with open("icecream.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line by ":" to get the stored flavor
            stored_flavour, _ = line.strip().split(":")
            # Check if the entered flavor matches the stored flavor
            if icecream_flavour == stored_flavour:
                # Open the file in write mode
                with open("icecream.txt", "w") as file:
                    # Write the new quantity to the file
                    file.write(str(icecream_quantity) + "\n")
                # Return True to indicate successful restock
                return True
    # Return False if the flavor was not found
    return False
    

    

