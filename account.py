def create_user(username, password):
    # Create a new user with the given username and password
    user_data = f"{username}:{password}\n"
    try:
        if check_user_exists(username):
            raise ValueError("User already exists")
        with open("users.txt", "a") as file:
            file.write(user_data)
    except ValueError as err:
        print(err)

        

def check_user_exists(username):
    # Check if a user with the given username exists
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(":")
            if username == stored_username:
                return True
    return False

def login(username, password):
    # Check if the given username and password combination is valid
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

def logout():
    # Perform logout operations
    # (e.g., clearing session data, redirecting to login page, etc.)
    pass

# Usage example:
create_user("john", "password123")
create_user("jane", "secret456")

print(login("john", "password123"))  # True
print(login("jane", "wrongpassword"))  # False

logout()

