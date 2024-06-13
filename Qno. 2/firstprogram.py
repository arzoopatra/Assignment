# Function to check if a number is even or odd
def check_even_odd():
    # Taking input from the user
    number = int(input("Enter a number: "))
    
    # Checking if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

# Call the function
check_even_odd()