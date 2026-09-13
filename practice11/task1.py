print("Oleksandr Romaniuk, IT-31")

name = "Oleksandr"
surname = "Romaniuk"
group = "IT-31"
y = 2008

# First function
def print_card():
    print(f"{"-" * 20} \nName: Oleksandr Romaniuk \nGroup: IT-31 \nBirth year: 2008")


print_card()
print_card()
print_card()

# Second function
def print_card_args(name, surname, year, group="IT-31"):
    print(f"{"-" * 20} \nName: {name} {surname} \nGroup: {group} \nBirth year: {year}")


print_card_args(name, surname, y, group)
print_card_args(year=y, surname=surname, name=name, group=group)
print_card_args(name, surname, group=group, year=y)
print_card_args(name, surname, y)

# print_card_args("Ivan") # TypeError: print_card_args() missing 2 required positional arguments: 'surname' and 'year'
# print_card_args(name="Ivan", "Petrenko") # SyntaxError: positional argument follows keyword argument