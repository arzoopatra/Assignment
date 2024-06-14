def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            with open(destination_file, 'w') as f_dest:
                # Read the contents of the source file and write to the destination file
                for line in f_source:
                    f_dest.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One of the files does not exist.")
    except IOError:
        print("Error: Unable to read from or write to the file.")

# Example usage:
source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
