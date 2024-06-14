def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two numbers in the sequence
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Add the last two numbers to generate the next number
    return fib_sequence[:n]  # Return the first n numbers in the sequence

# Example usage:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))
