print("Oleksandr Romaniuk, IT-31");

first_number = float(input("Enter first number (float): "));
operation_sign = input("Enter operation sign (string): ");
second_number = float(input("Enter second number (float): "));

if operation_sign == "+":
    print(f"{first_number} + {second_number} = {round(first_number + second_number, 4)}");
elif operation_sign == "-":
    print(f"{first_number} - {second_number} = {round(first_number - second_number, 4)}");
elif operation_sign == "*":
    print(f"{first_number} * {second_number} = {round(first_number * second_number, 4)}");
elif operation_sign == "/":
    if second_number == 0:
        print(f"Operation does not succeed. The second number is {second_number}");
    else:
        print(f"{first_number} / {second_number} = {round(first_number / second_number, 4)}");
elif operation_sign == "//":
    if second_number == 0:
        print(f"Operation does not succeed. The second number is {second_number}");
    else:
        print(f"{first_number} // {second_number} = {round(first_number // second_number, 4)}");
elif operation_sign == "%":
    if second_number == 0:
        print(f"Operation does not succeed. The second number is {second_number}");
    else:
        print(f"{first_number} % {second_number} = {round(first_number % second_number, 4)}");
elif operation_sign == "**":
    print(f"{first_number} ** {second_number} = {round(first_number ** second_number, 4)}");
else:
    print(f"Operation sign is undefined. Please try again");