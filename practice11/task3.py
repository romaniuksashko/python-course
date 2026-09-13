print("Oleksandr Romaniuk, IT-31")

name = "Oleksandr"
surname = "Romaniuk"
c = len("Romaniuk")

def get_initials(name: str, surname: str) -> str:
    return f"Initials: {name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """ Counts how many some letters in text and prints it """
    count = 0

    for cycle_letter in letter:
        if letter != "a":
            for k in text:
                if cycle_letter == k.lower():
                    count += 1
                
            print(f"{cycle_letter}: {count}")    
            count = 0
        else:
            for i in text:
                if i.lower() == letter:
                    count += 1

            return count


def count_vowels(text: str) -> int:
    vowels = 0

    for letter in text:
        if letter in "aeiouy":
            vowels += 1

    return vowels


def reverse_text(text: str) -> str:
    counter = ""
    for i in range(len(text) - 1, -1, -1):
        counter += text[i]
    return counter


print(get_initials(name, surname))
print(f"Letters in surname: {c}")
print(f"Vowels: {count_vowels(surname)}, consonants: {c - count_vowels(surname)}")
count_letters(surname, letter="aoeui")
print(f"Default letter 'a': {count_letters(surname)}")
print(f"Reversed surname: {reverse_text(surname)}")
print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")