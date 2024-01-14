
from data import get_cart
from account import create_user, login, logout
from shoppingItemsList import display_shopping_list, get_shopping_items_list_from_file
from add_to_cart import add_to_cart
from cart import display_shopping_cart
from checkout import checkout
# Import necessary functions from other modules
# Start an infinite loop for the main program
while True:
    print("Welcome to the shopping cart program!")
    print("Please choose from the following options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Please enter your choice: ")

    # If the user chooses option 1 (Login)
    if choice == "1":
        name = input("Please enter your username: ")
        password = input("Please enter your password: ")

        # Check if the login credentials are valid
        if login(name, password):
            print("Login successful!")

            # Start an infinite loop for the logged-in user menu
            while True:
                print("Please choose from the following options:")
                print("1. Add item to cart")
                print("2. Remove item from cart")
                print("3. View Items")
                print("4. View cart")
                print("5. Checkout")
                print("6. Logout")
                choice = input("Please enter your choice: ")

                # If the user chooses option 1 (Add item to cart)
                if choice == "1":
                    item = input("Please enter the item you wish to add: ")

                # If the user chooses option 2 (Remove item from cart)
                elif choice == "2":
                    item = input("Please enter the item you wish to remove: ")

                # If the user chooses option 3 (View Items)
                elif choice == "3":
                    # Display the shopping items list
                    display_shopping_list(get_shopping_items_list_from_file())
                    # Add items to the cart
                    add_to_cart()

                    # Start an infinite loop for adding more items to the cart
                    while True:
                        choice = input("Would you like to add another item? (y/n): ")
                        if choice == "y":
                            add_to_cart()
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")

                # If the user chooses option 4 (View cart)
                elif choice == "4":
                    # Display the shopping cart for the logged-in user
                    user_cart=get_cart()
                    display_shopping_cart(user_cart)
                    if user_cart:
                        choice = input("Would you like to proceed to checkout? (y/n): ")
                        if choice == "y":
                            checkout()
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")

                # If the user chooses option 5 (Checkout)
                elif choice == "5":
                    checkout()

                # If the user chooses option 6 (Logout)
                elif choice == "6":
                    logout()
                    break

                else:
                    print("Invalid choice!")

        else:
            print("Invalid username or password!")

    # If the user chooses option 2 (Register)
    elif choice == "2":
        name = input("Please enter your username: ")
        password = input("Please enter your password: ")
        create_user(name, password)

    # If the user chooses option 3 (Exit)
    elif choice == "3":
        print("Thank you for using the shopping cart program!")
        break

    else:
        print("Invalid choice!")
