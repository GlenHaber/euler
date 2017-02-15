"""
Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has
been seen before. For example:

    44 -> 32 -> 13 -> 10 -> 1 -> 1
    85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
from time import time

LIMIT = 10000000
endings = [0] * LIMIT
endings[1] = 1
endings[89] = 89

squares = [n ** 2 for n in range(10)]


def square_digit_sum(n):
    total = 0
    while n:
        total += (n%10)**2
        n //= 10
    return total


def build_chain(start):
    chain = [start]
    while chain[-1] not in (1, 89):
        if endings[chain[-1]]:
            chain.append(endings[chain[-1]])
        else:
            chain.append(square_digit_sum(chain[-1]))
    for n in chain[:-1]:
        endings[n] = chain[-1]


if __name__ == '__main__':
    start_time = time()
    for i in range(1, LIMIT):
        build_chain(i)
    print(endings.count(89))
    print(time() - start_time)
