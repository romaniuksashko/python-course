# Завдання 5, Романюк, група ІТ-31

a = 12;
b = 5;
multiplication_of_a_and_b = a*b;

is_a_positive = a > 0;
is_a_even = (a % 2) == 0;

print(f"is_a_positive: {is_a_positive}");
print(f"is_a_even: {is_a_even}");
print(f"is_a_positive and is_a_even: {is_a_positive and is_a_even}");

is_multiplication_of_a_and_b_positive = multiplication_of_a_and_b > 0;
is_multiplication_of_a_and_b_even = (multiplication_of_a_and_b % 2) == 0;

print(f"is_multiplication_of_a_and_b_positive: {is_multiplication_of_a_and_b_positive}");
print(f"is_multiplication_of_a_and_b_even: {is_multiplication_of_a_and_b_even}");
print(f"is_multiplication_of_a_and_b_positive and is_multiplication_of_a_and_b_even: {is_multiplication_of_a_and_b_positive and is_multiplication_of_a_and_b_even}");