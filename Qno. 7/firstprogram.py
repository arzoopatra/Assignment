# Function to take a string input from the user and return its length
def get_string_length():
    # Taking input from the user
    user_input = input("Enter a string: ")
    
    # Calculating the length of the string
    length = len(user_input)
    
    # Returning the length
    print(f"The length of the entered string is: {length}")

# Call the function
get_string_length()