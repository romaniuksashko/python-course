print("Oleksandr Romaniuk, IT-31")

y = 2008

def print_age(year):
    print(f"Age: {2026 - year}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    
    return current_year - year
    print("after return")


print(f"print_age: {print_age(y)}")
print(f"get_age: {get_age(y)}")

months = get_age(y) * 12
weeks = months * 4

print(f"Age in months: {months}")
print(f"Age in weeks: {weeks}")
print(f"Age in 2030: {get_age(y, 2030)}")
# print(print_age(y) * 12)  # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print(f"Invalid year 3000 gives: {get_age(3000)}")
