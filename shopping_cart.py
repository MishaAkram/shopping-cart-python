
from data import get_cart, get_username, cart
from account import create_user, login, logout
from shoppingItemsList import display_shopping_list, get_shopping_items_list_from_file
from add_to_cart import add_to_cart, remove_from_cart
from cart import display_shopping_cart
from checkout import checkout
from display_history import display_history

# Import necessary functions from other modules
# Start an infinite loop for the main program
while True:
    print("˚☽˚｡⋆｡❅*WELCOME TO FROSTY FLAVOURS!˚☽˚｡⋆｡❅*")
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
                # If the user chooses option 1 (View Items)
                if choice == "1":
                    while True:
                        # Display the shopping items list
                        display_shopping_list(get_shopping_items_list_from_file())
                        # Add items to the cart or
                        # Remove items from the cart
                        # Go back to the main menu
                        print("1. Add an item from the cart")
                        print("2. Remove an item from the cart")
                        print("3. Go back")
                        n = input("Please enter your choice: ")
                        # if the user chooses option 1 (Add an item from the cart)
                        if n == "1":
                            add_to_cart()                            
                            # Start an infinite loop for adding more items to the cart
                            while True:
                                choice = input("Would you like to add another item? (y/n): ")
                                # If the user chooses option 1 (Yes) then add another item to the cart
                                if choice == "y":
                                    add_to_cart()
                                # If the user chooses option 2 (No) then go back to the main menu   
                                elif choice == "n":
                                    break
                                else:
                                    print("Invalid choice!")
                        # if the user chooses option 2 (Remove an item from the cart) by inputting the item number           
                        elif n == "2":
                            remove_from_cart(cart, get_username())
                        # if the user chooses option 3 (Go back) then go back to the main menu    
                        elif n == "3":
                            break
                        else:
                            print("Invalid choice!")    


                # If the user chooses option 2 (View cart)
                elif choice == "2":
                    # Display the shopping cart for the logged-in user
                    user_cart=get_cart()
                    print(user_cart)
                    # Start an infinite loop for the shopping cart menu
                    display_shopping_cart(user_cart)
                    if user_cart:
                        choice = input("Would you like to proceed to checkout? (y/n): ")
                        # If the user chooses option 1 (Yes) then proceed to checkout
                        if choice == "y":
                            checkout()
                        # If the user chooses option 2 (No) then go back to the main menu    
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")
                # If the user chooses option 3 (View History)
                elif choice == "3":
                    print("\nView History for", get_username() + ":")  # Print a heading for the view history
                    display_history(get_username())

                # If the user chooses option 4 (Logout)
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
