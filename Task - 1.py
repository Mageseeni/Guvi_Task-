numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)