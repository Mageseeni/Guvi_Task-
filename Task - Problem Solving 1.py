#1
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

 #2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in numbers if is_prime(num)]

prime_count = len(prime_numbers)

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)

#3
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in numbers if is_happy(num)]

happy_count = len(happy_numbers)

print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", happy_count)

#4
def sum_first_last_digit(num):
    # Convert the integer to a string
    num_str = str(num)
    
    # Get the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    # Calculate the sum
    digit_sum = first_digit + last_digit
    return digit_sum

number = 12345
result = sum_first_last_digit(number)
print(f"The sum of the first and last digit of {number} is: {result}")

def min_difference(mango_bags, M):
    if len(mango_bags) < M:
        return -1  # Not enough bags for the students

    # Step 1: Sort the list of bags
    mango_bags.sort()
    
    # Step 2: Initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # Step 3: Find the minimum difference for M bags
    for i in range(len(mango_bags) - M + 1):
        current_diff = mango_bags[i + M - 1] - mango_bags[i]
        min_diff = min(min_diff, current_diff)
    
    return min_diff

# Example usage
mango_bags = [12, 3, 5, 7, 19]
M = 3
result = min_difference(mango_bags, M)
print(f"The minimum difference between maximum and minimum bags given to {M} students is: {result}")

def find_duplicates(list1, list2, list3):
    # Convert lists to sets for easier intersection
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find duplicates by intersecting the three sets
    duplicates = set1.intersection(set2).intersection(set3)
    
    return list(duplicates)

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [6, 7, 8, 9, 10]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", duplicates)
