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


#5

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


#6 

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

#7

def first_non_repeating(nums):
    # Dictionary to count occurrences
    count = {}
    
    # Count the occurrences of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Find the first non-repeating element
    for num in nums:
        if count[num] == 1:
            return num
    
    return None  # Return None if there are no non-repeating elements

# Example usage
numbers = [4, 5, 1, 2, 0, 4, 5]
result = first_non_repeating(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There are no non-repeating elements.")


#8
def find_minimum(sorted_list):
    if not sorted_list:  # Check if the list is empty
        return None
    return sorted_list[0]  # Return the first element

# Example usage
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minimum = find_minimum(sorted_numbers)

if minimum is not None:
    print(f"The minimum element in the sorted list is: {minimum}")
else:
    print("The list is empty.")


#9

def find_triplet(nums, target_sum):
    n = len(nums)
    # Sort the list for better performance and to avoid duplicates
    nums.sort()
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target_sum:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    
    return None  # Return None if no triplet is found

# Example usage
numbers = [10, 20, 30, 9]
target_value = 59
triplet = find_triplet(numbers, target_value)

if triplet:
    print(f"The triplet that sums to {target_value} is: {triplet}")
else:
    print("No triplet found that sums to the target value.")


#10

def has_zero_sum_sublist(nums):
    cumulative_sum = 0
    seen_sums = set()
    
    for num in nums:
        cumulative_sum += num
        
        # Check if cumulative sum is zero or has been seen before
        if cumulative_sum == 0 or cumulative_sum in seen_sums:
            return True
        
        seen_sums.add(cumulative_sum)
    
    return False

# Example usage
numbers = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(numbers)

if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
