def find_min_max(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None
    
    # Use min() and max() functions to find the minimum and maximum values
    minimum = min(numbers)
    maximum = max(numbers)
    
    return minimum, maximum

# Test the function
number_list = [5, 8, 2, 10, 3]
min_value, max_value = find_min_max(number_list)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
