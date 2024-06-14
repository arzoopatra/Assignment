def check_prefix_suffix(text, prefix, suffix):
    starts_with_prefix = text.startswith(prefix)
    ends_with_suffix = text.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

# Test the function
input_string = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"
prefix_result, suffix_result = check_prefix_suffix(input_string, prefix_to_check, suffix_to_check)

# Output the results
if prefix_result:
    print(f"The string '{input_string}' starts with '{prefix_to_check}'")
else:
    print(f"The string '{input_string}' does not start with '{prefix_to_check}'")

if suffix_result:
    print(f"The string '{input_string}' ends with '{suffix_to_check}'")
else:
    print(f"The string '{input_string}' does not end with '{suffix_to_check}'")
