print("Oleksandr Romaniuk, IT-31");

mark = int(input("Enter your mark (integer): "));
missed_lessons = int(input("Enter number of your missed lessons (integer): "));
is_passed = "passed";

if mark < 0 or mark > 100:
    print(f"Error! Mark can be only within 0 and 100");
else:
    if mark > 89:
        letter_mark = "A";
    elif mark > 81:
        letter_mark = "B";
    elif mark > 73:
        letter_mark = "C";
    elif mark > 63:
        letter_mark = "D";
    elif mark > 59:
        letter_mark = "E";
    else:
        letter_mark = "F";
        is_passed = "failed";

    if missed_lessons * 100 / 16 > 30:
        print(f"Not allowed to pass. Too many lessons skipped!");
        is_passed = "failed";

    print(f"Mark is {mark}, letter mark is {letter_mark} and exam is {is_passed}");