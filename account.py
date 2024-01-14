import  data
def create_user(name, password):
    # Create a new user with the given username and password
    user_data = f"{name}:{password}\n"
    try:
        if check_user_exists(name):
            raise ValueError("User already exists")
        with open("users.txt", "a") as file:
            file.write(user_data)
    except ValueError as err:
        print(err)

        

def check_user_exists(name):
    # Check if a user with the given username exists
    with open("users.txt", "r") as file:
        for line in file:
            stored_username= line.strip().split(":")
            if name == stored_username[0]:
                return True
    return False

def login(name, password):
    # Check if the given username and password combination is valid
    with open("users.txt", "r") as file:
        for line in file:
            user= line.strip().split(":")
            if len(user) == 2:
                stored_username, stored_password = user
                if name == stored_username and password == stored_password:
                    data.username= name
                    return True
    return False

def logout():
    data.username= ""
    pass


