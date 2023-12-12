import re

def extract_numbers(input_string):
    
    numbers = re.findall(r'\d+', input_string)
    
    
    numbers = [int(num) for num in numbers]
    
    return numbers


input_string = "Hello123World456"
result = extract_numbers(input_string)

print(f"Input String: {input_string}")
print(f"Numbers extracted: {result}")
