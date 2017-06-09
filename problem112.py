"""Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for
example, 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for
example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand
(525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
import time


def is_bouncy(number):
    s = list(str(number))
    return sorted(s) not in (s, s[::-1])


assert is_bouncy(155349)
assert not is_bouncy(134468)
assert not is_bouncy(66420)
assert len([n for n in range(1000) if is_bouncy(n)]) == 525


def find_bouncy_proportion(proportion):
    bouncy_count = 0
    n = 100
    while bouncy_count / n != proportion:
        n += 1
        if is_bouncy(n):
            bouncy_count += 1
    return n


assert find_bouncy_proportion(0.5) == 538
assert find_bouncy_proportion(0.9) == 21780

start = time.time()
print('Answer:', find_bouncy_proportion(0.99))
end = time.time()
print('Took {}s'.format(end - start))
