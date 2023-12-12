import re

def extract_numbers(input_string):
    # Use regular expression to find numbers in the input string
    numbers = re.findall(r'\d+', input_string)
    
    # Convert the list of strings to integers
    numbers = [int(num) for num in numbers]
    
    return numbers

# Example usage:
input_string = "Hello123World456"
result = extract_numbers(input_string)

print(f"Input String: {input_string}")
print(f"Numbers extracted: {result}")
