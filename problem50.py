"""
Consecutive prime sum

The prime 41 can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred. The longest sum of consecutive
primes below one-thousand that adds to a prime contains 21 terms and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from problem3 import is_prime
from problem47 import prime_sieve


def solve(ceiling):
    primes = prime_sieve(ceiling)
    # Sum up consecutive primes starting at 2 until we reach ceiling.
    count = 0
    total = 0
    while total <= ceiling:
        total += primes[count]
        count += 1
    count -= 1
    while True:
        for i in range(len(primes) - count + 1):
            value = sum(primes[i:i + count])
            if value > ceiling:
                break
            if is_prime(value):
                return value, count
        count -= 1


print(solve(100))
print(solve(1000))
print('Answer:', solve(1000000))
