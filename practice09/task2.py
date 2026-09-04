print("Oleksandr Romaniuk, IT-31")

user_number = abs(int(input("Enter an integer (ddmmyyyy): ")))

digits_counter = 0
digits_sum = 0
reversed_number = 0

k = 0
digits_smallest = user_number
digits_largest = 0

while user_number > 0:
    digits_sum = digits_sum + user_number % 10

    digits_large = user_number % 10
    digits_small = user_number % 10
    k = user_number % 10

    if digits_large > digits_largest:  
        digits_largest = digits_large

    if digits_small < digits_smallest:
        digits_smallest = digits_small

    reversed_number = reversed_number * 10 + k 

    user_number = user_number // 10
    digits_counter = digits_counter + 1

print(f"Digits: {digits_counter}")
print(f"Sum of digits: {digits_sum}")
print(f"Max digit: {digits_largest}, min digit: {digits_smallest}")
print(f"Reversed: {reversed_number}")
