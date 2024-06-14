import string

def remove_punctuation(text):
    # Define a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    
    # Use translate method to remove punctuation
    return text.translate(translator)

# Test the function
input_string = "Hello, Arzoo! How are you?"
result = remove_punctuation(input_string)
print("String without punctuation:", result)
