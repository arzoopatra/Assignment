def calculate_sum(numbers):
    # sourcery skip: simplify-generator, sum-comprehension
    # Initialize sum to 0
    total = 0
    
    # Iterate through the numbers and add them to the total
    for num in numbers:
        total += num
    
    return total

# Test the function
number_list = [1, 2, 3, 4, 5]
total_sum = calculate_sum(number_list)
print("Sum of the numbers:", total_sum)
