from problem12 import prime_factors


def measure_cycle(n):
    if set(prime_factors(n)) <= {2, 5}:
        return 0
    power = 1
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    while (10 ** power - 1) % n != 0:
        power += 1
    return power


print(max(range(1000), key=measure_cycle))