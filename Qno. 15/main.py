import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

# Example usage:
file_path = input("Enter the path to the CSV file: ")
read_csv_file(file_path)
