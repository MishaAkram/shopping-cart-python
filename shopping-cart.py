
from account import create_user, login, logout
from shoppingItemsList import display_shopping_list, get_shopping_items_list_from_file
from add_to_cart import add_to_cart
from cart import display_shopping_cart

cart = {}
username = ""
while True:
    print("Welcome to the shopping cart program!")
    print("Please choose from the following options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if login(username, password):
            username = username
            print("Login successful!")
            while True:
                print("Please choose from the following options:")
                print("1. Add item to cart")
                print("2. Remove item from cart")
                print("3. View Items")
                print("4. View cart")
                print("5. Checkout")
                print("6. Logout")
                choice = input("Please enter your choice: ")
                if choice == "1":
                    item = input("Please enter the item you wish to add: ")
                elif choice == "2":
                    item = input("Please enter the item you wish to remove: ")
                elif choice == "3":
                    display_shopping_list(get_shopping_items_list_from_file())
                    add_to_cart(cart, username)
                    while True:
                        choice = input("Would you like to add another item? (y/n): ")
                        if choice == "y":
                            add_to_cart(cart, username)
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")
                elif choice == "4":
                    display_shopping_cart(cart[username])
                    
                elif choice == "5":
                    checkout(username)
                elif choice == "6":
                    logout()
                    break
                else:
                    print("Invalid choice!")
        else:
            print("Invalid username or password!")
    elif choice == "2":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        create_user(username, password)
    elif choice == "3":
        print("Thank you for using the shopping cart program!")
        break
    else:
        print("Invalid choice!")
