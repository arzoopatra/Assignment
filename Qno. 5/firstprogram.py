def write_to_file():

    # Taking input from the user
    user_input = input (" enter a string to write to the file:")

    # Writing the input to a text file 
    with open (" output.txt", "w") as file:
        file.write(user_input)

print (" The string has been written to output.txt.")

# Call to function
write_to_file()
