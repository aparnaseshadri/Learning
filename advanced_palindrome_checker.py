import re

def is_palidrome(s):
    cleaned_string = re.sub(r'[^a-zA-z0-9]',"",s).lower()
    
    return cleaned_string == cleaned_string[::-1]

test_string ="appa"
test_string2 = "1appa1"

print(f"Is '{test_string}' a palidrome, {is_palidrome(test_string)}")
print(f"Is '{test_string2}' a palidrome, {is_palidrome(test_string2)}")
