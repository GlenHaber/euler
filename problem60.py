"""
Prime pair sets

The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, by taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from itertools import combinations

import time

from problem3 import is_prime
from problem47 import prime_sieve

primes = set(prime_sieve(20000)[1:])  # We can ignore 2. It can't be in the solution

checked_pairs = {}


def check_set(nums):
    for a, b in combinations(nums, 2):
        key = tuple(sorted((a, b)))
        if key in checked_pairs:
            valid = checked_pairs[key]
        else:
            valid = is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))
            checked_pairs[key] = valid
        if not valid:
            return False
    return True


def find_sets(size):
    answer = size
    while True:
        print(answer, '...')
        subset = [p for p in primes if p < answer]
        for combo in combinations(subset, size - 1):
            other = answer - sum(combo)
            if other > max(combo) and other in primes:
                if check_set(combo + (other,)):
                    return answer
        answer += 2


# The solution above takes ages. Brute-force manually instead of using a general function


pair_hash = {}
def check_pair(a, b):
    if (a, b) in pair_hash:
        return pair_hash[(a, b)]
    else:
        valid = is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))
        pair_hash[(a, b)] = valid
        return valid


def brute_force():
    primes = prime_sieve(10000)
    primes.remove(2)
    primes.remove(5)
    best = float('inf')
    for ai, a in enumerate(primes):
        if a * 5 >= best:
            break
        for bi, b in enumerate(primes[ai + 1:]):
            if (a + b) * 2.5 >= best:
                break
            if not check_pair(a, b):
                continue
            for ci, c in enumerate(primes[bi + 1:]):
                if a + b + c >= best:
                    break
                if not (check_pair(a, c) and check_pair(b, c)):
                    continue
                for di, d in enumerate(primes[ci + 1:]):
                    if a + b + c + d >= best:
                        break
                    if not (check_pair(a, d) and check_pair(b, d) and check_pair(c, d)):
                        continue
                    for ei, e in enumerate(primes[di + 1:]):
                        if a + b + c + d + e >= best:
                            break
                        if not (check_pair(a, e) and check_pair(b, e) and check_pair(c, e) and check_pair(d, e)):
                            continue
                        best = min(best, a + b + c + d + e)
                        # if best == a + b + c + d + e:
                        #     print([a, b, c, d, e], '=>', a + b + c + d + e)
    return best


# start = time.time()
# print(find_sets(4))
# print(time.time() - start)
#
# print(find_sets(5))
start = time.time()
print(brute_force())
print(time.time() - start)
