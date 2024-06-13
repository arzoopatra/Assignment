# Function to check if a substring is present in a given string
def check_substring_presence(main_string, substring):
    return substring in main_string

# Example usage
main_string = "Hello, world!"
substring1 = "world"
substring2 = "python"

# Checking presence of substring1 in main_string
result1 = check_substring_presence(main_string, substring1)
print(f"Substring '{substring1}' is present in '{main_string}': {result1}")

# Checking presence of substring2 in main_string
result2 = check_substring_presence(main_string, substring2)
print(f"Substring '{substring2}' is present in '{main_string}': {result2}")