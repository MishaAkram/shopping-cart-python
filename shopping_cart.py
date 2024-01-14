
from data import get_cart, get_username
from account import create_user, login, logout
from shoppingItemsList import display_shopping_list, get_shopping_items_list_from_file
from add_to_cart import add_to_cart
from cart import display_shopping_cart
from checkout import checkout
from display_history import display_history

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
                print("1. View Items")
                print("2. View cart")
                print("3. View History")
                print("4. Logout")
                choice = input("Please enter your choice: ")
                # If the user chooses option 3 (View Items)
                if choice == "1":
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
                elif choice == "2":
                    # Display the shopping cart for the logged-in user
                    user_cart=get_cart()
                    print(user_cart)
                    display_shopping_cart(user_cart)
                    if user_cart:
                        choice = input("Would you like to proceed to checkout? (y/n): ")
                        if choice == "y":
                            checkout()
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")
                # If the user chooses option 4 (View History)
                elif choice == "3":
                    print("\nView History for", get_username() + ":")  # Print a heading for the view history
                    display_history(get_username())

                # If the user chooses option 6 (Logout)
                elif choice == "4":
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
