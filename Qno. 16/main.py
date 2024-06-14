def count_characters(string):
    # Initialize an empty dictionary to store character frequencies
    char_freq = {}

    # Iterate through each character in the string
    for char in string:
        # Increment the count of the character in the dictionary
        char_freq[char] = char_freq.get(char, 0) + 1

    return char_freq

# Test the function
input_string = "Hello, World!"
result = count_characters(input_string)
print("Character frequencies:")
for char, freq in result.items():
    print(f"'{char}': {freq}")
