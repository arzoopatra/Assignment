def string_to_list_using_list_constructor(input_string):
    return list(input_string)

# Test the function
input_string = "Hello, World!"
char_list = string_to_list_using_list_constructor(input_string)
print("List of characters:", char_list)


def string_to_list_using_comprehension(input_string):
    return [char for char in input_string]

# Test the function
input_string = "Hello, World!"
char_list = string_to_list_using_comprehension(input_string)
print("List of characters:", char_list)
