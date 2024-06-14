from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate the age
age = calculate_age(birth_year)

# Print the result
print("You are", age, "years old.")
