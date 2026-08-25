# Завдання 1, Романюк, група ІТ-31

birthday_year = 2008;
height = 1.6;
name = "Oleksandr";
is_payment_receiver = True;

print(f"birthday_year: {birthday_year} {type(birthday_year)}");
print(f"height: {height} {type(height)}");
print(f"name: {name} {type(name)}");
print(f"payment_receiver: {is_payment_receiver} {type(is_payment_receiver)}");

birthday_year = str(birthday_year);
is_payment_receiver = float(is_payment_receiver);

print(f"birthday_year: {birthday_year} {type(birthday_year)}");
print(f"payment_receiver: {is_payment_receiver} {type(is_payment_receiver)}");

print(f"birthday_year: {birthday_year + 1} {type(birthday_year)}");