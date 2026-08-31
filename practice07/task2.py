print("Oleksandr Romaniuk, IT-31");

integer_number = int(input("Enter your number (integer): "));

if integer_number > 0:
    number_sign = "positive";

    if integer_number % 2 == 0:
        number_evenness = "even";
    else:
        number_evenness = "odd";
    
    print(f"The number are {number_sign} and {number_evenness}");
elif integer_number == 0:
    number_sign = "zero";

    print(f"The number is {number_sign}");
else: 
    number_sign = "negative";

    if integer_number % 2 == 0:
        number_evenness = "even";
    else:
        number_evenness = "odd";

    print(f"The number are {number_sign} and {number_evenness}");