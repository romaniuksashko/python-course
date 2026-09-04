print("Oleksandr Romaniuk, IT-31")

d = 12
c = len("Romaniuk")

n = d * c

divisors_count = 0
sum = 0

print("Divisors:")

for num in range(1, n + 1):
    
    if n % num == 0:
        divisors_count = divisors_count + 1
        sum = sum + num

        print(num, end=" ")

print(f"\nDivisors count: {divisors_count}, sum: {sum}")

prime_count = 0

for j in range(2, n + 1):
    if divisors_count == 2:
        print(f"\n{n} is prime number")
        break;
else: 
    print(f"\n{n} is not prime number")

print(f"Primes up to {n}:")

for prime in range(2, n + 1):

    for i in range(2, prime):
        if prime % i == 0:
            break
    else:
        print(prime, end=" ")
        prime_count = prime_count + 1

print(f"\nPrimes count: {prime_count}")