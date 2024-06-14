def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

# Example usage:
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
