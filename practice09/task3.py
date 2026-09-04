print("Oleksandr Romaniuk, IT-31")

name = "Oleksandr"
surname = "Romaniuk"

vowels = 0
consonants = 0

for letter in (name+surname).lower():
    if letter in ("e","o","i","u","a","y"):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {len(name+surname)}")
print(f"Is vowels and consonants together equal to length? {len(name + surname)==vowels + consonants}")