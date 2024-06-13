# Function to calculate the factorial of a given number
def calculate_factorial():
    try:
        # Taking input from the user
        number = int(input("Enter a non-negative integer: "))
        
        if number < 0:
            print("Please enter a non-negative integer.")
            return
        
        # Initialize the factorial to 1 (as 0! is 1)
        factorial = 1
        
        # Calculate the factorial
        for i in range(1, number + 1):
            factorial *= i
        
        # Print the result
        print(f"The factorial of {number} is {factorial}.")
    
    except ValueError:
        print("Please enter a valid integer.")

# Call the function
calculate_factorial()