name = "Oleksandr"
surname = "Romaniuk"
group = "IT-31"

print(f"{name} {surname}, group {group} \n")


c = len("Romaniuk")
grades = [10, 9, 7, 9, 10, 8, 9, 9]

print(f"Grades: {grades}")
print(f"Number of grades: {len(grades)}")
print(f"Sum of grades: {sum(grades)}")
print(f"Best grade: {max(grades)}")
print(f"Worst grade: {min(grades)}")
print(f"Average of grades: {round(sum(grades) / len(grades), 2)} \n")

print(f"Grades from best to worst: {sorted(grades, reverse=True)}")
print(f"Grades: {grades} \n")

print(f"Best 3 grades: {sorted(grades, reverse=True)[:3]}")
print(f"Worst 3 grades: {sorted(grades)[:3]} \n")

print(f"Position of the worst grade: {grades.index(min(grades)) + 1} \n")

grades_higher_than_average = []

for grade in grades:
    if grade > (sum(grades) / len(grades)):
        grades_higher_than_average.append(grade)

print(f"Grades higher than average: {grades_higher_than_average}")
print(f"Number of grades higher than average: {len(grades_higher_than_average)} \n")

print(f"Is there in grades 12? {12 in grades}")
print(f"Is there in grades 1? {1 in grades} \n")

grades.append(c % 12 + 1)
print(f"Grades: {grades}")

grades.insert(0, 12)
print(f"Grades: {grades}")

grades.remove(min(grades))
print(f"Grades: {grades}")

removed = grades.pop()
print(f"Grades: {grades}, removed: {removed}")

print(f"How many times there is 12? {grades.count(12)} time(s) \n")

grades.sort()
print(f"Sorted grades: {grades}")