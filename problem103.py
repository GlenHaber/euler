"""
Special subset sums: optimum

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty
disjoint subsets, B and C, the following properties are true:

    1. S(B) != S(C); that is, sums of subsets cannot be equal.
    2. If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum
sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form
B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117.
However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum
set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.
"""
from itertools import combinations
from math import inf
from time import time


def S(a):
    return sum(a)


def subsets(s, allow_full=False):
    for i in range(1, len(s)):
        for c in combinations(s, i):
            yield set(c)
    if allow_full:
        yield set(s)


def is_special(a):
    for b in subsets(a):
        for c in subsets(a - b, allow_full=True):
            if sum(b) == sum(c):
                return False
            if len(b) > len(c) and sum(b) < sum(c):
                return False
    return True


assert is_special({3, 5, 6, 7})


def next_set(prev):
    nums = sorted(prev)
    b = nums[len(nums) // 2]
    return {b}.union({a + b for a in prev})


def build_initial(num_digits, min_value):
    nums = [min_value, min_value + 1]
    while len(nums) < num_digits:
        sums = {S(sub) for sub in subsets(nums, allow_full=True)}.union({0})
        disallowed = {abs(a - b) for a, b in combinations(sums, 2)}
        i = max(nums) + 1
        while i in disallowed:
            i += 1
        nums.append(i)
    return nums


def find_optimal(num_digits, approximate_set):
    best = sum(approximate_set) or inf
    best_set = set(approximate_set)
    nums = build_initial(num_digits, min(approximate_set) - 1)
    nums[-1] += best - sum(nums) - 3
    print('Initial check:', nums)
    while True:
        while sum(nums) < best:
            if is_special(set(nums)):
                best = sum(nums)
                best_set = set(nums)
                print('Better set found:', nums)
            nums[-1] += 1
            if nums[-1] >= 2 * sum(nums):
                break
        i = -2
        try:
            while nums[i] + 1 == nums[i + 1]:
                i -= 1
        except IndexError:
            break
        nums[i] += 1
        for j in range(i + 1, 0):
            nums[j] = nums[j - 1] + 1
        nums[-1] += best - sum(nums) - 5
        if nums[-1] <= nums[-2]:
            nums[-1] = nums[-2] + 1  # Prevent infinite loop
    return best_set


assert next_set({3, 5, 6, 7}) == {6, 9, 11, 12, 13}
assert next_set({6, 9, 11, 12, 13}) == {11, 17, 20, 22, 23, 24}


def set_string(a):
    return ''.join(map(str, sorted(a)))


if __name__ == '__main__':
    s6 = {11, 18, 19, 20, 22, 25}
    start = time()
    print(set_string(find_optimal(6, next_set({6, 9, 11, 12, 13}))))
    print('Verifying s6 took {}s'.format(time() - start))
    start = time()
    print('Answer:', set_string(find_optimal(7, next_set(s6))))
    print(time() - start)
