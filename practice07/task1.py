print("Oleksandr Romaniuk, IT-31");

name = input("Enter your name (string): ");
age = int(input("Enter your age (integer): "));

if not name:
    name = "Anonymous";

if age < 0:
    age_category = "incorrect";
elif age < 7:
    age_category = "child";
elif age < 18:
    age_category = "schoolchild";
elif age < 65:
    age_category = "adult";
else:
    age_category = "senior";

print(f"Hi, {name}. You are {age_category}");