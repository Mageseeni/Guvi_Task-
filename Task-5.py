#1 what is the expected output of the following python code given below

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

#2 integer or string

data = [10, "hello", 22, "world", 37, 100, "test"]

# Check if all elements are either integer or string
result = all(map(lambda x: isinstance(x, (int, str)), data))

print(result)

#3 Generate Fibonacci series from 1 to 50

fibonacci = [0, 1]  # Starting values for Fibonacci series

# Using lambda to generate Fibonacci numbers
while True:
    next_fib = (lambda a, b: a + b)(fibonacci[-2], fibonacci[-1])
    if next_fib > 50:
        break
    fibonacci.append(next_fib)

# Print Fibonacci series from 1 to 50 (excluding 0)
print(fibonacci[1:])


#4 

import re

def validate_email(email):
    # Regular expression to validate email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_bangladesh_mobile(mobile):
    # Regular expression to validate Bangladesh mobile number
    # Bangladeshi numbers start with +8801 or 01 followed by 9 digits (in total 11 digits)
    mobile_regex = r'^(?:\+8801|01)\d{9}$'
    return re.match(mobile_regex, mobile) is not None

def validate_usa_telephone(telephone):
    # Regular expression to validate USA telephone number (with optional country code +1)
    # Pattern: (XXX) XXX-XXXX or XXX-XXX-XXXX or +1 XXX-XXX-XXXX
    usa_telephone_regex = r'^(?:\+1\s?)?(\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$'
    return re.match(usa_telephone_regex, telephone) is not None

def validate_password(password):
    # Regular expression to validate 16-character alphanumeric password with at least:
    # 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;"\'<>,.?/-]).{16}$'
    return re.match(password_regex, password) is not None

# Example usage:
if __name__ == '__main__':
    # Test cases
    print(validate_email("example@email.com"))  
    print(validate_bangladesh_mobile("+8801976543210"))  
    print(validate_usa_telephone("(123) 456-7890"))  
    print(validate_password("Password@1234567890"))  

   