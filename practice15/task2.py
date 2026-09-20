name = "Oleksandr"
surname = "Romaniuk"
group = "IT-31"

print(f"{name} {surname}, group {group} \n")


letters = list(surname.lower())
c = len(surname)
print(f"List: {letters}, length: {c}\n")

print(f"First letter: {letters[0]}")
print(f"Last letter: {letters[-1]}")
print(f"Middle letter(first): {letters[c // 2]}")
print(f"Middle letter(second): {letters[c // 2 : c // 2 + 1]} \n")

print(f"First three letters: {letters[:3]}")
print(f"Letters, but first three: {letters[3:]}")
print(f"Every second letter: {letters[::2]}")
print(f"Reverse letters: {letters[::-1]}")
print(f"Last two letters: {letters[-2:]}")
print(f"Five letters length list from c: {letters[c:c+5]} \n")

unique = []
not_repeated = True

for letter in letters:
    if letter not in unique:
        count = letters.count(letter)
        
        if count > 1:
            not_repeated = False
            print(f"{letter}: {count}")

    unique.append(letter)

if not_repeated:
    print("No repeated letters")

print(f"Unique letters: {unique} \n")

print(f"In alphabet order: {sorted(letters)}")