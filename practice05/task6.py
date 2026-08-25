# Завдання 6, Романюк, група ІТ-31

user_age = int(input("Your age: "));

print(f"Is age bigger than 18 and lesser than 60: {18 <= user_age <= 60}");
print(f"Is age even: {(user_age % 2) == 0}");
print(f"Is age bigger than 18 and lesser than 60 and Is age even: {(user_age % 2) == 0 and 18 <= user_age <= 60}");
print(f"Is age bigger than 18 and lesser than 60 or Is age even: {(user_age % 2) == 0 or 18 <= user_age <= 60}");