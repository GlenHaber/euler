"""
Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""



def prime_sieve(ceiling):
    results = [True] * ceiling
    results[0] = results[1] = False
    for i, isprime in enumerate(results):
        if isprime:
            for n in range(i * i, ceiling, i):
                results[n] = False
    return [i for i, n in enumerate(results) if n]


primes = prime_sieve(1000000)


def count_prime_factors(n):
    factors = 0
    for p in primes:
        if n % p == 0:
            factors += 1
        if p * 2 > n:
            break
    return factors


def solve(count):
    i = 1
    stream_start = None
    while True:
        if count_prime_factors(i) == count:
            if stream_start is None:
                stream_start = i
            elif i - stream_start == count - 1:
                break
        elif stream_start:
            stream_start = None
        i += 1
    return stream_start


def way_smarter(count):
    """https://projecteuler.net/thread=47;post=1714"""
    limit = 1000000
    factors = [0] * limit
    stream = 0
    for i in range(2, limit):
        if factors[i] == 0:  # i is prime
            stream = 0
            for val in range(i, limit, i):
                factors[val] += 1
        elif factors[i] == count:
            stream += 1
            if stream == count:
                return i - count + 1
        else:
            stream = 0


if __name__ == '__main__':
    print(way_smarter(2))
    print(way_smarter(3))
    print(way_smarter(4))
    print(solve(2))
    print(solve(3))
    print('Answer:', solve(4))
