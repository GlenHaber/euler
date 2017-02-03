"""
Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
count = 0
n = 1
i = 1
digits = 0
while n < 25:
    # print(i ** n)
    digits = len(str(i ** n))
    if digits == n:
        count += 1
        print('{}^{} = {}'.format(i, n, i ** n))
    elif digits > n:
        i = 2
        n += 1
        continue
    i += 1
print(count)
