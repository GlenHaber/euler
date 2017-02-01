"""
Permuted multiples

It can be seen that the number 125874 and its double 251748 contain exactly the same digits, but in a different order.

Find the smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contain the same digits.
"""
n = int(1e5)
while True:
    multiples = [x * n for x in range(1, 7)]
    if len({''.join(sorted(str(m))) for m in multiples}) == 1:
        break
    n += 1
print(n)
