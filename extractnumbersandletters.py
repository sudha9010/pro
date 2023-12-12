import re

def extract_numbers_and_letters(input_string):
    
    numbers = re.findall(r'\d+', input_string)
    letters = re.findall(r'[a-zA-Z]+', input_string)
    
    
    numbers = [int(num) for num in numbers]
    
    return numbers, letters


input_string = "Hello World @123"
numbers, letters = extract_numbers_and_letters(input_string)

print(f"Input String: {input_string}")
print(f"Numbers extracted: {numbers}")
print(f"Letters extracted: {letters}")
