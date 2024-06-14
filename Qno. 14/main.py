def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

# Read multiple lines of input from the user
lines = read_multiple_lines()

# Print all the lines
print("You entered the following lines:")
for line in lines:
    print(line)
