"""
Amicable chains

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28
are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a
chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""
from time import time


def factor_sum(length):
    rv = [0] * (length + 1)
    for f in range(1, length // 2 + 1):
        x = 2 * f
        while x <= length:
            rv[x] += f
            x += f
    return rv


CEILING = 1000000
start = time()
factors = factor_sum(CEILING)
if __name__ == '__main__':
    print('Generated factor sums in {}s'.format(time() - start))


def chain(n):
    ns = [n]
    while ns[-1] <= CEILING:
        n = factors[ns[-1]]
        ns.append(n)
        if n in ns[:-1]:
            break
    return ns


if __name__ == '__main__':
    start = time()
    chain_lengths = [0] * (CEILING + 1)
    longest_chain = 0, 0
    for num in range(2, CEILING):
        if chain_lengths[num]:
            continue
        nums = chain(num)
        if nums[-1] == 0 or nums[-1] > CEILING:
            for i in nums[:-1]:
                chain_lengths[i] = -1
        else:
            cycle_start = nums.index(nums[-1])
            cycle = nums[cycle_start:-1]
            for i in nums[:cycle_start]:
                chain_lengths[i] = -1
            for i in cycle:
                chain_lengths[i] = len(cycle)
            if len(cycle) > longest_chain[1]:
                longest_chain = min(cycle), len(cycle)
    print('Answer:', longest_chain[0])
    print(time() - start)
