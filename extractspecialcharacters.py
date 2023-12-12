import re

def extract_numbers_letters_special_chars(input_string):

    numbers = re.findall(r'\d+', input_string)
    letters = re.findall(r'[a-zA-Z]+', input_string)
    special_chars = re.findall(r'[^a-zA-Z0-9\s]', input_string)
    
    numbers = [int(num) for num in numbers]
    
    return numbers, letters, special_chars

input_string = "Hello123@World456!"
numbers, letters, special_chars = extract_numbers_letters_special_chars(input_string)

print(f"Input String: {input_string}")
print(f"Numbers extracted: {numbers}")
print(f"Letters extracted: {letters}")
print(f"Special characters extracted: {special_chars}")


