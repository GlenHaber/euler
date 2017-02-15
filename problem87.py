"""
Prime power triplets

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there
are exactly four numbers below fifty that can be expressed in such a way:

    28 = 2^2 + 2^3 + 2^4
    33 = 3^2 + 2^3 + 2^4
    49 = 5^2 + 2^3 + 2^4
    47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

from problem47 import prime_sieve

LIMIT = 50000000
primes = prime_sieve(10000)

numbers = [False] * LIMIT

for square in primes:
    for cube in primes:
        if square**2+cube**3 >= LIMIT:
            break
        for quart in primes:
            value = square ** 2 + cube ** 3 + quart ** 4
            if value < LIMIT:
                numbers[value] = True
            else:
                break
print(numbers.count(True))
