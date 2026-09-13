print("Oleksandr Romaniuk, IT-31")

def read_grade(prompt):
    """ Returns grades from user n times"""
    while True:
        grade = int(input(f"Enter grade {prompt}: ")) 

        if int(grade) < 0 or int(grade) > 100:
            print("Grade must be between 0 and 100")
            continue

        return int(grade)


def to_letter(grade):
    """ Returns grade in letter """
    if grade > 89:
        return "A"
    
    if grade > 81:
        return "B"
    
    if grade > 73:
        return "C"
    
    if grade > 63:
        return "D"
    
    if grade > 59:
        return "E"
    
    return "F"


def average(grades):
    """ Returns average of numbers """
    sum = 0

    for grade in grades:
        sum += grade

    calcucation = sum / len(grades)

    return round(calcucation, 2)


def count_above(grades, limit):
    """ Returns count of grades higher than average """
    higher_than_average = 0

    for grade in grades:
        if grade > limit:
            higher_than_average += 1

    return higher_than_average


def print_report(name, group, grades):
    """ Prints report from data of other functions """
    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print(f"Grades: {grades}")
    print(f"Average: {average(grades)} -> {to_letter(average(grades))}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, average(grades))}")


def main():
    """ Gives base date to print_report() """
    name = "Oleksandr"
    group = "IT-31"
    n = len("Oleksandr")

    grades = []

    for grade in range(1, n):
        prompt = read_grade(grade)
        grades.append(prompt)

    print_report(name, group, grades)

    
main()