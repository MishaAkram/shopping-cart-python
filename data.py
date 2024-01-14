
# Initialize an empty cart and an empty username
cart = {} 
username = "zara"

def get_cart():
    """
    Get the cart for the current user.
    
    Returns:
        dict: The cart for the current user.
        
    Raises:
        KeyError: If the cart does not exist for the current user.
    """
    try:
        print("username8", username)
        print("cart8", cart)
        return cart[username]
    except KeyError as Err:
        print("Cart does not exist for this user")
        
def get_username():
    """
    Get the current username.
    
    Returns:
        str: The current username.
    """
    return username

def set_username(name):
    """
    Set the username to the given name.
    
    Args:
        name (str): The new username.
    """
    username = name
