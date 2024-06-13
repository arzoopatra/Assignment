# Function to read and print the content of a text file
def read_file_and_print(filename):
    try:
        # Opening the file in read mode
        with open(filename, "r") as file:
            # Reading the entire content of the file
            file_content = file.read()
            
            # Printing the content to the console
            print("File content:")
            print(file_content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "sample.txt"  # Replace with the path to your text file
read_file_and_print(filename)