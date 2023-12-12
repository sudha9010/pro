import re

def extract_numbers_and_letters(input_string):
    # Use regular expression to find numbers and letters in the input string
    numbers = re.findall(r'\d+', input_string)
    letters = re.findall(r'[a-zA-Z]+', input_string)
    
    # Convert the list of strings to integers for numbers
    numbers = [int(num) for num in numbers]
    
    return numbers, letters

# Example usage:
input_string = "Hello World @123"
numbers, letters = extract_numbers_and_letters(input_string)

print(f"Input String: {input_string}")
print(f"Numbers extracted: {numbers}")
print(f"Letters extracted: {letters}")
