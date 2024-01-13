

# BEGIN: Writing data to the file
# user input
def input_icecream():
    icecream_flavour = input("Please enter the name of the icecream_flavour you wish to add: ")
    icecream_price = float(input("Please enter the price of the icecream_flavour you wish to add: "))
    icecream_quantity = int(input("Please enter the quantity of the icecream_flavour you wish to add: "))
    icecream = icecream_flavour + ": " + icecream_price + ", " + icecream_quantity
    return icecream
# write to file
def add_new_icecream(icecream):
    with open("icecream.txt", "a") as file:
        file.write(icecream + "\n")

def update_icecream_price():
    icecream_flavour = input("Please enter the name of the icecream_flavour you wish to update: ")
    icecream_price = float(input("Please enter the new price of the icecream_flavour you wish to update: "))
    with open("icecream.txt", "r") as file:
        for line in file:
            stored_flavour, _ = line.strip().split(":")
            if icecream_flavour == stored_flavour:
                file.write(icecream_price + "\n")
                return True
    return False
    

    

