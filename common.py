from math import sqrt, factorial


# PRIME NUMBERS
def prime_sieve(ceiling, min_value=2):
    results = [True] * ceiling
    results[0] = results[1] = False
    for i, prime in enumerate(results):
        if prime:
            for n in range(i * i, ceiling, i):
                results[n] = False
    return [i for i, n in enumerate(results) if n if i >= min_value]


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def miller_rabin_test(n):
    # Some simple checks
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0 or n % 5 == 0:
        return False
    # Create candidate lists
    if n < 2047:
        test_nums = (2,)
    elif n < 1373653:
        test_nums = (2, 3)
    elif n < 9080191:
        test_nums = (31, 73)
    elif n < 25326001:
        test_nums = (2, 3, 5)
    elif n < 3215031751:
        test_nums = (2, 3, 5, 7)
    elif n < 4759123141:
        test_nums = (2, 7, 61)
    elif n < 1122004669633:
        test_nums = (2, 13, 23, 1662803)
    else:
        raise ValueError("Didn't account for witnesses that high.")
    return not any(_miller_rabin_witness(n, a) for a in test_nums)


def _miller_rabin_witness(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Two conditions: a^d != 1 and a^(2^r*d) != -1 for all 0=<r<=s-1 (all mod n)
    check_1 = pow(a, d, n)
    for _ in range(s):
        check_2 = check_1 ** 2 % n
        if check_1 == 1 and check_2 not in {1, n - 1}:
            return False
        check_1 = check_2
    if check_1 != 1:
        return True
    return False


# COMBINATORICS
def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    print(miller_rabin_test(23))
    print(miller_rabin_test(25))
    for i in range(1, 50):
        if miller_rabin_test(i):
            print(i)
