print("Oleksandr Romaniuk, IT-31")

user_tries = 0

while True:
    user_mark = int(input("Enter your mark: "))
    user_tries = user_tries + 1

    if 0 <= user_mark <= 100:
        print(f"Accepted after {user_tries} tries");

        if user_mark > 89:
            letter_mark = "A";
        elif user_mark > 81:
            letter_mark = "B";
        elif user_mark > 73:
            letter_mark = "C";
        elif user_mark > 63:
            letter_mark = "D";
        elif user_mark > 59:
            letter_mark = "E";
        else:
            letter_mark = "F";
        
        print(f"Grade: {letter_mark}")
        break
    elif user_mark < 0:
        print("Mark is too small. Minimum 0")
    elif user_mark > 100:
        print("Mark is too big. Maximum 100")