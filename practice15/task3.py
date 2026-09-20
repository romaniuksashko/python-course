name = "Oleksandr"
surname = "Romaniuk"
group = "IT-31"

print(f"{name} {surname}, group {group}")


def print_table(subject_list):
    print(f"{'#':<4}{'Subject':<35}{'Pairs':<7}{'Grade':<7}")
    for index, item in enumerate(subject_list, 1):
        print(f"{index:<4}{item[0]:<35}{item[1]:<7}{item[2]:<7}")


def sum_pairs(subject_list):
    pairs = 0
    for item in subject_list:
        pairs = pairs + item[1]

    print(f"Pairs per week: {pairs}")


def print_most_pairs(subject_list):
    title = ""
    pairs = 0

    for item in subject_list:
        if item[1] > pairs:
            pairs = item[1]

    for subject in subject_list:
        if pairs == subject[1]:
            title = subject[0]

    print(f"Most pairs: {title} ({pairs})")


def print_weakest_subject(subject_list):
    title = ""
    grade = subject_list[0][2]

    for item in subject_list:
        if item[2] < grade:
            grade = item[2]

    for item in subject_list:
        if grade == item[2]:
            title = item[0]

    return title, grade


def print_titles(subject_list):
    titles = []

    for item in subject_list:
        titles.append(item[0])

    print(f"Titles: {titles}")


def print_grades(subject_list):
    grades = []

    for item in subject_list:
        grades.append(item[2])

    print(f"Grades: {grades}, average: {round(sum(grades) / len(grades), 2)}")


def print_best_subjects(subject_list):
    titles = []

    for item in subject_list:
        if item[2] >= 10:
            titles.append(item[0])

    print(f"Grades 10+: {titles}")


def print_histogram(subject_list):
    for item in subject_list:
        print(f"{item[0]:<27} {'#'*item[2]}")


def retake_weakest_subject(subject_list):
    title, grade = print_weakest_subject(subject_list)
    pairs = 0
    new_list = []

    for item in subject_list:
        if title == item[0]:
            pairs = item[1]
        else:
            new_list.append(item)

    print(f"Retake: {title} {grade} => {grade + 2}")

    new_tulip = (title, pairs, grade + 2)
    new_list.append(new_tulip)

    return new_list


def main():
    subjects = [
        ("Programming", 3, 8),
        ("Web development", 2.5, 10),
        ("IT law", 2, 10),
        ("English", 2, 9),
        ("Ukrainian", 1, 9),
        ("Data bases", 2.5, 8),
        ("Administration of OS and CN", 2, 9)
    ]

    print_table(subjects)

    sum_pairs(subjects)

    print_most_pairs(subjects)

    weakest_title, weakest_grade = print_weakest_subject(subjects)
    print(f"Weakest subject: {weakest_title} ({weakest_grade})")

    print_titles(subjects)

    print_grades(subjects)

    print_best_subjects(subjects)

    print_histogram(subjects)

    subjects = retake_weakest_subject(subjects)
    print(f"Subjects: {subjects}")


main()