print("Oleksandr Romaniuk, IT-31")

d = 12
c = len("Romaniuk")
counter = 0
sum = 0
product = 1
even = 0
odd = 0

print(f"Number from {d} to 31:")

for i in range(d, 32):
    print(i, end=" ")
    counter = counter + 1
    sum = sum + i
    product = product * i

    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(f"\nCount: {counter}")
print(f"Sum: {sum}")
print(f"Product: {product}")

print(f"Average: {round(sum / counter, 2)}")
print(f"Even: {even}, odd: {odd}")

#while version
k = d
counter_in_while = 0
sum_in_while = 0
product_in_while = 1
even_in_while = 0
odd_in_while = 0

print(f"\nWhile version:")
print(f"Number from {k} to 31:")

while k < 32:
    print(k, end=" ")
    k = k + 1

    counter_in_while = counter_in_while + 1
    sum_in_while = sum_in_while + i
    product_in_while = product_in_while * i

    if k % 2 == 0:
        even_in_while = even_in_while + 1
    else:
        odd_in_while = odd_in_while + 1

print(f"\nCount: {counter_in_while}")
print(f"Sum: {sum_in_while}")
print(f"Product: {product_in_while}")

print(f"Average: {round(sum_in_while / counter_in_while, 2)}")
print(f"Even: {even_in_while}, odd: {odd_in_while} \n")

print("Countdown:")

for j in range(c, 0, -1):
    print(j, end=" ")