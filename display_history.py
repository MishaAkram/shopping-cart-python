from datetime import datetime
def parse_view_history(input_string):
    # Splitting the input into username, items, and timestamp
    parts = input_string.split('|')
    print(parts)
    if len(parts) != 3:
        raise ValueError("Invalid input format")

    # Extracting username, items, and timestamp
    username = parts[0].strip()
    data = parts[1].strip()
    timestamp = parts[2].strip()

    # Splitting the items into a list
    items_data = [item.strip() for item in data[1:-1].split(':')]

    # Parsing each item into a dictionary
    items_list = []
    for item in items_data:
        item_parts = item.split(',')
        item_dict = {
            'Item Name': item_parts[0].strip(),
            'Price': float(item_parts[1]),
            'Quantity': int(item_parts[2])
        }
        items_list.append(item_dict)

    # Creating the view history dictionary
    view_history = {
        'Username': username,
        'Items': items_list,
        'Timestamp': timestamp
    }

    return view_history

# Define a function to display the view history
def display_view_history(username, view_history):
    total_cost = 0  # Initialize the total cost variable to 0
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))  # Print the column headers
    print("="*50)  # Print a line of equal signs for separation
    
    # Iterate through each item in the view history
    try:
        for details in view_history['Items']:
            item_name = details['Item Name']  # Get the name of the item
            item_price = details['Price']  # Get the price of the item
            item_quantity = details['Quantity']  # Get the quantity of the item
            item_total = float(item_price) * float(item_quantity)  # Calculate the total cost for the item
            total_cost += item_total  # Add the item total to the total cost
            
            # Print the item details in a formatted manner
            print("{:<20} ${:<10} {:<10} ${:<10.2f}".format(item_name, item_price, item_quantity, item_total))
        print("-"*50)  # Print a line of dashes for separation
        print("{:<40} ${:<10.2f}".format("Total Cost:", total_cost))  # Print the total cost of the view history
        timestamp = datetime.strptime(view_history['Timestamp'], "%Y-%m-%d %H:%M:%S.%f")

        # Format the datetime object as a string in a desired format
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print("Timestamp:", formatted_timestamp)  # Print the timestamp of the view history
    except TypeError as err:
        print("No view history available for", username)


def display_history(username):
    # Open the "history.txt" file in read mode
    with open("history.txt", 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into a list of items using newline as the delimiter
        items = content.split("\n")
        history=[]
        for item in items:
            # Check if the username is in the item
            if username in item:
                history.append(item)
        for item in history:
            parse_history = parse_view_history(item)
            display_view_history(username, parse_history)
        
